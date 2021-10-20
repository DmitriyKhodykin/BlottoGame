"""
Module for caching current game score.
"""

from pymemcache.client import base


class CacheResult:

    def __init__(self):
        self.client = base.Client(('localhost', 11211))

    def set_result(self, winner: str):
        self.client.set(winner, 1)

    def get_result(self):
        user_count = self.client.get('user')
        comp_count = self.client.get('comp')
        print('User Score:', user_count, 'Computer Score:', comp_count)


if __name__ == '__main__':
    cache = CacheResult()
    cache.set_result('user')
