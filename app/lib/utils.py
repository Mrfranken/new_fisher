# -*- coding: utf-8 -*-
import logging


def is_isbn(value):
    short_value = value.replace('-', '') if '-' in value else value
    length_of_value = len(value)
    if (length_of_value == 13 or length_of_value == 10) and short_value.isdigit():
        return True
    return False


def get_logger():
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger()
    return logger


def extract_dict_from_class(class_name):
    outcome = {}
    for name in class_name.__dict__:
        if not name.startswith('_'):
            outcome.update({name: getattr(class_name, name)})
    return outcome
