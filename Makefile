up:
	docker-compose up -d

down:
	docker-compose down
	docker system prune -a -f
	docker-compose rm -f

restart: down up
