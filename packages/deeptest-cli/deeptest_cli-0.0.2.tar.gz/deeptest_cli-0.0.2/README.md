1. Run `pip install -e .` in this directory (for development).
2. To build:

   First, bump the version in `pyproject.toml`.

   ```
   pip install build
   <!-- Make sure you're in the deeptest/cli directory -->
   rm -rf dist/*
   python -m build

   pip install twine
   <!-- Upload to test pypi -->
   <!-- You must create an account and get an API key from test.pypi.org -->
   twine upload --repository testpypi dist/*

    <!-- Upload to real pypi -->
    twine upload dist/*


   ```
