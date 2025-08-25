from django.db import models
from django.contrib.auth.models import User

class forumUser(User):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

