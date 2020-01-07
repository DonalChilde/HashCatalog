# example_project
Skeleton of a python project


in the parent folder, clone the example_project from github

```bash
git clone git@github.com:DonalChilde/example_project.git
```

make a virtual environment in the project folder

```bash
cd ~/{path to provect folder}
python3 -m venv ./.venv
pip install -U pip
pip install wheel
pip install -r ./requirements-dev.txt

```

Update config files to represent new project.

>Note: version is stored in the `__init__.py` of the package folder

.pylintrc

- consider adding `bad-continuation` to list of disabled messages

.coveragerc

- source = ./src/{project package folder}

setup.cfg

- name
- version
- description
- keywords
- license
- classifiers

tox.ini

- pytest --cov={project package} tests/ --cov-append --cov-report=html --cov-report=term --cov-config=tox.ini

sphinx

- delete the contents of the doc folder
- in the doc folder, run sphinx-quickstart
- use separate source and build directories
- add `#  type: ignore` to top of doc/source/conf.py
- TODO update with further config instructions, autodoc, napoleon, etc.