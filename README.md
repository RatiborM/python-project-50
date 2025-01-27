### Hexlet tests and linter status:
[![Actions Status](https://github.com/RatiborM/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/RatiborM/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/maintainability)](https://codeclimate.com/github/RatiborM/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/test_coverage)](https://codeclimate.com/github/RatiborM/python-project-50/test_coverage)

# Gendiff

Welcome to the Gendiff project! This project is designed to help you compare configuration files and see the differences between them. It supports various formats such as JSON, YAML, and YML. The tool provides a clear and structured output, making it easy to understand the changes.

## Requirements

To run this project, you need to have the following software installed:

- Python >=3.12.0
- Uv

## Installation

To set up the project, navigate to the project directory and run the following command:

```bash
make i
```
or
```bash
uv tool install .
```

## Usage

To start using the Brain Games, use the following command:

```bash
gendiff -h
```
```bash
gendiff path/file1.json path/file2.yaml | file.yml