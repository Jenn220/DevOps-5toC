build:
	docker build -t mateous:latest .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml mateous

rm:
	docker stack rm mateous

ps:
	docker service ls

restart:
	make rm
	sleep 5
	make build
	make deploy