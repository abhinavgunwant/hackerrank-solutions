import collections

n = int(input())

deq = collections.deque()

for i in range(n):
    inp = input().split()
    try:
        if inp[0] == 'append':
            deq.append(int(inp[1]))
        elif inp[0] == 'appendleft':
            deq.appendleft(int(inp[1]))
        elif inp[0] == 'pop':
            deq.pop()
        else:
            deq.popleft()
    except(IndexError):
        continue

print(' '.join(list(map(str, deq))))