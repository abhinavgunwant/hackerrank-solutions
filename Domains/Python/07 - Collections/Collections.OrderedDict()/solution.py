import collections

n = int(input())
products = collections.OrderedDict()

for i in range(n):
    inp = input().split()
    price = int(inp[-1])
    if len(inp) > 2:
        product = ' '.join(inp[0:-1])
    else:
        product = inp[0]
    
    if product in list(products.keys()):
        products[product] += price
    else:
        products[product] = price
        
for key,value in products.items():
            print(key  + ' ' + str(value))