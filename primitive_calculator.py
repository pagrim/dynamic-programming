from typing import List
from operator import itemgetter
import logging
import sys

logging.basicConfig()


class PrimitiveCalculator:

    def __init__(self, operations, validators):
        self.operations = operations
        self.validators = validators
        self.memo = {}
        self.logger = logging.getLogger('primitive_calculator')

    def clear_memo(self):
        self.memo = {}

    def find_min_operations(self, target: int) -> List[int]:
        return self._find_min_operations([], target)

    def count_min_operations(self, target: int):
        return len(self.find_min_operations(target))

    def _find_min_operations(self, sequence: List[int], target: int) -> List[int]:
        self.logger.debug('Seq: %s Target: %s', sequence, target)
        if target == 1:
            return [target] + sequence
        else:
            try:
                seq_result = self.memo[target]
            except KeyError:
                valid_operations = [i for i, vld in enumerate(self.validators) if vld(target)]
                self.logger.debug('Valid operations: %s', valid_operations)
                sequence_options = [self._find_min_operations([target] + sequence, self.operations[vo](target)) for vo
                                    in valid_operations]
                self.logger.debug('Sequence options: %s', sequence_options)
                min_seq = min([(i, len(so)) for i, so in enumerate(sequence_options)], key=itemgetter(1))[0]
                self.logger.debug('Minimum seq idx: %s', min_seq)
                seq_result = sequence_options[min_seq]
                self.logger.debug('Min operations: %s', seq_result)
                self.memo[target] = seq_result
            return seq_result


if __name__ == '__main__':
    target = int(sys.stdin.read())
    pc = PrimitiveCalculator([lambda x: x // 2, lambda x: x // 3, lambda x: x - 1],
                             [lambda x: x % 2 == 0, lambda x: x % 3 == 0, lambda x: x > 1])
    min_ops = pc.find_min_operations(target)
    print(len(min_ops) - 1)
    print(" ".join([str(el) for el in min_ops]))

