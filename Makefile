
start:
	docker compose up -d
	docker compose build
	docker cp ./daemons Router1:etc/frr/
	docker cp ./daemons Router2:etc/frr/
	docker cp ./daemons Router3:etc/frr/
	docker cp ./daemons Router4:etc/frr/

stop:
	docker compose down

refresh:
	git pull