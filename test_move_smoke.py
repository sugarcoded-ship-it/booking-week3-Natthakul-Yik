"""Three starter checks. They are deliberately incomplete coverage of SPEC.md."""
import unittest
from copy import deepcopy
from models import Booking
from service import move_booking

class MoveSmokeTests(unittest.TestCase):
    def test_ordinary_move_keeps_object_and_id(self):
        target = Booking(17, "Room 201", 600, 660)
        bookings = [target]
        result = move_booking(bookings, 17, "Room 202", 720, 780)
        self.assertIs(result, target)
        self.assertIs(bookings[0], target)
        self.assertEqual(bookings, [Booking(17, "Room 202", 720, 780)])

    def test_unknown_id_rejected(self):
        bookings = [Booking(17, "Room 201", 600, 660)]
        before = deepcopy(bookings)
        with self.assertRaises(ValueError):
            move_booking(bookings, 99, "Room 202", 720, 780)
        self.assertEqual(bookings, before)

    def test_conflict_rejected_without_change(self):
        bookings = [Booking(17, "Room 201", 600, 660),
                    Booking(18, "Room 202", 720, 780)]
        before = deepcopy(bookings)
        with self.assertRaises(ValueError):
            move_booking(bookings, 17, "Room 202", 750, 810)
        self.assertEqual(bookings, before)

if __name__ == "__main__":
    unittest.main()
