"""Urls config for modules app."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modules.views import EducationalModulesViewSet


router = DefaultRouter()
router.register(r'educational-modules', EducationalModulesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
