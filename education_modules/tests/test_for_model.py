"""Tests for CRUD."""

from django.test import TestCase
from modules.models import EducationalModules
from modules.serializers import EducationalModulesSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import json


class EducationalModulesTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.module_data = {'module_number': 1, 'module_name': 'Test Module', 'module_description': 'Test Description'}
        self.module = EducationalModules.objects.create(**self.module_data)

    def test_create_module(self):
        response = self.client.post(reverse('educationalmodules-list'), data=self.module_data)
        serializer = EducationalModulesSerializer(data=self.module_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['module_name'], self.module_data['module_name'])

    def test_get_module(self):
        module_id = str(self.module.id)
        response = self.client.get(reverse('educationalmodules-detail', args=[module_id]))
        serializer = EducationalModulesSerializer(instance=self.module)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['module_name'], serializer.data['module_name'])

    def test_update_module(self):
        module_id = str(self.module.id)
        updated_module_data = {
            'module_number': 1,
            'module_name': 'Updated Module',
            'module_description': 'Updated Description',
        }
        response = self.client.put(
            reverse('educationalmodules-detail', args=[module_id]),
            data=json.dumps(updated_module_data),
            content_type='application/json',
        )
        serializer = EducationalModulesSerializer(instance=self.module, data=updated_module_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_module(self):
        module_id = str(self.module.id)
        response = self.client.delete(reverse('educationalmodules-detail', args=[module_id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(EducationalModules.objects.filter(id=self.module.id).exists())
