from typing import (
    List,
)

"""
Definition of Interval:
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals)

        last_end = -1
        for s, e in intervals:
            if s < last_end:
                return False
            last_end = e

        return True


s = Solution()
print(s.can_attend_meetings([(0, 30), (5, 10), (15, 20)]))
