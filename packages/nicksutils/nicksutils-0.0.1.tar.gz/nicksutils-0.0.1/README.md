# python-default

Default setup for my python programs

    pip install --upgrade build
    # install utility to upload wheel
    pip install --upgrade twine

Go to https://pypi.org to get/generate API Key

## First time upload:

    # Create the wheel, they will be stored in ./dist
    python3 -m build
    ## pip install nicksutils # install the library locally
    
    python3 -m twine upload dist/*
    ## input API Key

## Updates:

*** Remember to update the version TAG in the pyproject.toml***

    python3 -m build
    python3 -m twine upload dist/*.whl

## Example

```python
import nicksutils
from nicksutils import logging

```
Available functions

* logging_setup()
