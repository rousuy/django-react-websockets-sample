# Constants
export USER_ID=$(shell id -u)
export GROUP_ID=$(shell id -g)

PY = python manage.py

DC = docker-compose -f local.yml

BE_PATH = ./backend

FE_PATH = ./frontend

RES_PATH = dev_resources

INDENT = --indent 2

NATURAL_PK = --natural-primary --natural-foreign

FIXTR_PATH = $(RES_PATH)/fixtures

ACCT_FIXTR = $(FIXTR_PATH)/account

SRVR_FIXTR = $(FIXTR_PATH)/server

AUTH_FIXTR = $(ACCT_FIXTR)/auth.json

ACCTS_FIXTR = $(ACCT_FIXTR)/accounts.json

SRVRS_FIXTR = $(SRVR_FIXTR)/servers.json

SRVR_CAT_FIXTR = $(SRVR_FIXTR)/categories.json

SRVR_CH_FIXTR = $(SRVR_FIXTR)/channels.json

SRVR_MEMBERS = $(SRVR_FIXTR)/members.json

DUMP_AUTH = dumpdata auth $(NATURAL_PK) $(INDENT) > $(BE_PATH)/$(AUTH_FIXTR)

DUMP_ACCT = dumpdata account.account $(NATURAL_PK) $(INDENT) > $(BE_PATH)/$(ACCTS_FIXTR)

DUMP_SRVRS = dumpdata server.server $(NATURAL_PK) $(INDENT) > $(BE_PATH)/$(SRVRS_FIXTR)

DUMP_CATS = dumpdata server.category $(NATURAL_PK) $(INDENT) > $(BE_PATH)/$(SRVR_CAT_FIXTR)

DUMP_CHS = dumpdata server.channel $(NATURAL_PK) $(INDENT) > $(BE_PATH)/$(SRVR_CH_FIXTR)

DUMP_MEMBERS = dumpdata server.server_members $(NATURAL_PK) $(INDENT) > $(BE_PATH)/$(SRVR_MEMBERS)

LOAD_ACCTS = loaddata $(AUTH_FIXTR) $(ACCTS_FIXTR)

LOAD_SRVRS = loaddata $(SRVR_CAT_FIXTR) $(SRVR_CH_FIXTR) $(SRVRS_FIXTR)


# Compose commands

up:
	$(DC) up backend db frontend

down:
	$(DC) down

exec:
	$(DC) exec $(cmd)

build:
	@echo "Copying environments files..."
	cp contrib/backend-env-sample $(BE_PATH)/.env
	cp contrib/frontend-env-sample $(FE_PATH)/.env
	$(DC) build --no-cache 

	@echo "Start project..."
	@make up

rebuild:
	@echo "Removing project containers..."
	-docker rm -vf backend db frontend -f
	@echo "Removing project images..."
	-docker rmi -f backend frontend -f
	@echo "Building containers..."
	@make build

migrations:
	@echo "Running migrations..."
	@make exec cmd="backend $(PY) makemigrations"
	@make exec cmd="backend $(PY) migrate"

compile:
	@rm -f $(BE_PATH)/$(RES_PATH)/dev-requirements.txt
	@rm -f $(BE_PATH)/requirements.txt
	@make exec cmd="backend pip-compile -o requirements.txt pyproject.toml"
	@make exec cmd="backend pip-compile --extra=dev -o $(RES_PATH)/dev-requirements.txt pyproject.toml"
	
sync:
	@make exec cmd="backend pip-sync dev-requirements.txt"

sh-backend:
	@make exec cmd="backend bash"

sh-frontend:
	@make exec cmd="frontend bash"

shell:
	@make exec cmd="backend $(PY) shell_plus"

flush:
	@echo "Reseting DATABASE..."
	@make exec cmd="backend $(PY) reset_db --noinput --close-sessions"
	@make setup

formatter:
	@echo "Formatting code accord Pep8 Style..."
	@echo "Sorting Imports..."
	@make exec cmd="backend isort --force-alphabetical-sort-within-sections ."
	@echo "Formatting code..."
	@make exec cmd="backend black ."
	@echo "Running flake8..."
	@make exec cmd="backend flake8"
	@echo "Completed with 0 erros!"

dump-auth:
	@make exec cmd="backend $(PY) $(DUMP_AUTH)"

dump-accts:
	@make exec cmd="backend $(PY) $(DUMP_ACCT)"

dump-srvrs:
	@make exec cmd="backend $(PY) $(DUMP_SRVRS)"

dump-srvr-cat:
	@make exec cmd="backend $(PY) $(DUMP_CATS)"

dump-srvr-ch:
	@make exec cmd="backend $(PY) $(DUMP_CHS)"

dump:
	@make dump-auth
	@make dump-accts
	@make dump-srvr-cat
	@make dump-srvr-ch
	@make dump-srvrs
	@echo "Done."

load-accts:
	@make exec cmd="backend $(PY) $(LOAD_ACCTS)"

load-srvrs:
	@make exec cmd="backend $(PY) $(LOAD_SRVRS)"

load:
	@make load-accts
	@make load-srvrs
	@echo "Done."
