from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentication.models import User
from django.contrib import messages

@login_required
def show_profile(request):
    current_user = request.user
    context = {"user" : current_user}
    return render(request, "profile.html", context)

@login_required
def edit_profile(request):
    current_user = request.user
    context = {"user":current_user}
    
    if (request.method == "PUT"):
        username = request.PUT.get("username")
        email = request.PUT.get("email")
        password = request.PUT.get("password")
        
        if (not validate_profile(current_user, username, email)):
            messages.info(request, message_list[validate_profile])
        
        else:
            contact = request.PUT.get("contact").strip()
            if (contact == "" ):
                current_user.contact = "-"
            else:
                current_user.contact = contact
            current_user.username = username
            current_user.email = request.PUT.get("email")
            current_user.password = request.PUT.get("password")
            current_user.save()
            return redirect("user_profile:")
        
    return render(request, "edit_profile.html", context)

# Utilities
message_list = {
    1:"Username already taken",
    2:"Email already taken",        
            }

def validate_profile(current_user, username, email):
    if (User.objects.filter(username=username) and current_user.username != username):
        return 1
    if (User.objects.filter(email=email) and current_user.email != email):
        return 2
    return 0
    