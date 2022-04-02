from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    
    def __str__(self):
        return self.user.username

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=6,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')],
        blank=True, null=True
    )
    
    def __str__(self):
        return f"{self.user.username}'s Account"
    