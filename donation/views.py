from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from donation.models import *

def show_available_donations(request):
    context = {
        "donations": Donation.objects.filter(status=True).order_by("-datetime_created"),
        "public": True
    }
    return render(request, "list_donations.html", context)

@login_required(login_url="authentication:login")
def show_my_donations(request):
    context = {
        "donations": Donation.objects.filter(donator=request.user).order_by("-datetime_created"),
        "public": False
    }
    return render(request, "list_donations.html", context)

def show_donation_details(request, id):
    context = {
        "donation": Donation.objects.get(pk=id),
        "logged_user": request.user
    }
    return render(request, "donation_details.html", context)

@login_required(login_url="authentication:login")
def create_new_donation(request):
    context = {"categories": Category.objects.all()}

    if request.method == "POST":
        print(request.POST["latitude"])
        print(request.POST["longitude"])
        title = request.POST["title"]
        category = Category.objects.get(pk=int(request.POST["category"]))
        weight_grams = int(request.POST["weight_grams"])
        address = request.POST["address"]
        description = request.POST["description"]
        if len(title) > 100:
            context["title_warning"] = "Title must be no more than 100 characters long."
        if weight_grams <= 0:
            context["weight_grams_warning"] = "Weight must be more than 0 grams."
        if "title_warning" in context or "weight_grams_warning" in context:
            return render(request, "create_donation.html", context)
        
        status = True
        datetime_created = datetime.now()
        new_donation = Donation(
            title=title,
            donator=request.user,
            status=status,
            category=category,
            datetime_created=datetime_created,
            weight_grams=weight_grams,
            address=address,
            description=description
        )
        new_donation.save()
        return redirect("donation:show_available_donations")
    
    return render(request, "create_donation.html", context)

@login_required(login_url="authentication:login")
def edit_existing_donation(request, id):
    context = {"categories": Category.objects.all()}

    if request.method == "POST":
        title = request.POST["title"]
        category = Category.objects.get(pk=int(request.POST["category"]))
        weight_grams = int(request.POST["weight_grams"])
        address = request.POST["address"]
        description = request.POST["description"]
        if len(title) > 100:
            context["title_warning"] = "Title must be no more than 100 characters long."
        if weight_grams <= 0:
            context["weight_grams_warning"] = "Weight must be more than 0 grams."
        if "title_warning" in context or "weight_grams_warning" in context:
            return render(request, "create_donation.html", context)
        
        edited_donation = Donation.objects.get(pk=id)
        edited_donation.title = title
        edited_donation.category = category
        edited_donation.weight_grams = weight_grams
        edited_donation.address = address
        edited_donation.description = description
        edited_donation.save()
        return redirect("donation:show_donation_details", id)

    context["donation"] = Donation.objects.get(pk=id)
    return render(request, "edit_donation.html", context)