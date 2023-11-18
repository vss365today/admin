# #vss365 today Admin

> Administration control panel for #vss365 today

**Note**: This project is now archived. It is also in an incomplete state and probably unusable.

## Required Configuration

- Flask secret key (`SECRET_KEY_ADMIN`)
- Running instance of [#vss365 today API v2](https://github.com/le717/vss365today-api/)
  - Operating domain (`API_DOMAIN`)
  - API key with `has_keys` and `has_hosts` permissions (`API_AUTH_TOKEN_ADMIN`)
- Static files hosting URL (prod only) (`STATIC_FILES_URL`)

## Install

1. Install Python 3.11+ and [Poetry](https://python-poetry.org/) 1.1.0+
1. Set missing configuration keys in appropriate `configuration/*.json` files
1. Create secret files in appropriate place (default: `/app/secrets`)
1. `poetry install`
1. `poetry run flask run`

## Build

1. `docker build -f "Dockerfile" -t vss365today-admin:latest .`

## License

2021-2023 Caleb

[MIT](LICENSE)
