from typing import Dict
import logging
import sys

logging.basicConfig()


class MemoItem:

    def __init__(self, num_ops, prev_op):
        self.num_ops = num_ops
        self.prev_op = prev_op

    def __eq__(self, other):
        return self.num_ops == other.num_ops and self.prev_op == other.prev_op


class PrimitiveCalculator:

    def __init__(self, operations, validators):
        self.operations = operations
        self.validators = validators
        self.op_val_zip = list(zip(self.operations, self.validators))
        self.memo = {}
        self.logger = logging.getLogger('primitive_calculator')

    def clear_memo(self):
        self.memo = {}

    def find_min_operations(self, target: int) -> MemoItem:
        self._find_min_operations(target)
        return self.memo[target]

    def _find_min_operations(self, target: int) -> Dict[int, MemoItem]:
        self.memo = {i: MemoItem(-1, -1) for i in range(2, target + 1)}
        self.memo[1] = MemoItem(0, -1)
        for trgt in range(2, target + 1):
            for op_idx, (op, vo) in enumerate(self.op_val_zip):
                if vo(trgt):
                    num_operations = self.memo[op(trgt)].num_ops + 1
                    if num_operations < self.memo[trgt].num_ops or self.memo[trgt].num_ops == -1:
                        self.memo[trgt] = MemoItem(num_ops=num_operations, prev_op=op_idx)
        return self.memo

    def backtrace(self, target):
        result = []
        trace_val = target
        while trace_val != 1:
            memo_item = self.memo[trace_val]
            result.insert(0, trace_val)
            trace_val = self.operations[memo_item.prev_op](trace_val)
        result.insert(0, 1)
        return result


if __name__ == '__main__':
    target = int(sys.stdin.read())
    pc = PrimitiveCalculator([lambda x: x // 2, lambda x: x // 3, lambda x: x - 1],
                             [lambda x: x % 2 == 0, lambda x: x % 3 == 0, lambda x: x > 1])
    min_ops = pc.find_min_operations(target)
    print(min_ops.num_ops)
    print(" ".join([str(el) for el in pc.backtrace(target)]))

