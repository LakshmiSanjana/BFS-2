# (https://leetcode.com/problems/cousins-in-binary-tree/)


# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on GFG : YES
# Any problem you faced while coding this : NO


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        pq = deque()

        q.append(root)
        pq.append(None)

        while q:
            len_q = len(q)
            x_found = False
            y_found = False
            x_parent = TreeNode(None)
            y_parent = TreeNode(None)

            for _ in range (len_q):
                curr = q.popleft()
                pqcurr = pq.popleft()

                if curr.val == x:
                    x_parent = pqcurr
                    x_found = True

                if curr.val == y:
                    y_parent = pqcurr
                    y_found = True
                
                if curr.left != None:
                    q.append(curr.left)
                    pq.append(curr)
                
                if curr.right != None:
                    q.append(curr.right)
                    pq.append(curr)
                
            if (x_found and y_found):
                return x_parent != y_parent
        
        #if (x_found or y_found):
         #   return False
        
        return False




###################################

# solution 2: DFS


#####################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __inti__(self):
        self.x_depth = -1
        self.y_depth = -1
        self.x_parent = TreeNode(None)
        self.y_parent = TreeNode(None)
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(root,0,None, x, y)
        return self.x_depth == self.y_depth and self.x_parent != self.y_parent
    
    def dfs(self, root: Optional[TreeNode], depth: int, parent, x: int, y: int):
        # base
        if (root == None):
            return
        # logic

        if (root.val == x):
            self.x_depth = depth 
            self.x_parent = parent
        
        if (root.val == y):
            self.y_depth = depth 
            self.y_parent = parent


        # recursion
        self.dfs(root.left,depth+1,root,x,y) 
        self.dfs(root.right,depth+1,root,x,y)
                
