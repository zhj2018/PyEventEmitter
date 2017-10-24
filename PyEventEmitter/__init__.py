# -*- coding: utf-8 -*-

import logging

__author__ = '''hongjie Zheng'''
__email__ = 'hongjie0923@gmail.com'
__version__ = '0.0.1'


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:  %(message)s')

from PyEventEmitter.EventEmitter import EventEmitter

__all__ = ['EventEmitter']

