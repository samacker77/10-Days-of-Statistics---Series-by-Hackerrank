def median(aList):
    if len(aList)%2 == 0:
        e1 = aList[int(len(aList)/2) - 1]
        e2 = aList[int(len(aList)/2)]
        #print(e1,e2)
        med = int((e1 + e2)/2)
        return med
    else:
        med = aList[int(len(aList)/2)]
        return med
n = int(input())
X = list(map(int,input().split()))
F = list(map(int,input().split()))
expandedList = []
for i in range(len(X)):
    #print(i)
    for j in range(F[i]):
        #print(j)
        expandedList.append(X[i])

expandedList.sort()
#print(expandedList)
Q2 = median(expandedList)
if len(expandedList)%2 == 0:
    Q1 = median(expandedList[:int(len(expandedList)/2)])
    Q3 = median(expandedList[int(len(expandedList)/2):])
else:
    Q1 = median(expandedList[:int(len(expandedList)/2)])
    Q3 = median(expandedList[int(len(expandedList)/2+1):])
sol = float(Q3-Q1)
print(round(sol,1))