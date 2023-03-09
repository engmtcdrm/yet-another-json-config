# Build and Distribute
```sh
python -m build
python -m twine upload --repository testpypi dist/*
```


# Run Test Environment
```sh
python -m venv env

.\env\Scripts\activate

python -m pip install --index-url https://test.pypi.org/simple/ --no-deps yet-another-json-config

python test.py
```