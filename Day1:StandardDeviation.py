import math
def mean(aList):
    return sum(aList)/len(aList)
N = int(input())
X = list(map(int,input().split()))

mu = mean(X)
squaredDistances = []
for i in X:
    xi = int(pow((i-mu),2))
    squaredDistances.append(xi)
variance = sum(squaredDistances)/len(squaredDistances)
standardDeviation = round(float(math.sqrt(variance)),1)
print(standardDeviation)