from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from .models import Contact
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):

    queryset = Contact.objects.all().order_by('-id')
    serializer_class = ContactSerializer

    def get_permissions(self):
        
        permission_class = []
        if self.action == 'create':
            permission_class = [IsAuthenticated]
        elif self.action == 'reterive' or self.action == 'update':
            permission_class = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'destroy':
            permission_class = [IsAdminUser]

        return [permission() for permission in permission_class]