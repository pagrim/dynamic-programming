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
        max_value = self._calc_max_value(self.capacity, [0 for _ in self.weights])
        logger.info('Memo: %s', self.memo)
        return max_value

    def _calc_max_value(self, target_weight, weights_used):
        if target_weight == 0:
            logger.debug('Found zero option, weights used %s', weights_used)
            max_val = 0
        else:
            option_triples = self.fetch_options(target_weight, weights_used)
            logger.debug('Target weight %s, options weights, values, indexes %s', target_weight, option_triples)
            options = [self._calc_max_value(opt_wgt, self.update_weights(weights_used, idx)) + val for opt_wgt, val, idx in option_triples]
            logger.debug('Target weight %s, options %s, weights used %s', target_weight, options, weights_used)
            if len(options) == 0:
                max_val = 0
            else:
                max_val = max(options)
            self.memo[target_weight] = max_val
        return max_val

    def fetch_options(self, target_weight, weights_used):
        return [(target_weight - wgt, val, idx) for idx, (wgt, val) in enumerate(self.weights_values) if self.valid_weight(wgt, target_weight) and self.available_weight(weights_used, idx)]


    def update_weights(self, weights_used, weight_index):
        return [wu +1 if i == weight_index else wu for i, wu in enumerate(weights_used)]

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

class KnapsackNoRepetition(Knapsack):

    def __init__(self, weights, values, capacity):
        super().__init__(weights, values, capacity)

    def available_weight(self, weights_used, index):
        return weights_used[index] == 0
