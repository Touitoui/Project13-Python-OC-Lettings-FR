Interfaces De Programmation
===========================

Vue D'Ensemble
--------------

Le projet expose des interfaces HTTP serveur-rendu (pas d'API REST dediee).

Routes HTTP Principales
-----------------------

- ``GET /``: page d'accueil
- ``GET /lettings/``: liste des locations
- ``GET /lettings/<letting_id>/``: detail d'une location
- ``GET /profiles/``: liste des profils
- ``GET /profiles/<username>/``: detail d'un profil
- ``/admin/``: interface d'administration Django

Gestion Des Erreurs
-------------------

- Gestionnaire 404 personnalise: ``oc_lettings_site.views.handler404``
- Gestionnaire 500 personnalise: ``oc_lettings_site.views.handler500``

Interfaces Internes
-------------------

Interface Django ORM:

- acces aux donnees via ``Letting.objects`` et ``Profile.objects`` ;
- recherche detail via identifiant de location ou nom d'utilisateur.

Interface De Monitoring:

- integration Sentry activee si ``SENTRY_DSN`` est renseigne.
