1. Run `pip install -e . --no-cache-dir` in this directory (for development). You can then run `deeptest` with your latest code (this will conflic with brew/pip installations).
2. To upload to pypi:

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

3. To upload to homebrew:

   ```
   <!-- Clear and build binaries -->
   rm -rf dist/*
   python -m build

   <!-- Copy the .tar.gz and .whl files to the homebrew-deeptest repo -->
   shasum -a 256 https://raw.githubusercontent.com/deeptuneai/homebrew-deeptest/main/releases/vX.X.X/deeptest_cli-X.X.X.tar.gz
   <!-- Copy the output and paste it into the sha256 field in homebrew-deeptest/Formula/deeptest.rb -->

   <!-- Untap the old deeptest tap -->
   brew uninstall deeptest
   brew untap deeptuneai/deeptest

   <!-- Install deeptest -->
   brew tap deeptuneai/deeptest
   brew install deeptest
   ```

Note: dependencies must be updated in the `pyproject.toml` and `homebrew-deeptest/Formula/deeptest.rb` files. For homebrew, dependencies must be recursively specified.

If the dependencies have changed, the easiest way to update `deeptest.rb` is to `pip install homebrew-pypi-poet deeptest-cli`, then
run `poet -f deeptest-cli`, this will generate a new `deeptest.rb` file. Caveats:

1. The public version of `deeptest-cli` must have the new dependencies for `poet` to work.
2. You have to change the first line of the `deeptest.rb` file from `class DeeptestCli < Formula` to `class Deeptest < Formula`
