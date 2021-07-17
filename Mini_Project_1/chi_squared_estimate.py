import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
import scipy.integrate as si
df = pd.read_csv("return_data.csv",encoding='utf-8')

df['NSE'] = df['NSE'].str.replace("%" , "").astype(float)
df['SGX'] = df['SGX'].str.replace("%" , "").astype(float)
df.plot(kind='scatter',x='NSE',y='SGX')
with open('linear_regression.txt') as file_xy:
    x,y = [],[]
    for l in file_xy:
        row = l.split()
        x.append(float(row[0]))
        y.append(float(row[1]))

sumx = 0
sumy = 0
sumx2 = 0
sumxy = 0


for i in range(0,len(x)):
    sumx = sumx + x[i]
    sumx2 = sumx2 + x[i]*x[i]
    sumy = sumy + y[i]
    sumxy = sumxy + x[i]*y[i]

a1 = (len(x)*sumxy - sumx*sumy)/ (len(x)*sumx2 - sumx*sumx)
a2 = (sumy- a1*sumx)/len(x)

print (sumxy, sumx, sumx2, sumy)
print(f"Equation of line is y = {a1}x + {a2}")

x1 = np.linspace(-5,5,100)
y1 = a1*x1+a2
plt.plot(x1,y1,'-r')

plt.show()
std_dev= np.std(y)

chisqr = 0

for i in  range(0,len(x)):
    chisqr = (np.square(y[i] - (a1*x[i] + a2)))/np.square(std_dev)
    chisqr += chisqr

print(f"The value of chi-square is {chisqr}")

df=200
def distribution(x,k):
    return np.power(x,k/2-1)*np.exp(-1*x/2)/(np.power(2,k/2)*ss.gamma(k/2))
I=si.quad(distribution,chisqr,np.inf,args=df)
print(f"P-value and error in calculation is {I}")