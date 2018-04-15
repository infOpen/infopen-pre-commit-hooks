# Infopen pre-commit hooks

This repository add more pre-commit used by Infopen company.

## Hooks

### check-rst

This hook lint the RST files to validate the syntax.


## Run tests

You can use Docker compose (or Docker only if you prefer) to run test suite.

1. Build docker image
```
docker-compose build
```

2. Run test container
```
docker-compose up -d
```

3. Run test suite
```
docker-compose exec -u pyenv-test infopen_pre_commit_hooks tox
```
