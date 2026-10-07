"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking

class MoveStudentTests(unittest.TestCase):

# Test 1
# Given: booking #17 in "Room 201" from 600 to 660, and no other bookings.
# When: move it to "Room 201" from 630 to 690 (overlaps its own old time).
# Expect: the move succeeds and returns the same object; its time becomes 630-690;
#         ID, room and active status stay the same, and the list still has only this booking.
    def test_move_overlapping_own_old_time(self):
        booking = Booking(17, "Room 201", 600, 660)
        bookings = [booking]

        result = move_booking(bookings, 17, "Room 201", 630, 690)

        self.assertIs(result, booking)
        self.assertEqual(booking.start, 630)
        self.assertEqual(booking.end, 690)
        self.assertEqual(booking.id, 17)
        self.assertEqual(booking.room, "Room 201")
        self.assertEqual(booking.status, "active")
        self.assertEqual(len(bookings), 1)
        self.assertIs(bookings[0], booking)

# Test 2
# Given: booking #17 in "Room 201" from 600 to 660, and no other bookings.
# When: move it to "Room 201" from 600 to 660 again (unchanged request).
# Expect: the move succeeds and returns the same object; room, times, ID and active
#         status are unchanged, and the list still has only this booking.
    def test_unchanged_move_preserves_booking(self):
        booking = Booking(17, "Room 201", 600, 660)
        bookings = [booking]

        result = move_booking(bookings, 17, "Room 201", 600, 660)

        self.assertIs(result, booking)
        self.assertEqual(booking.room, "Room 201")
        self.assertEqual(booking.start, 600)
        self.assertEqual(booking.end, 660)
        self.assertEqual(booking.id, 17)
        self.assertEqual(booking.status, "active")
        self.assertEqual(len(bookings), 1)
        self.assertIs(bookings[0], booking)

if __name__ == "__main__":
    unittest.main()
