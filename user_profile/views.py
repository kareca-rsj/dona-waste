from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentication.models import User
from django.contrib import messages

@login_required(login_url='/auth/login')
def show_profile(request):
    current_user = request.user
    context = {"user" : current_user}
    return render(request, "profile.html", context)

@login_required(login_url='/auth/login')
def edit_profile(request):
    current_user = request.user
    context = {"user":current_user}
    
    if (request.method == "POST"):
        username = request.POST.get("username")
        email = request.POST.get("email")
        
        if (validate_profile(current_user, username, email)):
            messages.info(request, message_list[validate_profile])
        
        else:
            contact = request.POST.get("contact")
            if (contact == "" ):
                current_user.contact = "-"
            else:
                current_user.contact = contact
            current_user.username = username
            current_user.email = email
            current_user.save()
            return redirect("user_profile:show_profile")
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
    