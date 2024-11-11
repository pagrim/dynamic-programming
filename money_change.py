import sys

from typing import List
import logging
logging.basicConfig()


class MoneyChange:
    def __init__(self, coin_set: List[int]):
        self.coin_set = coin_set
        self.memo = []
        self.logger = logging.getLogger('money_change')

    def _change(self, target: int) -> List[int]:
        self.memo = [sys.maxsize for _ in range(target + 1)]
        self.memo[0] = 0
        for trgt in range(1, target + 1):
            for coin in self.coin_set:
                if trgt - coin >= 0:
                    self.memo[trgt] = min(self.memo[trgt], self.memo[trgt - coin] + 1)
        self.logger.info('Built memo %s', self.memo)

    def change(self, target: int) -> int:
        self._change(target)
        return self.memo[target]

if __name__ == '__main__':
    target = int(sys.stdin.read())
    mc = MoneyChange([4, 3, 1])
    print(mc.change(target))
