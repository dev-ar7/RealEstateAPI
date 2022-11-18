from django.urls import path, include
from rest_framework import routers
from .views import ContactViewSet


router = routers.DefaultRouter()
router.register('', ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
]