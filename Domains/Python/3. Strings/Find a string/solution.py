import re

def count_substring(string, sub_string):
    count = 0
    sslen = len(sub_string)
    for i in range(len(string) - sslen + 1):
        if string[i:i+sslen] == sub_string:
            count += 1
    
    #return len([ i for i in re.finditer(sub_string, string)])
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)