from django.urls import path
from user_profile.views import show_profile, edit_profile

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('edit/', edit_profile, name='edit_profile'),
]