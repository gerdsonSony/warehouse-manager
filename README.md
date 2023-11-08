# Warehouse Manager

## About

This is a project used to present my Software Engineering and Python skills to Sierra Studio.

### Buit with

![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

## Getting Started


### Prerequisites

Install the following requirements:
  - [aws-cli](https://aws.amazon.com/cli/)
  - [aws-sam-cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
  - [docker](https://www.docker.com/)
  - [docker-compose](https://docs.docker.com/compose/)
  - [poetry](https://python-poetry.org/)
  - [pre-commit](https://pre-commit.com/)
  - [pyenv](https://github.com/pyenv/pyenv)

1. Install python *3.9.14* for pyenv, and set the python version for the local environment.
    ```
    pyenv install 3.11.6
    pyenv local 3.11.6
    ```
2. Create a new virtual environment of the python local version
    ```
    python -m venv .venv
    ```
3. Create a new virtual environment and install the python dependencies.
   ```
   poetry install
   ```

## API

### Running the serverless API locally

1. To calculate the distances using Google Maps API, create/enable a Google
developer profile [API key](https://cloud.google.com/docs/authentication/api-keys?sjid=2560348064154854540-NC)
2. Make a copy of the .example.env file and create your local .env file
   * The unique that is not filled by default is the GOOGLE_MAPS_API_KEY.
   Fill it with the key created in the first step. 
3. Run the database docker image
   ```
   docker compose up mysql-db -d
   ```
   Wait a few seconds for the database building.
4. Build a API local image
   ```
   sam build --cached
   ```
   **_NOTE:_** Use the --cached option to avoid build unchanged dependencies for every build command
5. Start the local API passing the Google Maps API key created before
   <pre>
   sam local start-api --parameter-overrides "GoogleMapsAPIkey=<i>{YOUR_API_KEY}</i>>"
   </pre>
6. After these steps you should be able to make API calls in the URL http://127.0.0.1:3000/{endpoint}

## Endpoints

### /authentication

#### [POST]

It will return a JWT token valid for 10 minutes in the API. This is a demonstration of the Bearer implementation

No users model was implemented, so every empty payload in  this endpoint will return valid (with expiration) token
in the API.

### /customers

#### [GET]

This endpoint returns all the customers from the database. Pagination is not implemented.

#### [POST]

This is the endpoint used to create a customer

Payload example:
```json
{
    "name": "Customer Name",
    "latitude": -27.69953233146274,
    "longitude": -48.51088762083777
}
```

### /customers/<customer_id>

#### [GET]

Retrieve a customer searching by its id

### /warehouses

#### [GET]

This endpoint returns all the warehouses from the database. Pagination is not implemented.

#### [POST]

This is the endpoint used to create a warehouse

Payload example:
```json
{
    "name": "Warehouse Name",
    "latitude": -27.69953233146274,
    "longitude": -48.51088762083777
}
```

### /warehouses/<warehouse_id>

#### [GET]

Retrieve a warehouse searching by its id

### /warehouses/<warehouse_id>/distance/<customer_id>

#### [GET]

This endpoint calculates the distance between a warehouse and a customer using the Google Maps API

## Testing

### Running Tests Locally

1. Run the command
   ```
   pytest
   ```

## Linting / Formatting

### Linters / Formatters

Linters and formatters used to maintain the code best practices patterns for all collaborations.

It can be used in the pipelines/actions to make sure that the PRs are well linted and formatted

Linters:
  - [flake8](https://flake8.pycqa.org/en/latest/):
    - [Pyflakes](https://pypi.org/project/pyflakes/) (error linter)
    - [pycodestyle](https://pypi.org/project/pycodestyle/) (style linter)
    - [mccabe](https://pypi.org/project/mccabe/) (complexity analysis)
  - [mypy](https://mypy-lang.org/) (type checker)

Formatters:
  - [autoflake](https://pypi.org/project/autoflake/) (dead code linter and formatter)
  - [black](https://github.com/psf/black) (style formatter)
  - [isort](https://pycqa.github.io/isort/) (style linter and formatter for imports)

### Running Linters / Formatters Locally

If you want to run all the linters and formatters locally on your code, you can use the `pre-commit` command.
```
pre-commit run -a
```

If you want to each of the linters / formatters individually, you can run them as separate commands as they are
installed as project development dependencies with `poetry`.

```
# Linters:
flake8 functions/ layers/src/ tests/
mypy

# Formatters:
autoflake .
black .
isort functions/ layers/src/ tests/
```
