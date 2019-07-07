cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    if n == 0:
        return []
    fib = []
    fib.append(0)
    num = 1
    for i in range(n-1):
        fib.append(num)
        num += fib[-2]
        
    return fib
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))