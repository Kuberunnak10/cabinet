from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    CHOISE = (
        ('Customer', 'customer'),
        ('Executor', 'executor'),
    )

    name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=CHOISE)
    contacts = models.CharField(max_length=255)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.username} - {self.role}'

