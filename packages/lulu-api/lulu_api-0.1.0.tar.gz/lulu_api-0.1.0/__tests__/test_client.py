"""
Tests pour le client Lulu Print API.
"""

import pytest
from unittest.mock import Mock, patch
from datetime import datetime, timedelta
import json
import hmac
import hashlib

from ..client import LuluClient
from ..models import (
    PrintJob, ShippingAddress, LineItem, PrintableNormalization,
    PrintableValidation, ValidationStatus, WebhookConfig, PrintJobStatus,
    ShippingLevel, Cost, ShippingCost, EstimatedShippingDates
)
from ..exceptions import LuluAPIError, LuluAuthError

@pytest.fixture
def mock_response():
    """Crée un mock de réponse HTTP."""
    response = Mock()
    response.status_code = 200
    response.content = b'{"test": "data"}'
    response.json.return_value = {"test": "data"}
    return response

@pytest.fixture
def client():
    """Crée une instance du client Lulu."""
    return LuluClient("test_key", "test_secret")

def test_init(client):
    """Teste l'initialisation du client."""
    assert client.client_key == "test_key"
    assert client.client_secret == "test_secret"
    assert client.base_url == client.SANDBOX_URL

@patch('requests.post')
def test_get_auth_token(mock_post, client, mock_response):
    """Teste l'obtention du jeton d'authentification."""
    mock_response.json.return_value = {
        "access_token": "test_token",
        "expires_in": 3600
    }
    mock_post.return_value = mock_response
    
    token = client._get_auth_token()
    
    assert token == "test_token"
    assert client._access_token == "test_token"
    assert isinstance(client._token_expires, datetime)

@patch('requests.post')
def test_get_auth_token_error(mock_post, client):
    """Teste la gestion des erreurs d'authentification."""
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.text = "Unauthorized"
    mock_post.return_value = mock_response
    
    with pytest.raises(LuluAuthError):
        client._get_auth_token()

@patch('requests.request')
def test_make_request(mock_request, client, mock_response):
    """Teste les requêtes API."""
    mock_request.return_value = mock_response
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        response = client._make_request("GET", "/test/")
        
    assert response == {"test": "data"}
    mock_request.assert_called_once()

@patch('requests.request')
def test_validate_interior(mock_request, client, mock_response):
    """Teste la validation des fichiers intérieurs."""
    mock_response.json.return_value = {
        "status": "VALIDATED",
        "errors": [],
        "warnings": []
    }
    mock_request.return_value = mock_response
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        result = client.validate_interior("http://test.com/file.pdf", "md5sum")
        
    assert isinstance(result, PrintableValidation)
    assert result.status == ValidationStatus.VALIDATED
    assert len(result.errors) == 0
    assert len(result.warnings) == 0

@patch('requests.request')
def test_validate_cover(mock_request, client, mock_response):
    """Teste la validation des fichiers de couverture."""
    mock_response.json.return_value = {
        "status": "VALIDATED",
        "errors": [],
        "warnings": []
    }
    mock_request.return_value = mock_response
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        result = client.validate_cover(
            "http://test.com/cover.pdf",
            "md5sum",
            "pod_123",
            100
        )
        
    assert isinstance(result, PrintableValidation)
    assert result.status == ValidationStatus.VALIDATED

@patch('requests.request')
def test_get_cover_dimensions(mock_request, client, mock_response):
    """Teste le calcul des dimensions de couverture."""
    mock_response.json.return_value = {
        "spine_width": 12.5,
        "cover_width": 200.0,
        "cover_height": 300.0
    }
    mock_request.return_value = mock_response
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        result = client.get_cover_dimensions("pod_123", 100)
        
    assert isinstance(result, dict)
    assert "spine_width" in result
    assert "cover_width" in result
    assert "cover_height" in result

@patch('requests.request')
def test_create_webhook(mock_request, client, mock_response):
    """Teste la création de webhook."""
    mock_response.json.return_value = {
        "id": "webhook_123",
        "url": "http://test.com/webhook",
        "topics": ["print.created"],
        "is_active": True
    }
    mock_request.return_value = mock_response
    
    config = WebhookConfig(
        url="http://test.com/webhook",
        topics=["print.created"]
    )
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        result = client.create_webhook(config)
        
    assert isinstance(result, dict)
    assert result["id"] == "webhook_123"
    assert result["url"] == "http://test.com/webhook"

def test_verify_webhook_signature(client):
    """Teste la vérification de signature de webhook."""
    payload = '{"test": "data"}'
    signature = hmac.new(
        "test_secret".encode('utf-8'),
        payload.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    assert client.verify_webhook_signature(payload, signature) is True
    assert client.verify_webhook_signature(payload, "invalid_signature") is False

@patch('requests.request')
def test_create_print_job(mock_request, client, mock_response):
    """Teste la création d'un travail d'impression."""
    mock_response.json.return_value = {
        "id": "job_123",
        "status": "CREATED"
    }
    mock_request.return_value = mock_response
    
    address = ShippingAddress(
        name="Test User",
        street1="123 Test St",
        city="Test City",
        country_code="US"
    )
    
    printable = PrintableNormalization(
        interior_url="http://test.com/interior.pdf",
        interior_md5_sum="md5sum",
        cover_url="http://test.com/cover.pdf",
        cover_md5_sum="md5sum"
    )
    
    line_item = LineItem(
        pod_package_id="pod_123",
        quantity=1,
        title="Test Book",
        page_count=100,
        printable_normalization=printable
    )
    
    job = PrintJob(
        shipping_address=address,
        line_items=[line_item],
        shipping_level=ShippingLevel.GROUND,
        contact_email="test@test.com"
    )
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        result = client.create_print_job(job)
        
    assert isinstance(result, dict)
    assert result["id"] == "job_123"
    assert result["status"] == "CREATED"

@patch('requests.request')
def test_get_print_jobs(mock_request, client, mock_response):
    """Teste la récupération des travaux d'impression."""
    mock_response.json.return_value = {
        "count": 1,
        "results": [{
            "id": "job_123",
            "status": "CREATED"
        }]
    }
    mock_request.return_value = mock_response
    
    with patch.object(client, '_get_auth_token', return_value="test_token"):
        result = client.get_print_jobs()
        
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["id"] == "job_123"
