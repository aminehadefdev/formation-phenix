import os
import sqlite3
import click
from flask import current_app, g


def get_db():
    """Obtient une connexion à la base de données."""
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    """Ferme la connexion à la base de données."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Initialise la base de données avec le schéma."""
    db = get_db()
    with current_app.open_resource("db.sql") as f:
        db.executescript(f.read().decode("utf8"))


@click.command("init-db")
def init_db_command():
    """Commande pour initialiser la base de données."""
    init_db()
    click.echo("Base de données initialisée.")


def init_app(app):
    """Initialise l'application avec les fonctions de base de données."""
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
