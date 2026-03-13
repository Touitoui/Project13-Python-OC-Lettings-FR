Deploiement Et Gestion Applicative
==================================

Pipeline CI/CD
--------------

Le workflow GitHub Actions comporte trois jobs:

1. ``ci``: linting, tests, couverture (seuil >= 80%).
2. ``containerize``: build et push de l'image Docker (tags ``latest`` et SHA court).
3. ``deploy_production``: declenchement du deploiement Render via hook.

Le deploiement complet est execute lors d'un push sur ``master``.

Procedure De Deploiement
------------------------

1. Verifier localement ``flake8`` et ``pytest``.
2. Pousser le code et merger sur ``master``.
3. Controler les jobs GitHub Actions.
4. Verifier l'image publiee sur Docker Hub.
5. Verifier l'etat du service Render.

Configuration Production
------------------------

Variables critiques:

+-------------------------+-------------+--------------------------------------------------------------+
| Variable                | Obligatoire | Description                                                  |
+=========================+=============+==============================================================+
| ``SECRET_KEY``          | Oui         | Cle secrete Django utilisee pour la securite applicative.    |
+-------------------------+-------------+--------------------------------------------------------------+
| ``DJANGO_ALLOWED_HOSTS``| Oui         | Liste des hotes autorises, separes par des virgules.         |
+-------------------------+-------------+--------------------------------------------------------------+
| ``DEBUG``               | Oui         | Doit etre ``0`` en production pour des raisons de securite.  |
+-------------------------+-------------+--------------------------------------------------------------+
| ``DJANGO_LOG_LEVEL``    | Oui         | Niveau de journalisation (souvent ``INFO`` en production).   |
+-------------------------+-------------+--------------------------------------------------------------+
| ``SENTRY_DSN``          | Non         | DSN Sentry pour la supervision des erreurs en production.    |
+-------------------------+-------------+--------------------------------------------------------------+

Exploitation Courante
---------------------

Au demarrage du conteneur, ``entrypoint.sh`` execute:

1. migrations,
2. collecte des statiques,
3. creation conditionnelle d'un superutilisateur,
4. demarrage Gunicorn.

Supervision Et Maintenance
--------------------------

- Logs applicatifs par logger (``lettings``, ``profiles``, ``oc_lettings_site``).
- Capture des exceptions non gerees via Sentry si configure.
- En cas d'erreur ``DisallowedHost``, ajuster ``DJANGO_ALLOWED_HOSTS``.
