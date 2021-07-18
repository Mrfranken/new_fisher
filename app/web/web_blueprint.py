# -*- coding: utf-8 -*-
from flask import Blueprint

web = Blueprint('web', 'web')
print('web Id: ', id(web))
