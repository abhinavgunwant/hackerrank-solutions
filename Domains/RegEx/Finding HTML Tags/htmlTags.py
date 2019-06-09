import sys
import re

l = 0
j = 0

tagList = []
replaceRegex1 = r'\s*<\s*'
replaceRegex2 = r'\s*>\s*'
replaceRegex3 = r'\s*(\w+\s*[=]+\s*[\"\']+.*[\"\']+)*[;]$'

n = int(raw_input())

for i in xrange(n):
    Test_String = raw_input()
    match = re.findall(r'[<]\s*\w+\s*[^<>]*\s*[>]', Test_String)                #re.findall(r'\s*[<]\s*\w+\s*.*[>]\s*', Test_String)

    # print(Test_String)
    # print(match)

    l = len(match)
    for i in match:
        p = re.sub(replaceRegex1, '', i)
        # print("\nAfter first replace...\n\t"+p)
        p = re.sub(replaceRegex2, ';', p)
        # print("\nAfter second replace...\n\t"+p)
        p = re.sub(replaceRegex3, '', p)
        # print("\nAfter third replace...\n\t"+p)

        # if j < l-1:
        #     p += ';'

        # sys.stdout.write(p)

        j += 1

        if p not in tagList:
            tagList.append(p)

tagList.sort()

l = len(tagList)

for i in xrange(l):
    sys.stdout.write(tagList[i])

    if(i < l-1):
        sys.stdout.write(';')
