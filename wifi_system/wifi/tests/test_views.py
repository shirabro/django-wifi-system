from rest_framework import status
from django.test import Client
from django.urls import reverse
from ..models import NetworkModel
from ..serializers import NetworkModelSerializer
from django.test import TestCase

# initialize the APIClient app
client = Client()


class Get_fetch_network_by_id(TestCase):
    def setUp(self):
        self.network1 = NetworkModel.objects.create(
            id='123456', auth='wpa')
        self.network2 = NetworkModel.objects.create(
            id='123', auth='public')

    def test_fetch_network_by_id(self):
        # response = client.get("/my-service/api/network?id=123456")
        response = client.get(reverse('fetch_network_by_id', kwargs={'id': "123456"}))
        network = NetworkModel.objects.get(id=self.network1.get_id())
        serializer = NetworkModelSerializer(network)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
