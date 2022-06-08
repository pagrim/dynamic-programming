import logging
import sys
import re
from collections import namedtuple


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('knapsack')

Option = namedtuple("Option", ["weight", "value", "idx"])
MemoItem = namedtuple("MemoItem", ["value", "weights_used", "prev_weight"])


class Knapsack:

    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.weights_values = self.zip_weights_values(weights, values)
        self.capacity = capacity
        self.memo = [MemoItem(-1, [], -1) for _ in range(self.capacity + 1)]
        self.weights_used = [0 for _ in self.weights]

    def calc_max_value(self):
        self._calc_max_value()
        logger.info('Memo: %s', self.memo)
        return max(self.memo, key=lambda mi: mi.value)

    def _calc_max_value(self):
        self.memo[0] = MemoItem(0, [0 for _ in self.weights], 0)
        for trgt in range(1, self.capacity + 1):
            for idx, (wgt, val) in enumerate(self.weights_values):
                opt = self.valid_option(idx, wgt, val, trgt)
                if opt:
                    opt_value = self.memo[opt.weight].value + opt.value
                    if opt_value > self.memo[trgt].value:
                        prev_weights = self.memo[opt.weight].weights_used
                        new_weights = [wgt + 1 if i == idx else wgt for i, wgt in enumerate(prev_weights)]
                        self.memo[trgt] = MemoItem(opt_value, new_weights, opt.weight)

    def valid_option(self, index, weight, value, target):
        option_weight = target - weight
        if option_weight >= 0 and self.available_weight(option_weight, index):
            return Option(option_weight, value, index)


    @staticmethod
    def zip_weights_values(wgts, vals):
        assert(len(wgts) == len(vals))
        return list(zip(wgts, vals))

    def available_weight(self, candidate_weight, index):
        pass


class KnapsackWithRepetition(Knapsack):

    def __init__(self, weights, values, capacity):
        super().__init__(weights, values, capacity)

    def available_weight(self, candidate_weight, index):
        return True


class KnapsackNoRepetition(Knapsack):

    def __init__(self, weights, values, capacity):
        super().__init__(weights, values, capacity)

    def available_weight(self, candidate_weight, weight_index):
        return self.weights_used[weight_index] == 0 and self.memo[candidate_weight].value != -1 and \
               self.memo[candidate_weight].weights_used[weight_index] == 0


if __name__ == '__main__':
    match_object = re.match(r'(\d+)\s(\d+)', sys.stdin.readline().rstrip())
    capacity = int(match_object.group(1))
    num_bars = int(match_object.group(2))
    weights = [int(w) for w in sys.stdin.readline().rstrip().split(" ")]
    knr = KnapsackNoRepetition(weights, weights, capacity)
    max_value = knr.calc_max_value()
    print(max_value.value)

