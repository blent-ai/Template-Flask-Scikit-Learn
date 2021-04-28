# API Machine Learning

Pour utiliser l'API, il faut avoir Python 3 d'installé et utiliser les [environnements virtuels](https://docs.python.org/fr/3/library/venv.html).

```
python3 -m venv venv
# Pour Linux et macOS
source venv/bin/activate
# Pour Windows
C:\\{chemin d'accès au dossier venv}\\Scripts\\activate.bat
```

## Configuration du projet

Pour l'API, il est nécessaire d'avoir 

```
git init
git add .
git commit -am "Mon premier commit"

```

Nous pouvons ensuite créer un nouveau projet Heroku.

```
heroku create
```

Puis il ne reste plus qu'à faire un `push`.

```
git push heroku main
```

## Dépendances

### En local

Pour tester l'API en local, il faut tout d'abord créer un environnement virtuel.

```
python3 -m venv venv
source venv/bin/activate
```

```
npm install --save serverless-python-requirements serverless-wsgi
```