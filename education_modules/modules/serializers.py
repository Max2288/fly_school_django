"""Serializers config for project."""

from rest_framework import serializers
from modules.models import EducationalModules


class EducationalModulesSerializer(serializers.ModelSerializer):
    """Education serializer for DRF."""

    class Meta:
        """Class that represent model in table."""

        model = EducationalModules
        fields = ('id', 'module_number', 'module_name', 'module_description')
