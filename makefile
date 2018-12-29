PACKAGE_NAME = drop_token
WORKON_HOME ?= $(PWD)/../virtualenvs
VIRTUAL_ENV ?= $(WORKON_HOME)/$(PACKAGE_NAME)
PATH := $(VIRTUAL_ENV)/bin:$(PATH)
MAKE := $(MAKE) --no-print-directory
SHELL = bash

default:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo
	@echo 'Usage:'
	@echo
	@echo '    make install    install the package in a virtual environment'
	@echo '    make reset      recreate the virtual environment'
	@echo '    make check      check coding style (PEP-8, PEP-257)'
	@echo '    make test       run the test suite, report coverage'
	@echo '    make formatter  use google yapf to format the code'
	@echo '    make tox        run the tests on all Python versions'
	@echo '    make readme     update usage in readme'
	@echo '    make docs       update documentation using Sphinx'
	@echo '    make publish    publish changes to GitHub/PyPI'
	@echo '    make clean      cleanup all temporary files'
	@echo

install:
	@echo "The virtual env is $(VIRTUAL_ENV)"
	@test -d "$(VIRTUAL_ENV)" || mkdir -p "$(VIRTUAL_ENV)"
	@test -x "$(VIRTUAL_ENV)/bin/python" || virtualenv --quiet "$(VIRTUAL_ENV)"
	@test -x "$(VIRTUAL_ENV)/bin/pip" || easy_install pip
	@$(VIRTUAL_ENV)/bin/pip uninstall --yes $(PACKAGE_NAME) &>/dev/null || true
	@$(VIRTUAL_ENV)/bin/pip install --quiet --no-deps --ignore-installed .

reset:
	$(MAKE) clean
	rm -Rf "$(VIRTUAL_ENV)"
	$(MAKE) install

check: install
	{ \
		source $(VIRTUAL_ENV)/bin/activate ;\
		pip install --quiet --requirement=requirements-checks-and-formatter.txt ;\
		flake8 ;\
		deactivate ;\
	}

formatter: install
	{ \
		source $(VIRTUAL_ENV)/bin/activate ;\
		pip install --quiet --requirement=requirements-checks-and-formatter.txt ;\
		yapf -i -r $(PWD) ;\
		echo "Finish Formatting" ;\
		deactivate ;\
	}

test: install
	{ \
		source $(VIRTUAL_ENV)/bin/activate ;\
		$(VIRTUAL_ENV)/bin/pip install --quiet --requirement=requirements-tests.txt ;\
		py.test --version ;\
		py.test --cov ;\
		coverage combine || true ;\
		coverage html ;\
		deactivate ;\
	}


tox: install
	{ \
		source $(VIRTUAL_ENV)/bin/activate ;\
		pip install --quite tox ;\
		tox ;\
		deactivate ;\
	}


docs: 
	{ \
		source $(VIRTUAL_ENV)/bin/activate ;\
		pip install --quiet sphinx ;\
		cd docs ;\
		sphinx-build -nb html -d build/doctrees . build/html ;\
		cd - ;\
		deactivate ;\
	}

publish: install
	git push origin && git push --tags origin
	$(MAKE) clean
	pip install --quiet twine wheel
	python setup.py sdist bdist_wheel
	twine upload dist/*
	$(MAKE) clean

clean:
	@rm -Rf *.egg .cache .coverage .tox build dist docs/build htmlcov
	@find . -depth -type d -name __pycache__ -exec rm -Rf {} \;
	@find . -type f -name '*.pyc' -exec rm -Rf {} \;


release: install test check docs

.PHONY: default install reset check test tox readme docs publish clean
