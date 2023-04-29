## Features
- registration/authentication
- custom User model with custom UserManager that without username
- change password
- reset password with email
- email subscription with celery
- get all shops
- get all menu items
- get detail information about shop/menu item

![image](https://user-images.githubusercontent.com/91421235/233180044-4b3dd8f4-c3a1-469d-931a-8afa2e7aef4b.png)

## Installation
- in env.example all variables used in project, change it to .env, several variables that are common, already define as example, secret variables is empty
- in app folder create `media/` and `static/` folders
- collect static
```bash
  docker exec -it django python manage.py collectstatic
```
- createsuperuser
```bash
  docker exec -it django python manage.py createsuperuser
```

## Run Locally
```bash
  docker compose up
```
OR `make up` - run without building, also you can prove -d flag to run as daemon

## Down docker
```bash
  docker compose down && docker network prune --force
```
OR `make down`

## Migrations
```bash
  docker exec -it django python manage.py makemigrations
  docker exec -it django python manage.py migrate
```
OR `make migrate`


## formatting and linting
- run ufmt: `ufmt format .`
- run black: `black --config=configs/.black.toml app`
- run ruff: `ruff check --config=configs/.ruff.toml --fix app`
- run flake8: `flake8 --config=configs/.flake8 app`
- OR `nox` in root