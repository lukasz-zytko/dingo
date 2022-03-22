from django.urls import path
from .views import hello, hello_name, welcome

urlpatterns = [
   path('', welcome, name="welcome"),
   path('<str:name>', hello_name),
]