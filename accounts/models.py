from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_choices = {
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
}

USERTYPE_choices = {
    ('Owner', 'Owner'),
    ('Broker', 'Broker'),
    ('Buyer', 'Buyer'),
}


class User(AbstractUser):

    first_name = models.CharField(max_length=175)
    last_name = models.CharField(max_length=175)
    username = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    email = models.CharField(max_length=175)
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=1, choices=GENDER_choices)
    user_type = models.CharField(max_length=15, choices=USERTYPE_choices)
    session_token = models.CharField(max_length=15, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.user_type} - {self.email} - {self.phone}'