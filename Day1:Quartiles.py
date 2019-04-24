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
array = list(map(int,input().split()))
array.sort()
print(array)
Q2 = median(array)
if len(array)%2 == 0:
    #print(array[:int(len(array)/2)])
    Q1 = median(array[:int(len(array)/2)])
    #print(array[int(len(array)/2):])
    Q3 = median(array[int(len(array)/2):])
else:
    #print(array[:int(array.index(Q2))])
    Q1 = median(array[:int(array.index(Q2))])
    #print(array[int(array.index(Q2)):])
    Q3 = median(array[int(len(array)/2+1):])

print(Q1)
print(Q2)
print(Q3)


