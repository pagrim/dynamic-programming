from operator import add, sub, mul, truediv
from itertools import product
import numpy as np
from operator import itemgetter
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('arithmetic_expression')


class ArithmeticExpression:

    def __init__(self, digits, operations):
        self.num_operations = len(operations)
        assert (self.num_operations == len(digits) - 1)
        self.digits = digits
        self.operations = self.format_ops(operations)
        self.operator_counts = self.get_operator_counts
        self.min_memo = self.init_memo(sys.maxsize)
        self.max_memo = self.init_memo(-sys.maxsize)

    @staticmethod
    def format_ops(operations):
        ops_dict = {'+': add, '-': sub, '*': mul, '/': truediv}
        return [ops_dict[op] for op in operations]

    def get_operator_counts(self):
        counts = [(j - i, i, j) for j in range(self.num_operations) for i in range(self.num_operations) if j - i > 0]
        return sorted(counts, key=itemgetter(0), reverse=True)

    def init_memo(self, init_val):
        return np.full(shape=(self.num_operations, self.num_operations), fill_value=init_val)

    def calculate_max(self):
        operator_counts = self.get_operator_counts()
        for _, i, j in operator_counts:
            logger.info('Calculating min max for (i, j)=(%s, %s)', i, j)
            self.min_memo[i, j], self.max_memo[i, j] = self.min_max(i, j)
        return self.max_memo[1, self.num_operations]

    def min_max(self, i, j):
        if i == j:
            min_combinations, max_combinations = self.digits[i], self.digits[i]
        else:
            min_combinations = min([self.get_combinations(i, j, k) for k in range(i, j)])
            max_combinations = max([self.get_combinations(i, j, k) for k in range(i, j)])
        return min_combinations, max_combinations

    def get_combinations(self, i, j, k):
        min_max_ops = [min, max]
        min_max_op_combinations = product(min_max_ops, min_max_ops)
        combinations = [self.operations[k](self.fetch_operate(op1, i, k), self.fetch_operate(op2, k + 1, j)) for
                        op1, op2 in min_max_op_combinations]
        logger.info('Combinations %s', combinations)
        return combinations

    def fetch_operate(self, operation, i, j):
        if operation == min and self.min_memo[i, j] != sys.maxsize:
            result = self.min_memo[i, j]
        elif operation == max and self.max_memo[i, j] != -sys.maxsize:
            result = self.max_memo[i, j]
        else:
            result = operation(self.min_max(i, j))
        return result
