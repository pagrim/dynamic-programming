import numpy as np

class EditDistance:

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
            edit_distance = 0
        else:
            if self.memo[i, j] != -1:
                edit_distance = self.memo[i, j]
            else:
                substitution_cost = 0 if self.word1[i] == self.word2[j] else 1
                next_indices = [(i-1, j), (i, j-1), (i-1, j-1)]
                next_costs = [1, 1, substitution_cost]
                next_indices_valid = [ni[0] >= 0 and ni[1] >= 0 for ni in next_indices]
                print('Next indices:', next_indices)
                print('Next costs:', next_costs)
                print('Next indices valid:', next_indices_valid)
                self.memo[i, j] = min([self._calculate(*ni) + nc for ni, nc, niv in zip(next_indices, next_costs, next_indices_valid) if niv])
                print('Set distance for (i, j)', i, j, 'to', self.memo[i, j])
                edit_distance = self.memo[i, j]
        print('Updated memo', self.memo)
        return edit_distance
