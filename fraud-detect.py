
#https://github.com/fcamuz/fraud-detection-for-mobile-transactions
import os
import math
from numpy import * 
import numpy as np
import pandas as pd
import random
import seaborn as sns #for visualization
import matplotlib.pyplot as plt #for visualization
#Load data 
data=pd.read_csv('paysim.csv')
#Check if there is anu null values
data.isna().sum().sum()

#check for duplicate values
data.duplicated(keep='first').any()


# Filter data by the labels. Safe and Fraud transaction
safe = data[data['isFraud']==0]
fraud = data[data['isFraud']==1]
#See the frequency of the transactions for each class on the same plot.


# sns.displot(tips_data["total_bill"], kde = False)
# plt.title("Histogram for Total Bill")
# plt.show()

plt.figure(figsize=(10, 3))
sns.displot(safe.step, label="Safe Transaction")
sns.displot(fraud.step, label='Fraud Transaction')
plt.xlabel('Hour')
plt.ylabel('Number of Transactions')
plt.title('Distribution of Transactions over the Time')
plt.legend()
print(plt)


#just use small portion of data to scatterplot the transaction happens every hour and their amount. 
smalldata=data.sample(n=100000, random_state=1)
smalldata=smalldata.sort_index()
smalldata=smalldata.reset_index(drop=True)

#plot the small data
plt.figure(figsize=(18,6))
plt.ylim(0, 10000000)
plt.title('Hourly Transaction Amounts')
ax = sns.scatterplot(x="step", y="amount", hue="isFraud",
                     data=smalldata)



#The hourly amount of al fraud transactions
plt.figure(figsize=(18,6))
plt.ylim(0, 10000000)
plt.title('Hourly Fraud Transaction Amounts')
ax = sns.scatterplot(x="step", y="amount", color='orange',
                     data=fraud)
# Fraud transactions does not show that 
# significant pattern like safe ones in 
# terms of number of accurance. They happen e
# very hour almast in the same frequency. T
# here are more fraud transactions in low amounts 
# and less in high amount. But the pattern does not 
# change time to time.



