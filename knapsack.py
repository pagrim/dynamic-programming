from dataclasses import dataclass
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
        max_value = self._calc_max_value(self.capacity)
        logger.info('Memo: %s', self.memo)
        return max_value

    def _calc_max_value(self, target_weight):
        if target_weight == 0:
            max_val = 0
        else:
            option_weights_values = self.fetch_options(target_weight)
            logger.info('Target weight %s, options weights, values %s', target_weight, option_weights_values)
            options = [self._calc_max_value(opt_wgt) + val for opt_wgt, val in option_weights_values]
            logger.info('Target weight %s, options %s', target_weight, options)
            if len(options) == 0:
                max_val = 0
            else:
                max_val = max(options)
            self.memo[target_weight] = max_val
        return max_val

    def fetch_options(self, target_weight):
        return [(target_weight - wgt, val) for wgt, val in self.weights_values if self.valid_weight(wgt, target_weight)]

    def zip_weights_values(self, weights, values):
        assert(len(weights) == len(values))
        return list(zip(weights, values))

    def valid_weight(self, weight, target_weight):
        return weight <= target_weight

    def available_weight(self, weights_used, index):
        pass



class KnapsackWithRepetition(Knapsack):

    def __init__(self, weights, values, capacity):
        super().__init__(weights, values, capacity)

    def available_weight(self, weights_used, index):
        return True
