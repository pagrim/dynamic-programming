import numpy as np
from itertools import product, groupby
from operator import mul
from functools import reduce
import logging


class Distance:

    def __init__(self, words):
        self.spacer = "-"
        self.words = [[self.spacer] + [char for char in word] for word in words]
        self.memo = self.initialise_memo()
        self.logger = logging.getLogger('distance')

    def initialise_memo(self):
        word_lengths = [len(word) for word in self.words]
        memo_size = reduce(mul, word_lengths)
        init_values = np.ones(memo_size) * -1
        init_values[0] = 0
        init_memo = np.reshape(init_values, word_lengths)
        return init_memo

    def calculate(self):
        return self._calculate([len(word) -1 for word in self.words])

    def _calculate(self, index):
        self.logger.debug('_calculate with: %s', index)
        if sum(index) == 0:
            distance = 0
        else:
            memo_value = self.memo[tuple(index)]
            if memo_value != -1:
                distance = memo_value
            else:
                computed_value = self.get_min_max(index)
                self.memo[tuple(index)] = computed_value
                self.logger.debug('Set distance for %s to %s', index, computed_value)
                distance = computed_value
        self.logger.debug('Updated memo \n%s', self.memo)
        return distance

    def check_valid(self, next_indices):
        next_indices_valid = ([all([ni >= 0 for ni in nxt_idcs]) for nxt_idcs in next_indices])
        self.logger.debug('Next indices valid: %s', next_indices_valid)
        return next_indices_valid

    def get_next_indices(self, index):
        index_ranges = [[idx, idx -1] for idx in index]
        next_indices = [list(idx) for idx in product(*index_ranges) if list(idx) != index]
        self.logger.debug('Next indices: %s', next_indices)
        return next_indices

    def get_min_max(self, index):
        pass

    def get_substitution_cost(self, index):
        pass


class EditDistance(Distance):

    def __init__(self, words):
        super().__init__(words)

    def get_substitution_cost(self, index):
        next_chars = [wrd[ni] for wrd, ni in zip(self.words, index)]
        grouped_next_chars = groupby(next_chars)
        substitution_cost = 1 if next(grouped_next_chars, True) and next(grouped_next_chars, False) else 0
        return substitution_cost

    def get_next_costs(self, index, next_indices):
        next_costs = [self.get_substitution_cost(index) if (sum(index) - sum(ni)) > 1 else 1 for ni in next_indices]
        self.logger.debug('Next costs: %s', next_costs)
        return next_costs

    def get_min_max(self, index):
        next_indices = self.get_next_indices(index)
        next_costs = self.get_next_costs(index, next_indices)
        next_indices_valid = self.check_valid(next_indices)
        return min([self._calculate(ni) + nc for ni, nc, niv in zip(next_indices, next_costs, next_indices_valid) if niv])


class LongestCommonSubsequence(Distance):

    def __init__(self, words):
        super().__init__(words)

    def get_substitution_cost(self, index):
        next_chars = [wrd[ni] for wrd, ni in zip(self.words, index)]
        grouped_next_chars = groupby(next_chars)
        substitution_cost = 0 if next(grouped_next_chars, True) and next(grouped_next_chars, False) else 1
        return substitution_cost

    def get_next_costs(self, index, next_indices):
        next_costs = [self.get_substitution_cost(index) if (sum(index) - sum(ni)) > 1 else 0 for ni in next_indices]
        self.logger.debug('Next costs: %s', next_costs)
        return next_costs

    def get_min_max(self, index):
        next_indices = self.get_next_indices(index)
        next_costs = self.get_next_costs(index, next_indices)
        next_indices_valid = self.check_valid(next_indices)
        return max([self._calculate(ni) + nc for ni, nc, niv in zip(next_indices, next_costs, next_indices_valid) if niv])
