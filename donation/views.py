from datetime import datetime
from django.shortcuts import redirect, render
from donation.models import Donation

def show_available_donations(request):
    context = {"donations": Donation.objects.all()}
    return render(request, "available_donations.html", context)

def show_donation_details(request, id):
    context = {"donation": Donation.objects.get(pk=id)}
    return render(request, "donation_details.html", context)

def create_new_donation(request):

    if request.method == "POST":
        title = request.POST["title"]
        weight_grams = int(request.POST["weight_grams"])
        address = request.POST["address"]
        description = request.POST["description"]
        context = {}
        if len(title) > 100:
            context["title_warning"] = "Title must be no more than 100 characters long."
        if weight_grams <= 0:
            context ["weight_grams_warning"] = "Weight must be more than 0 grams."
        if context:
            return render(request, "create_donation.html", context)
        
        status = True
        datetime_created = datetime.now()
        new_donation = Donation(
            title=title,
            status=status,
            datetime_created=datetime_created,
            weight_grams=weight_grams,
            address=address,
            description=description
        )
        new_donation.save()
        return redirect("donation:show_available_donations")
    
    return render(request, "create_donation.html")

def edit_existing_donation(request, id):
    context = {"donation": Donation.objects.get(pk=id)}
    return render(request, "edit_donation.html", context)