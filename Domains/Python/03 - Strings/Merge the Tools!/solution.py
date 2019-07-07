from collections import OrderedDict

def merge_the_tools(string, k):
    start = 0
    strlen = len(string)
    while start < strlen:
        print(''.join(OrderedDict.fromkeys(string[start:start+k])))
        start += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)