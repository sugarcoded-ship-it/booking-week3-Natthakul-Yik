"""Booking records for a single day's meeting-room reservations."""
from dataclasses import dataclass

@dataclass
class Booking:
    id: int
    room: str
    start: int
    end: int
    status: str = "active"
