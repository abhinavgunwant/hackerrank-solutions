n = int(input())
s = set(map(int, input().split())) 
N = int(input())

for i in range(N):
    command = input().split()
    cmd = command[0]
    try:
        num = int(command[1])
    except(IndexError):
        num = None
        
    if cmd == 'pop':
        s.pop()
    elif cmd == 'remove':
        s.remove(num)
    elif cmd == 'discard':
        s.discard(num)
        
print(sum(s))