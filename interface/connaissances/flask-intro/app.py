import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"
app.config["DATABASE"] = os.path.join(app.instance_path, "flaskr.sqlite")

# Assure que le dossier instance existe
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Initialise la base de données
db.init_app(app)


@app.before_request
def load_logged_in_user():
    """Charge l'utilisateur connecté avant chaque requête."""
    user_id = session.get('user_id')
    
    if user_id is None:
        g.user = None
    else:
        database = db.get_db()
        g.user = database.execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(f):
    """Décorateur pour les routes nécessitant une connexion."""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash('Veuillez vous connecter pour accéder à cette page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    """Page d'accueil."""
    if g.user:
        message = f"Bienvenue, {g.user['username']} !"
    else:
        message = "Bienvenue dans votre application Flask !"
    return render_template("hello.html", message=message)


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    """Route hello world."""
    if name is None:
        name = "Monde"
    return render_template("hello.html", message=f"Bonjour, {name} !")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Route d'inscription."""
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Créer l'utilisateur
        database = db.get_db()
        database.execute(
            'INSERT INTO user (username, email, password_hash) VALUES (?, ?, ?)',
            (username, email, password)
        )
        database.commit()
        
        flash("Inscription réussie ! Vous pouvez maintenant vous connecter.", "success")
        return redirect(url_for("login"))
    
    return render_template("auth/register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Route de connexion."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Chercher l'utilisateur
        database = db.get_db()
        user = database.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        
        if user and user['password_hash'] == password:
            # Connexion réussie
            session.clear()
            session['user_id'] = user['id']
            flash(f"Bienvenue, {user['username']} !", "success")
            return redirect(url_for('index'))
        else:
            flash("Nom d'utilisateur ou mot de passe incorrect.", "error")
    
    return render_template("auth/login.html")


@app.route("/logout")
@login_required
def logout():
    """Route de déconnexion."""
    session.clear()
    flash("Vous avez été déconnecté.", "info")
    return redirect(url_for("index"))


@app.route("/profile")
@login_required
def profile():
    """Page de profil utilisateur."""
    return render_template("auth/profile.html")


if __name__ == "__main__":
    app.run(debug=True)
