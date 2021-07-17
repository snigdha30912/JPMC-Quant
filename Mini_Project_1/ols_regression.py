import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
df = pd.read_csv("return_data.csv",encoding='utf-8')

df['NSE'] = df['NSE'].str.replace("%" , "").astype(float)
df['SGX'] = df['SGX'].str.replace("%" , "").astype(float)

NSE_SGX_corr = df.corr()['NSE']['SGX']
print("Correlation of the daily returns of NSE and SGX = \n",df.corr()['NSE']['SGX'])
INDA_stdv = 1.5
NSE_stdv = np.std(df['NSE'])
print(f"\nStandard Deviation of daily returns of NSE = {NSE_stdv}%")
print(f"\nStandard Deviation of daily returns of INDA.P = {INDA_stdv}%")
mean_NSE = np.mean(df['NSE'])
mean_INDA = 0
print(f"\nMean of daily returns of NSE is {mean_NSE}%")
print("\nMean of daily returns of INDA.P is approximately 0%")
print("\nBy using OLS Regression")
slope = NSE_SGX_corr*(INDA_stdv/NSE_stdv)
intercept = mean_INDA - slope*(mean_NSE)
print("\nEquation of Regression line: ")
print(f"\n y = {slope}x +{intercept}")

#find T critical value
t_value=scipy.stats.t.ppf(q=0.95,df=248)
print(f"\n t value = {t_value}")
p = scipy.stats.t.cdf(t_value, df=248)
print(p)
standard_error = np.sqrt(1-NSE_SGX_corr*NSE_SGX_corr)*(INDA_stdv/100)
print(f"\nstandard_error for slope in ols regression = {standard_error}")
upperBound = slope + t_value*standard_error
lowerBound = slope - t_value*standard_error
print(f"\nconfidence interval for slope = [{upperBound} , {lowerBound}]")

x1 = np.linspace(-1,1,100)
y1 = slope*x1 + intercept
y2 = upperBound*x1 + intercept
y3 = lowerBound*x1+intercept

plt.plot(x1,y1,'-r')
plt.plot(x1,y2,'-b')
plt.plot(x1,y3,'-b')

with open('linear_regression.txt') as file_xy:
    x_data = []
    for l in file_xy:
        row = l.split()
        x_data.append(float(row[0]))
    y_point_estimate = [] 
    y_lowerBound = []
    y_upperBound = []
for i in range(0,len(x_data)):
    y_point_estimate.append(slope*x_data[i]+intercept)
    y_lowerBound.append(slope*x_data[i]+intercept)
    y_upperBound.append(slope*x_data[i]+intercept)
    
x_data1 = np.array(x_data)
y_point_estimate1 = np.array(y_point_estimate)
plt.title('Predicted Returns of INDA.P')
plt.axis([-1, 1, -1, 1])
plt.scatter(x_data1, y_point_estimate1)
plt.show()