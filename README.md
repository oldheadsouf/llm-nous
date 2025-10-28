# llm-nous

[![PyPI](https://img.shields.io/pypi/v/llm-nous.svg)](https://pypi.org/project/llm-nous/)
[![Changelog](https://img.shields.io/github/v/release/oldheadsouf/llm-nous?include_prereleases&label=changelog)](https://github.com/oldheadsouf/llm-nous/releases)
[![Tests](https://github.com/oldheadsouf/llm-nous/actions/workflows/test.yml/badge.svg)](https://github.com/oldheadsouf/llm-nous/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/oldheadsouf/llm-nous/blob/main/LICENSE)

Access [nouseresearch.com](https://nousresearch.com/) Hermes models via [simonw's llm cli](https://github.com/simonw/llm)

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).
```bash
llm install llm-nous
```
## Usage

Obtain a [Nous API key](https://portal.nousresearch.com/login) and save it like this:

```bash
llm keys set nous
# <Paste key here>
```
Run `llm models` to get a list of models.

Run prompts like this:
```bash
llm -m Hermes-4-405B 'five great names for a pet ocelot'
llm -m Hermes-4-70B 'how to reverse a linked list in python'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-nous
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
