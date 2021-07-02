# -*- coding: utf-8 -*-
import requests


def is_isbn(value):
    short_value = value.replace('-', '') if '-' in value else value
    length_of_value = len(value)
    if (length_of_value == 13 or length_of_value == 10) and short_value.isdigit():
        return True
    return False
