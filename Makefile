all: build

pull:
	docker compose pull

build: pull
	docker compose build

up: build
	docker compose up --detach --force-recreate

down:
	docker compose down

.PHONY: pull build up down
