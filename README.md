# #vss365 today Admin
> Administration control panel for #vss365 today


## Required Configuration

TK

## Install

1. Install Python 3.9+ and [Poetry](https://python-poetry.org/) 1.1.0+
1. Set missing configuration keys in appropriate `configuration/*.json` files
1. Create secret files in appropriate place (default: `/app/secrets`)
1. `poetry install`
1. `poetry run flask run`

## Build

1. `docker build -f "Dockerfile" -t vss365today-admin:latest .`

## License

2021 Caleb Ely

[MIT](LICENSE)
