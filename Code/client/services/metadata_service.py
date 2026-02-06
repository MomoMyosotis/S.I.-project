# first line

from client.services.http_helper import http_client

class MetadataService:
    """Service for fetching and caching metadata (instruments, genres, authors, etc.)"""
    
    _cache = None
    
    @staticmethod
    def get_metadata(user_id=None):
        """
        Fetch metadata from server. Caches result to avoid repeated requests.
        
        Args:
            user_id: Optional user ID to send to server. If None, will attempt to get from session.
        
        Returns a dict with keys: instruments, genres, authors, performers, media_titles
        """
        if MetadataService._cache is not None:
            return MetadataService._cache
        
        try:
            # If no user_id provided, try to extract from http_client token
            if user_id is None:
                # Best effort: try to get from session or session storage
                try:
                    from client.services.http_helper import http_client
                    # Can't reliably extract user_id from token, so send empty args
                    # Server will use user_obj if it's available
                    args = []
                except Exception:
                    args = []
            else:
                args = [user_id]
            
            res = http_client.send_request("GET_METADATA", args, require_auth=True)
            
            # Handle error responses
            if isinstance(res, dict) and res.get("status") and str(res.get("status")).lower() not in ("ok", "true"):
                print(f"[ERROR] GET_METADATA failed: {res.get('error_msg', 'Unknown error')}")
                return {
                    "instruments": [],
                    "genres": [],
                    "authors": [],
                    "performers": [],
                    "media_titles": []
                }
            
            # Extract metadata from response envelope if needed
            metadata = res
            if isinstance(res, dict) and "response" in res:
                metadata = res.get("response") or res
            
            # Ensure all keys exist
            if isinstance(metadata, dict):
                metadata.setdefault("instruments", [])
                metadata.setdefault("genres", [])
                metadata.setdefault("authors", [])
                metadata.setdefault("performers", [])
                metadata.setdefault("media_titles", [])
                MetadataService._cache = metadata
                return metadata
            
            return {
                "instruments": [],
                "genres": [],
                "authors": [],
                "performers": [],
                "media_titles": []
            }
        except Exception as e:
            print(f"[ERROR] MetadataService.get_metadata failed: {e}")
            return {
                "instruments": [],
                "genres": [],
                "authors": [],
                "performers": [],
                "media_titles": []
            }
    
    @staticmethod
    def clear_cache():
        """Clear the metadata cache (useful after updates)"""
        MetadataService._cache = None
    
    @staticmethod
    def invalidate():
        """Alias for clear_cache"""
        MetadataService.clear_cache()

# last line
