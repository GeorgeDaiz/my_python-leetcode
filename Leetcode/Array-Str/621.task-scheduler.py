"""
621.任务调度器
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 ：
输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。

提示：
任务的总个数为[1, 10000]。
n 的取值范围为 [0, 100]。
"""
from typing import List
import collections


class Solution:
    # 桶
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = collections.Counter(tasks)
        # print(ct.most_common(1))
        bucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(bucket)
        res = (bucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))

    # 排序
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        ct = collections.Counter(tasks)
        max_time = ct.most_common(1)[0][1]
        res = (max_time - 1) * (n + 1)
        for key in ct.keys():
            if ct[key] == max_time:
                res += 1

        return max(length, res)


Solution().leastInterval1(['1', '2', '1', '4', '4', '2', '3', '1'], 3)
