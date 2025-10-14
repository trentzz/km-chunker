# Developer Guide for kmtools

This document is intended for contributors and developers working on `kmtools`.

---

## Development Setup

```bash
# Clone and enter the repository
git clone https://github.com/trentzz/kmtools.git
cd kmtools

# Install Poetry if not already installed
pip install poetry

# Install dependencies
poetry install

# Run the CLI directly
poetry run kmtools --help
````

To install your development version globally via pipx for testing:

```bash
pipx install --force .
```

---

## Project Layout

```text
kmtools/
├── cli.py         # Main CLI entrypoint using argparse
├── chunk.py       # Chunk class for multi-threaded km find_mutation execution
├── merge.py       # Merge class for combining chunk results
├── filter.py      # Filter class for cleaning and refining results
├── plot.py        # Plot class for visualization and summaries
└── utils.py       # Utility functions (logging, validation, timing)
```

---

## Code Style and Conventions

* Code must be **PEP8 compliant**.
* Use **type hints** for all public functions and class methods.
* Avoid inline lambdas for subcommand functions; use named `run_*` functions for readability.
* All logging and timing should be handled through `Utils.log()` to maintain consistent formatting.

---

## Testing

Add lightweight unit tests for:

* Argument parsing in `cli.py`
* Core logic in `Chunk`, `Merge`, `Filter`, and `Plot`
* Utility logging and validation

To run tests (once you have a test suite configured):

```bash
pytest -v
```

---

## Release Process

1. Ensure all tests pass.
2. Update version in `pyproject.toml`.
3. Tag and push a release:

```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin vX.Y.Z
```

4. If targeting PyPI later:

```bash
poetry publish --build
```

---

## Contributing

* Use feature branches: `feature/<short-description>`
* Open a pull request with a clear description of the change.
* Keep commits focused and atomic.

---

## Roadmap

* Add automatic chunk detection for `runall`
* Improve error handling and user feedback for missing binaries
* Integrate optional multiprocessing
* Add support for alternate `km` subcommands beyond `find_mutation`
