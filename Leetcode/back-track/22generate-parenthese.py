"""
22.括号生成

数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""


class Solution:
    def generateParenthesis(self, n: int) -> list:
        if n == 0:
            return []

        def get_parenthese(S, left, right):
            if len(S) == 2 * n:
                combinations.append(''.join(S))
                return
            if left < n:
                S.append('(')
                get_parenthese(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                get_parenthese(S, left, right+1)
                S.pop()

        combinations = []
        get_parenthese([], 0, 0)
        return combinations
