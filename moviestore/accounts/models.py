from django.db import models
from django.contrib.auth.models import User

class UserSecurityQuestion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_answer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s Security Question Answer"
