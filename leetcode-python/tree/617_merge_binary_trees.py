"""
题目：
    617. 合并二叉树：https://leetcode-cn.com/problems/merge-two-binary-trees/
题解：
    https://leetcode-cn.com/problems/merge-two-binary-trees/solution/he-bing-er-cha-shu-by-leetcode/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # condition：其中一个为空，就返回非空的那个
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # recursion：节点值相加
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root


if __name__ == "__main__":
    # tree
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    # merge
    s = Solution()
    t = s.mergeTrees(t1, t2)
    print(t.val, t.left.val, t.right.val, t.left.left.val, t.left.right.val, t.right.right.val)
