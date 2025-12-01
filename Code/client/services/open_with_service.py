# ...existing code...
import os
import sys
import tempfile
import base64
import subprocess
import shutil
from typing import Dict, Any, Optional

from client.services.show_service import ShowService
from client.services.http_helper import http_client


class OpenWithService:
    """
    Responsible for fetching the single media file from backend (base64),
    writing it to a temporary file and opening it with a chosen external app.
    Only allowed apps listed in ALLOWED_APPS are accepted.
    """

    ALLOWED_APPS = {"default", "vlc", "quicktime", "music", "wmp"}

    @staticmethod
    def _unwrap_response(resp: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        if not isinstance(resp, dict):
            return None
        inner = resp
        # unwrap nested envelope like {"response": {...}} or {"result": {...}}
        seen = set()
        while isinstance(inner, dict) and any(k in inner for k in ("response", "result", "media")):
            candidate = inner.get("response") or inner.get("result") or inner.get("media")
            if candidate is None:
                break
            cid = id(candidate)
            if cid in seen:
                break
            seen.add(cid)
            inner = candidate
        return inner if isinstance(inner, dict) else None

    @staticmethod
    def _guess_file_info(media: Dict[str, Any]) -> Optional[Dict[str, str]]:
        # normalize fields that show_bp expects
        if not isinstance(media, dict):
            return None
        filename = media.get("filename") or (media.get("stored_at") and os.path.basename(media.get("stored_at"))) or media.get("file")
        file_type = (media.get("type") or "").lower() or None
        # If filename might include path, extract name only
        if isinstance(filename, str) and filename:
            filename = filename.split("/")[-1].split("\\")[-1]
        return {"filename": filename, "type": file_type}

    @staticmethod
    def open_media(media_id: Any, app_id: str) -> Dict[str, Any]:
        if app_id not in OpenWithService.ALLOWED_APPS:
            return {"status": "ERROR", "error_msg": "unsupported app"}

        # fetch metadata
        resp = ShowService.get_media(media_id)
        media = OpenWithService._unwrap_response(resp)
        if not media:
            return {"status": "ERROR", "error_msg": "could not fetch media metadata"}

        info = OpenWithService._guess_file_info(media)
        if not info or not info.get("filename"):
            return {"status": "ERROR", "error_msg": "media filename not available"}

        filename = info["filename"]
        file_type = info.get("type") or "document"

        # fetch file bytes from backend (RPC FETCH_FILE)
        fetch_res = http_client.send_request("FETCH_FILE", [file_type, filename], require_auth=True)
        # unwrap possible envelope
        file_b64 = None
        if isinstance(fetch_res, dict):
            file_b64 = (fetch_res.get("response") or fetch_res.get("data") or fetch_res.get("file"))
            # sometimes deeper envelope
            if isinstance(file_b64, dict) and "response" in file_b64:
                file_b64 = file_b64["response"]
        if not file_b64:
            return {"status": "ERROR", "error_msg": "file not available from backend"}

        try:
            content = base64.b64decode(file_b64)
        except Exception as e:
            return {"status": "ERROR", "error_msg": f"invalid file encoding: {e}"}

        # store in temp file (do not auto-delete -- external app needs it)
        ext = ""
        if "." in filename:
            ext = "." + filename.split(".")[-1]
        try:
            tmp_dir = tempfile.gettempdir()
            fd, tmp_path = tempfile.mkstemp(suffix=ext, prefix="is_media_")
            os.close(fd)
            with open(tmp_path, "wb") as f:
                f.write(content)
        except Exception as e:
            return {"status": "ERROR", "error_msg": f"failed to write temp file: {e}"}

        # Prepare platform-specific open commands
        try:
            # Default open
            if app_id == "default":
                if sys.platform.startswith("win"):
                    os.startfile(tmp_path)  # type: ignore
                elif sys.platform == "darwin":
                    subprocess.Popen(["open", tmp_path])
                else:
                    # linux/others
                    opener = shutil.which("xdg-open") or shutil.which("gio") or shutil.which("gnome-open")
                    if opener:
                        subprocess.Popen([opener, tmp_path])
                    else:
                        return {"status": "ERROR", "error_msg": "no system opener found (xdg-open/gio)"}
                return {"status": "OK", "message": f"Opened with default app (temp file: {tmp_path})"}

            # VLC
            if app_id == "vlc":
                # prefer explicit binary if available
                vlc_bin = shutil.which("vlc")
                if sys.platform.startswith("win") and not vlc_bin:
                    # common Windows install path
                    cand = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
                    if os.path.exists(cand):
                        vlc_bin = cand
                if vlc_bin:
                    subprocess.Popen([vlc_bin, tmp_path])
                    return {"status": "OK", "message": f"Opened with VLC (temp file: {tmp_path})"}
                # fallback to system opener
                return OpenWithService.open_media(media_id, "default")

            # QuickTime (mac only)
            if app_id == "quicktime":
                if sys.platform == "darwin":
                    subprocess.Popen(["open", "-a", "QuickTime Player", tmp_path])
                    return {"status": "OK", "message": f"Opened with QuickTime Player (temp file: {tmp_path})"}
                # otherwise fallback to default
                return OpenWithService.open_media(media_id, "default")

            # Apple Music / iTunes
            if app_id == "music":
                if sys.platform == "darwin":
                    subprocess.Popen(["open", "-a", "Music", tmp_path])
                    return {"status": "OK", "message": f"Opened with Music (temp file: {tmp_path})"}
                if sys.platform.startswith("win"):
                    # try iTunes binary
                    itunes = r"C:\Program Files\iTunes\iTunes.exe"
                    if os.path.exists(itunes):
                        subprocess.Popen([itunes, tmp_path])
                        return {"status": "OK", "message": f"Opened with iTunes (temp file: {tmp_path})"}
                return OpenWithService.open_media(media_id, "default")

            # Windows Media Player
            if app_id == "wmp":
                if sys.platform.startswith("win"):
                    # attempt to launch wmplayer
                    wmp = shutil.which("wmplayer") or r"C:\Program Files\Windows Media Player\wmplayer.exe"
                    if wmp and os.path.exists(wmp):
                        subprocess.Popen([wmp, tmp_path])
                        return {"status": "OK", "message": f"Opened with Windows Media Player (temp file: {tmp_path})"}
                    # fallback to start shell
                    subprocess.Popen(["start", tmp_path], shell=True)
                    return {"status": "OK", "message": f"Opened with system start (temp file: {tmp_path})"}
                return OpenWithService.open_media(media_id, "default")

            # unknown app_id (should not happen due to ALLOWED_APPS)
            return {"status": "ERROR", "error_msg": "unsupported app id"}
        except Exception as e:
            return {"status": "ERROR", "error_msg": f"failed to launch app: {e}"}
# ...existing code...