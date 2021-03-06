"""
给定一个二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有next 指针都被设置为 NULL。

示例：

输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

提示：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 完美二叉树
    @staticmethod
    def connect(root: Node) -> Node or None:
        # BFS
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            p = None
            for _ in range(len(queue)):
                cur = queue.popleft()
                if p:
                    p.next = cur
                    p = p.next
                else:
                    p = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            p.next = None

        return root

    @staticmethod
    def connect1(root: Node) -> Node or None:
        # 迭代
        if not root:
            return None
        pre = root
        while pre:
            cur = pre
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left
        return root

    def connect2(self, root: Node) -> Node or None:
        # 递归
        if not root:
            return None
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect2(root.left)
        self.connect2(root.right)
        return root

    # 普通二叉树
    def connect3(self, root: Node) -> Node or None:
        if not root:
            return None
        head = root
        while head:
            cur = head
            pre = head = None
            while cur:
                if cur.left:
                    if not pre:
                        pre = head = cur.left
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not pre:
                        pre = head = cur.right
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur = cur.next
        return root
