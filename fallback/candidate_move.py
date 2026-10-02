"""Supplied candidate for IA 3.2 when an AI tool is unavailable.
This is a proposal for review, not a reference solution. Do not import it into tests.
Copy only the function into service.py after reviewing its plan and dependencies.
"""

def move_booking(bookings, booking_id, new_room, new_start, new_end):
    target = find_booking(bookings, booking_id)
    if target.status != "active":
        raise ValueError("Cannot move a cancelled booking")
    validate_room(new_room)
    validate_interval(new_start, new_end)
    if has_conflict(bookings, new_room, new_start, new_end):
        raise ValueError("Booking conflict")
    target.room = new_room
    target.start = new_start
    target.end = new_end
    return target
