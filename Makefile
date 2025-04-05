
start:
	docker compose up -d
	docker compose build
	docker cp ./daemons Router1:etc/frr/
	docker cp ./daemons Router2:etc/frr/
	docker cp ./daemons Router3:etc/frr/
	docker cp ./daemons Router4:etc/frr/
	docker exec -it Router1 service frr restart
	docker exec -it Router2 service frr restart
	docker exec -it Router3 service frr restart
	docker exec -it Router4 service frr restart

stop:
	docker compose down

refresh:
	git pull