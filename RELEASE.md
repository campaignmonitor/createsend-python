# Releasing createsend-python

## Requirements

- You must have a [PyPI](https://pypi.python.org/pypi) account and must be an owner or maintainer of the [createsend](https://pypi.python.org/pypi/createsend/) package.
- You must have the 'twine' and 'wheel' packages installed

## Prepare the release

- Increment `version` in the `setup.py` file, ensuring that you use [Semantic Versioning](http://semver.org/).
- Add an entry to `HISTORY.md` which clearly explains the new release.
- Commit your changes:

  ```
  git commit -am "Version X.Y.Z"
  ```

- Tag the new version:

  ```
  git tag -a vX.Y.Z -m "Version X.Y.Z"
  ```

- Push your changes to GitHub, including the tag you just created:

  ```
  git push origin master --tags
  ```

- Ensure that all [tests](https://travis-ci.org/campaignmonitor/createsend-python) pass, and that [coverage](https://coveralls.io/r/campaignmonitor/createsend-python) is maintained or improved.

- Add a new [GitHub Release](https://github.com/campaignmonitor/createsend-python/releases) using the newly created tag.

## Build the package

```
python setup.py sdist bdist_wheel
```

This will create a 'dist' directory. It should contain 2 files: a '.tar.gz' file and a '.whl' file. This is what will be published to PyPI

## Release the package

```
twine upload dist/*
```

This publishes the package to [PyPI](https://pypi.python.org/pypi/createsend/). You should see the newly published version of the package there. All done!
