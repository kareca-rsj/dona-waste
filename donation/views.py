from django.shortcuts import redirect, render
from donation.models import Donation

def show_available_donations(request):
    context = {"donations": Donation.objects.all()}
    return render(request, "available_donations.html", context)

def create_new_donation(request):
    if request.method == "POST":
        return redirect("donation:show_available_donations")
    return render(request, "create_donation.html")