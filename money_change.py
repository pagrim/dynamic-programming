import sys

from typing import List
import logging
logging.basicConfig()


class MoneyChange:
    def __init__(self, coin_set: List[int]):
        self.coin_set = coin_set
        self.memo = {}
        self.logger = logging.getLogger('money_change')

    def change(self, target: int) -> int:
        self._change([], target)
        return len(self.memo[0])

    def _change(self, coins_used: List[int], target: int) -> None:
        self.logger.debug('Used coins: %s target: %s, memo: %s ', coins_used, target, self.memo)
        try:
            curr_num_coins = len(self.memo[target])
        except KeyError:
            curr_num_coins = sys.maxsize
        if len(coins_used) < curr_num_coins:
            self.memo[target] = coins_used
        if target == 0:
            return
        else:
            candidates = [cn for cn in self.coin_set if target - cn >= 0]
            for coin in candidates:
                self._change(coins_used + [coin], target - coin)

    def clear_memo(self):
        self.memo = {}


if __name__ == '__main__':
    target = int(sys.stdin.read())
    mc = MoneyChange([4, 3, 1])
    print(mc.change(target))
