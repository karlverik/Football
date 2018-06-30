import numpy as np
from scipy import stats

file = open('AD.txt',encoding='utf-8').read()
dict = eval(file)

a =dict['日本'][0]*dict['塞内加尔'][1]
b =dict['日本'][1]*dict['塞内加尔'][0]

k5 = 5
X4 = np.arange(0,k5+1,1)

f = stats.poisson.pmf(X4,a)
e = stats.poisson.pmf(X4,b)
p = 0
for i in range(0,5):
    m = f[i]*e[i:5]
    for n in m:
        p += n
print(p)
print(f)
print(e)
#0.42996443476756285 0.23303253481725883
#0.666151311842898

#0.10453986740141427



