## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure, mais inférieure à 3.14 (3.10 conseillée)

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Paramétrer les variables d'environnement

Le projet charge ses variables depuis un fichier `.env` à la racine (via `python-dotenv`).

Copiez le fichier d'exemple puis éditez-le :

- macOS / Linux : `cp .env.example .env`
- Windows : `copy .env.example .env`

Renseignez les variables suivantes dans `.env` :

| Variable | Obligatoire | Description |
|---|---|---|
| `SECRET_KEY` | Oui | Clé secrète Django. Générez-en une avec `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `ALLOWED_HOST` | Oui | Hôte autorisé. En développement local, utilisez `localhost`. |
| `SENTRY_DSN` | Non | DSN de votre projet Sentry. Si absent ou vide, Sentry est désactivé. |
| `DJANGO_LOG_LEVEL` | Non | Niveau de log (`DEBUG`, `INFO`, `WARNING`…). Défaut : `INFO`. |

> **Sécurité** : `.env` est listé dans `.gitignore` — ne le committez jamais.

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires (avec couverture et rapport html)

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest --cov=lettings --cov=profiles --cov=oc_lettings_site --cov-report=term-missing --cov-report html`

#### Sentry

Sentry est utilisé pour le suivi des erreurs en production. Il est **désactivé par défaut** si `SENTRY_DSN` est absent du `.env`.

Pour l'activer :

- Créez un compte sur [sentry.io](https://sentry.io) et créez un nouveau projet de type **Django**.
- Copiez le DSN fourni par Sentry (Settings → Projects → votre projet → Client Keys).
- Ajoutez-le dans votre `.env` :
   ```
   SENTRY_DSN=https://<key>@<org>.ingest.sentry.io/<project>
   ```
- Redémarrez le serveur. Les erreurs non gérées seront désormais remontées automatiquement dans votre tableau de bord Sentry.



#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

