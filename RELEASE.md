# Releasing createsend-python

## Requirements

- You must have a [PyPI](https://pypi.python.org/pypi) account and must be an owner or maintainer of the [createsend](https://pypi.python.org/pypi/createsend/) package.

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
rake build
```

This builds a source distribution of the package locally to a file named something like `dist/createsend-X.Y.Z.tar.gz`. You're now ready to release the package.

## Release the package

```
rake release
```

This publishes the package to [PyPI](https://pypi.python.org/pypi/createsend/). You should see the newly published version of the package there. All done!
