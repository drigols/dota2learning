# Dota2Learning

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](LICENSE.md)
[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)

> Statistics and Machine Learning for your Dota2 Games.

## Contents

 - [Overview](#overview)
 - [Settings](#settings)
 - [CLI](#cli)
 - [Testing](#testing)
 - [New Features](#new-features)
 - [Tech Stack](#tech-stack)

---

<div id="overview"></div>

## Overview

> The main **Dota2Learning** project goals are to provide <u>Statistics</u> and <u>Machine Learning Algorithms</u> for your Dota2 Games.

Another crucials features from **Dota2Learning** project are:

 - Dota2 resources (Like, heroes resources).
 - Provide statistics for the currently Dota2 patch.
 - Machine learning algorithms predictions.

**NOTE:**<br>
You can follow the development feature process on the [Trello Board](https://trello.com/b/3hM5390C/dota2learning).

---

<div id="settings"></div>

## Settings

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

**NOTE:**<br>
However, dev dependencies are needed for tests.

You also will need *Docker* and *Docker Compose* in your machine to use the MySQL databases.

We've two containers with one MySQL each:

 - **db-production:**
   - **Database:** dota2learning-db
     - Used to store all application data.
 - **db-testing:**
   - **Database:** Create manually for tests.

To start docker container just enter on console:

```
sudo docker compose up -d
```

The folder [./data](data) is used to shared MySQL data (database) between host machine and container.

**NOTE:**<br>
MySQL services can delay some minutes to work. Knowing that, I strongly recommended waiting for MySQL service is ready:

**First, Let's entering on the container:**
```python
sudo docker exec -it db-production bash
```

**Try this until MySQL service is ready:**
```python
mysql --user=root --password=toor dota2learning-db
```

**ERROR OUTPUT:**
```python
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```

**OK OUTPUT:**
```python
Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

**Finally, dump data (You'll first need exit from MySQL):**
```python
mysql --user=root --password=toor dota2learning-db < /home/db-production/dumb-db-production.sql
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

**NOTE:**<br>
Currently the CLI is being, but has a **hero** command to get a hero's stats.

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

**NOTE:**<br>
To see the second approach just find for **htmlcov** directory and open **index.html** on the browser.

---

<div id="new-features"></div>

# New Features

If you wish to create new features install dev dependencies and run **"pre-commit install"** to check your code style:

```python
pre-commit install
```

If you want to manually run all pre-commit hooks on a repository, run **pre-commit run --all-files**. To run individual hooks use **pre-commit run <hook_id>**. You can see individual hooks in [.pre-commit-config.yaml](.pre-commit-config.yaml)

---

<div id="tech-stack"></div>

### Tech Stack

 - **Frondend (View):**
   - **CLI:**
     - Python:
       - typer
   - **Jupyter Notebook:**
 - **Backend:**
   - **Data Validators:**
     - Python:
       - Pydantic
   - **Consuming API [(OpenDota)](https://docs.opendota.com/):**
     - Python:
       - requrest
       - json
   - **Database (Docker + MySQL):**
     - Python:
       - SQLAlchemy
       - PyMySQL
 - **Testing:**
   - **Python:**
     - pytest
     - pytest-cov
 - **Code Style:**
   - **Black**
   - **Flake8**

---

**Rodrigo Leite -** *drigols*
