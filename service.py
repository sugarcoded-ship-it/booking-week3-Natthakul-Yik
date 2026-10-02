"""Booking operations. Implement only the agreed rescheduling change."""
from models import Booking
from rules import validate_room, validate_interval, has_conflict

def find_booking(bookings: list[Booking], booking_id: int) -> Booking:
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise ValueError("Booking not found")

def add_booking(bookings: list[Booking], room: str, start: int, end: int) -> Booking:
    validate_room(room)
    validate_interval(start, end)
    if has_conflict(bookings, room, start, end):
        raise ValueError("Booking conflict")
    next_id = max((booking.id for booking in bookings), default=0) + 1
    booking = Booking(next_id, room, start, end)
    bookings.append(booking)
    return booking

def move_booking(bookings: list[Booking], booking_id: int, new_room: str,
                 new_start: int, new_end: int) -> Booking:
    """See SPEC.md. This stub deliberately has no implementation yet."""
    raise NotImplementedError("Week 3: implement the agreed rescheduling feature")
