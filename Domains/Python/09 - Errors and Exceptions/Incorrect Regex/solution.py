import re

for i in range(int(input())):
    pat = input()
    try:
        re.compile(pat)
    except re.error:
        print(False)
        continue
    print(True)