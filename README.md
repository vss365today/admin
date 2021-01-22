# #vss365 today Admin

> Administration control panel for #vss365 today

## Required Configuration

- Running instance of [#vss365 today API](https://github.com/le717/vss365today-api/) (domain configurable)
  - API key with api_key endpoint permission
- Flask secret key

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
