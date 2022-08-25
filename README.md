> :warning: **Project still a WIP**: Installation and usage instructions will not work presently.

# dbt-markdoc

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Lint status](https://github.com/bd3dowling/dbt-markdoc/actions/workflows/lint.yml/badge.svg)](https://github.com/bd3dowling/dbt-markdoc/actions)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
<!-- [![Test status](https://github.com/bd3dowling/dbt-markdoc/actions/workflows/test.yml/badge.svg)](https://github.com/bd3dowling/dbt-markdoc/actions) -->

A command line utility for creating a markdown wiki for your DBT project.

---

## Installation

In the environment you use for running your DBT project, run:

```sh
pip install dbt_markdoc
```

---

## Usage

`dbt-markdoc` requires a generated [`manifest.json`](https://docs.getdbt.com/reference/artifacts/manifest-json) to create the documentation. Once generated, in a shell run:

```sh
dbt-markdoc generate
```

to generate a flat directory of markdown files.

The generated file structure can be dropped straight into a GitHub repo's wiki directory (usually cloned as a directory beside your project's directory). Once pushed up, you'll have fully navigatable documentation for your project all within GitHub.

You can generate the markdown files straight to the directory with the `--target` option:

```sh
dbt-markdoc generate --target ../project_repo.wiki
```

or use the short-hand flag:

```sh
dbt-markdoc generate --wiki
```

---
