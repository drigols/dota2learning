# Dota2Learning

> Statistics and Machine Learning for your Dota2 Games.

## Project Overview

 - [Testing](#testing)

---

<div id="testing"></div>

## Testing

To testing the project you need install dev dependences (poetry approach):

```console
poetry install
```

Now just run **pytest -v** in the console to see pytest outputs:

```python
pytest -v
```

You also can see coverage approaches:

```python
pytest --cov=dota2learning tests/
or
py.test --cov-report html --cov dota2learning/ --verbose
```

**NOTE:**  
To see the second approach just find for **htmlcov** directory and open **index.html** on the browser.

---

**Rodrigo Leite -** *drigols*
