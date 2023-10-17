up:
	docker-compose up -d

down:
	docker-compose down
	docker system prune -a -f
	docker rmi playground

restart: down up
