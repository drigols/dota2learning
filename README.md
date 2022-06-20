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

 - **dota2learning-db:**
   - Used to store all application data.
 - **test-dota2learning-db:**
   - Used for testing.

**NOTE:**  
You can change MySQL ports on [docker-compose.yml](docker-compose.yml).

To start docker container just enter on terminal:

```
sudo docker compose up -d
```

**NOTE:**  
The **flag -d** is used to start the container in background mode (daemon).

To see docker images you can use:

```
sudo docker images
```

And to see docker containers use:

```
sudo docker container ps -a
```

**NOTE:**  
The **flag -a (all)** is used to list all docker containers, running or not.

**[/data](data)**  
The folder [./data](data) is used to shared MySQL data between host machine and container. By default the data coming from the container will be without permissions because it is coming from **/var/lib/mysql**, so I recommend using the following command in the folder to release permissions:

```
sudo chmod 777 data/ -R
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
