import statistics as st
from scipy import stats
from collections import Counter
N = int(input())
X = list(map(int,input().split()))
print(st.mean(X))
print(st.median(X))
print(stats.mode(X)[0][0])
