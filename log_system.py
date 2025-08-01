from collections import defaultdict
from typing import List


class LogSystem:

    def __init__(self):
        self.logs = defaultdict(set)
        self.prefixes = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19,
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs[timestamp].add(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        res = list()
        prefix = self.prefixes[granularity]
        start_prefix = start[:prefix]
        end_prefix = end[:prefix]
        for timestamp, ids in self.logs.items():
            if start_prefix <= timestamp[:prefix] <= end_prefix:
                res.extend(ids)
        return res
