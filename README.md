## Features
- registration/authentication
- custom User model with custom UserManager without username
- change password
- reset password with email
- email subscription with celery
- edit profile information
- get all shops/products/recipes
- add new shop/product/recipe
- filter & ordering information about shops by name/address, etc
- filter & ordering information about products by name/price/category/shop, etc
- filter & ordering information about recipes by name/product, etc
- get detail information about shop/product
- edit shops/product
- delete shops/product after confirmation
- different roles for users
- add comments for products for authorized users
- ask questions
- add to favorites/remove from favorites
- self-created css and html

## Installation
- in env.example all variables used in project, change it to .env, several variables that are common, already define as example, secret variables is empty
- in app folder create `media/` folder
- collect static:
```bash
  docker exec -it django python manage.py collectstatic
```
OR `make static`
- apply migrations:
```bash
  docker exec -it django python manage.py makemigrations && docker exec -it django python manage.py migrate
```
OR `make migrate`
- createsuperuser
```bash
  docker exec -it django python manage.py createsuperuser
```
OR `make superuser`
## Run Locally
```bash
  docker compose up
```
OR `make up` - run without building, also you can prove -d flag to run as daemon

## Down docker
```bash
  docker compose down && docker network prune --force
```
OR `make down` OR `make clean` to cleanup all containers and networks

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
