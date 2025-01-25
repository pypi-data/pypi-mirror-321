from datetime import datetime
from enum import StrEnum
from typing import TypedDict
from uuid import UUID


class WayPointAction(StrEnum):
    PICKUP = "PICKUP"
    DROP_OFF = "DROP_OFF"


class WayPoint(TypedDict):
    order_id: UUID
    location_id: UUID
    action: WayPointAction
    eta: datetime
    sequence: int


class Route(TypedDict):
    waypoints: list[WayPoint]
    estimated_distance_in_kms: float
    estimated_time_in_minutes: int
