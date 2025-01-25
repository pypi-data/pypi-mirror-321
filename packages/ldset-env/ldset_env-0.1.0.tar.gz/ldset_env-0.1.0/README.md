# ldset_env

A command-line tool to set Launch Darkly environment variables.

## Installation

```console
pip install ldset_env
```

## Usage

```console
ldset_env
```

## Development

### Dependencies:

- python 3.11.2
- pyenv (recommended, but I'm sure there's alternatives)
- pipenv


### Create and enter pipenv shell

```console
pipenv install
pipenv shell
```

### Install package

```console
pip install -e .
```

### Update and run

```console
git pull && pip uninstall ldset_env && pip install -e . && ldset_env
```
