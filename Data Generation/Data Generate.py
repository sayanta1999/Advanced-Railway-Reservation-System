#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Generating Dataset

import numpy as np
import random
#total_seats = random.randint(180,360)
total_seats = 180
print("Total Seats: "+str(total_seats))
no_of_bookings = random.randint(60,500)
#no_of_bookings = 500
print("No of bookings: "+str(no_of_bookings))


# In[18]:


import string
import datetime

pnr=[]
gender=[]
pregnant=[]
age=[]
date=[]
time=[]
priority=[]
source=[]
destination=[]

station = ['1.A','2.B','3.C','4.D','5.E','6.F','7.G','8.H','9.I','10.J','11.K','12.L','13.M','14.N','15.O','16.P','17.Q','18.R','19.S','20.T','21.U','22.V','23.W','24.X','25.Y','26.Z']

for i in range(no_of_bookings):
    pnr.append(random.randint(1000,9999))
    temp=random.randint(0,1)
    if(temp==0):
        gender.append('F')
        temp1=random.randint(0,1)
        if(temp1==0):
            pregnant.append(0)
            age.append(random.randint(6,80))
        else:
            pregnant.append(1)
            age.append(random.randint(20,50))
    else:
        gender.append('M')
        pregnant.append(0)
        age.append(random.randint(6,80))
    
    date.append(datetime.date(2020, random.randint(1,2),random.randint(1,28)))
    time.append("13:05")
    priority.append(random.choice(['L','U','M','SU','SL']))
    temp = random.choice(station[:-1])
    source.append(temp)
    index = random.choice(np.arange(station.index(temp)+1,len(station)))
    destination.append(station[index])


# In[19]:


import pandas as pd
df = pd.DataFrame(list(zip(pnr,gender,pregnant,age,date,time,priority,source,destination)),columns=["pnr","gender","pregnant","age","date","time","preference",'source','destination'])
df.shape
df = df.sort_values(['pnr'],ascending=True)
df.drop_duplicates(['pnr'],inplace=True)
df.to_csv('data.csv',index=False)

