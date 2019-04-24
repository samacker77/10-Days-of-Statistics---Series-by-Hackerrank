N = int(input())
X = list(map(int,input().split()))
W = list(map(int,input().split()))
weightedSum = sum(W)
pweight = [(i*j) for i,j in zip(X,W)]
print(round(sum(pweight)/weightedSum,1))
