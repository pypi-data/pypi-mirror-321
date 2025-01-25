# Client API Lulu Print

Ce package fournit une interface Python pour interagir avec l'API Lulu Print, permettant de créer et gérer des travaux d'impression.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```python
from lulu_api import LuluClient, PrintJob, ShippingAddress, LineItem, PrintableNormalization

# Initialiser le client
client = LuluClient(
    client_key="votre_client_key",
    client_secret="votre_client_secret",
    sandbox=True  # Utiliser l'environnement sandbox
)

# Créer une adresse de livraison
shipping_address = ShippingAddress(
    name="John Doe",
    street1="123 Main St",
    city="Paris",
    country_code="FR",
    postal_code="75001",
    phone_number="+33123456789"
)

# Créer une normalisation de fichier
printable = PrintableNormalization(
    interior_url="https://example.com/interior.pdf",
    interior_md5_sum="abc123",
    cover_url="https://example.com/cover.pdf",
    cover_md5_sum="def456"
)

# Créer un élément de ligne
line_item = LineItem(
    pod_package_id="0850X1100BWSTDLW060UW444MNG",
    quantity=1,
    title="Mon Livre",
    printable_normalization=printable
)

# Créer un travail d'impression
print_job = PrintJob(
    shipping_address=shipping_address,
    line_items=[line_item],
    shipping_level="MAIL",
    contact_email="contact@example.com"
)

# Calculer les coûts
costs = client.calculate_costs(print_job)

# Créer le travail d'impression
job = client.create_print_job(print_job)

# Obtenir la liste des travaux d'impression
jobs = client.get_print_jobs()
```

## Documentation

Le package fournit les classes principales suivantes :

- `LuluClient` : Client principal pour interagir avec l'API
- `PrintJob` : Représente un travail d'impression
- `ShippingAddress` : Représente une adresse de livraison
- `LineItem` : Représente un élément de ligne dans un travail d'impression
- `PrintableNormalization` : Gère la normalisation des fichiers source

## Gestion des erreurs

Le package définit deux types d'exceptions :

- `LuluAPIError` : Erreur générale de l'API
- `LuluAuthError` : Erreur d'authentification

## Environnements

L'API peut être utilisée dans deux environnements :

- Production : https://api.lulu.com
- Sandbox : https://api.sandbox.lulu.com (recommandé pour les tests)
