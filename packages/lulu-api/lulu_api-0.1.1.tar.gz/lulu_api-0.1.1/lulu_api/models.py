"""
Modèles de données pour l'API Lulu Print.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Union
from datetime import datetime
from enum import Enum

class ShippingLevel(str, Enum):
    """Niveaux d'expédition disponibles."""
    MAIL = "MAIL"
    PRIORITY_MAIL = "PRIORITY_MAIL"
    GROUND = "GROUND"
    EXPEDITED = "EXPEDITED"
    EXPRESS = "EXPRESS"

class PrintJobStatus(str, Enum):
    """États possibles d'un travail d'impression."""
    CREATED = "CREATED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    IN_PRODUCTION = "IN_PRODUCTION"
    SHIPPED = "SHIPPED"
    RECEIVED = "RECEIVED"
    ERROR = "ERROR"

class ValidationStatus(str, Enum):
    """États possibles de la validation des fichiers."""
    NULL = "NULL"
    VALIDATING = "VALIDATING"
    VALIDATED = "VALIDATED"
    ERROR = "ERROR"

@dataclass
class ShippingAddress:
    """Adresse de livraison pour un travail d'impression."""
    name: str
    street1: str
    city: str
    country_code: str
    street2: Optional[str] = None
    state_code: Optional[str] = None
    postal_code: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    is_business: bool = False
    company: Optional[str] = None
    title: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convertit l'objet en dictionnaire."""
        return {k: v for k, v in self.__dict__.items() if v is not None}

@dataclass
class PrintableValidation:
    """Résultat de validation d'un fichier."""
    status: ValidationStatus
    errors: List[Dict[str, str]] = field(default_factory=list)
    warnings: List[Dict[str, str]] = field(default_factory=list)

@dataclass
class PrintableNormalization:
    """Représente le processus de normalisation des fichiers source."""
    interior_url: Optional[str] = None
    interior_md5_sum: Optional[str] = None
    cover_url: Optional[str] = None
    cover_md5_sum: Optional[str] = None
    printable_id: Optional[str] = None
    interior_validation: Optional[PrintableValidation] = None
    cover_validation: Optional[PrintableValidation] = None
    
    def to_dict(self) -> Dict:
        """Convertit l'objet en dictionnaire."""
        result = {}
        if self.interior_url:
            result["interior"] = {
                "url": self.interior_url,
                "md5_sum": self.interior_md5_sum
            }
        if self.cover_url:
            result["cover"] = {
                "url": self.cover_url,
                "md5_sum": self.cover_md5_sum
            }
        if self.printable_id:
            result["printable_id"] = self.printable_id
        return result

@dataclass
class Cost:
    """Représente les coûts d'un article."""
    cost_excl_discounts: str
    cost_excl_tax: str
    tax_rate: str
    total_cost_excl_discounts: str
    total_tax: str
    total_cost_excl_tax: str
    total_cost_incl_tax: str
    discounts: List[Dict[str, str]] = field(default_factory=list)
    unit_tier_cost: Optional[str] = None

@dataclass
class LineItem:
    """Élément de ligne pour un travail d'impression."""
    pod_package_id: str
    quantity: int
    title: str
    page_count: int
    printable_normalization: PrintableNormalization
    external_id: Optional[str] = None
    costs: Optional[Cost] = None
    status: Optional[PrintJobStatus] = None
    tracking_urls: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        """Convertit l'objet en dictionnaire."""
        result = {
            'pod_package_id': self.pod_package_id,
            'quantity': self.quantity,
            'title': self.title,
            'page_count': self.page_count,
            'printable_normalization': self.printable_normalization.to_dict()
        }
        if self.external_id:
            result['external_id'] = self.external_id
        return result

@dataclass
class ShippingCost:
    """Représente les coûts d'expédition."""
    tax_rate: str
    total_cost_excl_tax: str
    total_cost_incl_tax: str
    total_tax: str

@dataclass
class EstimatedShippingDates:
    """Dates estimées d'expédition et de livraison."""
    arrival_min: datetime
    arrival_max: datetime
    ship_min: datetime
    ship_max: datetime

@dataclass
class PrintJob:
    """Représente un travail d'impression Lulu."""
    shipping_address: ShippingAddress
    line_items: List[LineItem]
    shipping_level: ShippingLevel
    contact_email: str
    external_id: Optional[str] = None
    status: Optional[PrintJobStatus] = None
    order_id: Optional[str] = None
    shipping_cost: Optional[ShippingCost] = None
    estimated_shipping_dates: Optional[EstimatedShippingDates] = None
    production_delay: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convertit l'objet en dictionnaire."""
        return {
            'shipping_address': self.shipping_address.to_dict(),
            'line_items': [item.to_dict() for item in self.line_items],
            'shipping_level': self.shipping_level.value,
            'contact_email': self.contact_email,
            **(({'external_id': self.external_id} if self.external_id else {}))
        }

@dataclass
class WebhookConfig:
    """Configuration d'un webhook."""
    url: str
    topics: List[str]
    is_active: bool = True
    webhook_id: Optional[str] = None

    def to_dict(self) -> Dict:
        """Convertit l'objet en dictionnaire."""
        result = {
            'url': self.url,
            'topics': self.topics,
            'is_active': self.is_active
        }
        if self.webhook_id:
            result['id'] = self.webhook_id
        return result
