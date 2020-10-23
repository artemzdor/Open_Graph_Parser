CURRENT_DIRECTORY := $(shell pwd)

SERVICE = server
TEST_SERVICE = server_test
TEST_SERVER_SERVICE = test_server

ifneq ("$(wildcard ./docker-compose.override.yml)","")
    DC_FILE := docker-compose.override.yml
else
    DC_FILE := docker-compose.yml
endif

DC_CMD = docker-compose -f ${DC_FILE}


.PHONY: up stop restart cli build pip-compile


help:
	@echo ""
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  build              to make all docker assembly images"
	@echo "  up                 run server"
	@echo "  stop               stop server"
	@echo "  cli                to run a console"
	@echo "  pylint             run pylint"
	@echo ""
	@echo "See contents of Makefile for more targets."

stop:
	$(DC_CMD) down

up: stop
	$(DC_CMD) up

cli:
	$(DC_CMD) run --rm $(SERVICE) sh

build:
	$(DC_CMD) build

pip-compile:
	$(DC_CMD) run --rm --no-deps $(SERVICE) pip-compile

pylint:
	pylint ./src

#test_server:
#	$(DC_CMD) run --rm $(TEST_SERVER_SERVICE) python -m pytest
