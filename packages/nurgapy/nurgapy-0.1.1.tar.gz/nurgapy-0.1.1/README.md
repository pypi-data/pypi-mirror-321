# nurgapy

```bash  _   _                       ____
 | \ | |_   _ _ __ __ _  __ _|  _ \ _   _
 |  \| | | | | '__/ _` |/ _` | |_) | | | |
 | |\  | |_| | | | (_| | (_| |  __/| |_| |
 |_| \_|\__,_|_|  \__, |\__,_|_|    \__, |
                  |___/             |___/
```

Small convenience Python library.

Rationality to build this library, that I don't want to copy over this code to multiple projects.

Currently, `nurgapy` library consists two functions:
- `tyme` - it is a small wrapper function, which is used for measuring execution time of functions. Also works for the class functions.
- `trackbar` - it is a simple progress bar, which just works without many imports. Inspired by [stackoverflow post](https://stackoverflow.com/a/34482761/15059130). There is well-known `tqdm` library, but it prevents user from using `print` statements. For simple use-cases this progress bar should be enough. There is another nice library `alive-progress`, which does not have this issue and many others. But I just wanted to have some simple progress bar, which lives in the single library with other convenience functions.

## Getting started
This project uses Poetry for the package management.

Install Poetry (if not installed)
```
curl -sSL https://install.python-poetry.org | python3 -
```

Install dependencies
```
poetry install
```

Run the project example
```
poetry run src/main.py
```

## Installing pre-commit checks

Install pre-commit
```
poetry run pre-commit install
```

Pre-commit will run automatically after running `git commit`.
But it is also possible to run pre-commit checks against all files manually.
Adding `--verbose` will also print more detailed info. Helpful for debugging test.
```
poetry run pre-commit run --all-files
```

Update the pre-commit hooks.
```
poetry run pre-commit autoupdate
```

## Running tests

Run tests using pytest.

```bash
poetry run pytest -v
```

`-s` - will print the `print()` statements. Use it for debug.

## Publish a new version

In NurgaPy semantic versioning is used. After pushing a new version, a GitHub Actions workflow will be triggered, which will push a new version to PyPi and will also create a new GitHub Release.
In order to publish a new version, apply the next steps:
```
poetry version patch  # 0.0.x

poetry version minor  # 0.x.0

poetry version majon  # x.0.0
```

Then create a proper git tag
```
git tag x.x.x
```

And push it
```
git push origin --tags
```

## Roadmap
- [x] ~~Add basic code~~
- [x] ~~Add pre-commit hook~~
    - Add more rules to pre-commit
- [x] ~~Add public API to the `init.py`~~
- [x] ~~Add tests~~
- [ ] Add tests automation [Nox](https://nox.thea.codes/en/stable/)
- [ ] Add badges
    - [ ] test coverage ([coveralls](https://coveralls.io/))
- [x] Add packaging
- [x] Publish nurgapy to pip
- [x] Add a runner, which automatically publishes a new version to pip
- [x] Add `documentation` folder
- [ ] Create an `examples` folder

Progress bar
- [ ] Add percentages
- [ ] Flexible size
- [ ] Progress bar runs in the independent thread
