### Hexlet tests and linter status:
[![Actions Status](https://github.com/RatiborM/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/RatiborM/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/maintainability)](https://codeclimate.com/github/RatiborM/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/acd05649de1fc98c22bc/test_coverage)](https://codeclimate.com/github/RatiborM/python-project-50/test_coverage)

# Description:

Project is about finding difference between files using cli tools


## install:

`make install`

## build:

`make build`

## package install:

`make package-install`

## usage:

## Show help:
    
`gendiff -h`

## Compare two files (default: stylish format):

`gendiff tests/test_data/file1.json tests/test_data/file2.json`

## Compare two files in plain format:

`gendiff --format plain tests/test_data/file1.yml tests/test_data/file2.yml`

## Compare two files in JSON format:

`gendiff --format json file1.json file2.json`


**To remove project just run `rm -rf .`**

## Asciinema's