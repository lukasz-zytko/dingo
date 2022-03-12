from django.db import models

OPERATION_CHOICES = (
   ("add", "add"),
   ("sub", "sub"),
   ("mul", "mul"),
   ("div", "div"),
)

class Math(models.Model):
    operation = models.CharField(max_length=5, choices=OPERATION_CHOICES)
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

