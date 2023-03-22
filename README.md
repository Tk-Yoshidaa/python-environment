# Python environment for small examples

## Initialization

Install python:
```
...
```

Install poetry
```
...
```

Configure poetry:
```
...
```

Initialize virtual environment:
```
poetry init
```

If you need to add new package:
```
poetry add PACKAGE_NAME
```

If you need to specify the version of the package:
```
poetry add "PACKAGE_NAME=1.0.0"
```

If you need to remove package already installed:
```
poetry remove PACKAGE_NAME
```

Recommend to create `.venv` in a project by the following command
```
poetry config virtualenvs.in-project true
```