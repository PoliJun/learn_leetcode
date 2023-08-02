class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dps(node):
            nonlocal ans
            if not node:
                return
            
            else:
                ans.append(node.val)
                dps(node.right)

        dps(root)
        res = []
        while ans:
            res.append(ans.pop())
        return res