# first line

from typing import Type, Optional, Dict, Any
from server.objects.media import Media, _probe_pdf_pages, _resolve_storage_file
import os
from server.utils.media_utils import fetch_dict_entry, create_dict_entry
import json
from server.db.db_crud import get_user_id_by_username, create_concert_db, fetch_concert_by_video_id, create_concert_segment_db, fetch_concert_segments_db, update_concert_segment_db, delete_concert_segment_db

# =========================
# GENERIC CREATION (optional, CLI/debug)
# =========================
FIELDS_MAP = {
    "SONG": ["title", "year", "duration", "location", "additional_info", "authors", "performers", "genres", "references", "is_author", "is_performer"],
    "DOC": ["title", "stored_at", "pages", "format", "references", "authors"],
    "VIDEO": ["title", "year", "duration", "location", "additional_info", "director", "authors", "performers", "genres", "references", "is_author", "is_performer"]
}

# =========================
# GENERIC OBJECT HELPERS
# =========================
def build_object(cls: Type[Media], data: Optional[Dict[str, Any]]):
    #print(f"[DEBUG][build_object] cls={cls.__name__}, data={data}")
    if not data:
        #print("[DEBUG][build_object] data is None/empty -> returning None")
        return None
    # If an object is passed already, return it
    if isinstance(data, Media):
        #print(f"[DEBUG][build_object] data is already a Media instance -> returning it")
        return data
    obj = cls.from_dict(data)
    #print(f"[DEBUG][build_object] Built object={obj}")
    return obj

def get_object(cls: Type[Media], object_id: int):
    #print(f"[DEBUG][get_object] cls={cls.__name__}, object_id={object_id}")
    # Use generic fetch method since all media types now use Media class
    obj = cls.fetch(object_id)
    #print(f"[DEBUG][get_object] Retrieved object={obj}")
    return obj

# Helper: flatten incoming relation values (strings, lists, nested lists)
def _flatten_relation(val):
    if isinstance(val, str):
        return [s.strip() for s in val.split(",") if s.strip()]
    if isinstance(val, (list, tuple)):
        out = []
        for part in val:
            if isinstance(part, (list, tuple)):
                for sub in part:
                    out.append(sub)
            else:
                out.append(part)
        return out
    if val:
        return [val]
    return []

def convert_relation_names_to_ids(updates: Dict[str, Any]):
    """
    Transform relation fields in updates dict by converting string names to integer IDs.
    
    Process authors, performers, genres, and tags (maps to genres).
    For each string name:
    1. Fetch existing entry by name
    2. Create if missing via create_dict_entry
    3. Refetch if creation failed (handle race conditions)
    4. Only add valid integer IDs to result
    
    This runs BEFORE update_object, ensuring it only receives integer IDs.
    """
    #print(f"[DEBUG][convert_relation_names_to_ids] START - updates keys={list(updates.keys())}")
    
    from server.db.db_crud import (
        create_dict_entry as db_create_dict_entry,
        fetch_dict_entry_by_name,
        fetch_one as _fetch_one
    )
    
    # Relation field mappings
    relation_map = {
        "authors": "authors",
        "genres": "genres",
        "performers": "performers",
        "tags": "genres",  # Map tags to genres
        "instruments": "instruments"
    }
    
    converted = {}
    
    for field_name, table_name in relation_map.items():
        if field_name not in updates:
            continue
        
        val = updates[field_name]
        if val is None:
            converted[field_name] = None
            continue
        
        #print(f"[DEBUG][convert_relation_names_to_ids] Processing {field_name} -> {table_name}")
        
        # Flatten to list
        items = _flatten_relation(val)
        #print(f"[DEBUG][convert_relation_names_to_ids] Flattened {field_name}: {items}")
        
        ids = []
        for it in items:
            try:
                # Already an integer ID
                if isinstance(it, int):
                    ids.append(int(it))
                    #print(f"[DEBUG][convert_relation_names_to_ids] Kept {field_name} integer id={it}")
                    continue
                
                # Dict with id field
                if isinstance(it, dict):
                    if it.get('id'):
                        ids.append(int(it['id']))
                        #print(f"[DEBUG][convert_relation_names_to_ids] Extracted {field_name} id from dict: {it['id']}")
                        continue
                    # Has name field: treat as string name
                    name = it.get('name')
                    if not name:
                        continue
                else:
                    # Treat as string name
                    name = str(it).strip()
                    if not name:
                        continue
                
                # Convert string name to ID
                entry_id = None
                
                # Step 1: Try to fetch
                try:
                    row = fetch_dict_entry_by_name(table_name, name)
                    if row and row.get("id"):
                        entry_id = row["id"]
                        #print(f"[DEBUG][convert_relation_names_to_ids] Found {table_name} '{name}' -> id={entry_id}")
                except Exception as e:
                    print(f"[DEBUG][convert_relation_names_to_ids] fetch_dict_entry_by_name error for '{name}': {e}")
                
                # Step 2: Create if not found
                if entry_id is None:
                    try:
                        nid = db_create_dict_entry(table_name, name)
                        if nid:
                            entry_id = nid
                            #print(f"[DEBUG][convert_relation_names_to_ids] Created {table_name} '{name}' -> id={entry_id}")
                        else:
                            print(f"[WARNING][convert_relation_names_to_ids] create_dict_entry returned None for {table_name} '{name}'")
                    except Exception as e:
                        print(f"[ERROR][convert_relation_names_to_ids] create_dict_entry error for '{name}': {e}")
                
                # Step 3: Refetch if creation failed
                if entry_id is None:
                    try:
                        row = fetch_dict_entry_by_name(table_name, name)
                        if row and row.get("id"):
                            entry_id = row["id"]
                            #print(f"[DEBUG][convert_relation_names_to_ids] Refetched {table_name} '{name}' -> id={entry_id}")
                    except Exception as e:
                        print(f"[ERROR][convert_relation_names_to_ids] refetch error for '{name}': {e}")
                
                # Step 4: Only add if we have valid ID
                if entry_id is not None:
                    ids.append(entry_id)
                    #print(f"[DEBUG][convert_relation_names_to_ids] Added {field_name} id={entry_id}")
                else:
                    print(f"[WARNING][convert_relation_names_to_ids] Skipping {field_name} '{name}' - could not obtain ID")
            
            except Exception as e:
                print(f"[ERROR][convert_relation_names_to_ids] Processing {field_name} item {it} failed: {e}")
        
        # Store converted IDs
        if field_name == "tags":
            # Map tags back to genres in result
            converted["genres"] = ids
            # Remove tags from updates since it maps to genres
            updates.pop("tags", None)
        else:
            converted[field_name] = ids if ids else None
    
    # Update with converted IDs
    for field_name, ids in converted.items():
        updates[field_name] = ids
    
    #print(f"[DEBUG][convert_relation_names_to_ids] DONE - converted updates: {updates}")
    return updates

def create_object(cls: Type[Media], user_obj: Optional[Any], data: Dict[str, Any]):
    #print(f"[DEBUG][create_object] cls={cls.__name__}, user_obj={user_obj}, data={data}")
    
    # CRITICAL FIX 0: Normalize field name aliases to canonical database column names
    # Map client-side aliases to actual database columns
    if 'recording_location' in data and 'location' not in data:
        data['location'] = data.pop('recording_location')
    if 'tags' in data and 'genres' not in data:
        data['genres'] = data.pop('tags')
    if 'url' in data and 'link' not in data:
        data['link'] = data.pop('url')
    
    # CRITICAL FIX: Convert is_author/is_performer flags to relational data BEFORE object creation
    # If is_author=True and no authors list, add user_id to authors
    if data.get('is_author') and not data.get('authors'):
        user_id = data.get('user_id')
        if user_id:
            data['authors'] = [user_id]
            #print(f"[DEBUG][create_object] Converted is_author=True to authors=[{user_id}]")
    
    # If is_performer=True and no performers list, add user_id to performers
    if data.get('is_performer') and not data.get('performers'):
        user_id = data.get('user_id')
        if user_id:
            data['performers'] = [user_id]
            #print(f"[DEBUG][create_object] Converted is_performer=True to performers=[{user_id}]")
    
    obj = build_object(cls, data) if not isinstance(data, Media) else data
    if not obj:
        #print("[DEBUG][create_object] Object is None -> returning None")
        return None
    target_user_id = getattr(obj, "user_id", None)
    actor_user_id = None
    if user_obj:
        if isinstance(user_obj, dict):
            actor_user_id = user_obj.get("id")
        else:
            actor_user_id = getattr(user_obj, "id", None)
    if target_user_id:
        print(f"[DEBUG][create_object] Using payload user_id={target_user_id}")
    elif actor_user_id:
        obj.user_id = actor_user_id
        #print(f"[DEBUG][create_object] Fallback obj.user_id={actor_user_id}")

    #print(f"[DEBUG][create_object] Saving object {obj}")
    obj.save()
    #print(f"[DEBUG][create_object] Object saved: {obj}")
    
    # If this is a document and pages/format are missing, try to probe the stored file and persist
    try:
        if getattr(obj, 'type', None) == 'document':
            missing_pages = getattr(obj, 'pages', None) is None
            missing_format = getattr(obj, 'format', None) is None
            if missing_pages or missing_format:
                try:
                    path = _resolve_storage_file(getattr(obj, 'stored_at', None), 'document')
                    doc_updates = {}
                    if path and os.path.isfile(path):
                        try:
                            pages = _probe_pdf_pages(path)
                            if pages and missing_pages:
                                doc_updates['pages'] = int(pages)
                        except Exception as e:
                            print(f"[DEBUG][create_object] _probe_pdf_pages failed: {e}")

                        # infer format from file extension if possible
                        try:
                            _, ext = os.path.splitext(path)
                            fmt = ext.lower().lstrip('.') if ext else None
                            if fmt and missing_format:
                                doc_updates['format'] = fmt
                        except Exception:
                            pass

                    # persist updates if any
                    if doc_updates:
                        try:
                            from server.db.db_crud import update_document_db
                            update_document_db(getattr(obj, 'id', None), doc_updates)
                            # update in-memory object
                            for k, v in doc_updates.items():
                                try:
                                    setattr(obj, k, v)
                                except Exception:
                                    pass
                            #print(f"[DEBUG][create_object] persisted document metadata: {doc_updates}")
                        except Exception as e:
                            print(f"[WARNING][create_object] failed to persist document metadata: {e}")
                except Exception as e:
                    print(f"[DEBUG][create_object] document metadata probe failed: {e}")
    except Exception:
        pass
    # CONCERT-SPECIFIC: Handle concert segments from payload (if provided in initial creation)
    if getattr(obj, 'type', None) == 'concert' and obj.id:
        segments_payload = data.get('segments') or data.get('subtracks')
        if segments_payload and isinstance(segments_payload, list):
            #print(f"[DEBUG][create_object] Creating {len(segments_payload)} concert segments")
            for seg in segments_payload:
                try:
                    seg_result = add_concert_segment_services(user_obj, obj.id, seg)
                    #print(f"[DEBUG][create_object] Created segment: {seg_result}")
                except Exception as e:
                    print(f"[WARNING][create_object] Failed to create concert segment: {e}")

    return obj

def update_object(obj: Media, updates: Dict[str, Any]):
    from datetime import datetime

    #print(f"[DEBUG][update_object] ===== START =====")
    #print(f"[DEBUG][update_object] obj={obj}")
    #print(f"[DEBUG][update_object] obj.id={getattr(obj, 'id', None)}, obj.type={getattr(obj, 'type', None)}")
    #print(f"[DEBUG][update_object] updates keys={list(updates.keys()) if isinstance(updates, dict) else 'NOT A DICT'}")
    #print(f"[DEBUG][update_object] updates: {updates}")
    # filter out problematic fields that may cause SQL errors or should not be updated directly
    # Also protect identity/ownership fields from casual updates coming from clients
    DISALLOWED_FIELDS = {"references", "raw", "created_at", "id", "media_id", "user_id", "username", "owner", "owner_id", "target_username", "on_behalf_of"} 
    # split keys between media table and document child table
    MEDIA_ONLY_KEYS = set()  # leave empty to default to media updates
    DOC_KEYS = {"pages", "format"}

    # CRITICAL FIX 1: Convert is_author/is_performer flags to relational data BEFORE processing
    # If is_author=True and no authors list provided, add user_id to authors
    if updates.get('is_author') and not updates.get('authors'):
        user_id = getattr(obj, 'user_id', None)
        if user_id:
            updates['authors'] = [user_id]
            #print(f"[DEBUG][update_object] Converted is_author=True to authors=[{user_id}]")

    # If is_performer=True and no performers list provided, add user_id to performers
    if updates.get('is_performer') and not updates.get('performers'):
        user_id = getattr(obj, 'user_id', None)
        if user_id:
            updates['performers'] = [user_id]
            #print(f"[DEBUG][update_object] Converted is_performer=True to performers=[{user_id}]")

    # CRITICAL FIX 2: Normalize common client aliases BEFORE processing
    # Map 'tags' -> 'genres', 'url' -> 'link', 'recording_location' -> 'location' so client/server use canonical names
    if isinstance(updates, dict):
        if 'tags' in updates and 'genres' not in updates:
            try:
                updates['genres'] = updates.pop('tags')
                #print(f"[DEBUG][update_object] Normalized alias 'tags' -> 'genres'")
            except Exception as e:
                print(f"[DEBUG][update_object] failed to normalize 'tags' -> 'genres': {e}")
        if 'url' in updates and 'link' not in updates:
            try:
                updates['link'] = updates.pop('url')
                #print(f"[DEBUG][update_object] Normalized alias 'url' -> 'link'")
            except Exception as e:
                print(f"[DEBUG][update_object] failed to normalize 'url' -> 'link': {e}")
        if 'recording_location' in updates and 'location' not in updates:
            try:
                updates['location'] = updates.pop('recording_location')
                #print(f"[DEBUG][update_object] Normalized alias 'recording_location' -> 'location'")
            except Exception as e:
                print(f"[DEBUG][update_object] failed to normalize 'recording_location' -> 'location': {e}")

    DATE_FIELDS = {"recording_date", "concert_date"}
    for date_field in DATE_FIELDS:
        if date_field in updates and updates[date_field] is not None:
            val = updates[date_field]
            if isinstance(val, str):
                try:
                    # Try ISO format first (YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS)
                    if "T" in val:
                        updates[date_field] = datetime.fromisoformat(val)
                    else:
                        updates[date_field] = datetime.strptime(val, "%Y-%m-%d")
                    #print(f"[DEBUG][update_object] Converted date string '{val}' to datetime for field '{date_field}'")
                except Exception as e:
                    print(f"[DEBUG][update_object] Failed to convert date string '{val}' for field '{date_field}': {e}")
                    # Leave as-is if conversion fails, DB will handle or error appropriately

    # CRITICAL FIX 3: Filter out None values to prevent overwriting with NULL
    # Only include fields that are explicitly set (not None)
    sanitized = {}
    for k, v in updates.items():
        if k in DISALLOWED_FIELDS:
            #print(f"[DEBUG][update_object] Skipping disallowed/identifier update field: {k}")
            continue
        if v is None:
            #print(f"[DEBUG][update_object] Skipping None value for field '{k}' to preserve existing data")
            continue
        sanitized[k] = v

    # Remove fields that are unchanged compared to current object to avoid unnecessary updates
    try:
        import json as _json
        to_drop = []
        for k, v in list(sanitized.items()):
            current = getattr(obj, k, None)
            equal = False
            try:
                # Compare complex structures by canonical JSON
                if isinstance(v, (dict, list, tuple)) or isinstance(current, (dict, list, tuple)):
                    cur_ser = _json.dumps(current, sort_keys=True) if current is not None else None
                    new_ser = _json.dumps(v, sort_keys=True)
                    if cur_ser == new_ser:
                        equal = True
                else:
                    if current == v:
                        equal = True
            except Exception:
                pass
            if equal:
                to_drop.append(k)
        for k in to_drop:
            #print(f"[DEBUG][update_object] Skipping unchanged field {k}")
            sanitized.pop(k, None)
    except Exception as e:
        print(f"[DEBUG][update_object] unchanged-field check failed: {e}")

    if not sanitized:
        #print("[DEBUG][update_object] No sanitized fields to update -> returning object")
        return obj

    # apply attributes in-memory
    for k, v in sanitized.items():
        #print(f"[DEBUG][update_object] Setting {k}={v}")
        try:
            setattr(obj, k, v)
        except Exception as e:
            print(f"[DEBUG][update_object] failed to set attribute {k} on object: {e}")

    # split into media vs document updates where relevant
    media_updates = {}
    doc_updates = {}
    for k, v in sanitized.items():
        if k in DOC_KEYS:
            doc_updates[k] = v
        else:
            media_updates[k] = v

    relation_map = {
        "authors": ("authors", "media_authors", "author_id"),
        "genres": ("genres", "media_genres", "genre_id"),
        "performers": ("performers", "media_performances", "performer_id")
    }

    try:
        from server.db.db_crud import create_dict_entry as db_create_dict_entry, create_relation as db_create_relation, delete_relation as db_delete_relation, fetch_one as _fetch_one
        for key, params in relation_map.items():
            # CRITICAL FIX: Only process if explicitly in updates (not inferred from missing fields)
            if key not in sanitized:
                #print(f"[DEBUG][update_object] Skipping {key} - not explicitly provided in update")
                continue
            
            #print(f"[DEBUG][update_object] ===== Processing relation: {key} =====")
            table_name, rel_table, rel_col = params
            val = sanitized[key]
            #print(f"[DEBUG][update_object] table_name={table_name}, rel_table={rel_table}, val={val}")
            if val is None:
                # clear relations
                try:
                    if getattr(obj, "id", None):
                        db_delete_relation(rel_table, {"media_id": getattr(obj, "id")})
                    setattr(obj, key, [])
                except Exception as e:
                    print(f"[DEBUG][update_object] failed to clear relations for {key}: {e}")
                # ensure we don't try to update media table with this field
                media_updates.pop(key, None)
                continue

            # normalize to list (flatten nested lists/tuples and split comma-separated strings)
            items = _flatten_relation(val)
            #print(f"[DEBUG][update_object] flattened items for {key}: {items}")

            ids = []
            for it in items:
                try:
                    #print(f"[DEBUG][update_object] processing item={it} (type={type(it).__name__}) for {key}")
                    # Handle string names first (most common from client)
                    if isinstance(it, str):
                        name = it.strip()
                        if not name:
                            continue
                        entry_id = None
                        # Step 1: Try to fetch existing entry by name
                        try:
                            from server.db.db_crud import fetch_dict_entry_by_name
                            row = fetch_dict_entry_by_name(table_name, name)
                            if row and row.get("id"):
                                entry_id = row["id"]
                                #print(f"[DEBUG][update_object] found existing {table_name} entry '{name}' -> id={entry_id}")
                        except Exception as e:
                            print(f"[DEBUG][update_object] fetch_dict_entry_by_name error for '{name}': {e}")
                        # Step 2: If not found, create new entry
                        if entry_id is None:
                            try:
                                nid = db_create_dict_entry(table_name, name)
                                if nid:
                                    entry_id = nid
                                    #print(f"[DEBUG][update_object] created {table_name} entry '{name}' -> id={entry_id}")
                                else:
                                    print(f"[WARNING][update_object] create_dict_entry returned None for {table_name} entry '{name}'")
                            except Exception as e:
                                print(f"[ERROR][update_object] create_dict_entry error for '{name}': {e}")

                        # Step 3: After creation, if we still don't have an ID, try to fetch again
                        if entry_id is None:
                            try:
                                from server.db.db_crud import fetch_dict_entry_by_name
                                row = fetch_dict_entry_by_name(table_name, name)
                                if row and row.get("id"):
                                    entry_id = row["id"]
                                    #print(f"[DEBUG][update_object] refetched {table_name} entry '{name}' after creation -> id={entry_id}")
                                else:
                                    print(f"[ERROR][update_object] {table_name} entry '{name}' not found after creation attempt")
                            except Exception as e:
                                print(f"[ERROR][update_object] refetch_dict_entry_by_name error for '{name}': {e}")

                        # Step 4: Only add to ids if we have a valid ID
                        if entry_id is not None:
                            ids.append(entry_id)
                            #print(f"[DEBUG][update_object] added id={entry_id} to ids list for {key}")
                        else:
                            print(f"[WARNING][update_object] skipping '{name}' - could not obtain ID from {table_name}")
                        continue

                    # Handle integer IDs
                    if isinstance(it, int):
                        if table_name == "authors":
                            try:
                                # prefer explicit authors.id
                                arow = _fetch_one("SELECT id FROM authors WHERE id=%s", (int(it),))
                                if arow and arow.get("id"):
                                    ids.append(int(arow.get("id")))
                                    continue
                                # try resolving as users.id -> create/get author linked to user
                                urow = _fetch_one("SELECT id, username FROM users WHERE id=%s", (int(it),))
                                if urow and urow.get("id"):
                                    # try to find existing author for user
                                    erow = _fetch_one("SELECT id FROM authors WHERE user_id=%s", (int(it),))
                                    if erow and erow.get("id"):
                                        ids.append(int(erow.get("id")))
                                    else:
                                        try:
                                            from server.db.db_crud import create_author_with_user
                                            new_aid = create_author_with_user(int(it), urow.get("username") or f"user_{it}")
                                            if new_aid:
                                                ids.append(int(new_aid))
                                        except Exception as e:
                                            print(f"[DEBUG][update_object] failed to create author for user id {it}: {e}")
                                    continue
                                # unknown integer for authors -> skip
                                #print(f"[DEBUG][update_object] provided id={it} not found in authors or users, skipping")
                                continue
                            except Exception as e:
                                #print(f"[DEBUG][update_object] author-id resolution failed for {it}: {e}")
                                continue
                        elif table_name == "performers":
                            try:
                                # Check if it's a performer ID
                                prow = _fetch_one("SELECT id FROM performers WHERE id=%s", (int(it),))
                                if prow and prow.get("id"):
                                    ids.append(int(prow.get("id")))
                                    continue
                                # Try resolving as user ID
                                urow = _fetch_one("SELECT id, username FROM users WHERE id=%s", (int(it),))
                                if urow and urow.get("id"):
                                    erow = _fetch_one("SELECT id FROM performers WHERE user_id=%s", (int(it),))
                                    if erow and erow.get("id"):
                                        ids.append(int(erow.get("id")))
                                    else:
                                        try:
                                            from server.db.db_crud import create_performer_with_user
                                            new_pid = create_performer_with_user(int(it), urow.get("username") or f"user_{it}")
                                            if new_pid:
                                                ids.append(int(new_pid))
                                        except Exception as e:
                                            print(f"[DEBUG][update_object] failed to create performer for user id {it}: {e}")
                                    continue
                                #print(f"[DEBUG][update_object] provided performer id={it} not found, skipping")
                                continue
                            except Exception as e:
                                #print(f"[DEBUG][update_object] performer-id resolution failed for {it}: {e}")
                                continue
                        else:
                            # For genres, instruments: just verify and use the ID
                            ids.append(int(it))
                            continue

                    # Handle dict form like {type:'user', id: ...}
                    if isinstance(it, dict):
                        if "id" in it and it["id"]:
                            ids.append(int(it["id"]))
                            continue

                        name = it.get("name") or it.get("username") or it.get("performer")
                        if name:
                            # Treat dict with name as a string name entry
                            entry_id = None

                            # Step 1: Try to fetch
                            try:
                                from server.db.db_crud import fetch_dict_entry_by_name
                                row = fetch_dict_entry_by_name(table_name, name)
                                if row and row.get("id"):
                                    entry_id = row["id"]
                                    ids.append(entry_id)
                                    #print(f"[DEBUG][update_object] found dict entry {table_name} '{name}' -> id={entry_id}")
                                    continue
                            except Exception as e:
                                print(f"[DEBUG][update_object] fetch dict entry error: {e}")

                            # Step 2: Create if not found
                            if entry_id is None:
                                try:
                                    nid = db_create_dict_entry(table_name, name)
                                    if nid:
                                        entry_id = nid
                                        #print(f"[DEBUG][update_object] created dict entry {table_name} '{name}' -> id={entry_id}")
                                    else:
                                        print(f"[WARNING][update_object] create_dict_entry returned None for dict {it}")
                                except Exception as e:
                                    print(f"[ERROR][update_object] create dict entry error: {e}")
                            
                            # Step 3: Refetch if creation failed
                            if entry_id is None:
                                try:
                                    from server.db.db_crud import fetch_dict_entry_by_name
                                    row = fetch_dict_entry_by_name(table_name, name)
                                    if row and row.get("id"):
                                        entry_id = row["id"]
                                        #print(f"[DEBUG][update_object] refetched dict entry {table_name} '{name}' -> id={entry_id}")
                                except Exception:
                                    pass
                            
                            # Step 4: Only add if we have ID
                            if entry_id is not None:
                                ids.append(entry_id)
                                #print(f"[DEBUG][update_object] added id={entry_id} to ids list for dict {it}")
                            else:
                                print(f"[WARNING][update_object] skipping dict entry - could not obtain ID")
                        continue
                    
                    # Fallback: convert to string and retry
                    name = str(it).strip()
                    if name:
                        entry_id = None
                        
                        # Step 1: Try to fetch
                        try:
                            from server.db.db_crud import fetch_dict_entry_by_name
                            row = fetch_dict_entry_by_name(table_name, name)
                            if row and row.get("id"):
                                entry_id = row["id"]
                                #print(f"[DEBUG][update_object] found fallback entry {table_name} '{name}' -> id={entry_id}")
                        except Exception as e:
                            print(f"[DEBUG][update_object] fallback fetch error: {e}")
                        
                        # Step 2: Create if not found
                        if entry_id is None:
                            try:
                                nid = db_create_dict_entry(table_name, name)
                                if nid:
                                    entry_id = nid
                                    #print(f"[DEBUG][update_object] created fallback entry {table_name} '{name}' -> id={entry_id}")
                                else:
                                    print(f"[WARNING][update_object] create_dict_entry returned None for fallback '{name}'")
                            except Exception as e:
                                print(f"[ERROR][update_object] fallback create error for '{name}': {e}")
                        
                        # Step 3: Refetch if creation failed
                        if entry_id is None:
                            try:
                                from server.db.db_crud import fetch_dict_entry_by_name
                                row = fetch_dict_entry_by_name(table_name, name)
                                if row and row.get("id"):
                                    entry_id = row["id"]
                                    #print(f"[DEBUG][update_object] refetched fallback entry {table_name} '{name}' -> id={entry_id}")
                            except Exception:
                                pass
                        
                        # Step 4: Only add if we have ID
                        if entry_id is not None:
                            ids.append(entry_id)
                            #print(f"[DEBUG][update_object] added fallback id={entry_id} to ids list")
                        else:
                            print(f"[WARNING][update_object] skipping fallback '{name}' - could not obtain ID")
                except Exception as e:
                    print(f"[ERROR][update_object] failed to normalize relation item {it} for {key}: {e}")

            # replace relations in DB: delete existing then insert new ones
            try:
                #print(f"[DEBUG][update_object] Final ids collected for {key}: {ids}")
                mid = getattr(obj, "id", None)
                #print(f"[DEBUG][update_object] Media id for relations: {mid}")
                if mid is not None:
                    #print(f"[DEBUG][update_object] Deleting existing relations from {rel_table}")
                    db_delete_relation(rel_table, {"media_id": mid})
                    #print(f"[DEBUG][update_object] Creating {len(ids)} new relations")
                    for iid in ids:
                        #print(f"[DEBUG][update_object] Creating relation: media_id={mid}, {rel_col}={iid}")
                        db_create_relation(rel_table, ("media_id", rel_col), (mid, iid))
                    # update in-memory object
                    setattr(obj, key, ids)
                    #print(f"[DEBUG][update_object] Updated {key} relations: {ids}")
                else:
                    print(f"[WARNING][update_object] Media id is None, cannot update relations for {key}")
            except Exception as e:
                print(f"[ERROR][update_object] failed to update relation table {rel_table}: {e}")
                import traceback
                traceback.print_exc()

            # make sure these are not attempted on media table
            media_updates.pop(key, None)

        # --- SPECIAL: handle 'instruments' field (attach to media_performances.performance_instruments) ---
        try:
            if 'instruments' in sanitized:
                raw = sanitized.get('instruments')
                items = _flatten_relation(raw)

                instr_ids = []
                for it in items:
                    try:
                        # Handle string names first
                        if isinstance(it, str):
                            name = it.strip()
                            if not name:
                                continue
                            instr_id = None
                            # Step 1: Try to fetch existing instrument by name
                            try:
                                from server.db.db_crud import fetch_dict_entry_by_name
                                row = fetch_dict_entry_by_name('instruments', name)
                                if row and row.get("id"):
                                    instr_id = row["id"]
                                    #print(f"[DEBUG][update_object] found existing instrument '{name}' -> id={instr_id}")
                            except Exception as e:
                                print(f"[DEBUG][update_object] fetch instrument error: {e}")
                            # Step 2: Create new instrument if not found
                            if instr_id is None:
                                try:
                                    nid = db_create_dict_entry('instruments', name)
                                    if nid:
                                        instr_id = nid
                                        #print(f"[DEBUG][update_object] created instrument '{name}' -> id={instr_id}")
                                    else:
                                        print(f"[WARNING][update_object] create_dict_entry returned None for instrument '{name}'")
                                except Exception as e:
                                    print(f"[ERROR][update_object] create instrument error: {e}")
                            # Step 3: Refetch if creation failed
                            if instr_id is None:
                                try:
                                    from server.db.db_crud import fetch_dict_entry_by_name
                                    row = fetch_dict_entry_by_name('instruments', name)
                                    if row and row.get("id"):
                                        instr_id = row["id"]
                                        #print(f"[DEBUG][update_object] refetched instrument '{name}' -> id={instr_id}")
                                except Exception:
                                    pass
                            # Step 4: Only add if we have ID
                            if instr_id is not None:
                                instr_ids.append(instr_id)
                                #print(f"[DEBUG][update_object] added instrument id={instr_id}")
                            else:
                                print(f"[WARNING][update_object] skipping instrument '{name}' - could not obtain ID")
                            continue
                        # Handle integer IDs
                        if isinstance(it, int):
                            instr_ids.append(int(it))
                            continue
                        # Handle dict form
                        if isinstance(it, dict):
                            if it.get('id'):
                                instr_ids.append(int(it.get('id')))
                                continue
                            name = it.get('name')
                            if name:
                                instr_id = None
                                # Step 1: Try to fetch
                                try:
                                    from server.db.db_crud import fetch_dict_entry_by_name
                                    row = fetch_dict_entry_by_name('instruments', name)
                                    if row and row.get("id"):
                                        instr_id = row["id"]
                                        #print(f"[DEBUG][update_object] found dict instrument '{name}' -> id={instr_id}")
                                except Exception:
                                    pass
                                # Step 2: Create if not found
                                if instr_id is None:
                                    try:
                                        nid = db_create_dict_entry('instruments', name)
                                        if nid:
                                            instr_id = nid
                                            #print(f"[DEBUG][update_object] created dict instrument '{name}' -> id={instr_id}")
                                        else:
                                            print(f"[WARNING][update_object] create_dict_entry returned None for dict instrument '{name}'")
                                    except Exception as e:
                                        print(f"[ERROR][update_object] create dict instrument error: {e}")
                                # Step 3: Refetch if creation failed
                                if instr_id is None:
                                    try:
                                        from server.db.db_crud import fetch_dict_entry_by_name
                                        row = fetch_dict_entry_by_name('instruments', name)
                                        if row and row.get("id"):
                                            instr_id = row["id"]
                                            #print(f"[DEBUG][update_object] refetched dict instrument '{name}' -> id={instr_id}")
                                    except Exception:
                                        pass

                                # Step 4: Only add if we have ID
                                if instr_id is not None:
                                    instr_ids.append(instr_id)
                                    #print(f"[DEBUG][update_object] added dict instrument id={instr_id}")
                                else:
                                    print(f"[WARNING][update_object] skipping dict instrument - could not obtain ID")
                            continue
                        # Fallback: convert to string
                        name = str(it).strip()
                        if not name:
                            continue
                        # Try to fetch existing
                        try:
                            from server.db.db_crud import fetch_dict_entry_by_name
                            row = fetch_dict_entry_by_name('instruments', name)
                            if row and row.get("id"):
                                instr_ids.append(row["id"])
                                continue
                        except Exception:
                            pass
                        # Create if not found
                        try:
                            nid = db_create_dict_entry('instruments', name)
                            if nid:
                                instr_ids.append(nid)
                        except Exception as e:
                            #print(f"[DEBUG][update_object] fallback instrument create error: {e}")
                            instr_ids.append(nid)
                    except Exception as e:
                        print(f"[ERROR][update_object] failed to normalize instrument item {it}: {e}")

                # attach instruments to each existing performance for this media
                mid = getattr(obj, 'id', None)
                if mid is not None and instr_ids:
                    from server.db.db_crud import fetch_one as _fetch_one
                    for pid in getattr(obj, 'performers', []) or []:
                        try:
                            row = _fetch_one("SELECT id FROM media_performances WHERE media_id=%s AND performer_id=%s", (mid, pid))
                            perf_id = row.get('id') if row else None
                            if perf_id:
                                # replace existing instruments for performance
                                db_delete_relation('performance_instruments', {'performance_id': perf_id})
                                for iid in instr_ids:
                                    db_create_relation('performance_instruments', ('performance_id','instrument_id'), (perf_id, iid))
                                print(f"[DEBUG][update_object] Attached instruments {instr_ids} to performance {perf_id} (performer {pid})")
                        except Exception as e:
                            print(f"[ERROR][update_object] failed to attach instruments to performer {pid}: {e}")
        except Exception as e:
            print(f"[ERROR][update_object] instruments handling failed: {e}")
    except Exception as e:
        print(f"[ERROR][update_object] relation handling failed: {e}")

    # perform DB updates directly to avoid Media.save() full-payload update
    try:
        from server.db.db_crud import update_media_db
        if media_updates:
            #print(f"[DEBUG][update_object] Updating media table id={getattr(obj,'id',None)} with {media_updates}")
            result = update_media_db(getattr(obj, "id", None), media_updates)
            if not result:
                print(f"[WARNING][update_object] media table update returned False for id={getattr(obj,'id',None)}")

            # If updating a link, ensure linked_media JSON is kept in sync and create concert row when appropriate.
            try:
                if 'link' in media_updates and media_updates.get('link'):
                    mid = getattr(obj, 'id', None)
                    link_raw = media_updates.get('link')

                    # sanitize link similarly to fetch-side logic
                    try:
                        cleaned = str(link_raw).strip().strip('"').strip("'")
                        if cleaned and not cleaned.startswith(("http://","https://")):
                            cleaned = "https://" + cleaned
                    except Exception:
                        cleaned = link_raw

                    # If media is a concert, upsert concerts table as before
                    try:
                        if mid is not None and getattr(obj, 'type', None) == 'concert':
                            from server.db.db_crud import create_concert_db, fetch_one, update_media_db as _update_media_db
                            try:
                                create_concert_db(mid, cleaned, media_updates.get('title') or getattr(obj, 'title', None), media_updates.get('description') or getattr(obj,'description',None))
                                #print(f"[DEBUG][update_object] Updated concerts table for video_id={mid}")
                            except Exception as e:
                                print(f"[WARNING][update_object] failed to upsert concerts table: {e}")
                    except Exception as e:
                        print(f"[WARNING][update_object] concert upsert failed: {e}")

                    # If client explicitly provided 'linked_media' in the update, respect that and do not auto-merge
                    if 'linked_media' not in sanitized:
                        try:
                            from server.db.db_crud import fetch_one, update_media_db as _update_media_db
                            cur_row = fetch_one("SELECT linked_media FROM media WHERE id=%s", (mid,)) if mid is not None else None
                            existing = cur_row.get('linked_media') if cur_row else None
                            try:
                                lm = json.loads(existing) if existing else []
                            except Exception:
                                lm = []
                            if not isinstance(lm, list):
                                lm = [lm]

                            entry = {"type": "link", "source": ("youtube" if "youtube" in (cleaned or "").lower() else "external"), "url": cleaned, "title": media_updates.get('title') or getattr(obj, 'title', None)}

                            # If an entry with same url exists, update its title/embed fields; otherwise append
                            found = False
                            for e in lm:
                                if isinstance(e, dict) and e.get('url') == cleaned:
                                    e.update({"title": entry.get('title')})
                                    found = True
                                    break
                            if not found:
                                lm.append(entry)

                            # persist only if changed
                            try:
                                _update_media_db(mid, {'linked_media': json.dumps(lm)})
                                #print(f"[DEBUG][update_object] Synced linked_media for media_id={mid}: {lm}")
                            except Exception as e:
                                print(f"[WARNING][update_object] failed to persist linked_media: {e}")
                        except Exception as e:
                            print(f"[WARNING][update_object] failed to sync linked_media: {e}")
            except Exception as e:
                print(f"[WARNING][update_object] link sync failed: {e}")
    except Exception as e:
        print(f"[ERROR][update_object] failed to update media table: {e}")
        # Return object in error state but don't crash
        return obj

    if doc_updates:
        try:
            from server.db.db_crud import update_document_db
            #print(f"[DEBUG][update_object] Updating documents table id={getattr(obj,'id',None)} with {doc_updates}")
            result = update_document_db(getattr(obj, "id", None), doc_updates)
            if not result:
                print(f"[WARNING][update_object] documents table update returned False for id={getattr(obj,'id',None)}")
        except Exception as e:
            print(f"[ERROR][update_object] failed to update documents table: {e}")
            # Return object in error state but don't crash
            return obj

    #print(f"[DEBUG][update_object] ===== END ===== Object after DB update {obj}")
    return obj

def delete_object(obj: Media):
    #print(f"[DEBUG][delete_object] Deleting object {obj}")
    obj.delete()
    #print(f"[DEBUG][delete_object] Deleted object {obj}")
    return {"success": True}

# =========================
# SONG SERVICES
# =========================
# MEDIA SERVICES (Generic - formerly type-specific)
# =========================

# Generic create that dispatches to type-specific logic
def create_media_services(user_obj, data: dict = None, **kwargs):
    """Generic media creation that handles song, document, video, concert types."""
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    # Data now uses canonical field names from client
    #print(f"\n[DEBUG][create_media_services] ===== START =====")
    #print(f"[DEBUG][create_media_services] Input payload keys: {list(data.keys())}")

    media_type = data.get("type", "song").lower()

    if media_type == "song":
        return create_song_services(user_obj, data)
    elif media_type == "document":
        return create_document_services(user_obj, data)
    elif media_type == "video":
        return create_video_services(user_obj, data)
    elif media_type == "concert":
        return create_concert_services(user_obj, data)
    else:
        return {"error": f"Unknown media type: {media_type}"}

def get_media_services(user_obj, media_id: int):
    """Generic media fetch."""
    return get_object(Media, media_id)

def update_media_services(user_obj, media_id: int, updates: dict):
    """Generic media update."""
    #print(f"[DEBUG][update_media_services] START - media_id={media_id} (type={type(media_id).__name__}), updates keys={list(updates.keys()) if isinstance(updates, dict) else 'not a dict'}")
    try:
        # Ensure media_id is an integer
        if isinstance(media_id, str):
            try:
                media_id = int(media_id)
                #print(f"[DEBUG][update_media_services] Converted media_id from string to int: {media_id}")
            except ValueError as e:
                #print(f"[ERROR][update_media_services] Failed to convert media_id '{media_id}' to int: {e}")
                return {"error": f"Invalid media_id: {media_id}"}
        
        #print(f"[DEBUG][update_media_services] Fetching media object for id={media_id}")
        media = get_object(Media, media_id)
        #print(f"[DEBUG][update_media_services] Fetched media: {media}")
        if not media:
            #print(f"[ERROR][update_media_services] Media not found for id={media_id}")
            return {"error": "Media not found"}
        
        # CRITICAL FIX: Convert all relation field names to IDs IMMEDIATELY
        # This ensures update_object ONLY receives integer IDs, not string names
        #print(f"[DEBUG][update_media_services] Converting relation names to IDs")
        updates = convert_relation_names_to_ids(updates)
        #print(f"[DEBUG][update_media_services] After name→ID conversion, updates: {updates}")
        
        #print(f"[DEBUG][update_media_services] Calling update_object with {len(updates)} updates (all relations are now IDs)")
        result = update_object(media, updates)
        #print(f"[DEBUG][update_media_services] update_object returned: {result}")
        return result
    except Exception as e:
        import traceback
        #print(f"[ERROR][update_media_services] Exception: {e}")
        traceback.print_exc()
        return {"error": str(e)}

def delete_media_services(user_obj, media_id: int):
    """Generic media delete."""
    media = get_object(Media, media_id)
    if not media:
        return {"error": "Media not found"}
    return delete_object(media)

# Legacy type-specific service names that delegate to generic or type-specific implementations
def get_song_services(user_obj, song_id: int):
    #print(f"[DEBUG][get_song_services] song_id={song_id}")
    return get_object(Media, song_id)

def create_song_services(user_obj, data: dict = None, **kwargs):
    # Accept either a single data dict or keyword args (dispatcher may unpack)
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        # unexpected shapes: treat kwargs as the payload
        data = dict(kwargs)

    # Data now uses canonical field names from client
    #print(f"\n[DEBUG][create_song_services] ===== SONG CREATION =====")
    #print(f"[DEBUG][create_song_services] user_obj={user_obj}, data keys={list(data.keys())}")

    # normalize alternate keys and aliases
    if 'i_am_author' in data and 'is_author' not in data:
        data['is_author'] = bool(data.pop('i_am_author'))
    if 'i_am_performer' in data and 'is_performer' not in data:
        data['is_performer'] = bool(data.pop('i_am_performer'))
    if 'is_composer' in data and 'is_author' not in data:
        data['is_author'] = bool(data.get('is_composer'))

    # year aliases
    if 'publication_year' in data and 'year' not in data:
        try:
            data['year'] = int(data.get('publication_year')) if data.get('publication_year') else None
        except Exception:
            data['year'] = None
    if 'composition_year' in data and 'year' not in data:
        try:
            data['year'] = int(data.get('composition_year')) if data.get('composition_year') else None
        except Exception:
            pass

    # single-string genre -> list
    if 'genre' in data and 'genres' not in data:
        g = data.get('genre')
        if isinstance(g, str):
            data['genres'] = [s.strip() for s in g.split(',') if s.strip()]
        elif isinstance(g, (list, tuple)):
            data['genres'] = list(g)

    # Normalize 'genres' when provided as a single comma-separated string (client may send this)
    if 'genres' in data and isinstance(data.get('genres'), str):
        try:
            data['genres'] = [s.strip() for s in data.get('genres', '').split(',') if s.strip()]
        except Exception:
            # leave as-is on failure; ensure it's not iterated as characters later
            data['genres'] = [data.get('genres')]

    # support publish-on-behalf: map on_behalf_of or target_username -> user_id if present
    behalf_username = data.get('target_username') or data.get('on_behalf_of')
    if behalf_username:
        try:
            ob = str(behalf_username).strip()
            if ob:
                uid = get_user_id_by_username(ob)
                if uid:
                    data['user_id'] = uid
                    #print(f"[create_song_services] Publishing on behalf of '{ob}' (user_id={uid})")
                else:
                    print(f"[create_song_services] target username '{ob}' not found")
        except Exception as e:
            print(f"[create_song_services] error resolving target_username: {e}")

    data["type"] = "song"
    # only set creator from actor if not explicitly publishing on behalf of someone
    if data.get("user_id") is None and user_obj:
        uid = user_obj.get("id") if isinstance(user_obj, dict) else getattr(user_obj, "id", None)
        if uid:
            data["user_id"] = uid
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/songs"

    # handle automatic metadata (duration/format)
    def _parse_duration(d):
        import re
        if d is None:
            return None
        if isinstance(d, (int, float)):
            return int(round(float(d)))
        s = str(d).strip()
        if ':' in s:
            try:
                parts = [int(p) for p in s.split(':')]
            except Exception:
                parts = []
            if len(parts) == 2:
                return parts[0] * 60 + parts[1]
            if len(parts) == 3:
                return parts[0] * 3600 + parts[1] * 60 + parts[2]
        import re
        m = re.search(r"([0-9]+(?:\.[0-9]+)?)", s)
        if m:
            try:
                return int(round(float(m.group(1))))
            except Exception:
                return None
        return None

    auto = data.get("automatic")
    if isinstance(auto, dict):
        if data.get("duration") is None and auto.get("duration") is not None:
            dur = _parse_duration(auto.get("duration"))
            if dur is not None:
                data["duration"] = dur
        if auto.get("format") is not None:
            data["file_format"] = auto.get("format")
            try:
                import json as _json
                info = {"detected_format": auto.get("format")}
                if data.get("additional_info"):
                    try:
                        existing = _json.loads(data.get("additional_info"))
                        if isinstance(existing, dict):
                            existing.update(info)
                            data["additional_info"] = _json.dumps(existing)
                        else:
                            data["additional_info"] = _json.dumps(info)
                    except Exception:
                        data["additional_info"] = _json.dumps(info)
                else:
                    data["additional_info"] = _json.dumps(info)
            except Exception:
                data["additional_info"] = f"format:{auto.get('format')}"

    if "performers" in data:
        # normalize performers to list of ids (db expects ids)
        try:
            perf_ids = prepare_performers(data["performers"])
        except Exception as e:
            return {"status": "ERROR", "error_msg": f"performers normalization failed: {e}"}
        # validate/repair performer ids: ensure we have performer rows for each
        from server.db.db_crud import fetch_one, get_or_create_performer_for_user
        final_pids = []
        seen = set()
        for pid in perf_ids:
            row = fetch_one("SELECT id FROM performers WHERE id=%s", (pid,))
            if row:
                nid = int(row['id'])
            else:
                # pid may be a user id: try to create a performer for that user
                urow = fetch_one("SELECT id, username FROM users WHERE id=%s", (pid,))
                if urow and urow.get('id'):
                    creator_uid = urow['id']
                    pname = urow.get('username') or str(creator_uid)
                    nid = get_or_create_performer_for_user(creator_uid, pname)
                    if nid is None:
                        return {"status": "ERROR", "error_msg": f"Unable to create performer entry for user id {creator_uid}"}
                else:
                    return {"status": "ERROR", "error_msg": f"Performer id {pid} does not exist"}
            if nid not in seen:
                seen.add(nid)
                final_pids.append(nid)
        data["performers"] = final_pids

    # Build object using generic Media class
    song = Media.from_dict(data)

    # Ensure the song's owner matches the requested owner (on_behalf or actor)
    if data.get('user_id') is not None:
        song.user_id = data.get('user_id')

    # Save in DB
    created_id = song.save()
    if not created_id:
        return {"status": "ERROR", "error_msg": "Failed to persist song"}
    return song

def update_song_services(user_obj, song_id: int, updates: dict):
    #print(f"[DEBUG][update_song_services] song_id={song_id}, updates={updates}")
    song = get_object(Media, song_id)
    if not song:
        #print("[DEBUG][update_song_services] Song not found")
        return {"error": "Song not found"}
    try:
        if isinstance(updates, dict):
            updates = convert_relation_names_to_ids(updates)
    except Exception as e:
        print(f"[WARNING][update_song_services] name->id conversion failed: {e}")
    return update_object(song, updates)

def delete_song_services(user_obj, song_id: int):
    #print(f"[DEBUG][delete_song_services] song_id={song_id}")
    song = get_object(Media, song_id)
    if not song:
        #print("[DEBUG][delete_song_services] Song not found")
        return {"error": "Song not found"}
    return delete_object(song)

# =========================
# DOCUMENT SERVICES
# =========================
def create_document_services(user_obj, data: dict = None, **kwargs):
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    # Data now uses canonical field names from client

    # support publish-on-behalf: map target_username -> user_id if present
    behalf_username = data.get('target_username') or data.get('on_behalf_of')
    if behalf_username:
        try:
            ob = str(behalf_username).strip()
            if ob:
                uid = get_user_id_by_username(ob)
                if uid:
                    data['user_id'] = uid
                    #print(f"[create_document_services] Publishing on behalf of '{ob}' (user_id={uid})")
                else:
                    print(f"[create_document_services] target username '{ob}' not found")
        except Exception as e:
            print(f"[create_document_services] error resolving target_username: {e}")

    # map automatic into document fields
    auto = data.get("automatic")
    if isinstance(auto, dict):
        if auto.get("format") and not data.get("format"):
            data["format"] = auto.get("format")
        if auto.get("pages") and not data.get("pages"):
            try:
                data["pages"] = int(auto.get("pages"))
            except Exception:
                pass

    # if linked_to is present, inherit owner from the linked media
    if data.get('linked_to'):
        try:
            from server.db.db_crud import fetch_one
            lm = fetch_one("SELECT user_id FROM media WHERE id=%s", (data.get('linked_to'),))
            if lm and lm.get('user_id'):
                data['user_id'] = lm['user_id']
        except Exception as e:
            print(f"[create_document_services] unable to inherit owner from linked media: {e}")

    # normalize single-string genre alias
    if 'genre' in data and 'genres' not in data:
        g = data.get('genre')
        if isinstance(g, str):
            data['genres'] = [s.strip() for s in g.split(',') if s.strip()]
        elif isinstance(g, (list, tuple)):
            data['genres'] = list(g)

    # Normalize 'genres' when provided as a single comma-separated string
    if 'genres' in data and isinstance(data.get('genres'), str):
        try:
            data['genres'] = [s.strip() for s in data.get('genres', '').split(',') if s.strip()]
        except Exception:
            data['genres'] = [data.get('genres')]

    data["type"] = "document"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/documents"

    return create_object(Media, user_obj, data)

def get_document_services(user_obj, doc_id: int):
    # Fetch the object first
    obj = get_object(Media, doc_id)
    try:
        if obj and getattr(obj, 'type', None) == 'document':
            pages = getattr(obj, 'pages', None)
            fmt = getattr(obj, 'format', None)
            if pages is None or fmt is None:
                # try to probe and persist missing metadata
                try:
                    path = _resolve_storage_file(getattr(obj, 'stored_at', None), 'document')
                    updates = {}
                    if path and os.path.isfile(path):
                        try:
                            probed = _probe_pdf_pages(path)
                            if probed and pages is None:
                                updates['pages'] = int(probed)
                        except Exception as e:
                            print(f"[DEBUG][get_document_services] _probe_pdf_pages failed: {e}")
                        try:
                            _, ext = os.path.splitext(path)
                            inferred = ext.lower().lstrip('.') if ext else None
                            if inferred and fmt is None:
                                updates['format'] = inferred
                        except Exception:
                            pass

                    if updates:
                        try:
                            from server.db.db_crud import update_document_db
                            update_document_db(getattr(obj, 'id', None), updates)
                            for k, v in updates.items():
                                try:
                                    setattr(obj, k, v)
                                except Exception:
                                    pass
                            print(f"[DEBUG][get_document_services] persisted fixes: {updates}")
                        except Exception as e:
                            print(f"[WARNING][get_document_services] failed to persist fixes: {e}")
                except Exception as e:
                    print(f"[DEBUG][get_document_services] probe attempt failed: {e}")
    except Exception:
        pass
    return obj


def fix_document_metadata_services(user_obj, media_id: int):
    """RPC to force probing of a document's stored file and persist pages/format."""
    try:
        obj = get_object(Media, media_id)
        if not obj:
            return {"status": "ERROR", "error_msg": "Document not found"}
        if getattr(obj, 'type', None) != 'document':
            return {"status": "ERROR", "error_msg": "Not a document"}
        path = _resolve_storage_file(getattr(obj, 'stored_at', None), 'document')
        updates = {}
        if path and os.path.isfile(path):
            try:
                probed = _probe_pdf_pages(path)
                if probed and getattr(obj, 'pages', None) is None:
                    updates['pages'] = int(probed)
            except Exception as e:
                print(f"[DEBUG][fix_document_metadata_services] _probe_pdf_pages failed: {e}")
            try:
                _, ext = os.path.splitext(path)
                inferred = ext.lower().lstrip('.') if ext else None
                if inferred and getattr(obj, 'format', None) is None:
                    updates['format'] = inferred
            except Exception:
                pass

        if updates:
            try:
                from server.db.db_crud import update_document_db
                update_document_db(getattr(obj, 'id', None), updates)
                return {"status": "OK", "updated": updates}
            except Exception as e:
                #print(f"[WARNING][fix_document_metadata_services] failed to persist updates: {e}")
                return {"status": "ERROR", "error_msg": str(e)}
        return {"status": "OK", "updated": {}}
    except Exception as e:
        #print(f"[ERROR][fix_document_metadata_services] Exception: {e}")
        return {"status": "ERROR", "error_msg": str(e)}

def update_document_services(user_obj, doc_id: int, updates: dict):
    doc_obj = get_object(Media, doc_id)
    if not doc_obj:
        return {"error": "Document not found"}
    try:
        if isinstance(updates, dict):
            updates = convert_relation_names_to_ids(updates)
    except Exception as e:
        print(f"[WARNING][update_document_services] name->id conversion failed: {e}")
    return update_object(doc_obj, updates)

def delete_document_services(user_obj, doc_id: int):
    doc_obj = get_object(Media, doc_id)
    if not doc_obj:
        return {"error": "Document not found"}
    return delete_object(doc_obj)

# =========================
# VIDEO SERVICES
# =========================
def create_video_services(user_obj, data: dict = None, **kwargs):
    #print(f"\n[DEBUG][create_video_services] ===== START =====")
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    # Data now uses canonical field names from client
    #print(f"[DEBUG][create_video_services] Input data keys: {list(data.keys())}")
    #print(f"[DEBUG][create_video_services] year={data.get('year')}, description={data.get('description')}, location={data.get('location')}")
    #print(f"[DEBUG][create_video_services] recording_date={data.get('recording_date')}, additional_info={data.get('additional_info')}")
    #print(f"[DEBUG][create_video_services] is_author={data.get('is_author')}, is_performer={data.get('is_performer')}")

    # support publish-on-behalf: map target_username -> user_id if present
    behalf_username = data.get('target_username') or data.get('on_behalf_of')
    if behalf_username:
        try:
            ob = str(behalf_username).strip()
            if ob:
                uid = get_user_id_by_username(ob)
                if uid:
                    data['user_id'] = uid
                    #print(f"[create_video_services] Publishing on behalf of '{ob}' (user_id={uid})")
                else:
                    print(f"[create_video_services] target username '{ob}' not found")
        except Exception as e:
            print(f"[create_video_services] error resolving target_username: {e}")

    # handle automatic metadata
    auto = data.get("automatic")
    if isinstance(auto, dict):
        if data.get("duration") is None and auto.get("duration") is not None:
            try:
                data["duration"] = int(round(float(auto.get("duration"))))
            except Exception:
                pass

    # Normalize single-string genre alias
    if 'genre' in data and 'genres' not in data:
        g = data.get('genre')
        if isinstance(g, str):
            data['genres'] = [s.strip() for s in g.split(',') if s.strip()]
        elif isinstance(g, (list, tuple)):
            data['genres'] = list(g)

    # Normalize 'genres' when provided as a single comma-separated string
    if 'genres' in data and isinstance(data.get('genres'), str):
        try:
            data['genres'] = [s.strip() for s in data.get('genres', '').split(',') if s.strip()]
        except Exception:
            data['genres'] = [data.get('genres')]

    data["type"] = "video"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/videos"
    
    #print(f"[DEBUG][create_video_services] Final data keys: {list(data.keys())}")
    result = create_object(Media, user_obj, data)
    #print(f"[DEBUG][create_video_services] ===== COMPLETE =====\n")
    return result


# =========================
# CONCERT SERVICES
# =========================

def _extract_user_lvl(user_obj):
    viewer_lvl_raw = user_obj.get("lvl") if isinstance(user_obj, dict) else getattr(user_obj, "lvl", None)
    viewer_lvl = int(viewer_lvl_raw) if isinstance(viewer_lvl_raw, (int, float, str)) and str(viewer_lvl_raw).isdigit() else None
    return viewer_lvl


def create_concert_services(user_obj, data: dict = None, **kwargs):
    #print(f"\n[DEBUG][create_concert_services] ===== START =====")
    if data is None:
        data = {}
    if isinstance(data, dict) and kwargs:
        data = {**data, **kwargs}
    elif not isinstance(data, dict) and kwargs:
        data = dict(kwargs)

    # Data now uses canonical field names from client
    #print(f"[DEBUG][create_concert_services] Input data keys: {list(data.keys())}")
    #print(f"[DEBUG][create_concert_services] year={data.get('year')}, description={data.get('description')}, location={data.get('location')}")
    #print(f"[DEBUG][create_concert_services] recording_date={data.get('recording_date')}, additional_info={data.get('additional_info')}")
    #print(f"[DEBUG][create_concert_services] is_author={data.get('is_author')}, is_performer={data.get('is_performer')}")

    # support publish-on-behalf: map target_username -> user_id if present
    behalf_username = data.get('target_username') or data.get('on_behalf_of')
    if behalf_username:
        try:
            ob = str(behalf_username).strip()
            if ob:
                uid = get_user_id_by_username(ob)
                if uid:
                    data['user_id'] = uid
                    #print(f"[create_concert_services] Publishing on behalf of '{ob}' (user_id={uid})")
                else:
                    print(f"[create_concert_services] target username '{ob}' not found")
        except Exception as e:
            print(f"[create_concert_services] error resolving target_username: {e}")

    data["type"] = "concert"
    if data.get("stored_at") is None:
        data["stored_at"] = "server/storage/videos"

    # disallow banned users (lvl 6) from creating concerts
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl == 6:
        return {"error": "Insufficient permissions to create concert"}

    #print(f"[DEBUG][create_concert_services] Calling create_object with data keys: {list(data.keys())}")
    # create concert media and concerts row will be created inside create_media_db
    concert = create_object(Media, user_obj, data)
    #print(f"[DEBUG][create_concert_services] ===== COMPLETE =====\n")
    return concert


def get_concert_services(user_obj, video_id: int):
    #print(f"[DEBUG][get_concert_services] user={user_obj}, video_id={video_id}")
    # Fetch concert data from database
    concert_data = fetch_concert_by_video_id(video_id)
    if not concert_data:
        return None
    # Return the concert as a generic Media object
    return Media.from_dict(concert_data)


def add_concert_segment_services(user_obj, video_id: int, segment_data: dict):
    #print(f"[DEBUG][add_concert_segment_services] user={user_obj}, video_id={video_id}, segment_data={segment_data}")
    # user must not be RESTRICTED or BANNED (lvl 5 or 6)
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl in (5, 6):
        #print(f"[DEBUG][add_concert_segment_services] permission denied for user lvl={lvl}")
        return {"error": "Insufficient permissions to add concert metadata"}

    concert = fetch_concert_by_video_id(video_id)
    #print(f"[DEBUG][add_concert_segment_services] fetched concert: {concert!r}")
    if not concert:
        #print(f"[DEBUG][add_concert_segment_services] concert not found for video_id={video_id}")
        return {"error": "Concert not found"}
    concert_id = concert.get("video_id")
    #print(f"[DEBUG][add_concert_segment_services] concert_id={concert_id}")

    # normalize performers -> ids
    performers_in = segment_data.get("performers")
    performers_ids = None
    if performers_in:
        try:
            performers_ids = prepare_performers(performers_in)
        except Exception:
            performers_ids = None

    # normalize instruments -> ids (create if needed)
    instruments_in = segment_data.get("instruments")
    instruments_ids = None
    if instruments_in:
        instruments_ids = []
        for itm in (instruments_in if isinstance(instruments_in, (list, tuple)) else [instruments_in]):
            try:
                if isinstance(itm, int):
                    instruments_ids.append(itm)
                elif isinstance(itm, dict) and itm.get("id"):
                    instruments_ids.append(int(itm.get("id")))
                else:
                    name = str(itm).strip()
                    if not name:
                        continue
                    # attempt to find existing
                    row = fetch_dict_entry("instruments", name)
                    if row and row.get("id"):
                        instruments_ids.append(row.get("id"))
                    else:
                        nid = create_dict_entry("instruments", name)
                        if nid:
                            instruments_ids.append(nid)
            except Exception:
                continue

    #print(f"[DEBUG][add_concert_segment_services] performers_ids={performers_ids}, instruments_ids={instruments_ids}")
    seg_id = create_concert_segment_db(
        concert_id=concert_id,
        media_id=segment_data.get("media_id"),
        song_title=segment_data.get("song_title"),
        start_time=segment_data.get("start_time"),
        end_time=segment_data.get("end_time"),
        comment=segment_data.get("comment"),
        performers=performers_ids,
        instruments=instruments_ids,
    )
    if not seg_id:
        #print(f"[DEBUG][add_concert_segment_services] failed to create segment for concert_id={concert_id}")
        return {"error": "Failed to create segment"}
    #print(f"[DEBUG][add_concert_segment_services] created segment_id={seg_id} for concert_id={concert_id}")
    return {"segment_id": seg_id}


def get_concert_segments_services(user_obj, video_id: int):
    #print(f"[DEBUG][get_concert_segments_services] user={user_obj}, video_id={video_id}")
    concert = fetch_concert_by_video_id(video_id)
    #print(f"[DEBUG][get_concert_segments_services] fetched concert: {concert!r}")
    if not concert:
        #print(f"[DEBUG][get_concert_segments_services] no concert found for video_id={video_id}")
        return []
    concert_id = concert.get("video_id")
    res = fetch_concert_segments_db(concert_id)
    #print(f"[DEBUG][get_concert_segments_services] returning {len(res) if isinstance(res, list) else 'unknown'} segments for concert_id={concert_id}")
    return res


def update_concert_segment_services(user_obj, segment_id: int, updates: dict):
    #print(f"[DEBUG][update_concert_segment_services] user={user_obj}, segment_id={segment_id}, updates={updates}")
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl in (5, 6):
        #print(f"[DEBUG][update_concert_segment_services] permission denied for user lvl={lvl}")
        return {"error": "Insufficient permissions to update concert metadata"}
    ok = update_concert_segment_db(segment_id, updates)
    #print(f"[DEBUG][update_concert_segment_services] update result for segment_id={segment_id}: {ok}")
    return {"success": ok}


def delete_concert_segment_services(user_obj, segment_id: int):
    #print(f"[DEBUG][delete_concert_segment_services] user={user_obj}, segment_id={segment_id}")
    lvl = _extract_user_lvl(user_obj) if user_obj else None
    if lvl in (5, 6):
        #print(f"[DEBUG][delete_concert_segment_services] permission denied for user lvl={lvl}")
        return {"error": "Insufficient permissions to delete concert metadata"}
    ok = delete_concert_segment_db(segment_id)
    #print(f"[DEBUG][delete_concert_segment_services] delete result for segment_id={segment_id}: {ok}")
    return {"success": ok}

def get_video_services(user_obj, video_id: int):
    #print(f"[DEBUG][get_video_services] user={user_obj}, video_id={video_id}")
    return get_object(Media, video_id)

def update_video_services(user_obj, video_id: int, updates: dict):
    #print(f"[DEBUG][update_video_services] user={user_obj}, video_id={video_id}, updates={updates}")
    video = get_object(Media, video_id)
    if not video:
        #print(f"[DEBUG][update_video_services] video not found for id={video_id}")
        return {"error": "Video not found"}
    try:
        if isinstance(updates, dict):
            updates = convert_relation_names_to_ids(updates)
    except Exception as e:
        print(f"[WARNING][update_video_services] name->id conversion failed: {e}")
    res = update_object(video, updates)
    #print(f"[DEBUG][update_video_services] update result for video_id={video_id}: {res}")
    return res

def update_concert_services(user_obj, concert_id: int, updates: dict):
    """
    Update a concert media record.
    Preserves concert-type identity and updates concert-specific fields (link, title, description)
    in the concerts table in addition to media table updates.
    
    SAFETY: Only allows updates to non-relational fields to prevent accidental data loss.
    Relation updates (authors, performers, genres) must be explicitly provided.
    """
    #print(f"[DEBUG][update_concert_services] user={user_obj}, concert_id={concert_id}, updates={updates}")
    
    # Fetch current concert to ensure it exists
    concert = get_object(Media, concert_id)
    if not concert:
        #print(f"[DEBUG][update_concert_services] concert not found for id={concert_id}")
        return {"error": "Concert not found", "status": "ERROR"}
    
    # Make updates copy to avoid mutating original
    safe_updates = updates.copy() if updates else {}
    
    # Enforce concert type (never allow type to change)
    if 'type' in safe_updates and safe_updates['type'] != 'concert':
        #print(f"[DEBUG][update_concert_services] ignoring type change attempt from {safe_updates['type']} to concert")
        safe_updates['type'] = 'concert'
    
    try:
        try:
            if isinstance(safe_updates, dict):
                safe_updates = convert_relation_names_to_ids(safe_updates)
        except Exception as e:
            print(f"[WARNING][update_concert_services] name->id conversion failed: {e}")
        res = update_object(concert, safe_updates)
        #print(f"[DEBUG][update_concert_services] update_object result: {res}")
        
        # Also update concert-specific fields in concerts table
        if concert_id and safe_updates:
            try:
                from server.db import db_crud
                concert_updates = {}
                if 'link' in safe_updates:
                    concert_updates['link'] = safe_updates['link']
                if 'title' in safe_updates:
                    concert_updates['title'] = safe_updates['title']
                if 'description' in safe_updates:
                    concert_updates['description'] = safe_updates['description']
                
                if concert_updates:
                    success = db_crud.execute(
                        """UPDATE concerts SET link=%s, title=%s, description=%s WHERE video_id=%s""",
                        (concert_updates.get('link'), concert_updates.get('title'), concert_updates.get('description'), concert_id)
                    )
                    if success:
                        # print(f"[DEBUG][update_concert_services] updated concerts table with {concert_updates}")
                        pass
                    else:
                        print(f"[WARNING][update_concert_services] concerts table update returned False")
            except Exception as e:
                print(f"[WARNING][update_concert_services] failed to update concerts table: {e}")
        
        return {"status": "OK", "id": concert_id}
    except Exception as e:
        #print(f"[ERROR][update_concert_services] update failed: {e}")
        # Return error but don't crash - allow client to retry
        return {"error": str(e), "status": "ERROR"}

def delete_video_services(user_obj, video_id: int):
    #print(f"[DEBUG][delete_video_services] user={user_obj}, video_id={video_id}")
    video = get_object(Media, video_id)
    if not video:
        #print(f"[DEBUG][delete_video_services] video not found for id={video_id}")
        return {"error": "Video not found"}
    res = delete_object(video)
    #print(f"[DEBUG][delete_video_services] delete result for video_id={video_id}: {res}")
    return res


def delete_concert_services(user_obj, concert_id: int):
    """Delete a concert media record (cascades to concerts table via foreign key)."""
    #print(f"[DEBUG][delete_concert_services] user={user_obj}, concert_id={concert_id}")
    concert = get_object(Media, concert_id)
    if not concert:
        #print(f"[DEBUG][delete_concert_services] concert not found for id={concert_id}")
        return {"error": "Concert not found"}
    res = delete_object(concert)
    #print(f"[DEBUG][delete_concert_services] delete result for concert_id={concert_id}: {res}")
    return res

# ========================
# SUPPORT
# =========================
def prepare_performers(performers: list) -> list:
    """Normalize performers into a list of performer IDs.
    Accepts several shapes:
      - list of dicts: {type:'user', id: <int>} or {type:'external', name: '...'}
      - list of ints: treated as performer ids
      - list of strings: treated as usernames (try resolve to user id) or external names
    """
    result_ids = []
    # handle comma-separated single string
    items = []
    if isinstance(performers, str):
        items = [s.strip() for s in performers.split(",") if s.strip()]
    elif isinstance(performers, (list, tuple)):
        items = list(performers)
    else:
        raise ValueError("Unsupported performers container")

    from server.db.db_crud import get_or_create_performer_for_user
    for p in items:
        # handle dict entries (existing behavior)
        if isinstance(p, dict):
            if p.get("type") == "user":
                if "id" in p:
                    uid = int(p["id"])
                    # ensure performer entry exists for user
                    pid = get_or_create_performer_for_user(uid, p.get("username") or str(uid))
                    if pid is None:
                        raise ValueError(f"Unable to map user performer id {uid} to performer entry")
                    result_ids.append(pid)
                elif "username" in p:
                    # try to resolve username
                    uname = p["username"].strip()
                    uid = get_user_id_by_username(uname)
                    if uid:
                        pid = get_or_create_performer_for_user(uid, uname)
                        if pid is None:
                            raise ValueError(f"Unable to create/fetch performer for user '{uname}'")
                        result_ids.append(pid)
                    else:
                        raise ValueError(f"Unable to resolve user performer '{uname}'")
            elif p.get("type") == "external":
                name = p.get("name")
                existing = fetch_dict_entry("performers", name)
                if existing:
                    pid = existing["id"]
                else:
                    pid = create_dict_entry("performers", name)
                if pid is None:
                    raise ValueError(f"Unable to create/fetch external performer '{name}'")
                result_ids.append(pid)
            else:
                raise ValueError(f"Tipo performer non valido: {p.get('type')}")

        # handle integers (assume performer id)
        elif isinstance(p, int):
            result_ids.append(int(p))

        # handle strings: try username -> user id -> performer, otherwise treat as external name
        elif isinstance(p, str):
            pstr = p.strip()
            if not pstr:
                continue
            # comma separated list in a single string
            if "," in pstr:
                for sub in [s.strip() for s in pstr.split(',') if s.strip()]:
                    uid = get_user_id_by_username(sub)
                    if uid:
                        pid = get_or_create_performer_for_user(uid, sub)
                        if pid is None:
                            raise ValueError(f"Unable to create/fetch performer for user '{sub}'")
                        result_ids.append(pid)
                    else:
                        existing = fetch_dict_entry("performers", sub)
                        if existing:
                            result_ids.append(existing["id"])
                        else:
                            pid = create_dict_entry("performers", sub)
                            if pid is None:
                                raise ValueError(f"Unable to create/fetch external performer '{sub}'")
                            result_ids.append(pid)
                continue

            uid = get_user_id_by_username(pstr)
            if uid:
                pid = get_or_create_performer_for_user(uid, pstr)
                if pid is None:
                    raise ValueError(f"Unable to create/fetch performer for user '{pstr}'")
                result_ids.append(pid)
            else:
                # external performer fallback
                existing = fetch_dict_entry("performers", pstr)
                if existing:
                    pid = existing["id"]
                else:
                    pid = create_dict_entry("performers", pstr)
                if pid is None:
                    raise ValueError(f"Unable to create/fetch external performer '{pstr}'")
                result_ids.append(pid)

        else:
            raise ValueError("Unsupported performer format")

    # dedupe while preserving order
    seen = set()
    final = []
    for i in result_ids:
        if i not in seen:
            seen.add(i)
            final.append(i)
    return final

def get_feed_services(user_obj, search: str = "", filter_by: str = "all", offset: int = 0, limit: int = 10):
    #print(f"[DEBUG] feed request received offset={offset}, limit={limit}, search='{search}', filter_by='{filter_by}'")

    # Pull a larger batch per media type (no per-type offset) then do global pagination.
    per_type_limit = max(offset + limit * 2, limit)  # fetch enough from each type to cover the requested window

    def fetch_media(media_type):
        """Fetch all media of a specific type using generic Media.fetch_all()"""
        return Media.fetch_all(search=search, filter_by=filter_by, offset=0, limit=per_type_limit, media_type=media_type)

    # Fetch media by type from DB
    songs = fetch_media("song")
    videos = fetch_media("video")
    documents = fetch_media("document")
    concerts = fetch_media("concert")

    # Combina risultati and include created_at for global ordering
    from server.db.db_crud import get_user_username_by_id as duck

    combined = []
    for m in songs + videos + documents + concerts:
        d = m.to_dict()
        user_id = d.get("user_id")
        username = duck(user_id)
        created = d.get("created_at")
        # normalize created_at to a comparable string if possible
        if hasattr(created, "isoformat"):
            created_iso = created.isoformat()
        else:
            created_iso = str(created) if created is not None else ""
        combined.append({
            "id": d.get("id"),
            "title": d.get("title"),
            "username": username or "Unknown",
            "thumbnail": d.get("thumbnail", "https://via.placeholder.com/100"),
            "tags": d.get("genres") or d.get("keywords") or [],
            "type": d.get("type"),
            "created_at": created_iso,
            "raw": d
        })

    # global ordering (newest first)
    combined.sort(key=lambda x: x.get("created_at") or "", reverse=True)

    total_count = len(combined)
    paged = combined[offset:offset + limit]

    # remove created_at/raw if you want to keep response small; keep them now for flexibility
    results = paged

    return {"status": "OK", "results": results, "count": total_count}


def composed_query_services(user_obj, composed: str, offset: int = 0, limit: int = 10):
    """Parse a composed query string (field:value;field2:val1,val2;...) and
    return media that satisfy ALL provided conditions (logical AND across fields
    and across comma-separated tokens within the same field).

    Supported fields (client UI): date, date_from, date_to, tag/genre, author,
    performer, instrument, user/username, title, publisher_only, from, to
    """
    if not composed or not str(composed).strip():
        return {"status": "OK", "results": [], "count": 0}

    from server.db.db_crud import fetch_all, fetch_all_media_db, get_user_username_by_id
    from datetime import datetime

    # --- parse composed string into {field: [tokens]} ---
    filters = {}
    parts = [p.strip() for p in str(composed).split(";") if p.strip()]
    for part in parts:
        if ":" not in part:
            continue
        k, v = part.split(":", 1)
        key = k.strip().lower()
        vals = [s.strip() for s in v.split(",") if s.strip()]
        if not vals:
            continue
        # normalize synonyms
        if key in ("genre", "genres"):
            key = "tag"
        if key in ("username", "user"):
            key = "publisher"
        if key in ("from",):
            key = "date_from"
        if key in ("to",):
            key = "date_to"
        filters[key] = vals

    # Helper: run a small DB query that returns media ids matching a single token for a field
    def ids_for_single_token(field: str, token: str):
        token = str(token).strip()
        if not token:
            return set()
        try:
            if field == "tag":
                # match genres by name or numeric id
                if token.isdigit():
                    rows = fetch_all("SELECT DISTINCT m.id FROM media m JOIN media_genres mg ON mg.media_id = m.id JOIN genres g ON g.id = mg.genre_id WHERE g.id = %s", (int(token),))
                else:
                    rows = fetch_all("SELECT DISTINCT m.id FROM media m JOIN media_genres mg ON mg.media_id = m.id JOIN genres g ON g.id = mg.genre_id WHERE g.name ILIKE %s", (f"%{token}%",))
                return set(r.get("id") for r in (rows or []) if r.get("id") is not None)

            if field == "author":
                if token.isdigit():
                    rows = fetch_all("SELECT DISTINCT ma.media_id AS id FROM media_authors ma JOIN authors a ON a.id = ma.author_id WHERE a.user_id = %s", (int(token),))
                else:
                    rows = fetch_all("SELECT DISTINCT ma.media_id AS id FROM media_authors ma JOIN authors a ON a.id = ma.author_id WHERE a.name ILIKE %s", (f"%{token}%",))
                return set(r.get("id") for r in (rows or []) if r.get("id") is not None)

            if field == "performer":
                if token.isdigit():
                    rows = fetch_all("SELECT DISTINCT mp.media_id AS id FROM media_performances mp JOIN performers p ON p.id = mp.performer_id WHERE p.user_id = %s", (int(token),))
                else:
                    rows = fetch_all("SELECT DISTINCT mp.media_id AS id FROM media_performances mp JOIN performers p ON p.id = mp.performer_id WHERE p.name ILIKE %s", (f"%{token}%",))
                return set(r.get("id") for r in (rows or []) if r.get("id") is not None)

            if field == "instrument":
                rows = fetch_all("SELECT DISTINCT mp.media_id AS id FROM media_performances mp JOIN performance_instruments pi ON pi.performance_id = mp.id JOIN instruments i ON i.id = pi.instrument_id WHERE i.name ILIKE %s", (f"%{token}%",))
                return set(r.get("id") for r in (rows or []) if r.get("id") is not None)

            if field == "title":
                rows = fetch_all("SELECT id FROM media WHERE title ILIKE %s", (f"%{token}%",))
                return set(r.get("id") for r in (rows or []) if r.get("id") is not None)

            if field == "publisher":
                if token.isdigit():
                    rows = fetch_all("SELECT id FROM media WHERE user_id = %s", (int(token),))
                else:
                    rows = fetch_all("SELECT m.id FROM media m JOIN users u ON u.id = m.user_id WHERE u.username ILIKE %s", (f"%{token}%",))
                return set(r.get("id") for r in (rows or []) if r.get("id") is not None)

            if field == "date":
                # reuse existing date parsing in fetch_all_media_db by calling Media.fetch_all
                # request a reasonably large limit to include all possible matches
                from server.objects.media import Media
                items = Media.fetch_all(search=token, filter_by="date", offset=0, limit=5000)
                return set(i.media_id for i in (items or []) if getattr(i, "media_id", None) is not None)

            # Fallback: broad match across media common fields (use fetch_all_media_db default 'all')
            # This supports keys that we don't explicitly handle by delegating to DB's broad matching
            from server.objects.media import Media
            items = Media.fetch_all(search=token, filter_by="all", offset=0, limit=5000)
            return set(i.media_id for i in (items or []) if getattr(i, "media_id", None) is not None)
        except Exception:
            return set()

    # For each field compute ids that match ALL tokens of that field (intersection per-field)
    per_field_sets = []
    for field, toks in filters.items():
        # special handling for date_from/date_to: defer to range filter later
        if field in ("date_from", "date_to"):
            continue
        if field == "publisher_only":
            # if publisher_only is present and truthy, ignore (handled via publisher token if provided)
            continue

        field_set = None
        for t in toks:
            ids = ids_for_single_token(field, t)
            if field_set is None:
                field_set = ids
            else:
                field_set = field_set.intersection(ids)
        # if there were no tokens or match none -> empty set
        per_field_sets.append(field_set or set())

    # If no explicit field produced candidates, return empty
    if not per_field_sets:
        return {"status": "OK", "results": [], "count": 0}

    # Intersection across fields -> only media satisfying ALL conditions
    final_ids = None
    for s in per_field_sets:
        if final_ids is None:
            final_ids = set(s)
        else:
            final_ids &= s
    final_ids = final_ids or set()

    # Apply date_from/date_to range filters if present by fetching matching medias and filtering by created_at
    if final_ids and ("date_from" in filters or "date_to" in filters):
        df = None
        dt = None
        try:
            if "date_from" in filters:
                df = datetime.fromisoformat(filters.get("date_from")[0])
            if "date_to" in filters:
                dt = datetime.fromisoformat(filters.get("date_to")[0])
        except Exception:
            # ignore parse errors and skip range filtering
            df = dt = None

        if df or dt:
            keep = set()
            for mid in list(final_ids):
                m = Media.fetch(mid)
                if not m:
                    continue
                created = getattr(m, "created_at", None)
                if isinstance(created, str):
                    try:
                        created_dt = datetime.fromisoformat(created)
                    except Exception:
                        created_dt = None
                else:
                    created_dt = created
                ok = True
                if df and created_dt and created_dt < df:
                    ok = False
                if dt and created_dt and created_dt > dt:
                    ok = False
                if ok:
                    keep.add(mid)
            final_ids = keep

    # Nothing matched
    if not final_ids:
        return {"status": "OK", "results": [], "count": 0}

    # Build result list (fetch Media objects, normalize and sort by created_at desc)
    from server.db.db_crud import get_user_username_by_id as duck
    results = []
    for mid in final_ids:
        m = Media.fetch(mid)
        if not m:
            continue
        d = m.to_dict()
        user_id = d.get("user_id")
        username = duck(user_id)
        created = d.get("created_at")
        created_iso = created.isoformat() if hasattr(created, "isoformat") else (str(created) if created is not None else "")
        results.append({
            "id": d.get("id"),
            "title": d.get("title"),
            "username": username or "Unknown",
            "thumbnail": d.get("thumbnail", "/static/images/unknown.jpg"),
            "tags": d.get("genres") or [],
            "type": d.get("type"),
            "created_at": created_iso,
            "raw": d
        })

    # global ordering (newest first)
    results.sort(key=lambda x: x.get("created_at") or "", reverse=True)

    total = len(results)
    paged = results[offset: offset + limit]

    return {"status": "OK", "results": paged, "count": total}

# =========================
# USER PUBLICATIONS SERVICES
# =========================
from server.db.db_crud import get_user_username_by_id as duck, fetch_all, fetch_one, get_user_id_by_username

def get_user_publications_services(user_obj, username: str, offset: int = 0, limit: int = 10):
    """
    Returns the list of media published by the specified username.
    Response shape: {"status":"OK", "results":[{...media...}], "count": total_count}
    """
    try:
        # Resolve username -> user_id
        uid = get_user_id_by_username(username)
        if uid is None:
            return {"status": "OK", "results": [], "count": 0}

        # fetch rows from media table for that user (ordered by created_at desc)
        query = "SELECT * FROM media WHERE user_id = %s ORDER BY created_at DESC OFFSET %s LIMIT %s;"
        rows = fetch_all(query, (uid, offset, limit))

        # total count (without pagination)
        cnt_row = fetch_one("SELECT COUNT(*) as cnt FROM media WHERE user_id = %s", (uid,))
        total_count = int(cnt_row["cnt"]) if cnt_row and "cnt" in cnt_row else len(rows)

        # small helper: infer type when DB row misses it
        def _infer_type_from_row(row: dict) -> str:
            if not row:
                return "unknown"
            t = (row.get("type") or row.get("media_type") or "").strip().lower()
            if t:
                # normalize common synonyms
                if t in ("audio","music","song"): return "song"
                if t in ("video","movie"): return "video"
                if t in ("document","doc","pdf"): return "document"
                return t
            stored = (row.get("stored_at") ).lower()
            if any(stored.endswith(ext) for ext in (".mp3",".wav",".m4a",".ogg",".flac")) or "/songs" in stored or "/audio" in stored:
                return "song"
            if any(stored.endswith(ext) for ext in (".mp4",".mov",".webm",".avi",".mkv")) or "/videos" in stored:
                return "video"
            if any(stored.endswith(ext) for ext in (".pdf",".docx",".doc",".txt",".odt",".pptx")) or "/documents" in stored:
                return "document"
            return "unknown"

        # Normalize rows into dicts with serializable fields using Media.from_dict -> to_dict
        results = []
        for r in rows:
            try:
                media_obj = Media.from_dict(dict(r))
                media_dict = media_obj.to_dict()
                # ensure 'type' present and normalized
                media_dict["type"] = (media_dict.get("type") or _infer_type_from_row(r) or "unknown")
                results.append(media_dict)
            except Exception:
                # fallback: include raw row but ensure created_at is isoformat if present and include a type
                raw = dict(r)
                ca = raw.get("created_at")
                if hasattr(ca, "isoformat"):
                    raw["created_at"] = ca.isoformat()
                # ensure we return a 'type' field so client can pick icons like the feed
                raw["type"] = (raw.get("type") or raw.get("media_type") or _infer_type_from_row(raw) or "unknown")
                results.append(raw)

        return {"status": "OK", "results": results, "count": total_count}

    except Exception as e:
        #print(f"[ERROR][get_user_publications_services] {e}")
        return {"status": "error", "error_msg": str(e)}

def get_media_services(user_obj, media_id: int):
    try:
        # allow string ids too
        mid = int(media_id)
        media_obj = Media.fetch(mid)
        if not media_obj:
            return {"status": "error", "error_msg": "Media not found"}

        m = media_obj.to_dict()

        # publisher username
        try:
            username = duck(m.get("user_id"))
            if username:
                m["username"] = username
        except Exception:
            m["username"] = m.get("username")  # keep existing if present

        # author_names and tags are ALREADY resolved by fetch_media_db with JOINs
        # Just ensure they have sensible defaults
        if not m.get("author_names"):
            m["author_names"] = []
        if not m.get("tags"):
            m["tags"] = []

        # Build single author/tag display string if needed
        if not m.get("author"):
            author_names = m.get("author_names", [])
            if author_names:
                m["author"] = ", ".join(str(name) for name in author_names if name)
            else:
                m["author"] = m.get("username") or None

        # duration formatting (seconds -> M:SS)
        try:
            dur = m.get("duration")
            if dur is not None:
                secs = int(dur)
                m["duration_display"] = f"{secs//60}:{secs%60:02d}"
                m["duration_seconds"] = secs
            else:
                m["duration_display"] = None
                m["duration_seconds"] = None
        except Exception:
            m["duration_display"] = None
            m["duration_seconds"] = None

        # published date: expose year as 'date' (client expects date)
        if m.get("year") is not None and not m.get("date"):
            m["date"] = str(m.get("year"))

        # provide legacy 'tags' alias for client-side that may expect 'tags' instead of 'genres'
        try:
            m['tags'] = m.get('genres') if isinstance(m.get('genres'), list) else (m.get('genres') or [])
        except Exception:
            m['tags'] = m.get('genres') or []

        # If this media is a concert, fetch the full concert row (link, segments)
        try:
            if (m.get("type") or "").lower() == "concert":
                full = fetch_concert_by_video_id(mid)
                if full:
                    # merge concert-specific fields (link, segments) without removing already-computed fields
                    for k, v in full.items():
                        if v is not None:
                            m[k] = v
                # Concerts are external links; ensure no file metadata is exposed so clients don't try to fetch a file
                if (m.get("type") or "").lower() == "concert":
                    m["stored_at"] = None
                    m["filename"] = None
                    m["file_available"] = False

                # sanitize link (strip surrounding quotes/whitespace) and add/embed_url when applicable
                try:
                    link = m.get("link")
                    if isinstance(link, str) and link.strip():
                        cleaned = link.strip().strip('"').strip("'")
                        # normalize simple missing scheme
                        if cleaned and not cleaned.startswith(("http://","https://")):
                            cleaned = "https://" + cleaned
                        m["link"] = cleaned
                    else:
                        # fallback: look at stored_at or filename for a youtube link/id
                        cand = m.get("stored_at") or m.get("filename") or ""
                        if isinstance(cand, str) and cand.strip():
                            cc = cand.strip()
                            # try to extract a youTube id or full watch URL
                            import re
                            ytm_c = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cc)
                            if ytm_c:
                                vid_c = ytm_c.group(1)
                                m["link"] = f"https://www.youtube.com/watch?v={vid_c}"
                            elif "youtube.com" in cc or "youtu.be" in cc:
                                # use candidate as-is
                                m["link"] = cc
                            else:
                                m["link"] = None
                        else:
                            m["link"] = None

                    # try to extract youtube id and add embed_url and verify availability via oEmbed
                    import re
                    cleaned_link = m.get("link") or ""
                    ytm = re.search(r"(?:v=|/embed/|youtu\.be/)([A-Za-z0-9_-]{11})", cleaned_link)
                    if not ytm and cleaned_link:
                        ytm = re.search(r"youtube\.com/watch\?[^#]*v=([A-Za-z0-9_-]{11})", cleaned_link)

                    if ytm:
                        vid = ytm.group(1)
                        embed_url = f"https://www.youtube.com/embed/{vid}?rel=0"
                        # verify via YouTube oEmbed to check existence/embeddability
                        try:
                            import requests
                            o = requests.get("https://www.youtube.com/oembed", params={"url": f"https://www.youtube.com/watch?v={vid}", "format": "json"}, timeout=5)
                            if o.status_code == 200:
                                m["embed_url"] = embed_url
                                m["embed_ok"] = True
                                m["embed_error"] = None
                            else:
                                m["embed_url"] = embed_url
                                m["embed_ok"] = False
                                m["embed_error"] = f"oembed status {o.status_code}"
                        except Exception as e:
                            m["embed_url"] = embed_url
                            m["embed_ok"] = False
                            m["embed_error"] = str(e)
                    else:
                        m["embed_url"] = None
                        m["embed_ok"] = False
                        m["embed_error"] = "no valid youtube id found"
                except Exception as e:
                    m["embed_url"] = None
                    m["embed_ok"] = False
                    m["embed_error"] = str(e)
        except Exception:
            pass

        try:
            if (m.get("type") or "").lower() == "concert" and m.get("link") and not m.get("linked_media"):
                try:
                    link = m.get("link")
                    entry = {"type": "link", "source": ("youtube" if "youtube" in link.lower() else "external"), "url": link, "title": m.get("title")}
                    from server.db.db_crud import update_media_db
                    update_media_db(m.get("id") or m.get("media_id"), {"linked_media": json.dumps([entry])})
                    m["linked_media"] = [entry]
                    # debug(f"[CONCERT SYNC] persisted linked_media for media_id={m.get('id') or m.get('media_id')}")
                except Exception:
                    pass
        except Exception:
            pass

        # Debug final concert link/embed state
        try:
            if (m.get("type") or "").lower() == "concert":
                print(f"[DEBUG][get_media_services] final concert media (post-merge): link='{m.get('link')}', embed_url='{m.get('embed_url')}', stored_at={m.get('stored_at')}, filename={m.get('filename')}")
        except Exception:
            pass

        return {"status": "OK", "response": m}
    except Exception as e:
        #print(f"[ERROR][get_media_services] {e}")
        print(f"[ERROR][get_media_services] {e}")
        return {"status": "error", "error_msg": str(e)}