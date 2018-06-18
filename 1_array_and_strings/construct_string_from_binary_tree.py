class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        s = str(t.val)
        if t.left or t.right:
            s += "(" + self.tree2str(t.left) + ")"
        if t.right:
            s += "(" + self.tree2str(t.right) + ")"
        return s


t = [1,2,3,4]
print(Solution().tree2str(t))
# "1(2(4))(3)"

t = [1,2,3,null,4]
print(Solution().tree2str(t))
# "1(2()(4))(3)"
