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
| `DJANGO_ALLOWED_HOSTS` | Oui | Hôtes autorisés, séparés par des virgules. En développement local, utilisez `localhost,127.0.0.1`. |
| `SENTRY_DSN` | Non | DSN de votre projet Sentry. Si absent ou vide, Sentry est désactivé. |
| `DJANGO_LOG_LEVEL` | Non | Niveau de log (`DEBUG`, `INFO`, `WARNING`…). Défaut : `INFO`. |
| `DEBUG` | Non | Active le mode debug Django. Utilisez `1` en local et `0` en production. |
| `DJANGO_SUPERUSER_USERNAME` | Non | Nom d'utilisateur de l'administrateur créé automatiquement au démarrage du conteneur. |
| `DJANGO_SUPERUSER_EMAIL` | Non | Email de l'administrateur créé automatiquement au démarrage du conteneur. |
| `DJANGO_SUPERUSER_PASSWORD` | Non | Mot de passe de l'administrateur créé automatiquement au démarrage du conteneur. |

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
- Si les variables `DJANGO_SUPERUSER_*` sont renseignées, connectez-vous avec ces identifiants.

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Docker (Python 3.10)

Cette configuration Docker utilise une image Python 3.10 multi-stage et demarre l'application avec Gunicorn. Au lancement, le conteneur applique automatiquement les migrations, collecte les fichiers statiques et peut creer un superuser si les variables requises sont presentes.

#### Prerequis

- Docker Desktop installe et demarre
- Fichier `.env` present a la racine (copiez `.env.example` si necessaire)

Valeurs conseillees dans `.env` pour du local :

- `SECRET_KEY=<votre-cle-secrete>`
- `DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1`
- `DEBUG=1`
- `DJANGO_LOG_LEVEL=INFO`
- `SENTRY_DSN=` (laisser vide si vous ne l'utilisez pas)
- `DJANGO_SUPERUSER_USERNAME=admin`
- `DJANGO_SUPERUSER_EMAIL=admin@example.com`
- `DJANGO_SUPERUSER_PASSWORD=<mot-de-passe-fort>`

#### Lancer l'application

- Construire et demarrer : `docker compose up --build`
- Ouvrir : `http://localhost:8000`

Le service execute automatiquement les migrations, collecte les fichiers statiques, cree le superuser si configure, puis lance Gunicorn.

#### Arreter

- `docker compose down`

#### Redemarrer apres modification de dependances

- `docker compose build --no-cache`
- `docker compose up`

#### Lancer une image Docker Hub localement

- Recuperer et lancer l'image publiee : `docker run --rm -p 8000:8000 --env-file .env <dockerhub-user>/oc-lettings-site:latest`

## Déploiement

### Vue d'ensemble

Le déploiement en production est orchestré par GitHub Actions et repose sur trois étapes chaînées :

1. Le job `ci` exécute `flake8`, `pytest` et vérifie que la couverture reste supérieure ou égale à 80 %.
2. Le job `containerize` construit l'image Docker puis la publie sur Docker Hub avec deux tags : `latest` et un tag basé sur le hash court du commit.
3. Le job `deploy_production` déclenche Render via un Deploy Hook pour déployer la dernière image publiée.

Les pushes sur `master` déclenchent toute la chaîne. Les autres branches n'exécutent que la CI.

### Configuration requise

#### GitHub

Dans `Settings > Secrets and variables > Actions`, créer les secrets suivants :

- `DOCKERHUB_USERNAME` : nom du compte Docker Hub.
- `DOCKERHUB_TOKEN` : access token Docker Hub avec droits de push.
- `RENDER_DEPLOY_HOOK_URL` : URL du Deploy Hook du service Render.

Le workflow est défini dans `.github/workflows/ci-cd.yml`.

#### Docker Hub

- Créer le repository qui recevra l'image, par exemple `<dockerhub-user>/oc-lettings-site`.
- Vérifier que le nom du repository correspond bien à celui utilisé dans le workflow GitHub Actions.

#### Render

- Créer un Web Service basé sur une image Docker Hub.
- Configurer l'image `docker.io/<dockerhub-user>/oc-lettings-site:latest`.
- Utiliser le plan souhaité et conserver le déploiement piloté par le Deploy Hook.
- Ajouter les variables d'environnement suivantes dans Render :
   - `SECRET_KEY`
   - `DJANGO_ALLOWED_HOSTS` avec le domaine Render, par exemple `mon-service.onrender.com`
   - `DJANGO_LOG_LEVEL=INFO`
   - `DEBUG=0`
   - `SENTRY_DSN` si utilisé, sinon vide
   - `DJANGO_SUPERUSER_USERNAME`
   - `DJANGO_SUPERUSER_EMAIL`
   - `DJANGO_SUPERUSER_PASSWORD`

### Procédure de déploiement

1. Vérifier que le code local passe `flake8` et `pytest`.
2. Committer et pousser les changements sur une branche de travail pour valider la CI seule.
3. Ouvrir une Pull Request et fusionner sur `master` une fois la CI validée.
4. Après le push sur `master`, contrôler dans GitHub Actions que les jobs `ci`, `containerize` puis `deploy_production` passent dans cet ordre.
5. Vérifier sur Docker Hub la présence des tags `latest` et du tag court de commit.
6. Vérifier sur Render que le déploiement s'est exécuté correctement et que le site répond.
7. Se connecter à `/admin` avec les identifiants définis dans `DJANGO_SUPERUSER_*`.

### Dépannage rapide

- Si `containerize` échoue, vérifier les secrets Docker Hub et le nom du repository cible.
- Si `deploy_production` échoue, vérifier `RENDER_DEPLOY_HOOK_URL` et la disponibilité du service Render.
- Si l'accès au site échoue avec `DisallowedHost`, corriger `DJANGO_ALLOWED_HOSTS` dans Render.
- Si l'administrateur n'existe plus après un redéploiement, vérifier les variables `DJANGO_SUPERUSER_*` et redéployer.

