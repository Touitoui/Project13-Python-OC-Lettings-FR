Guide De Demarrage Rapide
=========================

Demarrage Local En 5 Minutes
----------------------------

1. Activer l'environnement virtuel.
2. Installer les dependances.
3. Configurer ``.env``.
4. Lancer le serveur.

Commandes:

.. code-block:: bash

   pip install -r requirements.txt
   python manage.py runserver

Acceder ensuite a:

- ``http://localhost:8000`` (site)
- ``http://localhost:8000/admin`` (administration)

Demarrage Rapide Docker
-----------------------

.. code-block:: bash

   docker compose up --build

Verification Rapide
-------------------

- La page d'accueil s'affiche.
- La liste des profils et des locations est accessible.
- L'interface admin est joignable.
