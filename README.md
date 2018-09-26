# Falcon RBAC Starter

## Introduction

This Project is a general starter/example of how to do Role Based Access Control(rbac) in Falcon using SQLAlchemy. Feel free to fork this project and contribute.

## Get Started

### Docker

To get started:
```
docker build . -t falcon-rbac
docker run --name fbac -p 9002:80 -d falcon-rbac

```

Nginx is listening on port 80 and Gunicorn can be accessed on port 8000 inside the container.

## To Do
- Add docker-compose
- Add base migrations
- Testing