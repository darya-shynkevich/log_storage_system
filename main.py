from typing import List


class LogSystem:

    def __init__(self):
        self.logs = {}

    def put(self, id: int, timestamp: str) -> None:
        pass

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        pass


# Your LogSystem object will be instantiated and called as such:
obj = LogSystem()
obj.put(0, "2017:01:01:23:59:59")
param_2 = obj.retrieve(
    start="2017:01:01:23:59:59", end="2017:01:02:23:59:59", granularity="Day"
)