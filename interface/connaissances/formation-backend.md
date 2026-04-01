# Formation Backend (Flask)

## 1/ Installation

Chaque apprenant part de flask-intro.zip

1. Dézipper
2. Suivre le readme.md pour installer et faire tourner le flask
3. Revenir ensuite sur chaque commande pour expliquer:

- que python se lance en ligne de commande, que c'est installer sur l'ordi contrairement aux html/CSS/JS qui ont besoin du navigateur
- qu'à l'époque il y avait le mélange python2.7 et python3 sur les ordis, que c'était horrible et que du coup pour éviter ca la commande c'est "python3 ..."
- que chaque language vient avec son installateur: python/pip, node/npm, et même linux/apt, d'où le pip install -r requirements.txt
- que là c'est notre premier projet mais si on en refait un de flask dans 2 mois, nouvelles versions... d'où le venv/bin/activate, que ce dossier on y touche jamais c'est l'usine de Python
- que ca fait beaucoup, c'est nouveau mais en fait de toutes ces commandes, au jour le jour, on garde que une ou deux + sortez vos post-its pour les noter !

## 2/ Découverte des routes

Pour chaqu'un des exos suivants, donner un exemple et l'expliquer puis seulement, donner un exo (variantes).

### Route simple

Ensemble: Route /salut qui retourne "Salut".
Variantes à faire seul: Route /bonjour, /bonsoir

### Premier template

Ensemble: Changer /salut pour qu'elle utilise salut.html
Seul: Idem pour /bonjour, /bonsoir

### Première variable dans un template et dans la route

- Faire faire d'abord en dûr /salut-salem /salut-amandine et /salut-thomas qui retrounes "Salut Salem" ...
- Donner et expliquer le code de /salut-<nom> qui retourne render_template("salut.hytml", name=nom) et utiliser {{ name }} dans le template
  Note: faire exprès de changer "nom" en "name" pour montrer la tuyauterie
- A eux de faire la même chose pour /bonjour-<nom>
- Puis /bonjour-<nom>-<prenom>

### Premiers calculs dans la route

- Ensemble /double-<nombre> => retourne 2 \* nombre
- Oh ! ca marche pas, ca montre "22" au lieu de "4"
- Expliquer qu'il y a des types
- Corriger la route /double-<int:nombre>
- Faire faire /triple-X, /addition-X-Y, /multiplication-X-Y-Z

## 3/ CRUD pas à pas

L'idée est de faire ensemble deux CRUD complets, un pour les users, un pour les posts.
Pour chaque route, donner le code et expliquer pour user et ensuite, leur dire de faire pareil pour posts seul

- GET /users /posts
- GET /users/<id> /posts/<id> + ajouter les liens "voir détail" devant chaque user dans users.html
- POST /users/new /posts/new + ajouter un lien "Ajouter" dans la page /users
- POST /users/<id>/update + ajouter les liens "modifier" devant chaque user dans users.html
- GET /users/<id>/delete + ajouter les liens "supprimer" devant chaque user dans users.html

## 4/ CRUD en autonomie

Leur dire de refaire tout ca pour une nouvelle table qu'il créeront eux-même, par exemple book ou song

## 5/ Divers

La base est normalement comprise à cette étape là. C'est l'occasion de rajouter des points un peu chaque jour:

### Blueprints

- Refactoriser le code pour utiliser des blueprints pour users, posts, puis la troisième table

### base.html

- Refactoriser le code pour utiliser un base.html
- expliquer que ca permet d'écrire une seule fois le <head> le <header> le <footer> etc.

### Améliorer New/update

- Ajouter des gestions d'erreurs
- Mutualiser new-user.html et update-user.html

### Login/signup

- Donner et expliquer le code du login/signup D'ABORD SANS LE generate_hash et decode_hash
- Expliquer que là ya une grosse faille de sécu parce que le password est en clair dans la base
- corriger le code avec generate_hash/decode_hash et montrer que ce sont juste ces deux "petites" fonctions qui font en fait un travail très important
- pour expliquer le hash, expliquer que c'est comme si on utilisait un gros projecteur devant chaque personne qui s'inscrit et qu'on ne sauvegarder que son ombre/silhouette sur le mur. On sait pas qui s'est mais on peut quand même t'identifier
- expliquer le @login_required
