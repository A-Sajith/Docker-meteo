# Docker-Météo   

Petite application en Python qui permet d’afficher la météo en temps réel d’une ville directement dans le terminal.

## Pourquoi ce projet ?  

J’ai choisi de faire ce projet pour travailler sur une application concrète qui utilise une API externe. L’idée était de sortir d’un simple script pour manipuler des données en temps réel et comprendre comment une application récupère et affiche des informations venant d’un service externe.  

Ce projet m’a aussi permis de mettre en place de bonnes pratiques, notamment la gestion des données sensibles avec un fichier `.env` au lieu de les mettre directement dans le code.  

Enfin, c’était un bon moyen de combiner plusieurs notions : requêtes HTTP, traitement de JSON et utilisation de Docker pour exécuter l’application dans un environnement isolé.

## Technologies utilisées  

- Python 3.11  
- Docker  
- API OpenWeatherMap (https://openweathermap.org)  
- python-dotenv  

## Fonctionnement  

Le principe est simple :  

1. L’utilisateur entre une ville  
2. L’application envoie une requête à l’API OpenWeatherMap  
3. Elle récupère les données au format JSON  
4. Elle affiche les infos utiles dans le terminal  

## Lancer le projet avec Docker  

### 1. Cloner le repo  
```bash
git clone https://github.com/A-Sajith/meteo-cli
cd meteo-cli
```

### 2. Créer le fichier `.env`

Pour simplifier l’utilisation du projet, la clé API est fournie directement.  
Il s’agit d’une API météo gratuite, donc il n’y a pas de risque particulier ici.  

⚠️ En revanche, dans un contexte réel (projet perso sérieux ou entreprise), il ne faut jamais partager une clé API. Chacun doit utiliser la sienne et la garder privée.  
Et ne pas abusez des requêtes car il existe une limite de requêtes gratuite par jour.  
Créer un fichier `.env` à la racine du projet avec :  

```bash
API_KEY=1c43ac61b776ea320a9f265e77c85b37
```

### 3. Builder l’image  
```bash
docker build -t meteo-cli .
```

### 4. Lancer le container  
```bash
docker run -it meteo-cli
```

## Structure du projet  

```bash
meteo-cli/
├── meteo.py       # Code principal
├── Dockerfile     # Configuration Docker
├── .env           # Clé API (non versionné)
└── .gitignore     # Ignore le .env
```
