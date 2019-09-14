# Contributing

## Example: setup, activate dev environment and install dev dependencies

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_dev.txt
```

## Run tests and examine code coverage

```
pytest --cov=itu_r_468_weighting
```

## Git workflow

Always develop on `ftr` branches or `fix` branches and do a pull request on
the `dev` branch.

## Code formatting

Afer code changes always run isort and black (in this order).
You can also use following script:

```
bash format_code.sh
```
