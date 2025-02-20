#  https://leetcode.com/problems/binary-tree-right-side-view/

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root == None:
            return [] 
        
        q = deque()
        q.append(root)
        res = []
        while q:
            len_q = len(q)
            for i in range(len_q):
                curr = q.popleft()

                if i == len_q - 1:
                    res.append(curr.val)

                if curr.left != None:
                    q.append(curr.left)
                
                if curr.right != None:
                    q.append(curr.right)
            
            #level += 1
        return res
                

# solution 2: DFS# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        if root == None:
            return self.result
        self.dfs(root,0,self.result)
        return self.result
    
    def dfs(self, root: Optional[TreeNode], level, result) -> List[int]:
        if root == None:
            return self.result

        if ( len(self.result) == level):
            self.result.append(root.val)
        
        self.dfs(root.right, level+1, self.result)
        self.dfs(root.left,level+1, self.result)


###############

# going left first nd then right

#############


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        if root == None:
            return self.result
        self.dfs(root,0,self.result)
        return self.result
    
    def dfs(self, root: Optional[TreeNode], level, result) -> List[int]:
        if root == None:
            return self.result

        if ( len(self.result) == level):
            self.result.append(root.val)
        else:
            self.result[level] = root.val
        
        self.dfs(root.left, level+1, self.result)
        self.dfs(root.right,level+1, self.result)

