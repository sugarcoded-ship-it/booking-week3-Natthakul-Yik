# Project guidance

Write 3–5 concrete bullets of your own and save as `AGENTS.md`. Combine related points where useful.
The instructions below are example ideas. Keep them relatively short and specific.

- Project and context: This Python repository implements in-memory meeting-room bookings; use 'SPEC.md' for move_booking rules.
- Preservation and scope: Preserve booking IDs, object identity, list order, cancellation behavior, and unchanged state after rejected moves. Keep changes limited to the agreed rescheduling feature.
- Checks: 'Run python3 -m unittest -v test_baseline test_move_smoke test_student' after implementation.
- Review: Stop for review after the agreed edit, especially if an edit goes wrong, and show the changed files and relevant diff.