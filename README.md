# python-flask-rest-api
Repositório Exempo API Restful com Flask API e HTTP Basic

[![Python application](https://github.com/pauloricmarinho/python-flask-rest-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/pauloricmarinho/python-flask-rest-api/actions/workflows/python-app.yml)

### Enviroment Python

```
py -3 -m venv env_service
```

### Active Enviromnent

```
env_service/Scripts/activate
```

### Install Flask, Flash-Restful, FlaskHTTPAuth, SQLAlchemy, PyTest

```
pip3 install flask
pip3 install flask-restful
pip3 install sqlalchemy
pip3 install flask-httpauth
pip3 install flake pytest
```
 
 ### Docker Project [Python with Alpine 3.14](https://hub.docker.com/_/python)

```
docker build -t srv-pyhton-flask .
docker run -itd -p 8080:5000 --rm --name api-pyhton-flask  srv-pyhton-flask
curl server.docker:8080/produto
```