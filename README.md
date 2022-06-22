# Dota2Learning

.. image:: https://img.shields.io/pypi/v/pytest.svg
    :target: https://pypi.org/project/pytest/

.. image:: https://img.shields.io/conda/vn/conda-forge/pytest.svg
    :target: https://anaconda.org/conda-forge/pytest

.. image:: https://img.shields.io/pypi/pyversions/pytest.svg
    :target: https://pypi.org/project/pytest/

.. image:: https://codecov.io/gh/pytest-dev/pytest/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/pytest-dev/pytest
    :alt: Code coverage Status

.. image:: https://github.com/pytest-dev/pytest/workflows/test/badge.svg
    :target: https://github.com/pytest-dev/pytest/actions?query=workflow%3Atest

.. image:: https://results.pre-commit.ci/badge/github/pytest-dev/pytest/main.svg
   :target: https://results.pre-commit.ci/latest/github/pytest-dev/pytest/main
   :alt: pre-commit.ci status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://www.codetriage.com/pytest-dev/pytest/badges/users.svg
    :target: https://www.codetriage.com/pytest-dev/pytest

.. image:: https://readthedocs.org/projects/pytest/badge/?version=latest
    :target: https://pytest.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/badge/Discord-pytest--dev-blue
    :target: https://discord.com/invite/pytest-dev
    :alt: Discord

.. image:: https://img.shields.io/badge/Libera%20chat-%23pytest-orange
    :target: https://web.libera.chat/#pytest
    :alt: Libera chat

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](LICENSE.md)

> Statistics and Machine Learning for your Dota2 Games.

## Project Overview

 - [Project Settings](#settings)
 - [CLI](#cli)
 - [Testing](#testing)
 - [Tech Stack](#tech-stack)

---

<div id="settings"></div>

## Project Settings

To use **Dota2Learning** project first install Python (^3.10) dependencies:

**pip approach:**
```
pip install --require-hashes --upgrade -r requirements.txt
```

or

```
pip install --require-hashes -r requirements.txt
```

**poetry approach:**
```
poetry install
```

You can specify to the command that you do not want the development dependencies installed by passing the **--no-dev** option:

```
poetry install --no-dev
```

**NOTE:**  
However, dev dependencies are needed for tests.

You also will need *Docker* and *Docker Compose* in your machine to use the MySQL databases.

We've two containers with one MySQL each:

 - **mysql-production:**
   - **Database:** dota2learning-db
     - Used to store all application data.
 - **db-testing:**
   - **Database:** Create manually for tests.

To start docker container just enter on console:

```
sudo docker compose up -d
```

**[/data](data)**  
The folder [./data](data) is used to shared MySQL data (database) between host machine and container.

**NOTE:**  
MySQL services can delay some minutes to work, that's why was created a "healthcheck" in Docker Compose that waits for the service to be available and then dumps the data:

```python
healthcheck:
  test: mysql --user=root --password=toor dota2learning-db < /home/db-production/dumb-db-production.sql
  interval: 30s
  timeout: 10s
  retries: 6
```

Ok, now you has Python dependencies and Docker container with MySQL Database let's go be happy!

---

<div id="cli"></div>

## CLI

The project has a CLI to get data from the Database. To see CLI commands just enter in the console:

```
dota2learning --help
```

**OUTPUT:**  
```
Usage: dota2learning [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  hero  Commands for getting Heroes attributes and insights.
```

**NOTE:**  
Currently the CLI is being, but has a hero command to get a hero's stats.

---

<div id="testing"></div>

## Testing

To testing the project you need install dev dependences (poetry approach):

```
poetry install
```

Now just run **pytest -v** in the console to see pytest outputs:

```
pytest -v
```

You also can see coverage approaches:

```
pytest --cov=dota2learning tests/
```

or

```python
pytest --cov-report html --cov dota2learning/ --verbose
```

**NOTE:**  
To see the second approach just find for **htmlcov** directory and open **index.html** on the browser.

---

<div id="tech-stack"></div>

### Tech Stack

 - **Frondend (View):**
   - **CLI:**
     - Python:
       - typer
   - **Jupyter Notebook:**
 - **Backend:**
   - **Consuming API [(OpenDota)](https://docs.opendota.com/):**
     - Python:
       - requrest
       - json
   - **Database (Docker + MySQL):**
     - **Python:**
       - mysql-connector-python
 - **Testing:**
   - **Python:**
     - pytest
     - pytest-cov

---

**Rodrigo Leite -** *drigols*
