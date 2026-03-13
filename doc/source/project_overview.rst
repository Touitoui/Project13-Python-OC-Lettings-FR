Description Du Projet
=====================

Contexte
--------

Orange County Lettings est une application web Django qui expose:

- une page d'accueil ;
- un module de locations (lettings) ;
- un module de profils utilisateurs ;
- une interface d'administration Django.

Le projet est decoupe en trois applications Django principales:

- ``oc_lettings_site``: coeur du projet (configuration, routes globales, vues de base) ;
- ``lettings``: gestion des locations et des adresses ;
- ``profiles``: gestion des profils relies aux utilisateurs Django.

Objectifs Techniques
--------------------

- Fournir une application web simple, testee et deployee en conteneur Docker.
- Assurer la qualite via linting, tests unitaires et seuil de couverture.
- Centraliser les erreurs applicatives via Sentry (optionnel selon configuration).

Architecture Generale
---------------------

L'application suit l'architecture MVC de Django (Model-Template-View):

- Models: persistance des donnees dans SQLite ;
- Views: logique de presentation et recuperation des donnees ;
- Templates: rendu HTML ;
- URL routing: correspondance des endpoints HTTP vers les vues.

Les fichiers statiques sont servis via WhiteNoise en execution Gunicorn.
