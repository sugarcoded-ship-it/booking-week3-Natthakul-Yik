# Week 3 specification: move a meeting-room booking

The office-space rental business from Week 2 rents meeting rooms by the hour. Booking staff need to move an existing reservation without losing it when the move fails. Use these agreed rules even if your IA 2.1 draft differs. You may consult your IA 2.2 plan, but check its file/function references against this repository.

## Model and scope

- `Booking` is a reservation record. Booking #17 might reserve Room 201, 10:00–11:00. A room is the physical space; a booking is the record reserving it.
- Records are held in a list in memory. There is no database, room catalogue or separately stored room-availability value. Availability comes from overlapping active records in the requested room.
- All records concern one day and have unique integer IDs. Requests run one at a time.
- Times are integer minutes after midnight: 10:00 = 600, 11:00 = 660, 24:00 = 1440. Python booleans are not valid times.
- Assume authorised staff have obtained any necessary approval before requesting a move. This exercise does not settle a real customer-consent policy or implement permission checks.

Implement this existing stub in `service.py`:

```python
move_booking(bookings, booking_id, new_room, new_start, new_end)
```

## Required behaviour

| ID | Requirement |
|---|---|
| R1 | Find an existing active booking. Reject an unknown ID or cancelled target with `ValueError` and an explanatory message. |
| R2 | On success, update and return the **same Booking object**. Preserve its ID and active status. Create or delete no record; preserve list order. |
| R3 | Reject overlap with **another active booking in the same room**. Ignore cancelled records and the booking being moved when checking for a conflict. |
| R4 | Allow back-to-back times and overlapping times in different rooms. An unchanged request succeeds without changing data. |
| R5 | Require integer times with `0 <= start < end <= 1440`. Require a room name that is text with at least one non-whitespace character. Match names exactly, including spaces and capitalisation. A valid name does not prove the room exists. |
| R6 | Rejection leaves **all records and list membership unchanged**. Success leaves every other booking unchanged. Calculate availability from the updated records. The obsolete position stops blocking requests, while the new position blocks overlapping requests. |
| R7 | Preserve creation behaviour, the existing model and public function signatures. Use the Python standard library. Do not add a database, room catalogue, login/consent workflow, notifications, recurring bookings, automatic alternative slots or support for multiple days/time zones. |

An explanatory error message is required, but its exact wording is not prescribed. If several inputs are invalid, any applicable rejection may be reported.

When a move overlaps its own old time in the same room, the shared period remains reserved by the moved booking. “Old position stops blocking” does not mean the new reservation becomes available.

## Allowed edits

- Implement `move_booking` in `service.py`.
- Add your two checks in `test_student.py`.
- Create or revise `AGENTS.md` as part of IA 3.1.
- If your reviewed plan needs a helper change in `rules.py`, explain why before approving it. Preserve existing callers and behaviour. An optional parameter is acceptable if current calls still work.
- Keep `models.py`, `test_baseline.py`, `test_move_smoke.py`, `SPEC.md` and the fallback example unchanged. Do not weaken supplied checks.

Completion concerns this prototype and the evidence you report. Passing the supplied checks alone does not establish every rule above.
