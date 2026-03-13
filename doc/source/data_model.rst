Structure De La Base Et Modeles
===============================

Base De Donnees
---------------

Le projet utilise SQLite via la configuration Django:

- Moteur: ``django.db.backends.sqlite3``
- Fichier: ``oc-lettings-site.sqlite3``

Modeles Applicatifs
-------------------

Modele ``Address`` (application ``lettings``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``number``: entier positif (max 9999)
- ``street``: chaine (64)
- ``city``: chaine (64)
- ``state``: chaine (2)
- ``zip_code``: entier positif (max 99999)
- ``country_iso_code``: chaine (3)

Modele ``Letting`` (application ``lettings``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``title``: chaine (256)
- ``address``: relation ``OneToOne`` vers ``Address``

Modele ``Profile`` (application ``profiles``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``user``: relation ``OneToOne`` vers ``django.contrib.auth.models.User``
- ``favorite_city``: chaine (64), optionnelle

Relations Entre Entites
-----------------------

- ``Letting`` $1 \leftrightarrow 1$ ``Address``
- ``Profile`` $1 \leftrightarrow 1$ ``User``

Tables Principales
------------------

Les tables varient selon les migrations, mais on retrouve notamment:

- tables Django natives (``auth_*``, ``django_*``)
- table des adresses (``lettings_address``)
- table des locations (``lettings_letting``)
- table des profils (``profiles_profile``)
