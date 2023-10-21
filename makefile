# Constants

export USER_ID=$(shell id -u)

export GROUP_ID=$(shell id -g)

PY = python manage.py

DC = docker-compose -f local.yml

BACK_PATH = ./backend

FRONT_PATH = ./frontend

RESOURCES_PATH = dev_resources

INDENT = --indent 2

NATURAL_PK = --natural-primary --natural-foreign

FIXTRS_PATH = $(RESOURCES_PATH)/fixtures

AUTH_FIXTR = $(FIXTRS_PATH)/auth.json

ACCTS_FIXTR = $(FIXTRS_PATH)/accounts.json

SRVRS_FIXTR = $(FIXTRS_PATH)/servers.json

SRVR_CAT_FIXTR = $(FIXTRS_PATH)/categories.json

SRVR_CH_FIXTR = $(FIXTRS_PATH)/channels.json

SRVR_MEMBERS = $(FIXTRS_PATH)/members.json

DUMP_AUTH = dumpdata auth $(NATURAL_PK) $(INDENT) > $(BACK_PATH)/$(AUTH_FIXTR)

DUMP_ACCT = dumpdata account.account $(NATURAL_PK) $(INDENT) > $(BACK_PATH)/$(ACCTS_FIXTR)

DUMP_SRVRS = dumpdata server.server $(NATURAL_PK) $(INDENT) > $(BACK_PATH)/$(SRVRS_FIXTR)

DUMP_CATS = dumpdata server.category $(NATURAL_PK) $(INDENT) > $(BACK_PATH)/$(SRVR_CAT_FIXTR)

DUMP_CHS = dumpdata server.channel $(NATURAL_PK) $(INDENT) > $(BACK_PATH)/$(SRVR_CH_FIXTR)

DUMP_MEMBERS = dumpdata server.server_members $(NATURAL_PK) $(INDENT) > $(BACK_PATH)/$(SRVR_MEMBERS)

LOAD_ACCTS = loaddata $(AUTH_FIXTR) $(ACCTS_FIXTR)

LOAD_SRVRS = loaddata $(SRVR_CAT_FIXTR) $(SRVR_CH_FIXTR) $(SRVRS_FIXTR)


# Compose commands

up:
	$(DC) up backend djmeet_db frontend

down:
	$(DC) down

run:
	$(DC) run --rm $(cmd)

build:
	@echo "Copying environments files"
	cp contrib/backend-env-sample ./backend/.env
	cp contrib/frontend-env-sample ./frontend/.env
	
	$(DC) build --no-cache frontend backend djmeet_db
	@make up frontend backend djmeet_db

clear-data-volumes:
	@echo "cleaning project data volumes"
	-docker volume rm -f djmeet_backend_data djmeet_frontend_data djmeet_db_data vscode

rebuild:
	@echo "Removing project containers"
	-docker rm -f backend frontend djmeet_db
	
	@-docker ps -a | grep 'vsc-djmeet' | awk '{print $1}' | xargs -r docker rm -f \
	&& docker images | grep 'vsc-djmeet' | awk '{print $3}' | xargs -r docker rmi
	
	@echo "Removing project images"
	-docker rmi -f backend frontend postgres:15.4-alpine
	@make clear-data-volumes
	@make build

migrations:
	@echo "Running migrations..."
	@make run cmd="backend $(PY) makemigrations"
	@make run cmd="backend $(PY) migrate"

compile:
	@rm -f $(BE_PATH)/$(RES_PATH)/dev-requirements.txt
	@rm -f $(BE_PATH)/requirements.txt
	@make run cmd="backend pip-compile -o requirements.txt pyproject.toml"
	@make run cmd="backend pip-compile --extra=dev -o $(RES_PATH)/dev-requirements.txt pyproject.toml"
	
sync:
	@make run cmd="backend pip-sync dev-requirements.txt"

sh-backend:
	$(DC) exec backend bash

sh-frontend:
	$(DC) exec frontend bash

shell:
	$(DC) exec backend $(PY) shell_plus

flush:
	@echo "Reseting DATABASE..."
	@make run cmd="backend $(PY) reset_db --noinput --close-sessions"
	@make migrations

formatter:
	@echo "Formatting code accord Pep8 Style..."
	@echo "Sorting Imports..."
	@make run cmd="backend isort --force-alphabetical-sort-within-sections ."
	@echo "Formatting code..."
	@make run cmd="backend black ."
	@echo "Running flake8..."
	@make run cmd="backend flake8"
	@echo "Completed with 0 erros!"

dump-auth:
	@make run cmd="backend $(PY) $(DUMP_AUTH)"

dump-accts:
	@make run cmd="backend $(PY) $(DUMP_ACCT)"

dump-srvrs:
	@make run cmd="backend $(PY) $(DUMP_SRVRS)"

dump-srvr-cat:
	@make run cmd="backend $(PY) $(DUMP_CATS)"

dump-srvr-ch:
	@make run cmd="backend $(PY) $(DUMP_CHS)"

dump:
	@make dump-auth
	@make dump-accts
	@make dump-srvr-cat
	@make dump-srvr-ch
	@make dump-srvrs
	@echo "Done."

load-accts:
	@make run cmd="backend $(PY) $(LOAD_ACCTS)"

load-srvrs:
	@make run cmd="backend $(PY) $(LOAD_SRVRS)"

load:
	@make flush
	@make load-accts
	@make load-srvrs
	@echo "Done."
