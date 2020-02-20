# Django 3 Project Template

[![Travis CI](https://travis-ci.com/bennett-jacob/django-project-starter.svg?branch=master)](https://travis-ci.com/bennett-jacob/django-project-starter)
[![Maintainability](https://api.codeclimate.com/v1/badges/38708ad0170fe95e8178/maintainability)](https://codeclimate.com/github/bennett-jacob/django-project-starter/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/38708ad0170fe95e8178/test_coverage)](https://codeclimate.com/github/bennett-jacob/django-project-starter/test_coverage)

Welcome to your new Django project!

## Getting Started

### Running the project

```bash
docker-compose up -d
```

### Development setup

1. Create a new Code Climate Test Reporter ID
1. Remove the secure Code Climate Test Reporter ID in [`.travis.yml`](./.travis.yml)
1. Run :

    ```bash
    travis encrypt CC_TEST_REPORTER_ID=<new_test_id> --add env.global
    ```
