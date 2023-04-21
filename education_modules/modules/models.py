"""Models for education project."""

from django.db import models
from uuid import uuid4


class EducationalModules(models.Model):
    """Class for education model."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    module_number = models.IntegerField()
    module_name = models.TextField()
    module_description = models.TextField()

    def __str__(self):
        """Representation of model.

        Returns:
            str: model in special format.
        """
        return 'Module {0}: {1}'.format(self.module_number, self.module_name)

    class Meta:
        """Class that represent model in table."""

        db_table = 'educational_modules'
