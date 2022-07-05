# Basic Flask ToDo API
A basic version of a ToDo API using Flask with SqlAlchemy. 

## Tech

![](https://img.shields.io/static/v1?style=for-the-badge&label=Python&message=3.10&color=006600&logo=python)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Flask&message=2.0&color=006600&logo=jetbrains)   
![](https://img.shields.io/static/v1?style=for-the-badge&label=Pycharm&message=2021.3.2&color=006600&logo=pycharm)  
![](https://img.shields.io/static/v1?style=for-the-badge&label=Sqlite&message=3.0&color=006600&logo=sqlite)  

## Get all ToDos

**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/todos/&color=005599)

```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/todos/
```

**Response**

```text
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "pk": "integerS",
    "body": "string",
    "created": "datetime"
}
```

## Create ToDo
**Request**

![](https://img.shields.io/static/v1?label=POST&message=/api/todos/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/todos/
```
**Response**
```text
HTTP/1.1 201 OK
Content-Type: application/json
```
```json
{
    "body": "string"
}
```

## Get single ToDo
**Request**

![](https://img.shields.io/static/v1?label=GET&message=/api/todos/<int:pk>&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/todos/:pk
```
**Response**
```text
HTTP/1.1 200 OK
Content-Type: application/json
```
```json
{
    "pk": "integer",
    "body": "string",
    "created": "datetime"
}
```

## Update ToDo
**Request**

![](https://img.shields.io/static/v1?label=PUT&message=/api/todos/:pk&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/todos/:pk
```
**Response**
```text
HTTP/1.1 200 OK
Content-Type: application/json
```
* Since it's a Patch request each item can be updated individually (except update date)
```json
{
    "pk": 1,
    "body": "string",
    "created": "datetime"
}
```

## Delete ToDo
**Request**

![](https://img.shields.io/static/v1?label=DELETE&message=/api/todos/<int:pk>/&color=005599)
```text
curl -i -H 'Accept: application/json' http://localhost:5000/api/todos/:pk
```
```text
HTTP/1.1 204 OK
Content-Type: application/json
```

**Response**
```text
[]
```

## Additional packages used

* [Flask-Sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
* [Marshmallow-Sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)

[//]: # (* [Psycopg]&#40;https://www.psycopg.org/&#41;  // PostgreSQL adapter for the Python programming language)
* [Gunicorn](https://gunicorn.org/)  // Python WSGI HTTP Server for UNIX

### Notes

* Requirements.txt file is included
* The latest Marshmallow version (3.14.1) throws a type error: got an unexpected keyword argument 'strict'. The workaround is to install an older version (2.20.1)

[//]: # (* For some reason I can't get the Postgress python adapter to work on m1 mac. )




