from django.urls import path
from .views import maths, add, sub, mul, div

urlpatterns = [
   path('', maths),
   path('add/<int:a>/<b>', add),
   path('sub/<int:a>/<b>', sub),
   path('mul/<int:a>/<b>', mul),
   path('div/<int:a>/<b>', div),
]