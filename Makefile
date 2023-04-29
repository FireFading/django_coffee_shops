build:
	docker compose up --build

up:
	docker compose up

down:
	docker compose down && docker network prune --force

clean:
	docker rm -f $(docker ps -qa) && docker volume rm $(docker volume ls)

test:
	docker exec -it django python manage.py test

migrate:
	docker exec -it django python manage.py makemigrations && docker exec -it django python manage.py migrate

static:
	docker exec -it django python manage.py collectstatic

shell:
	docker exec -it django python manage.py shell