"""
Client principal pour l'API Lulu Print.
"""

import requests
from typing import Optional, Dict, List, Union
from datetime import datetime, timedelta
import json
import hmac
import hashlib

from .models import (
    PrintJob, ShippingAddress, LineItem, PrintableNormalization,
    PrintableValidation, ValidationStatus, WebhookConfig, PrintJobStatus,
    ShippingLevel, Cost, ShippingCost, EstimatedShippingDates
)
from .exceptions import LuluAPIError, LuluAuthError

class LuluClient:
    """Client pour interagir avec l'API Lulu Print."""
    
    PROD_URL = "https://api.lulu.com"
    SANDBOX_URL = "https://api.sandbox.lulu.com"
    TOKEN_ENDPOINT = "/auth/realms/glasstree/protocol/openid-connect/token"
    
    def __init__(self, client_key: str, client_secret: str, sandbox: bool = True):
        """
        Initialise le client Lulu.
        
        Args:
            client_key: Clé client pour l'authentification
            client_secret: Secret client pour l'authentification
            sandbox: Utiliser l'environnement sandbox (par défaut: True)
        """
        self.client_key = client_key
        self.client_secret = client_secret
        self.base_url = self.SANDBOX_URL if sandbox else self.PROD_URL
        self._access_token = None
        self._token_expires = None
        
    def _get_auth_token(self) -> str:
        """Obtient un nouveau jeton d'authentification."""
        if self._access_token and self._token_expires and datetime.now() < self._token_expires:
            return self._access_token
            
        auth = (self.client_key, self.client_secret)
        data = {'grant_type': 'client_credentials'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        response = requests.post(
            f"{self.base_url}{self.TOKEN_ENDPOINT}",
            auth=auth,
            data=data,
            headers=headers
        )
        
        if response.status_code != 200:
            raise LuluAuthError(f"Échec de l'authentification: {response.text}")
            
        token_data = response.json()
        self._access_token = token_data['access_token']
        self._token_expires = datetime.now() + timedelta(seconds=token_data['expires_in'])
        
        return self._access_token
        
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, params: Optional[Dict] = None) -> Dict:
        """
        Effectue une requête à l'API Lulu.
        
        Args:
            method: Méthode HTTP (GET, POST, etc.)
            endpoint: Point de terminaison de l'API
            data: Données à envoyer (optionnel)
            params: Paramètres de requête (optionnel)
            
        Returns:
            Dict: Réponse de l'API
        """
        headers = {
            'Authorization': f'Bearer {self._get_auth_token()}',
            'Content-Type': 'application/json'
        }
        
        url = f"{self.base_url}{endpoint}"
        
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=data,
            params=params
        )
        
        if response.status_code >= 400:
            raise LuluAPIError(f"Erreur API: {response.status_code} - {response.text}")
            
        return response.json() if response.content else {}

    def validate_interior(self, url: str, md5_sum: str) -> PrintableValidation:
        """
        Valide un fichier intérieur.
        
        Args:
            url: URL publique du fichier à valider
            md5_sum: Somme MD5 du fichier
            
        Returns:
            PrintableValidation: Résultat de la validation
        """
        data = {
            'url': url,
            'md5_sum': md5_sum
        }
        response = self._make_request('POST', '/print-jobs/validations/interior/', data=data)
        return PrintableValidation(
            status=ValidationStatus(response['status']),
            errors=response.get('errors', []),
            warnings=response.get('warnings', [])
        )

    def validate_cover(self, url: str, md5_sum: str, pod_package_id: str, page_count: int) -> PrintableValidation:
        """
        Valide un fichier de couverture.
        
        Args:
            url: URL publique du fichier à valider
            md5_sum: Somme MD5 du fichier
            pod_package_id: ID du package POD
            page_count: Nombre de pages du livre
            
        Returns:
            PrintableValidation: Résultat de la validation
        """
        data = {
            'url': url,
            'md5_sum': md5_sum,
            'pod_package_id': pod_package_id,
            'page_count': page_count
        }
        response = self._make_request('POST', '/print-jobs/validations/cover/', data=data)
        return PrintableValidation(
            status=ValidationStatus(response['status']),
            errors=response.get('errors', []),
            warnings=response.get('warnings', [])
        )

    def get_cover_dimensions(self, pod_package_id: str, page_count: int, unit: str = 'pt') -> Dict[str, float]:
        """
        Calcule les dimensions requises pour la couverture.
        
        Args:
            pod_package_id: ID du package POD
            page_count: Nombre de pages du livre
            unit: Unité de mesure (pt, mm, in)
            
        Returns:
            Dict[str, float]: Dimensions de la couverture
        """
        data = {
            'pod_package_id': pod_package_id,
            'page_count': page_count,
            'unit': unit
        }
        return self._make_request('POST', '/print-jobs/cover-dimensions/', data=data)
        
    def calculate_costs(self, print_job: PrintJob) -> Dict:
        """
        Calcule les coûts d'un travail d'impression.
        
        Args:
            print_job: L'objet PrintJob contenant les détails du travail
            
        Returns:
            Dict: Détails des coûts
        """
        return self._make_request('POST', '/print-job-cost-calculations/', data=print_job.to_dict())
        
    def create_print_job(self, print_job: PrintJob) -> Dict:
        """
        Crée un nouveau travail d'impression.
        
        Args:
            print_job: L'objet PrintJob contenant les détails du travail
            
        Returns:
            Dict: Détails du travail d'impression créé
        """
        return self._make_request('POST', '/print-jobs/', data=print_job.to_dict())
        
    def get_print_jobs(self, page: int = 1, page_size: int = 20) -> List[Dict]:
        """
        Récupère la liste des travaux d'impression.
        
        Args:
            page: Numéro de la page à récupérer
            page_size: Nombre d'éléments par page
            
        Returns:
            List[Dict]: Liste des travaux d'impression
        """
        params = {
            'page': page,
            'page_size': page_size
        }
        response = self._make_request('GET', '/print-jobs/', params=params)
        return response.get('results', [])

    def get_print_job(self, job_id: str) -> Dict:
        """
        Récupère les détails d'un travail d'impression.
        
        Args:
            job_id: ID du travail d'impression
            
        Returns:
            Dict: Détails du travail d'impression
        """
        return self._make_request('GET', f'/print-jobs/{job_id}/')

    def create_webhook(self, config: WebhookConfig) -> Dict:
        """
        Crée une nouvelle configuration de webhook.
        
        Args:
            config: Configuration du webhook
            
        Returns:
            Dict: Détails de la configuration créée
        """
        return self._make_request('POST', '/webhooks/', data=config.to_dict())

    def get_webhooks(self) -> List[Dict]:
        """
        Récupère la liste des webhooks configurés.
        
        Returns:
            List[Dict]: Liste des webhooks
        """
        response = self._make_request('GET', '/webhooks/')
        return response.get('results', [])

    def update_webhook(self, webhook_id: str, config: WebhookConfig) -> Dict:
        """
        Met à jour une configuration de webhook.
        
        Args:
            webhook_id: ID du webhook
            config: Nouvelle configuration
            
        Returns:
            Dict: Configuration mise à jour
        """
        return self._make_request('PUT', f'/webhooks/{webhook_id}/', data=config.to_dict())

    def delete_webhook(self, webhook_id: str) -> None:
        """
        Supprime une configuration de webhook.
        
        Args:
            webhook_id: ID du webhook
        """
        self._make_request('DELETE', f'/webhooks/{webhook_id}/')

    def test_webhook(self, webhook_id: str, topic: str) -> Dict:
        """
        Teste l'envoi d'un webhook.
        
        Args:
            webhook_id: ID du webhook
            topic: Sujet du webhook à tester
            
        Returns:
            Dict: Résultat du test
        """
        data = {'topic': topic}
        return self._make_request('POST', f'/webhooks/{webhook_id}/test/', data=data)

    def verify_webhook_signature(self, payload: str, signature: str) -> bool:
        """
        Vérifie la signature d'un webhook.
        
        Args:
            payload: Contenu brut du webhook
            signature: Signature HMAC du webhook
            
        Returns:
            bool: True si la signature est valide
        """
        calculated_signature = hmac.new(
            self.client_secret.encode('utf-8'),
            payload.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(calculated_signature, signature)
