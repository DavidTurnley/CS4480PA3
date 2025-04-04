
start:
	sudo ./dockersetup
	sudo bash
	docker compose up -d
	clear
	docker ps

stop:
	docker compose down

refresh:
	cd ~
	git pull https:github.com/DavidTurnley/CS4480PA3