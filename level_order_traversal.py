# level order traversal
# time complexity: O(N)
# space complexity: O(N)
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : NA

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        level = 0
        res = []
        while q:
            res.append([])
            for i in range(len(q)):
                node = q.popleft()
                res[level].append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            level +=1
            

        
        return res