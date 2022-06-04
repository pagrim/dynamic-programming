import sys

from typing import List
from operator import itemgetter


class MoneyChange:
    def __init__(self, coin_set: List[int]):
        self.coin_set = coin_set
        self.memo = {}

    def change(self, target: int) -> List[int]:
        return self._change([], target)

    def _change(self, coins_used: List[int], target: int) -> List[int]:
        print('Used coins:', coins_used, 'target:', target, 'memo:', self.memo)
        if target == 0:
            return coins_used
        else:
            try:
                result = self.memo[target]
            except KeyError:
                candidates = [cn for cn in self.coin_set if target - cn >= 0]
                options = [self._change(coins_used + [cn], target - cn) for cn in candidates]
                option_lengths = [(i, len(opt)) for i, opt in enumerate(options)]
                result_index = min(option_lengths, key=itemgetter(1))[0]
                result = options[result_index]
                self.memo[target] = result
            return result


if __name__ == '__main__':
    target = int(sys.stdin.read())
    mc = MoneyChange([4, 3, 1])
    print(mc.change(target))
