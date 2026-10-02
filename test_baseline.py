"""Baseline tests cover creation only, not the proposed rescheduling feature."""

import unittest
from copy import deepcopy
from models import Booking
from service import add_booking, find_booking


class CreationTests(unittest.TestCase):
    def test_creates_and_finds_booking(self):
        bookings = []
        created = add_booking(bookings, "Room 201", 600, 660)
        self.assertEqual(created, Booking(1, "Room 201", 600, 660))
        self.assertIs(find_booking(bookings, 1), created)

    def test_conflict_rejected_without_change(self):
        bookings = [Booking(1, "Room 201", 600, 660)]
        before = deepcopy(bookings)
        with self.assertRaises(ValueError):
            add_booking(bookings, "Room 201", 630, 690)
        self.assertEqual(bookings, before)

    def test_adjacency_allowed(self):
        bookings = [Booking(1, "Room 201", 600, 660)]
        self.assertEqual(add_booking(bookings, "Room 201", 660, 720).id, 2)

    def test_other_room_allowed(self):
        bookings = [Booking(1, "Room 201", 600, 660)]
        self.assertEqual(add_booking(bookings, "Room 202", 600, 660).room, "Room 202")

    def test_cancelled_booking_does_not_block(self):
        bookings = [Booking(1, "Room 201", 600, 660, "cancelled")]
        self.assertEqual(add_booking(bookings, "Room 201", 600, 660).id, 2)

    def test_invalid_inputs_rejected_without_change(self):
        for room, start, end in [(" ", 600, 660), ("Room 201", 660, 600),
                                 ("Room 201", -1, 60), ("Room 201", 600, 1441),
                                 ("Room 201", True, 60), ("Room 201", 600.0, 660)]:
            with self.subTest(room=room, start=start, end=end):
                bookings = [Booking(1, "Room 202", 100, 200)]
                before = deepcopy(bookings)
                with self.assertRaises(ValueError):
                    add_booking(bookings, room, start, end)
                self.assertEqual(bookings, before)


if __name__ == "__main__":
    unittest.main()
