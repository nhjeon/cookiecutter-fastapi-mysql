# {{ cookiecutter.project_name }}

&nbsp;[![Python Version: 3.9.1](https://badgen.net/badge/python/3.9.1/blue)](https://docs.python.org/3.7.4/)

&nbsp;[![Code Style: Black](https://badgen.net/badge/code%20style/black/black)](https://github.com/ambv/black)


## Getting Started


### Installation

```sh
$ make
```

## Test

```sh
$ make check
$ make test
```


## Run

``` sh
make run
```

## Docker

```
docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage
```

## Hot Reloading with Local Docker Development

```
docker build -t myimage -f Dockerfile-local .
docker run -d --name mycontainer -p 80:80 -v $(PWD)/app:/app myimage
```


## Requirements

<!-- TODO: Describe stack of this project -->

* [Poetry](https://python-poetry.org/)
* FastAPI
* uvicorn
* sqlalchemy
* mysqlclient