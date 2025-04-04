
start:
	sudo ./dockersetup
	sudo bash
	docker compose up -d
	clear
	docker ps

stop:
	docker compose down

refresh:
	git pull