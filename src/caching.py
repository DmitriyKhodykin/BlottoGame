"""
Module for caching current game score.
"""

from pymemcache.client.base import Client


class CacheResult:

    def __init__(self):
        self.client = Client(('localhost', 11211))

    def set_result(self, winner: str) -> None:
        """
        Cache current game score.
        :param winner: 'comp' or 'user'
        :return: None
        """
        self.client.set(winner, 1)

    def get_result(self) -> list:
        """

        :return: List like user - [10, 3] - comp
        """
        user_count = self.client.get('user')
        comp_count = self.client.get('comp')
        print('User Score:', user_count,
              'Computer Score:', comp_count)
        current_score = [user_count, comp_count]
        return current_score


if __name__ == '__main__':
    client = Client('localhost:11211')
    client.set('some_key', 'some_value')
    result = client.get('some_key')
