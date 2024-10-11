
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Assignments(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    admin = models.CharField(max_length=20)
    statusChoices = [
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected")
    ]
    status = models.CharField(choices=statusChoices, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.task
        


