import pytest
from pages.roombookingpage import roombooking

def test_roomBooking(page,data):
    page.goto(data["booking_url"])
    r=roombooking(page)
    r.check_in_out_date()
    r.room_book_process()

