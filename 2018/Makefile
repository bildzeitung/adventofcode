PYTHON := python
PYTHON_VERSION_FULL := $(wordlist 2,4,$(subst ., ,$(shell $(PYTHON) --version 2>&1)))
PYTHON_VERSION_MAJOR := $(word 1,${PYTHON_VERSION_FULL})
PYTHON_VERSION_MINOR := $(word 2,${PYTHON_VERSION_FULL})

venv: venv/bin/activate

venv/bin/activate: requirements.txt
ifeq ($(shell test $(PYTHON_VERSION_MAJOR) -gt 2; echo $$?),1)
	$(error "Python must be at least version 3.7 or higher; saw $(PYTHON_VERSION_MAJOR)")
endif
ifeq ($(shell test $(PYTHON_VERSION_MINOR) -gt 6; echo $$?),1)
	$(error "Python must be version 3.6 or higher; saw $(PYTHON_VERSION_MAJOR).$(PYTHON_VERSION_MINOR)")
endif
	test -d venv || $(PYTHON) -mvenv ./venv
	. ./venv/bin/activate && pip install --upgrade pip
	. ./venv/bin/activate && pip install -Ur requirements.txt
	touch ./venv/bin/activate

clean:
	rm -fr venv
	find . -name "*.pyc" -delete
	find . -name '__pycache__' | xargs rm -fr
	find . -name '*.egg-info' | xargs rm -fr

.PHONY: clean

# vim: ft=make
