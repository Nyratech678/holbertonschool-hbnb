# 1. Detailed Class Diagram for Business Logic Layer

## Objectif
Ce document présente un **diagramme de classes détaillé** pour la **Business Logic Layer** de l’application HBnB.
Il montre les entités principales, leurs attributs, méthodes, et les relations entre elles, afin de représenter clairement la logique métier du système.

---

## Diagramme de classes

```mermaid
classDiagram
%% Classe de base pour l’héritage
class BaseModel {
    +UUID id
    +datetime created_at
    +datetime updated_at
    +save()
    +delete()
}

%% Utilisateur
class User {
    +string email
    +string password
    +string first_name
    +string last_name
    +list<Place> places
    +list<Review> reviews
    +save()
    +delete()
}

%% Logement
class Place {
    +string name
    +string description
    +float price_by_night
    +string city_id
    +UUID owner_id
    +list<Amenity> amenities
    +list<Review> reviews
    +save()
    +delete()
    +add_amenity()
    +remove_amenity()
}

%% Avis
class Review {
    +string text
    +UUID user_id
    +UUID place_id
    +int rating
    +save()
    +delete()
}

%% Équipement
class Amenity {
    +string name
    +list<Place> places
    +save()
    +delete()
}

%% Héritage de BaseModel
User --|> BaseModel
Place --|> BaseModel
Review --|> BaseModel
Amenity --|> BaseModel

%% Relations
User "1" --> "*" Place : owns
User "1" --> "*" Review : writes
Place "1" --> "*" Review : has
Place "*" --> "*" Amenity : includes
