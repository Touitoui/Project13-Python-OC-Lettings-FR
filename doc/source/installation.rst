Installation Du Projet
======================

Prerequis
---------

- Git
- Python 3.10 recommande
- pip
- SQLite3 (optionnel, pour inspection manuelle de la base)
- Docker Desktop (optionnel, pour execution des images en local)

Installation Locale
-------------------

1. Cloner le depot:

   .. code-block:: bash

      git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git
      cd Python-OC-Lettings-FR

2. Creer un environnement virtuel:

   .. code-block:: bash

      python -m venv venv

3. Activer l'environnement virtuel:

   .. code-block:: powershell

      .\venv\Scripts\Activate.ps1

   .. code-block:: bash

      source venv/bin/activate

4. Installer les dependances:

   .. code-block:: bash

      pip install -r requirements.txt

Configuration Des Variables D'Environnement
-------------------------------------------

1. Copier le fichier d'exemple:

   .. code-block:: bash

      cp .env.example .env

   Sous Windows (PowerShell):

   .. code-block:: powershell

      copy .env.example .env

2. Renseigner au minimum:

+-------------------------+--------------------------------------------------------------+
| Variable                | Description                                                  |
+=========================+==============================================================+
| SECRET_KEY              | Cle secrete Django utilisee pour la securite applicative.    |
+-------------------------+--------------------------------------------------------------+
| DJANGO_ALLOWED_HOSTS    | Liste des hotes autorises, separes par des virgules.         |
+-------------------------+--------------------------------------------------------------+

Variables utiles:

+---------------------------+-------------+--------------------------------------+
| Variable                  | Obligatoire | Description                          |
+===========================+=============+======================================+
| DEBUG                     | Non         | Active le mode debug.                |
+---------------------------+-------------+--------------------------------------+
| DJANGO_LOG_LEVEL          | Non         | Definit le niveau de logs.           |
+---------------------------+-------------+--------------------------------------+
| SENTRY_DSN                | Non         | Active la remontee d'erreurs Sentry. |
+---------------------------+-------------+--------------------------------------+
| DJANGO_SUPERUSER_USERNAME | Non         | Nom du superutilisateur auto-cree.   |
+---------------------------+-------------+--------------------------------------+
| DJANGO_SUPERUSER_EMAIL    | Non         | Email du superutilisateur auto-cree. |
+---------------------------+-------------+--------------------------------------+
| DJANGO_SUPERUSER_PASSWORD | Non         | Mot de passe du superutilisateur.    |
+---------------------------+-------------+--------------------------------------+

Installation Avec Docker
------------------------

1. Verifier la presence du fichier ``.env``.
2. Construire l'image:

   .. code-block:: bash

      docker compose build

3. Lancer l'application:

   .. code-block:: bash

      docker compose up

Le conteneur execute automatiquement:

- ``python manage.py migrate``
- ``python manage.py collectstatic``
- creation optionnelle du superutilisateur
- demarrage Gunicorn
