from datetime import datetime
from typing import TypedDict
from uuid import UUID


class Otp(TypedDict):
    id: UUID
    user_id: UUID
    value: str
    create_datetime: datetime
    expiry_datetime: datetime
