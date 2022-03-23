from django.urls import path
from .views import welcome, about, contact

urlpatterns = [
   path("", welcome, name="welcome"),
   path("about/", about, name="about"),
   path("contact/", contact, name="contact"),
]