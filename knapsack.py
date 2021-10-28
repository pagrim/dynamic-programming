from operator import itemgetter
from dataclasses import dataclass
from functools import reduce
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('knapsack')


@dataclass
class WeightsValue:
    weights: list
    value: int


class Knapsack:

    def __init__(self, weights, values, capacity):
        self.weights = weights
        self.values = values
        self.weights_values = self.zip_weights_values(weights, values)
        self.capacity = capacity
        self.memo = [None for _ in range(capacity + 1)]

    def calc_max_value(self):
        return self._calc_max_value([0 for _ in self.weights], self.capacity)

    def _calc_max_value(self, weights_used, target_weight):
        logger.info('Weights used: %s, target weight %s', weights_used, target_weight)
        if target_weight == 0:
            max_val_weights = WeightsValue(weights=weights_used, value=0)
        elif self.memo[target_weight] is not None:
            max_val_weights = self.memo[target_weight]
        else:
            options = [self.fetch_option(weights_used, idx, target_weight) for idx, _ in enumerate(self.weights_values)
                       if self.available_weight(weights_used, idx) and self.valid_weight(idx, target_weight)]
            if len(options) == 0:
                max_val_weights = WeightsValue(weights=weights_used, value=self.compute_value(weights_used))
            else:
                option_values = (opt.value + self.values[idx] for idx, opt in enumerate(options))
                max_idx, max_val = max(enumerate(option_values), key=itemgetter(1))
                max_val_weights = WeightsValue(weights=options[max_idx].weights, value=max_val)
            self.memo[target_weight] = max_val_weights
        return max_val_weights
    
    def zip_weights_values(self, weights, values):
        assert(len(weights) == len(values))
        return zip(weights, values)

    def fetch_option(self, weights_used, index, target_weight):
        new_weights_used = [wu + 1 if i == index else wu for i, wu in enumerate(weights_used)]
        value_weight_option = self._calc_max_value(new_weights_used, target_weight - self.weights[index])
        return value_weight_option

    def compute_value(self, weights_used):
        multiples = list(map(lambda x: x[0]*x[1], zip(self.values, weights_used)))
        return reduce(lambda x, y: x+y, multiples)

    def valid_weight(self, index, target_weight):
        return self.weights[index] <= target_weight

    def available_weight(self, weights_used, index):
        pass



class KnapsackWithRepetition(Knapsack):

    def __init__(self, weights, values, capacity):
        super().__init__(weights, values, capacity)

    def available_weight(self, weights_used, index):
        return True




