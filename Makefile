build:
	docker build -f ./docker/Dockerfile -t be_assessment .

up:
	docker-compose -f ./docker/docker-compose.yml -p be_assessment up

down:
	docker-compose -f .docker/docker-compose.yml -p be_assessment down
