from itertools import product
from operator import mul, add, sub, truediv
import re
import sys

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('arithmetic_expression')


class ArithmeticExpression:

    def __init__(self, digits, operations):
        assert (len(operations) == len(digits) - 1)
        self.digits = digits
        self.op_map = {'+': add, '-': sub, '/': truediv, '*': mul}
        self.num_digits = len(digits)
        self.operations_str = operations
        self.operations = self.init_operations(operations)
        self.min_results = {}
        self.max_results = {}

    def init_operations(self, operations):
        return [self.op_map[op] for op in operations]

    def calculate(self):
        ordered_indices = [(i, i + s) for s in range(0, self.num_digits) for i in range(0, self.num_digits - s)]
        logger.debug('Calculated ordered indices as %s', ordered_indices)
        for (i, j) in ordered_indices:
            self._calculate(i, j)
        logger.info('Computed min memo \n%s', self.min_results)
        logger.info('Computed max memo \n%s', self.max_results)
        return self

    def calculate_min_max(self):
        calculated = self.calculate()
        return calculated.min_results[0, self.num_digits - 1], calculated.max_results[0, self.num_digits - 1]

    def _calculate(self, i, j):
        logger.debug('Calcularting for (%d, %d)', i, j)
        if i == j:
            min_val, max_val = self.digits[i], self.digits[i]
            self.set_memo(i, j, min_val, max_val)
        elif self.has_memo_value(i, j):
            min_val, max_val = self.fetch_memo(i, j)
        else:
            combination_min_max = [self.get_combinations(i, j, k) for k in range(i, j)]
            min_val = min([val for val, _ in combination_min_max])
            max_val = max([val for _, val in combination_min_max])
            self.set_memo(i, j, min_val, max_val)
        logger.debug('Computed min and max for (%d, %d) as (%d, %d)', i, j, min_val, max_val)
        return min_val, max_val

    def set_memo(self, i, j, min_val, max_val):
        self.min_results[i, j] = min_val
        self.max_results[i, j] = max_val

    def has_memo_value(self, i, j):
        return (i, j) in self.min_results and (i, j) in self.max_results

    def fetch_memo(self, i, j):
        return self.min_results[i, j], self.max_results[i, j]

    def get_combinations(self, i, j, k):
        min_max_combinations = product(self._calculate(i, k), self._calculate(k + 1, j))
        combination_values = [self.operations[k](prod1, prod2) for prod1, prod2 in min_max_combinations]
        return min(combination_values), max(combination_values)

    def retrace(self, target_min_max, target_value):
        retrace_str = self._retrace(Expression(0, self.num_digits - 1), target_min_max, target_value)
        return self.tidy_retrace(retrace_str)

    def _retrace(self, expression, target_min_max, target_value):
        if expression.lower_index == expression.upper_index:
            return str(self.digits[expression.lower_index])
        else:
            for k in range(expression.lower_index, expression.upper_index + 1):
                logger.debug('For index k %s', k)
                candidate_expression_indices = [(expression.lower_index, k), (k + 1, expression.upper_index)]
                logger.debug('Candidate expression indices %s', candidate_expression_indices)
                target_min_max_pair = self.evaluate(self.operations_str[k], target_min_max)
                logger.debug('Target min max pair %s', target_min_max_pair)
                candidate_expression_components = self.fetch_components(candidate_expression_indices,
                                                                        target_min_max_pair)
                logger.debug('Candidate expression components %s', candidate_expression_components)
                candidate_expression_value = self.operations[k](*candidate_expression_components)
                if candidate_expression_value == target_value:
                    retrace_lower = self._retrace(Expression(expression.lower_index, k), target_min_max_pair[0],
                                                  candidate_expression_components[0])
                    retrace_upper = self._retrace(Expression(k + 1, expression.upper_index), target_min_max_pair[1],
                                                  candidate_expression_components[1])
                    return f'({retrace_lower}){self.operations_str[k]}({retrace_upper})'

    @staticmethod
    def tidy_retrace(retrace_str):
        return re.sub(r'\((\d)\)', r'\1', retrace_str)

    def evaluate(self, operator, target_min_max):
        target_operator_map = {
            'max': {'+': ('max', 'max'), '*': ('max', 'max'), '-': ('max', 'min'), '/': ('max', 'min')},
            'min': {'+': ('min', 'min'), '*': ('min', 'min'), '-': ('min', 'max'), '/': ('min', 'max')},
        }
        return target_operator_map[target_min_max][operator]

    def fetch_components(self, candidate_expression_indices, target_min_max_pair):
        components = [
            self.min_results[indices[0], indices[1]] if tmm == 'min' else self.max_results[indices[0], indices[1]]
            for tmm, indices in zip(list(target_min_max_pair), candidate_expression_indices)]
        return components


class Expression:

    def __init__(self, lower_index, upper_index):
        self.lower_index = lower_index
        self.upper_index = upper_index


if __name__ == '__main__':
    digits = []
    operations = []
    input = sys.stdin.readline().rstrip()
    for in_char in input:
        if re.match('\d', in_char):
            digits.append(int(in_char))
        else:
            operations.append(in_char)
    _, max_res = ArithmeticExpression(digits, operations).calculate_min_max()
    print(max_res)
