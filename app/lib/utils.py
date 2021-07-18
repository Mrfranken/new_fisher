# -*- coding: utf-8 -*-
import logging


def is_isbn(value):
    short_value = value.replace('-', '') if '-' in value else value
    length_of_value = len(value)
    if (length_of_value == 13 or length_of_value == 10) and short_value.isdigit():
        return 'isbn'
    return 'keyword'


def get_logger():
    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger()
    return logger





class A(object):
    def run(self):
        return 3


if __name__ == '__main__':
    a = A()
    a.run()
