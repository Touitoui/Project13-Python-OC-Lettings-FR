Guide D'Utilisation
===================

Profils D'Utilisateurs
----------------------

- Visiteur: consulte les locations et profils.
- Administrateur: gere les donnees via ``/admin``.

Cas D'Utilisation
-----------------

Consulter Les Locations
^^^^^^^^^^^^^^^^^^^^^^^

1. Ouvrir la page d'accueil ``/``.
2. Cliquer sur le lien vers ``/lettings/``.
3. Selectionner une location pour afficher son detail.

Consulter Les Profils
^^^^^^^^^^^^^^^^^^^^^

1. Ouvrir la page d'accueil ``/``.
2. Cliquer sur le lien vers ``/profiles/``.
3. Selectionner un profil pour afficher son detail.

Administrer L'Application
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Ouvrir ``/admin``.
2. Se connecter avec un compte superutilisateur.
3. Ajouter, modifier ou supprimer des enregistrements.

Bonnes Pratiques D'Usage
------------------------

- En local, utiliser ``DEBUG=1`` ; en production, ``DEBUG=0``.
- Ne jamais versionner le fichier ``.env``.
- Verifier les journaux applicatifs pour diagnostiquer les erreurs.
