from django.test import TestCase

# Create your tests here.
import pytest
from django.urls import reverse
from control.models import Client, Pet

@pytest.fixture
def create_client(db):
    return Client.objects.create(
        name="Test Client",
        last_name="Test LastName",
        address="123 Test Street",
        phone=1234567890,  # Valor válido para phone
        city="Test City"
    )


@pytest.fixture
def create_pet(db, create_client):
    return Pet.objects.create(
        name="Test Pet",
        race="Dog",
        size="M", 
        client=create_client
    )

@pytest.mark.django_db
def test_index_manage_client_view(client, create_client, create_pet):
    # Simular solicitud GET
    response = client.get(reverse('index_manage'))

    # Verificar respuesta exitosa
    assert response.status_code == 200

    # Verificar que los datos del contexto sean correctos
    context = response.context
    assert context['client'].name == "Test Client"
    assert context['pet'].name == "Test Pet"
    assert context['pet'].race == "Dog"
