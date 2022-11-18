from django.urls import path
from .views import ListingListAPIView, ListiniCreateAPIView, ListingDetailAPIView, ListingUpdateAPIView, ListingDeleteAPIView


urlpatterns = [
    path('', ListingListAPIView.as_view(), name='listing_list'),
    path('create/', ListiniCreateAPIView.as_view(), name='listing_create'),
    path('detail/<int:pk>', ListingDetailAPIView.as_view(), name='lising_detail'),
    path('update/<int:pk>', ListingUpdateAPIView.as_view(), name='listing_update'),
    path('delete/<int:pk>', ListingDeleteAPIView.as_view(), name='listing_delete')
]