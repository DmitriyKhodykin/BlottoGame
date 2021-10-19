"""
Module for caching current game score.
"""

from pymemcache.client import base


class CacheResult:

    def __init__(self):
        self.client = base.Client(('localhost', 11211))

    def set_result(self):
        self.client.set('some_key', 'some value')

    def get_result(self):
        self.client.get('some_key')
