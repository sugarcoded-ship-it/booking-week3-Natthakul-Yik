"""Shared input and overlap rules used by booking operations."""
from models import Booking

def validate_room(room: str) -> None:
    if not isinstance(room, str) or not room.strip():
        raise ValueError("Room must contain a non-whitespace character")

def validate_interval(start: int, end: int) -> None:
    if type(start) is not int or type(end) is not int:
        raise ValueError("Times must be integers")
    if not 0 <= start < end <= 1440:
        raise ValueError("Expected 0 <= start < end <= 1440")

def has_conflict(bookings: list[Booking], room: str, start: int, end: int) -> bool:
    return any(
        booking.status == "active"
        and booking.room == room
        and start < booking.end
        and booking.start < end
        for booking in bookings
    )
