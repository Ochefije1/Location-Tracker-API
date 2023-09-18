from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import PhoneNumberLocationViewSet

# Create a router and register the viewset with it.
router = DefaultRouter()
router.register(r'phone-locations', PhoneNumberLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
