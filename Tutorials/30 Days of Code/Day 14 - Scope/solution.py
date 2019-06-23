class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        self.maximumDifference = 0

        for i in self.__elements:
            for j in self.__elements:
                if i == j:
                    continue

                difference = abs(i - j)

                if difference > self.maximumDifference:
                    self.maximumDifference = difference

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)