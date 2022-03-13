from django.urls import path
from .views import maths, add, sub, mul, div, maths_list, math_details

app_name = "maths"

urlpatterns = [
   path('', maths),
   path('add/<int:a>/<b>', add),
   path('sub/<int:a>/<b>', sub),
   path('mul/<int:a>/<b>', mul),
   path('div/<int:a>/<b>', div),
   path("histories/", maths_list, name="list"),
   path("histories/<int:id>", math_details, name="details")
]