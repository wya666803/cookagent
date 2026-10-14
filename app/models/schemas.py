from typing import Optional, List

from pydantic import BaseModel

# --- 2. 数据模型 ---
class ChatRequest(BaseModel):
    message: str
    image_url: Optional[str] = None
    thread_id: str