from django.db import models


class Contact(models.Model):

    listing = models.CharField(max_length=275)
    listiong_id = models.PositiveIntegerField()
    name = models.CharField(max_length=275)
    email = models.EmailField(max_length=275)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=275)
    message = models.TextField(blank=True)
    contacted_at = models.DateTimeField(auto_now=True)
    user_id = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'
