
start:
	docker compose up -d
	docker compose build

stop:
	docker compose down

refresh:
	git pull