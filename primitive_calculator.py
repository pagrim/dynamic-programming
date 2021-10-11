from typing import List
from operator import itemgetter


class PrimitiveCalculator:

    def __init__(self, operations, validators):
        self.operations = operations
        self.validators = validators
        self.memo = {}

    def clear_memo(self):
        self.memo = {}

    def find_min_operations(self, target: int) -> List[int]:
        return self._find_min_operations([], target)

    def count_min_operations(self, target: int):
        return len(self.find_min_operations(target))

    def _find_min_operations(self, sequence: List[int], target: int) -> List[int]:
        print('Seq:', sequence, 'Target:', target)
        if target == 1:
            return [target] + sequence
        else:
            try:
                seq_result = self.memo[target]
            except KeyError:
                valid_operations = [i for i, vld in enumerate(self.validators) if vld(target)]
                print('Valid operations:', valid_operations)
                sequence_options = [self._find_min_operations([target] + sequence, self.operations[vo](target)) for vo in valid_operations]
                print('Sequence options:', sequence_options)
                min_seq = min([(i, len(so)) for i, so in enumerate(sequence_options)], key=itemgetter(1))[0]
                print('Minimum seq idx:', min_seq)
                seq_result = sequence_options[min_seq]
                print('Min operations:', seq_result)
                self.memo[target] = seq_result
            return seq_result
