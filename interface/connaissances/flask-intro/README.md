# 🌟 Projet Flask - Introduction

Ce projet est une application Flask simple qui suit le tutoriel officiel, sans les tests et sans les blueprints.

## 📦 Fonctionnalités

- ✅ Application Flask de base
- ✅ Base de données SQLite
- ✅ Templates HTML avec Jinja2
- ✅ Routes dynamiques (`/hello` et `/hello/<name>`)
- ✅ Commande d'initialisation de la base de données
- ✅ Gestion des connexions à la base de données

## 🚀 Installation et Configuration

### 1. Prérequis

- Python 3.8 ou plus récent
- pip (gestionnaire de paquets Python)

### 2. Installation

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## 🗄️ Configuration de la base de données

### Initialiser la base de données

```bash
# Initialiser la base de données avec le schéma
flask --app app init-db
```

Cette commande :

- Crée la base de données SQLite
- Exécute le script `db.sql`
- Ajoute des données d'exemple

## 🏃‍♂️ Lancement de l'application

### Méthode 1 : Avec Flask CLI

```bash
# Lancer le serveur de développement
flask --app app run

# Ou en mode debug
flask --app app run --debug
```

### Méthode 2 : Avec Python

```bash
python app.py
```

### Méthode 3 : Configuration avec variables d'environnement

```bash
# Configurer Flask
export FLASK_APP=app
export FLASK_ENV=development

# Lancer l'application
flask run
```

## 🌐 Routes disponibles

- `http://localhost:5000/` - Page d'accueil
- `http://localhost:5000/hello` - Hello World
- `http://localhost:5000/hello/<nom>` - Hello personnalisé

## 📁 Structure du projet

```
flask-intro/
│
├── app.py                 # Application principale Flask
├── db.py                  # Gestion de la base de données
├── db.sql                 # Script de création de la base de données
├── requirements.txt      # Dépendances Python
├── README.md            # Ce fichier
│
├── static/              # Fichiers statiques (CSS, JS, images)
│   └── css/
│       ├── reset.css   # Reset CSS
│       └── hello.css   # Styles pour les pages
│
├── templates/           # Templates HTML
│   └── hello.html      # Template pour les pages hello
│
├── instance/           # Dossier pour la base de données (créé automatiquement)
│   └── flaskr.sqlite  # Base de données SQLite
│
└── venv/              # Environnement virtuel (créé lors de l'installation)
```

## 🔧 Développement

### Commandes utiles

```bash
# Réinitialiser la base de données
flask --app app init-db

# Lancer en mode debug
flask --app app run --debug

# Accéder au shell Flask
flask --app app shell
```

### Ajouter de nouvelles routes

Modifiez le fichier `app.py` et ajoutez vos routes :

```python
@app.route('/nouvelle-route')
def nouvelle_fonction():
    return render_template('nouveau_template.html')
```

### Modifier la base de données

1. Modifiez `db.sql`
2. Réinitialisez la base : `flask --app app init-db`

## 🐛 Dépannage

### Problème : "No module named flask"

```bash
# Vérifier que l'environnement virtuel est activé
source venv/bin/activate

# Réinstaller Flask
pip install Flask
```

### Problème : Base de données non trouvée

```bash
# Initialiser la base de données
flask --app app init-db
```

## 📚 Ressources

- [Documentation officielle Flask](https://flask.palletsprojects.com/)
- [Tutoriel Flask](https://flask.palletsprojects.com/tutorial/)
- [SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

---

**Bon développement ! 🐍✨**
