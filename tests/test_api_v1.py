import pytest

from app import app


@pytest.fixture
def client():
    test_client = app.test_client()
    yield test_client


def test_sum_endpoint_with_default_values(client):
    response = client.get('/api/v1/sum/')
    assert 'Sum of 1+2 is: 3' in response.data.decode()


def test_sum_endpoint_with_args(client):
    response = client.get('/api/v1/sum/?a=10&b=20')
    assert 'Sum of 10+20 is: 30' in response.data.decode()


def test_sum_endpoint_with_invalid_args_should_return_400(client):
    response = client.get('/api/v1/sum/?a=10x&b=20')
    assert response.status_code == 400
