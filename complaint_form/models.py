from django.db import models

# Create your models here.
from django.db import models


class UserComplaint(models.Model):
    username = models.CharField(max_length=100)
    user_complaint = models.TextField()

    def __str__(self):
        return self.username
