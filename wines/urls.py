from django.urls import path, include
from rest_framework import urlpatterns
from .views import WineViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', WineViewSet, basename='wine')
urlpatterns = router.urls