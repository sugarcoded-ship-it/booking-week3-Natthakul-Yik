# REVIEW

## Identity
Natthakul Yikusung, 6680972. AI tool used: GitHub Copilot (Agent mode, Interactive approval). Claude was used for setup help and for checking my review. Worked independently.

## Review decision
In `service.py / move_booking`, the diff added:
`other_bookings = [booking for booking in bookings if booking is not target]`
before calling `has_conflict`. I kept this. `has_conflict` checks every active booking in the room, including the one being moved, so passing the full list would wrongly reject a move that overlaps the booking's own old time, or an unchanged request. SPEC R3 says to ignore the booking being moved. This does it inside `service.py` without changing `rules.py`, and `is not` compares object identity, so only the target is excluded. Before implementation, I also corrected the plan: it did not mention rejecting cancelled bookings, and `find_booking` does not check status, so I asked for that check; the diff includes it.

## Checks
- Baseline commit: 6798c98 (Week 3 starter baseline). Diff compared against 7e46036 (AGENTS.md checkpoint).
- Baseline: `uv run --python 3.12 python -m unittest -v test_baseline` ran 6 tests, OK. `uv run --python 3.12 python -m unittest -v test_move_smoke` ran 3 tests, 3 errors (NotImplementedError).
- Final: `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student` ran 11 tests, OK.

## Remaining uncertainty
SPEC says a valid room name does not prove the room exists, so moving a booking to a misspelled room such as "Room 201" succeeds. My tests do not settle whether staff should be protected from that, which is a business question. My tests also do not check that the old time slot becomes free for other bookings after a move.