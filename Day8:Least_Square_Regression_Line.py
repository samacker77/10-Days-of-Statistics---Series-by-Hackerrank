from sklearn.linear_model import LinearRegression
import numpy as np
regLine = []
for i in range(5):
    tempList = []
    values = list(map(int,input().split()))
    regLine.append(values)
#print(*regLine)
xList = []
yList = []

for i in regLine:
    #print(i)
    xList.append(i[0])
    yList.append(i[1])
#print(*xList)
#print(*yList)
x = np.asarray(xList).reshape(-1,1)
y = np.asarray(yList).reshape(-1,1)
regressionLine = LinearRegression()
regressionLine.fit(x,y)
print(round(regressionLine.predict([[80]])[0][0],3))
