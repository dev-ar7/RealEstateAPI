from django.urls import path, include
from .views import signIN, signOUT, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('', signIN, name='login'),
    path('logout/<int:pk>/', signOUT, name='logout'),
    path('user/', include(router.urls), name='user'),
]