from rest_framework import serializers
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['id', 'title', 'address', 'city', 'state', 'zipcode', 'desc',
                      'bedrooms', 'bathrooms', 'garage', 'sqft', 'plot_size',
                      'price', 'pic_1', 'pic_2', 'pic_3', 'pic_4', 'pic_5', 'pic_6',
                      'is_published']