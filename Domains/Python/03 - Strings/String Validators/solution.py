s = input()

alnum = False
alpha = False
digit = False
lower = False
upper = False

for i in s:
    if i.isalnum():
        alnum = True
    
    if i.isalpha():
        alpha = True
    
    if i.isdigit():
        digit = True
        
    if i.islower():
        lower = True
        
    if i.isupper():
        upper = True
    
    if alnum and alpha and digit and lower and upper:
        break
        
print(alnum)
print(alpha)
print(digit)
print(lower)