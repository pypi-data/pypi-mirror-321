# ourtils

[![Documentation Status](https://readthedocs.org/projects/ourtils/badge/?version=latest)](https://ourtils.readthedocs.io/en/latest/?badge=latest)

A collection of useful code for working with data.

## Install from github

```
$ python -m pip install git+https://github.com/ayoskovich/ourtils@main
```

## Dev Tips

From the root of this directory, run:
```
$ python -m pip install -e .
```

Run tests (after activating the virtual environment)
```
$ python -m pytest
$ pytest -rP
```

When you download the package from test pypi, you'll need to install like this:
```
python3 -m pip install ourtils==0.1.1 --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/
```

to avoid 

## Buildings docs locally

First make sure you have `make` installed, if you're on windows you can download it here: https://chocolatey.org/install

Then, create and activate a _new_ virtual environment using `requirements.txt` in the `docs/` directory. Then run this from inside the `docs` directory:
```
$ make clean html
```

### Distributing

To create distribution archives
```
$ python3 -m pip install --upgrade build
$ python3 -m build
```

To upload package to test pypi
```
$ python3 -m twine upload -r testpypi dist/*
```

https://packaging.python.org/en/latest/