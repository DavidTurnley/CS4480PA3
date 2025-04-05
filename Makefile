
start:
	docker compose up -d
	docker compose build
	docker cp ./Daemons Router1:etc/frr/
	docker cp ./Daemons Router2:etc/frr/
	docker cp ./Daemons Router3:etc/frr/
	docker cp ./Daemons Router4:etc/frr/

stop:
	docker compose down

refresh:
	git pull