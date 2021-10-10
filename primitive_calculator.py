from typing import List
from operator import itemgetter


class PrimitiveCalculator:

    def __init__(self, operations):
        self.operations = operations
        self.memo = {}

    def find_min_operations(self, target: int) -> int:
        min_operations_seq = self._find_min_operations([], 1, target)
        return len(min_operations_seq)

    def _find_min_operations(self, sequence: List[int], curr: int, target: int) -> List[int]:
        print('Seq:', sequence, 'Current:', curr, 'Target:', target)
        if curr == target:
            return sequence + [curr]
        else:
            try:
                min_ops = self.memo[curr]
            except KeyError:
                valid_operations = [i for i, op in enumerate(self.operations) if op(curr) <= target]
                print('Valid operations:', valid_operations)
                sequence_options = [self._find_min_operations(sequence + [curr], self.operations[vo](curr), target) for vo in valid_operations]
                print('Sequence options:', sequence_options)
                min_seq = min([(i, len(so)) for i, so in enumerate(sequence_options)], key=itemgetter(1))[0]
                print('Minimum seq idx:', min_seq)
                min_ops = sequence_options[min_seq]
                print('Min ops:', min_ops)
                self.memo = min_ops
            return min_ops
