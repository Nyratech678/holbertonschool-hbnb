Présentation

Ce projet implémente la couche logique métier de l'application HBnB, comprenant les entités principales qui modélisent les utilisateurs, lieux, avis et agréments. Chaque classe gère ses attributs, validations, identifiants uniques (UUID) et timestamps de création et modification.
Entités principales
User (Utilisateur)

    id : Identifiant unique UUID généré automatiquement.

    first_name : Prénom (chaine, max 50 caractères).

    last_name : Nom (chaine, max 50 caractères).

    email : Adresse email valide et unique.

    is_admin : Booléen indiquant les privilèges administrateur (défaut False).

    created_at / updated_at : Timestamps automatiques.

Rôle

Représente un utilisateur de la plateforme. Peut posséder plusieurs lieux.
Place (Lieu)

    id : Identifiant unique UUID.

    title : Titre du lieu (chaine, max 100 caractères).

    description : Description optionnelle (chaine).

    price_by_night : Prix par nuit (float positif).

    latitude / longitude : Coordonnées géographiques valides.

    owner : Utilisateur propriétaire (instance de User).

    created_at / updated_at : Timestamps.

Relations

    Possède plusieurs avis (reviews).

    Associé à plusieurs agréments (amenities).

Review (Avis)

    id : Identifiant unique UUID.

    text : Contenu de l'avis (chaine non vide).

    rating : Note entière entre 1 et 5.

    place : Lieu concerné (instance de Place).

    user : Utilisateur auteur (instance de User).

    created_at / updated_at : Timestamps.

Amenity (Agrément)

    id : Identifiant unique UUID.

    name : Nom de l’agrément (ex : "Wi-Fi", max 50 caractères).

    created_at / updated_at : Timestamps.

Relations entre Entités

    Un User peut posséder plusieurs Place (relation un-à-plusieurs).

    Un Place peut recevoir plusieurs Review (relation un-à-plusieurs).

    Un Place peut avoir plusieurs Amenity (relation plusieurs-à-plusieurs) gérée par une liste d’objets amenity dans la classe Place.

EXEMPLE D'UTILISATION

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

 Création d'un utilisateur
user = User(first_name="Alice", last_name="Smith", email="<alice@example.com>")

 Création d'un lieu avec ce propriétaire
place = Place(title="Cozy Apartment", description="Nice place", price_by_night=100, latitude=48.85, longitude=2.35, owner=user)

 Ajout d'un agrément
wifi = Amenity(name="Wi-Fi")
place.add_amenity(wifi)

 Création d'un avis
review = Review(text="Great stay!", rating=5, place=place, user=user)
place.add_review(review)
