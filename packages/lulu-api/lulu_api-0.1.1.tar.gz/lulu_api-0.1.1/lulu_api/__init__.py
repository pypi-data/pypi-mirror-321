"""
Package pour interagir avec l'API Lulu Print.
Ce package fournit une interface Python pour l'API Lulu Print, permettant de créer et gérer des travaux d'impression.
"""

from .client import LuluClient
from .models import PrintJob, ShippingAddress, LineItem, PrintableNormalization
from .exceptions import LuluAPIError, LuluAuthError

__version__ = "0.1.0"

__all__ = [
    "LuluClient",
    "PrintJob",
    "ShippingAddress",
    "LineItem",
    "PrintableNormalization",
    "LuluAPIError",
    "LuluAuthError"
]
