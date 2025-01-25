<!--
SPDX-FileCopyrightText: Peter Pentchev <roam@ringlet.net>
SPDX-License-Identifier: BSD-2-Clause
-->

# Changelog

All notable changes to the vetox project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2025-01-18

### Fixes

- Bump the `hatchling` required version to 1.14 for Python 3.13 support

### Additions

- Add Python 3.14 as a supported version
- Test infrastructure:
    - allow uv 0.2, 0.3, 0.4, and 0.5 in the runtime test
- Nix test infrastructure:
    - also run the tests on Python 3.14

### Other changes

- Switch to a PEP 639 license specification
- Documentation:
    - use mkdocstrings 0.25 with no changes
- Test infrastructure:
    - Ruff:
        - use Ruff 0.9.2
        - override one more docstring check

## [0.2.0] - 2024-08-08

### Breaking changes

- Drop support for Tox 3.x
- Drop support for Python 3.8

### Other changes

- Always pass `upgrade_deps` when creating the virtual environment using `venv`
- Import the `Iterator` class from its new home at `collections.abc`
- Test infrastructure:
    - check which version of Tox was installed in the virtual environment
    - Ruff:
        - use the concise output format even in preview mode
        - use Ruff 0.5.6
        - override two new docstring-related warnings (`DOC201` and `DOC501`)

## [0.1.4] - 2024-07-18

### Fixes

- Documentation:
    - sync `README.md` with `docs/index.md`
- Nix test infrastructure:
    - run `python3.X`, not `python3`, so as to not accidentally invoke
      a "more preferred" Python version that is also installed in
      the Nix environment

### Other changes

- Drop some obsolete Black configuration settings
- Test infrastructure:
    - use Ruff 0.5.2 with no changes
    - use REUSE 0.4.x with no changes
- Nix test infrastructure:
    - only pass the minor version of Python, we only support Python 3.x
    - pass the Python minor version as a string for easier interpolation

## [0.1.3] - 2024-03-15

### Semi-incompatible changes

- Command-line tool behavior changes:
    - remove environment variables related to virtual environments, Tox, or
      pytest before invoking any tools or libraries that manipulate
      virtual environments and the packages installed within them.
      The `VIRTUAL_ENV` variable and any variables with names starting
      with `PYTEST`, `PYTHON`, and `TOX` are unset.
- API changes if `vetox` is imported as a Python module:
    - do not pass the full `Config` object to `get_tox_min_version()`, only pass
      the path to the configuration file

### Fixes

- Fix the handling of the `features` or `version` commands.
- Documentation:
    - document the `--tox-req` option to `run` and `run-parallel` in the manual page

### Additions

- Add the `--tox-uv` command-line option to install `tox-uv` into the ephemeral
  environment so that Tox can create its own virtual environments faster.
- Add the `--uv` command-line option to use the `uv` package installer to
  create the ephemeral virtual environment itself.
- Documentation:
    - add `publync` definitions to the `pyproject.toml` file
- Test infrastructure:
    - add unit tests for the trivial command-line processing cases: `--help`,
      `features`, `version`, invalid arguments, missing command, etc.

### Other changes

- Use `pip freeze` instead of `pip list` to obtain the list of packages installed
  within a virtual environment.
- Documentation:
    - use `mkdostrings` 24.x with no changes
- Test infrastructure:
    - Ruff:
        - use Ruff 0.3.2 with no changes
        - simplify the Ruff configuration files layout
    - pytest:
        - allow pytest 8.x with no changes
        - use `pytest-xdist` to parallelize the test runs
- Nix test infrastructure:
    - start with Python 3.9; nixpkgs/unstable dropped Python 3.8
    - bring in `uv` as a runtime dependency so that the tests may pass
    - pass the new `--uv` and `--tox-uv` command-line options to
      the `vetox` invocation
    - since `uv` requires an SSL certificate file,
      use `/etc/ssl/certs/ca-certificates` as the default path and
      let it be overridden by the `VETOX_CERT_FILE` environment variable

## [0.1.2] - 2024-02-08

### Fixes

- Documentation:
    - drop some unneeded whitespace in code blocks

### Additions

- Add the `--tox-req` (`-t`) command-line option to specify PEP508-like
  version requirements for Tox itself, allowing e.g. Tox 3.x to be used.
- Test infrastructure:
    - also build the documentation in the second Tox stage
    - use Ruff 0.2.1 with no changes

## [0.1.1] - 2024-02-03

### Fixes

- Pass "vetox", not "logging-std", as the name of the main logger.

### Additions

- Documentation:
    - add a "Download" page

### Other changes

- Let Ruff insist on trailing commas.
- Documentation:
    - README.md: catch up with the main documentation page
- Test infrastructure:
    - use Ruff 0.2.0
        - disable another subprocess-related check
        - push some of the configuration settings into the new `ruff.lint.*`
          hierarchy
        - drop the override for the deprecated "no self use" check

## [0.1.0] - 2023-12-21

### Started

- First public release.

[Unreleased]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.2.1...main
[0.2.1]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.2.0...release%2F0.2.1
[0.2.0]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.1.4...release%2F0.2.0
[0.1.4]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.1.3...release%2F0.1.4
[0.1.3]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.1.2...release%2F0.1.3
[0.1.2]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.1.1...release%2F0.1.2
[0.1.1]: https://gitlab.com/ppentchev/vetox/-/compare/release%2F0.1.0...release%2F0.1.1
[0.1.0]: https://gitlab.com/ppentchev/vetox/-/tags/release%2F0.1.0
