# Dota2Learning

> Statistics and Machine Learning for your Dota2 Games.

## Project Overview

 - [Settings](#settings)
 - [Testing](#testing)
 - [Tech Stack](#tech-stack)

---

<div id="settings"></div>

## Settings

To use the **Dota2Learning** project  you'll need *Docker* and *Docker Compose* in your machine to use the MySQL databases.

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
The folder [./data](data) is used to shared MySQL data between host machine and container.

**NOTE:**  
MySQL services can delay some minutes to work, that's why was created a "healthcheck" in Docker Compose that waits for the service to be available and then dumps the data:

```python
healthcheck:
  test: mysql --user=root --password=toor dota2learning-db < /home/db-production/dumb-db-production.sql
  interval: 30s
  timeout: 10s
  retries: 6
```



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
   - **Consuming API:**
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
