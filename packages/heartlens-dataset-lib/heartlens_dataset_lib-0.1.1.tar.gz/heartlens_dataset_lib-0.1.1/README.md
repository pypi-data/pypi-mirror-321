# Heartlens Datasest Library

This is a library for managing Hearlens Datasets.

To rebuild, run: `python setup.py sdist bdist_wheel`

To push new changes to PyPi:
1. Update the version in `setup.py` and `heartlens_dataset_lib/__init__.py`
2. If you do not have twine installed, run `pip install twine`
3. Run `twine upload dist/*` from the home directory to push changes. You must enter the Heartlens Project API Key to do this.
