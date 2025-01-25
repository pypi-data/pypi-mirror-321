VERSION = 0.3.0
DIST_PATH = ./dist
VENV_PATH = ./venv
VENV = . $(VENV_PATH)/bin/activate;
NAME = $(shell uname -a)

.PHONY: publish
publish: clean build
	$(VENV) python3 -m twine upload --repository pypi dist/*
	git add Makefile
	git commit -m "chore: release v$(VERSION)"
	git tag "v$(VERSION)"
	git push
	git push --tags

.PHONY: clean
clean:
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .ruff_cache

.PHONY: build
build:
	echo "$(VERSION)" > .version
	$(VENV) python3 -m build

.PHONY: install
install: $(DIST_PATH)
	pip3 install .

.PHONY: install-venv
install-venv:
	$(VENV) pip install .

.PHONY: lint
lint:
	$(VENV) ruff check src/
	$(VENV) pylint src/

configure: requirements.txt
	rm -rf $(VENV_PATH)
	make $(VENV_PATH)

.PHONY: test
test:
	$(VENV) pytest -o log_cli=true -vv tests/*.py

$(VENV_PATH):
	python3 -m venv $(VENV_PATH)
	$(VENV) pip install -r requirements.txt

$(CONFIG_PATH): config.json
	mkdir -p $(CONFIG_DIR)
	rm -f $(CONFIG_PATH)
	cp config.json $(CONFIG_PATH)
