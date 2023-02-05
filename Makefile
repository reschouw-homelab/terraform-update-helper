PYTHON := $(shell which python3)
ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip

setup: $(ENV) 
	$(PIP) install --upgrade -r requirements.txt

$(ENV):
	$(PYTHON) -m venv env
	$(PIP) install --upgrade pip setuptools

clean: 
	rm -rf $(ENV)
