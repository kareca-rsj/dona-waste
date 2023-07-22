from django.urls import path
from donation.views import *

app_name = "donation"

urlpatterns = [
    path("available-donations/", show_available_donations, name="show_available_donations"),
    path("my-donations/", show_my_donations, name="show_my_donations"),
    path("donation-details/<int:id>", show_donation_details, name="show_donation_details"),
    path("create-donation/", create_new_donation, name="create_new_donation"),
    path("edit-donation/<int:id>", edit_existing_donation, name="edit_existing_donation"),
    path("close-donation/<int:id>", close_donation, name="close_donation")
]