#!/bin/python3

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        totalHeight = self.height(root)
        self.traversal = []

        for i in range(1, totalHeight + 1):
            self.printLevel(root, i)

        print(' '.join(map(str, self.traversal)))
    
    def printLevel(self, root, level):
        if root == None:
            return
        
        if level == 1:
            self.traversal.append(root.data)
        elif level > 1:
            self.printLevel(root.left, level - 1)
            self.printLevel(root.right, level - 1)

    def height(self, root):
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1

        return 1 + max([self.height(root.left), self.height(root.right)])

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
