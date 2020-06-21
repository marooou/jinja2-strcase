# -*- coding: utf-8 -*-

import re

from jinja2 import nodes
from jinja2.ext import Extension

import re

def _space_numbers(match):
    return f'{match.group(1)} {match.group(2)} {match.group(3)}'

def _add_word_boundaries_to_numbers(string):
    pattern = re.compile(r'([a-zA-Z])(\d+)([a-zA-Z]?)')
    return pattern.sub(_space_numbers, string)

def _to_camel_init_case(string, init_case):
    string = _add_word_boundaries_to_numbers(string)
    string = string.strip(" ")
    n = ""
    cap_next = init_case
    for v in string:
        if (v >= 'A' and v <= 'Z') or (v >= '0' and v <= '9'):
            n += v
        if v >= 'a' and v <= 'z':
            if cap_next:
                n += v.upper()
            else:
                n += v
        if v == '_' or v == ' ' or v == '-':
            cap_next = True
        else:
            cap_next = False
    return n

def to_camel(string):
    return _to_camel_init_case(string, True)

def to_lower_camel(string):
    if not string:
        return string
    if string[0] >= 'A' and string[0] <= 'Z':
        string = string[0].lower() + string[1:]
    return _to_camel_init_case(string, False)

def _to_screaming_delimited(string, delimiter, screaming):
    string = _add_word_boundaries_to_numbers(string)
    string = string.strip(" ")
    n = ""
    for i, v in enumerate(string):
        next_case_is_changed = False
        if i + 1 < len(string):
            next_char = string[i+1]
            if (v >= 'A' and v <= 'Z' and next_char >= 'a' and next_char <= 'z') or (
                    v >= 'a' and v <= 'z' and next_char >= 'A' and next_char <= 'Z'):
                next_case_is_changed = True

        if i > 0 and n[-1] != delimiter and next_case_is_changed:
            if v >= 'A' and v <= 'Z':
                n += delimiter + v
            elif v >= 'a' and v <= 'z':
                n += v + delimiter
        elif v == ' ' or v == '_' or v == '-':
            n += delimiter
        else:
            n += v
    if screaming:
        n = n.upper()
    else:
        n = n.lower()
    return n

def to_delimited(string, delimiter):
    return _to_screaming_delimited(string, delimiter, False)

def to_kebab(string):
    return to_delimited(string, '-')

def to_snake(string):
    return to_delimited(string, '_')

def to_screaming_kebab(string):
    return _to_screaming_delimited(string, '-', True)

def to_screaming_snake(string):
    return _to_screaming_delimited(string, '_', True)

def to_screaming_delimited(string, delimiter):
    return _to_screaming_delimited(string, delimiter, True)

class StrcaseExtension(Extension):
    """A python package for converting string case in jinja2 templates."""

    def __init__(self, environment):
        super(StrcaseExtension, self).__init__(environment)
        environment.filters['to_camel'] = to_camel
        environment.filters['to_lower_camel'] = to_lower_camel
        environment.filters['to_kebab'] = to_kebab
        environment.filters['to_screaming_kebab'] = to_screaming_kebab
        environment.filters['to_snake'] = to_snake
        environment.filters['to_screaming_snake'] = to_screaming_snake
        environment.filters['to_delimited'] = to_delimited
        environment.filters['to_screaming_delimited'] = to_screaming_delimited
