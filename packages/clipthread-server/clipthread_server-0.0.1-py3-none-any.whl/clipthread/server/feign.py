import requests
import time
from typing import Optional, List, Callable
from functools import wraps
from clipthread.core.models import Clipboard

def retry_with_backoff(retries: int = 5, backoff_in_seconds: int = 1):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    if x == retries:
                        raise e
                    sleep = (backoff_in_seconds * 2 ** x)
                    time.sleep(sleep)
                    x += 1
        return wrapper
    return decorator


class ClipboardClient:
    def __init__(self, host: str, port: int):
        self.root_url = f"http://{host}:{port}/clipboard"

    @retry_with_backoff()
    def create_clipboard(self, text: str, pinned: bool = False) -> Clipboard:
        response = requests.post(
            f"{self.root_url}/",
            json={"text": text, "pinned": pinned}
        )
        response.raise_for_status()
        return Clipboard.model_validate(response.json())

    @retry_with_backoff()
    def get_clipboard(self, clip_id: str) -> Clipboard:
        response = requests.get(f"{self.root_url}/{clip_id}")
        response.raise_for_status()
        return Clipboard.model_validate(response.json())

    @retry_with_backoff()
    def get_all_clipboards(self, limit: Optional[int] = None) -> List[Clipboard]:
        params = {"limit": limit} if limit else {}
        response = requests.get(f"{self.root_url}/", params=params)
        response.raise_for_status()
        return [Clipboard.model_validate(clip) for clip in response.json()]

    @retry_with_backoff()
    def update_clipboard(self, clip_id: str, text: Optional[str] = None, pinned: Optional[bool] = None) -> Clipboard:
        update_data = {}
        if text is not None:
            update_data["text"] = text
        if pinned is not None:
            update_data["pinned"] = pinned

        response = requests.put(f"{self.root_url}/{clip_id}", json=update_data)
        response.raise_for_status()
        return Clipboard.model_validate(response.json())

    @retry_with_backoff()
    def delete_clipboard(self, clip_id: str) -> dict:
        response = requests.delete(f"{self.root_url}/{clip_id}")
        response.raise_for_status()
        return response.json()

    @retry_with_backoff()
    def clear_clipboard(self) -> dict:
        response = requests.delete(f"{self.root_url}/")
        response.raise_for_status()
        return response.json()