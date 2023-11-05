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
