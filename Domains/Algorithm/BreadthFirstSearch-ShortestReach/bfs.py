#!/bin/env/python

t = int(raw_input())
edges = []

class node:
    def __init__(self, idOfNode):
        self.children = []
        self.parent = None
        self.id = idOfNode

    def setParent(self, someNode):
        self.parent = someNode
        return self.parent

    def getId(self):
        return self.id

def shortestReach(arr, start):
    

for i in xrange(t):
    nm = raw_input().split(' ')
    n = int(nm[0])
    m = int(nm[1])

    edges = []

    for j in xrange(m):
        xy = raw_input().split(' ')
        edges.append([int(xy[0], int(xy[1]))])

    start = int(raw_input())
    shortestReach(edges, start)
