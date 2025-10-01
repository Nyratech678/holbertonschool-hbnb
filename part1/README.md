# Ce document présente la conception technique de l’application HBnB Evolution, un système simplifié inspiré d’AirBnB

Il décrit :

L’architecture haut-niveau avec ses couches (Présentation, Logique Métier, Persistance).

Le modèle métier détaillé avec les classes principales (User, Place, Review, Amenity).

Les interactions entre les couches via des séquences d’appels API.

L’objectif est de fournir un plan technique clair pour guider le développement ultérieur.


# 1.High-Level Package Diagram

''mermaid
classDiagram
class PresentationLayer {
    <<Interface>>
    +API Endpoints
    +Services
}

class Facade {
    +HBnBFacade
    +createUser()
    +listPlaces()
    +bookPlace()
    +addReview()
}

class BusinessLogicLayer {
    +User
    +Place
    +Review
    +Amenity
}

class PersistenceLayer {
    +Repositories
    +DatabaseConnector
}

PresentationLayer --> Facade : appels (API)
Facade --> BusinessLogicLayer : utilise
BusinessLogicLayer --> PersistenceLayer : lit/écrit
''

# Presentation Layer : les API exposées aux utilisateurs.

# Facade : point d’entrée unique simplifiant l’accès aux services.

# Business Logic Layer : logique métier et entités principales.

# Persistence Layer : interaction avec la base de données.


# 2.Business Logic – Detailed Class Diagram

Ce diagramme détaille les entités du domaine métier : User, Place, Review, Amenity

''mermaid
classDiagram
class User {
    +UUID id
    +String firstName
    +String lastName
    +String email
    +String password
    +Boolean isAdmin
    +DateTime createdAt
    +DateTime updatedAt
    +register()
    +updateProfile()
    +delete()
}

class Place {
    +UUID id
    +String title
    +String description
    +Float price
    +Float latitude
    +Float longitude
    +DateTime createdAt
    +DateTime updatedAt
    +create()
    +update()
    +delete()
    +list()
}

class Review {
    +UUID id
    +Integer rating
    +String comment
    +DateTime createdAt
    +DateTime updatedAt
    +create()
    +update()
    +delete()
    +listByPlace()
}

class Amenity {
    +UUID id
    +String name
    +String description
    +DateTime createdAt
    +DateTime updatedAt
    +create()
    +update()
    +delete()
    +list()
}

User "1" --> "many" Place : owns >
User "1" --> "many" Review : writes >
Place "1" --> "many" Review : receives >
Place "1" --> "many" Amenity : has >
''

# User : gère l’inscription, le profil et peut être admin.

# Place : représente une annonce créée par un utilisateur.

# Review : évaluations laissées par des utilisateurs sur un lieu.

# Amenity : équipements associés à un lieu.

# Relations :

# Un utilisateur peut posséder plusieurs places et écrire plusieurs reviews.

# Une place a plusieurs reviews et plusieurs amenities.



# 3.Sequence Diagrams – API Calls

Ces séquences illustrent le flux d’exécution des principales API de l’application.

# User Registration:
''mermaid
sequenceDiagram
participant User
participant API
participant Facade
participant BusinessLogic
participant Database

User->>API: POST /register
API->>Facade: createUser(data)
Facade->>BusinessLogic: validate + create User
BusinessLogic->>Database: insert User
Database-->>BusinessLogic: success
BusinessLogic-->>Facade: return User object
Facade-->>API: return success response
API-->>User: User created
''

# Place Creation
''mermaid
sequenceDiagram
participant User
participant API
participant Facade
participant BusinessLogic
participant Database

User->>API: POST /places
API->>Facade: createPlace(data)
Facade->>BusinessLogic: validate + create Place
BusinessLogic->>Database: insert Place
Database-->>BusinessLogic: success
BusinessLogic-->>Facade: return Place object
Facade-->>API: return success response
API-->>User: Place created
''

# Review Submission
''mermaid
sequenceDiagram
participant User
participant API
participant Facade
participant BusinessLogic
participant Database

User->>API: POST /reviews
API->>Facade: addReview(data)
Facade->>BusinessLogic: validate + create Review
BusinessLogic->>Database: insert Review
Database-->>BusinessLogic: success
BusinessLogic-->>Facade: return Review object
Facade-->>API: return success response
API-->>User: Review submitted
''

# Fetching a List of Places
''mermaid
sequenceDiagram
participant User
participant API
participant Facade
participant BusinessLogic
participant Database

User->>API: GET /places
API->>Facade: listPlaces(criteria)
Facade->>BusinessLogic: fetch list
BusinessLogic->>Database: query Places
Database-->>BusinessLogic: results
BusinessLogic-->>Facade: return list
Facade-->>API: return response
API-->>User: List of Places
''
