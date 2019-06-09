#!/usr/bin/python3

class Tree:
    def __init__(self, num):
        self.noOfNodes = num
        self.root = Node(1)
        self.nodes = []
        for i in range(num):
            self.nodes.append(Node(i+1))

    def addEdge(self, v1, v2):
        if v1 < v2:
            self.nodes[v1-1].addChild(self.nodes[v2-1])
        else:
            self.nodes[v2-1].addChild(self.nodes[v1-1])


class Node:
    def __init__(self, num = None):
        self.num = num
        self.children = []
        self.noOfChildren = 0

    def addChild(self, child = Node()):
        self.children.append(child)
        self.noOfChildren += 1

inp = [int(i) for i in input().split(' ')]

n = inp[0]
m = inp[1]

t = Tree(n)

for i in range(m):
    inp = [int(i) for i in input().split(' ')]
    u = inp[0]
    v = inp[1]

    t.addEdge(u, v)
