# jinja2-strcase

[![PyPI version](https://badge.fury.io/py/jinja2-strcase.svg)](https://badge.fury.io/py/jinja2-strcase)

A python package for converting string case in jinja2 templates (including cookiecutter).

It is a port of the go package [strcase](https://github.com/iancoleman/strcase)

## Installation

jinja2-strcase is available for download from PyPI via pip:

```
$ pip install jinja2-strcase
```

## Example

```
from jinja2 import Environment

env = Environment(extensions=['jinja2_strcase.StrcaseExtension'])

# This will convert 'Any kind of string' -> 'any_kind_of_string'
template = env.from_string("{{ 'Any kind of string' |  to_snake }}")

template.render()
```

| Function                        | Result               |
|---------------------------------|----------------------|
| `to_snake`                      | `any_kind_of_string` |
| `to_screaming_snake`            | `ANY_KIND_OF_STRING` |
| `to_kebab`                      | `any-kind-of-string` |
| `to_screaming_kebab`            | `ANY-KIND-OF-STRING` |
| `to_camel`                      | `AnyKindOfString`    |
| `to_lower_camel`                | `anyKindOfString`    |
| `to_sentence_lower`             | `any kind of string` |
| `to_sentence`                   | `Any kind of string` |
| `to_title`                      | `Any Kind Of String` |
| `to_sentence_upper`             | `ANY KIND OF STRING` |
