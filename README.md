![GitHub last commit](https://img.shields.io/github/last-commit/opentaal/opentaal-python)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/opentaal/opentaal-python)
![GitHub Repo stars](https://img.shields.io/github/stars/opentaal/opentaal-python)
![GitHub watchers](https://img.shields.io/github/watchers/opentaal/opentaal-python)
![GitHub Sponsors](https://img.shields.io/github/sponsors/opentaal)
![Liberapay patrons](https://img.shields.io/liberapay/patrons/opentaal)

# OpenTaal Python

Python package by OpenTaal for quickly processing Dutch texts.

![logo Stichting OpenTaal](images/logo-shape-trans-640x360.png?raw=true)

## Prerequisites

Install the following packages for usage

    sudo apt-get -y install libexttextcat-dev
    pip install -U hunspell py_gnuplot python-ucto
    python3 -c "import ucto; ucto.installdata()"

Install the following packages for development

    pip install -U twine pytest-cov sphinx-autodoc-typehints mock snakeviz

## Unit tests

Run unit tests with

    pytest

Noting the following options

    -v verbose
    -s show output print statements
    --durations=10 show 10 slowest methods

## Code coverage

Run unit tests with code coverage and view report in HTML

    pytest --cov=opentaal --cov-branch --cov-report=html
    browse htmlcov/index.html

## Profiling

Profile unit tests and view report in HTML

    python3 -m cProfile -o pytest.prof -m pytest
    snakeviz pytest.prof

## API documentation

Generate API documentation and view it in HTML with

    cd docs
    make html
    browse _build/html/index.html

Donating is also possible with <noscript><a href="https://liberapay.com/opentaal/donate"><img alt="Donate using Liberapay" src="https://liberapay.com/assets/widgets/donate.svg"></a></noscript>
