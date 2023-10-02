docker-build:
	docker build -t playground .

docker-run:
	docker run -d --name playground -p 8000:80 playground

docker-trash:
	docker stop playground
	docker rm playground

run: docker-build docker-run

restart: docker-trash run