# Python environment for small examples

## Initialization

### 1. Install pyenv
Install pyenv (MacOS):
```
brew install pyenv
```

Configure path (Add following to the rc file):
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

### 2. Install python
Check available versions:
```
pyenv install --list
```

Install python:
```
pyenv install 3.10.10
```

### 3. Install poetry
Install poetry:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Configure path (Add following to the rc file):
```
export PATH="$HOME/.local/bin:$PATH"
```

Configure poetry:
```
poetry config virtualenvs.in-project true
```

## Building Environment
Initialize virtual environment:
```
poetry install
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