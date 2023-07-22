from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def show_profile(request):
    current_user = request.user
    context = {"user":current_user}
    return render(request, "profile.html", context)

@login_required
def edit_profile(request):
    current_user = request.user
    context = {"user":current_user}
    
    if (request.method == "PUT"):
        current_user.username = request.PUT.get("username")
        current_user.email = request.PUT.get("email")
        current_user.password = request.PUT.get("password")
        contact = request.PUT.get("contact").strip()
        
        if (contact == "" ):
            current_user.contact = None
        else:
            current_user.contact = contact

        current_user.save()
        
    return render(request, "edit_profile.html", context)