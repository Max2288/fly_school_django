"""View file, handle user's requests."""

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from modules.models import EducationalModules
from modules.serializers import EducationalModulesSerializer


class EducationalModulesViewSet(viewsets.ModelViewSet):
    """Viewset for education model."""

    queryset = EducationalModules.objects.all()
    serializer_class = EducationalModulesSerializer

    def create(self, request, *args, **kwargs):
        """Create education model.

        Args:
            request (Response): user's request.

        Returns:
            Response: response after creation.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """Update education model.

        Args:
            request (Response): user's request.

        Returns:
            Response: response after update.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        """Delete education model.

        Args:
            request (Response): user's request.

        Returns:
            Response: response after removal.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
