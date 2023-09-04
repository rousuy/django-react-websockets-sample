
user_id:=$(shell id -u)

group_id:=$(shell id -g)

py = python manage.py

dc = docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml

up:
	$(dc) up djmeet_api djmeet_db

down:
	$(dc) down

exec:
	$(dc) run --rm djmeet_api $(cmd)

build:
	@echo "Copying environments files"
	cp contrib/env-sample .env

	docker build . -t djmeet_api --build-arg USER_ID=$(user_id) --build-arg GROUP_ID=$(group_id) --no-cache

	@echo "Build project"
	@make up

rebuild:
	@echo "Removing project containers"
	-docker rm -vf djmeet_api djmeet_db djmeet_vscode -f

	@echo "Removing project image"
	-docker rmi -f djmeet_api vscode -f

	@echo "Building containers"
	@make build

migrations:
	@echo "Running migrations"
	@make exec cmd="$(py) makemigrations"
	@make exec cmd="$(py) migrate"

compile:
	@rm -f dev-requirements.txt
	@rm -f requirements.txt

	@make exec cmd="pip-compile -o requirements.txt pyproject.toml"
	@make exec cmd="pip-compile --extra=dev --output-file=dev-requirements.txt pyproject.toml"
	
sync:
	@make exec cmd="pip-sync dev-requirements.txt"

sh:
	@make exec cmd="bash"

shell:
	@make exec cmd="$(py) shell_plus"

flush:
	@echo "Reseting DATABASE..."
	@make exec cmd="$(py) reset_db --noinput --close-sessions"
	@make setup

formatter:
	@echo "Formatting code accord Pep8 Style..."

	@echo "Sorting Imports..."
	@make exec cmd="isort --force-alphabetical-sort-within-sections ."

	@echo "Formatting code..."
	@make exec cmd="black ."

	@echo "Running flake8"
	@make exec cmd="flake8"

	@echo "Completed with 0 erros"