from django.test import TestCase

# Create your tests here.
import pytest
from .models import Client

@pytest.mark.django_db
def test_client_str_method():
    # Crear un cliente de prueba
    client = Client.objects.create(
        name="John",
        last_name="Doe",
        address="123 Main St",
        phone=123456789,
        city="Springfield"
    )

    # Comprobar que __str__ devuelve el formato esperado
    assert str(client) == "John Doe"

@pytest.mark.django_db
def test_client_creation():
    # Crear un cliente de prueba
    client = Client.objects.create(
        name="Jane",
        last_name="Smith",
        address="456 Elm St",
        phone=987654321,
        city="Metropolis"
    )

    # Verificar que los campos se guardan correctamente
    assert client.name == "Jane"
    assert client.last_name == "Smith"
    assert client.address == "456 Elm St"
    assert client.phone == 987654321
    assert client.city == "Metropolis"
