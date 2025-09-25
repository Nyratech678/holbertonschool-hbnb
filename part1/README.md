# 0. High-Level Package Diagram

## Objectif
Ce document présente un diagramme de haut niveau qui illustre l’architecture en trois couches de l’application **HBnB**, ainsi que l’utilisation du **Facade Pattern** pour organiser la communication entre les couches.

---

## Diagramme des packages

```mermaid
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
