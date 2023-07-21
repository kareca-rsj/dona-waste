from django.urls import path
from donation.views import *

app_name = "donation"

urlpatterns = [
    path("", show_available_donations, name="show_available_donations"),
    path("available-donations/", show_available_donations, name="show_available_donations"),
    path("create-donation/", create_new_donation, name="create_new_donation")
]