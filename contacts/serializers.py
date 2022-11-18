from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'listing','name', 'email',
                      'phone', 'subject', 'message', 'contacted_at', 'user_id']