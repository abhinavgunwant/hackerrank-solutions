import math

# Get n
n = int(input())

# Get X
X = list(map(int, input().split()))

mean = sum(X) / n

#---- Calculate squared difference from mean ----
sDiff = []
for i in X:
    diff = i - mean     # difference
    diff *= diff        # squared

    sDiff.append(diff)

# Calculate Standard Deviation and round off to 
# nearest 1 decimal place
stdDeviation = round( math.sqrt(sum(sDiff) / n) , 1)
print(stdDeviation)