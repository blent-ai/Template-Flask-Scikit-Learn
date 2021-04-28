# API Machine Learning

Pour utiliser l'API, il faut avoir Python 3 d'installé et utiliser les [environnements virtuels](https://docs.python.org/fr/3/library/venv.html).

```
python3 -m venv venv
# Pour Linux et macOS
source venv/bin/activate
# Pour Windows
C:\\{chemin d'accès au dossier venv}\\Scripts\\activate.bat
```

On peut ensuite installer en local les dépendances.

```
pip install -r requirements.txt
```

Et il ne reste plus qu'à lancer l'API.

```
python3 app.py
```

## Déploiement de l'API

Pour déployer l'API, il est nécessaire d'avoir Git d'installé et d'avoir un compte Heroku.

```
git init
git add .
git commit -am "Mon premier commit"

```

Nous pouvons ensuite créer un nouveau projet Heroku.

```
heroku create
```

Cela va configurer automatiquement le projet avec Heroku. Il ne reste plus qu'à faire un `push`.

```
git push heroku master
```