Two stocks NSE-Nifty and SGX-Nifty are traded at 2 different places. The price-time series of NSE and SGX follows a normal distribution. There is another stock INDIA.P. The price changes of NSE and INDIA.P move in the same way as NSE and SGX.

The correlation between NSE and SGX is same as between NSE and INDIA.P. Firstly the price-time series of NSE and SGX is converted into return-time series and Pearson's correlation coefficient is calculated using pandas. We then calculate chi-square value which comes out to close to 0 which suggests that the two variables have a linear relationship and therefore we calculate the equation of the regression line that best fits the data of NSE-SGX percentage return s with a degree of freedom of 248.

Given below is the output and the scatter plot of the NSE returns taken on x-axis and SGX returns taken on y-axis.

![image](https://user-images.githubusercontent.com/58564764/126130368-a0993239-7c80-4594-afc6-d1156aea0ed1.png)

![image](https://user-images.githubusercontent.com/58564764/126130439-fb9dec8a-42c2-421d-9152-16e4e72991a6.png)


Next, we need to calculate the daily returns of INDIA.P. We use OLS regression (Ordinary Least Squared) to achieve this in 95% confidence level of the slope of the regression line. The standard error and the point estimate of the slope is calculated using OLS regression and the t-value at 95% confidence level and n-2 degrees of freedom (n = 250 working days) is calculated so that the confidence interval of the slope becomes (point estimate +- t-value*std error).



![image](https://user-images.githubusercontent.com/58564764/126130481-44fac0c7-9e09-41a9-9c54-633fbdff3733.png)

As the slope is now predicted we can use the line-equation y(estimated) = mx + c to calculate the predicted returns of INDIA.P.

![image](https://user-images.githubusercontent.com/58564764/126130458-8eb614d2-a6ec-4490-a348-5c8ad2368581.png)

