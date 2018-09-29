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

## Building Your Auth System

### Overview

#### Permissions

This system relies on bitwise operators and permissions that corrospond with integers. List your permissions under hooks/authorize.py and multiply the permissions value by 2 against the last permission.

Example:
```python

AvailablePermissions = {
	'allowAPI:'1,
	'canDeleteUsers':2,
	'canAddNotes':4,
	'canModifyNotes':8,
	#...
}

```

#### Roles

Roles define a set of permissions that might encompass a user type or a subset of functions.

Example:
```python

PermissionRoles = {
	'is_free_user': [
		'allowAPI',
		'canAddNotes'
	],
	'is_free_admin': [
		'canDeleteUsers'
	]
}

````


#### Roles





## To Do
- Add docker-compose
- Add base migrations
- Finish the readme
- Testing