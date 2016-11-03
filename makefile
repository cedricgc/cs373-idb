# Space separated list of git hook paths
GIT_HOOKS := scripts/git/pre-commit
# Set options like proxies here
PIPOPTS :=
# Port number to bind gunicorn to; can be overidden in environment
PORT ?= 5000

ifeq ($(TRAVIS_CI_BUILD), 1)
	PYTEST = pytest
else
	PYTEST = venv/bin/pytest
endif

FILES :=                              \
    .gitignore                        \
    .travis.yml                       \
    apiary.apib                       \
    IDB1.log                          \
    models.html                       \
    app/models.py                     \
    app/tests.py                      \
    UML.pdf                           \

init: hooks venv

venv:
	python3.5 -m venv --copies venv
	venv/bin/pip install --upgrade pip

install: venv
	venv/bin/pip install -r requirements.txt $(PIPOPTS)

# Set up testing commands here; will be used in git hook
test:
	PYTHONPATH="." $(PYTEST) \
		--cov=website \
		--no-cov-on-fail \
		tests/unit/*

# run in production mode, meant to run behind nginx proxy so bind to
# localhost instead of 0.0.0.0
run: venv/bin/gunicorn
	venv/bin/gunicorn \
		-w 5 \
		-b localhost:$(PORT) \
		--log-level=debug \
		website:app

dev_server: venv/bin/python
	venv/bin/gunicorn \
		-w 5 \
		-b 0.0.0.0:$(PORT) \
		--log-level=debug \
		--reload \
		website:app

# Ensure environment vars are set
db_migrations: venv/bin/alembic
	venv/bin/alembic upgrade head

# Ensure environment vars are set
db_reset: venv/bin/alembic
	venv/bin/alembic downgrade base
	venv/bin/alembic upgrade head

adddeps: venv pkgs
	venv/bin/pip install -r requirements-to-freeze.txt $(PIPOPTS)
	venv/bin/pip freeze > requirements.txt

# For any system packages need to be installed for project ex: C header files
pkgs:
	# Python C FFI header files
	sudo apt-get install python3.5-dev --yes
	# libpq for psycopg2 postgres driver
	sudo apt-get install libpq-dev --yes

hooks:
	# Set up any git hooks for development
	cp $(GIT_HOOKS) .git/hooks
	chmod 0755 $(GIT_HOOKS)

check:
	@not_found=0;                                   \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f .coverage
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

IDB1.log:
	git log > IDB1.log

models.html:
	venv/bin/python -m pydoc -w website/api/models.py
