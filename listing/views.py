from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import Listing
from .serializers import ListingSerializer


class ListiniCreateAPIView(generics.CreateAPIView):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    pagination_class = [IsAuthenticated]


class ListingListAPIView(generics.ListAPIView):

    queryset = Listing.objects.all().order_by('-id')
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]


class ListingDetailAPIView(generics.RetrieveAPIView):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]


class ListingUpdateAPIView(generics.RetrieveUpdateAPIView):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]


class ListingDeleteAPIView(generics.DestroyAPIView):

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAdminUser]