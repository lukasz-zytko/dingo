from django.urls import path
from .views import hello, hello_name

urlpatterns = [
   path('', hello),
   path('<str:name>', hello_name),
]