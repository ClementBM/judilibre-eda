# Development setup
## Prerequisites
This following packages must be installed
* python
* poetry
* git

## Configuration
* `poetry` configuration, add environment variable `POETRY_VIRTUALENVS_IN_PROJECT=true`
* `vscode` configuration, add environment variable `PYTHON_VENV_LOC`
  * on windows: `PYTHON_VENV_LOC=.venv\\bin\\python.exe`
  * on linux: `PYTHON_VENV_LOC=.venv/bin/python`
* `git` configuration
```shell
git config --global user.name 'your name'
git config --global user.email 'your email'
```

## Initialization
* First setup `poetry install`
* Then `poetry shell`

## Installation with pip
```shell
pip install --index-url https://test.pypi.org/simple/ judilibre-eda
```
or
```shell
pip3 install --index-url https://test.pypi.org/simple/ judilibre-eda
```

# JUDILIBRE API

La Cour de cassation, dans le cadre de la refonte de son site Web, a initié le projet JUDILIBRE visant à la conception et au développement en interne d'un moteur de recherche dans le corpus jurisprudentiel, mettant celui-ci à disposition du public dans l'esprit du décret sur l'Open Data des décisions de justice.

OpenAPI spec version: 1.0.3

## Requirements

Python 2.7 and 3.4+

## Getting Started

```python
from __future__ import print_function
import time
import judilibre_client
from judilibre_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = judilibre_client.DefaultApi(judilibre_client.ApiClient(configuration))
id = NULL # object | Identifiant de la décision à récupérer.
resolve_references = NULL # object | Lorsque ce paramètre vaut `true`, le résultat de la requête contiendra, pour chaque information retournée par défaut sous forme de clé, l'intitulé complet de celle-ci (vaut `false` par défaut). (optional)
query = NULL # object | Chaîne de caractères correspondant à la recherche. Ce paramètre est utilisé pour surligner en retour, dans le texte intégral de la décision, les termes correspondant avec la recherche initiale (ces termes étant délimitées par des balises `<em>`). (optional)
operator = NULL # object | Opérateur logique reliant les multiples termes que le paramètre `query` peut contenir (`or` par défaut, `and` ou `exact` – dans ce dernier cas le moteur recherchera exactement le contenu du paramètre `query`). (optional)

try:
    # Permet de récupérer le contenu intégral d'une décision.
    api_instance.decision(id, resolve_references=resolve_references, query=query, operator=operator)
except ApiException as e:
    print("Exception when calling DefaultApi->decision: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**decision**](docs/DefaultApi.md#decision) | **GET** /decision | Permet de récupérer le contenu intégral d&#39;une décision.
*DefaultApi* | [**export**](docs/DefaultApi.md#export) | **GET** /export | Permet d&#39;effectuer un export par lot de décisions de justice.
*DefaultApi* | [**healthcheck**](docs/DefaultApi.md#healthcheck) | **GET** /healthcheck | Permet de récupérer l&#39;état de disponibilité du service.
*DefaultApi* | [**search**](docs/DefaultApi.md#search) | **GET** /search | Permet d&#39;effectuer une recherche dans les données ouvertes des décisions de justice.
*DefaultApi* | [**stats**](docs/DefaultApi.md#stats) | **GET** /stats | Permet de récupérer des statistiques sur le contenu de la base JUDILIBRE.
*DefaultApi* | [**taxonomy**](docs/DefaultApi.md#taxonomy) | **GET** /taxonomy | Permet de récupérer les listes des termes employés par le processus de recherche.


## Documentation For Authorization

Add `.env` file in the root directory:

```shell
JUDILIBRE_API_KEY=XXX
```

## Author
sebastien.courvoisier@justice.fr
