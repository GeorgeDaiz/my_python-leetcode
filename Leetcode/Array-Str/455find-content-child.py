"""
分糖果(leetcode455)
题目：已知一些孩子和一些糖果，每个孩子有需求因子g，每个糖果有大小s，当某个糖果的大小s>=某个孩子的需求因子g时，代表该糖果可以满足该孩子，求使用这些糖果，最多能满足多少孩子（注意，某个孩子最多只能用1个糖果满足）

思考：
当某个孩子可以被多个糖果满足时，是否需要优先用某个糖果满足这个孩子？
当某个糖果可以满足多个孩子时，是否需要优先满足某个孩子？
贪心规律是什么？

贪心规律：
某个糖果如果不能满足某个孩子，则该糖果也一定不能满足需求因子更大的孩子

某个孩子可以用更小的糖果满足，则没必要用更大糖果满足，因为可以保留更大的糖果满足需求因子更大的孩子
孩子的需求因子更小则其更容易被满足，故优先从需求因子小的孩子尝试，可以得到正确的结果(因为我们追求更多的孩子被满足，所以用一个糖果满足需求因子较小或较大的孩子都是一样的)。
算法设计：

(1)对需求因子数组g和糖果大小数组s进行从小到大的排序
(2)按照从小到大的顺序使用各糖果尝试是否可满足某个孩子，每个糖果只尝试1次，只有尝试成功时，换下一个孩子尝试，直到发现没更多的孩子或者没有更多的糖果，循环结束。
"""


class Solution:
    @staticmethod
    def find_content_child(g: list, s: list) -> int:
        g = sorted(g)
        s = sorted(s)
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child

