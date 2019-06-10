import collections

for _ in range(int(input())):
    n = input()
    sideLens = collections.deque(list(map(int, input().split())))
    
    solved = True
    
    left = sideLens.popleft()
    right = sideLens.pop()
    
    below = -1
    
    if left >= right:
        below = left
        left = None
    else:
        below = right
        right = None

    while len(sideLens) > 0:
        if left == None:
            left = sideLens.popleft()
        if right == None:
            right = sideLens.pop()
        
        if left <= below and left >= right:
            below = left
            left = None
        elif right <= below and right >= left:
            below = right
            right = None
        else:
            solved = False
            break
    
    if solved:
        print('Yes')
    else:
        print('No')