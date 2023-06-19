import json
import pytest
from flask import Flask

from application import application


@pytest.fixture
def client():
    application.config['TESTING'] = True
    with application.test_client() as client:
        yield client


def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) == 4  # Assuming 3 products are initially present