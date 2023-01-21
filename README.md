## Crear un entorno virtual
```py
python -m venv venv
```

## Activamos el entorno virtual

## Instalamos flask

```py
pip install flask
```

## Correr la aplicacion de flask

```py
flask --debug run
```
## Instalar  Sql Alquemy

```py
pip install Flask-SQLAlchemy
```
## Registrar las dependencias que estamos instalando
```py
pip freeze > requirements.txt
```

## Migrar la base de datos
```py
pip install Flask-Migrate
flask db init
flask db migrate -m "Comentario"
flask db upgrade
```