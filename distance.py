import numpy as np

class Distance:

    def __init__(self, word1, word2):
        self.spacer = "-"
        self.word1 = self.spacer + word1
        self.word2 = self.spacer + word2
        self.memo = self.initialise_memo()

    def initialise_memo(self):
        init_memo = np.ones((len(self.word1), len(self.word2))) * -1
        init_memo[0, 0] = 0
        return init_memo

    def calculate(self):
        return self._calculate(len(self.word1) -1, len(self.word2) -1)

    def _calculate(self, i, j):
        print('_calculate with:', i, j)
        if i == 0 and j == 0:
            distance = 0
        else:
            if self.memo[i, j] != -1:
                distance = self.memo[i, j]
            else:
                self.memo[i, j] = self.get_min_max(i, j)
                print('Set distance for (i, j)', i, j, 'to', self.memo[i, j])
                distance = self.memo[i, j]
        print('Updated memo', self.memo)
        return distance

    @staticmethod
    def check_valid(next_indices):
        next_indices_valid = [ni[0] >= 0 and ni[1] >= 0 for ni in next_indices]
        print('Next indices valid:', next_indices_valid)
        return next_indices_valid

    @staticmethod
    def get_next_indices(i, j):
        next_indices = [(i-1, j), (i, j-1), (i-1, j-1)]
        print('Next indices:', next_indices)
        return next_indices

    def get_min_max(self, i, j):
        pass


class EditDistance(Distance):

    def __init__(self, word1, word2):
        super().__init__(word1, word2)

    def get_next_costs(self, i, j):
        substitution_cost = 0 if self.word1[i] == self.word2[j] else 1
        next_costs = [1, 1, substitution_cost]
        print('Next costs:', next_costs)
        return next_costs

    def get_min_max(self, i, j):
        next_indices = self.get_next_indices(i, j)
        next_costs = self.get_next_costs(i, j)
        next_indices_valid = self.check_valid(next_indices)
        return min([self._calculate(*ni) + nc for ni, nc, niv in zip(next_indices, next_costs, next_indices_valid) if niv])


class LongestCommonSubsequence(Distance):

    def __init__(self, word1, word2):
        super().__init__(word1, word2)

    def get_next_costs(self, i, j):
        substitution_cost = 1 if self.word1[i] == self.word2[j] else 0
        next_costs = [0, 0, substitution_cost]
        print('Next costs:', next_costs)
        return next_costs

    def get_min_max(self, i, j):
        next_indices = self.get_next_indices(i, j)
        next_costs = self.get_next_costs(i, j)
        next_indices_valid = self.check_valid(next_indices)
        return max([self._calculate(*ni) + nc for ni, nc, niv in zip(next_indices, next_costs, next_indices_valid) if niv])
