from django.db import models
from django.contrib.auth.models import AbstractUser
 
 
class User(AbstractUser):
    """unser Model erbt von Abstract User."""
    address = models.CharField(max_length=250, blank=True, null=True)
