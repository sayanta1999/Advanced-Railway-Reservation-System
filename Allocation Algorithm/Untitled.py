#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('data.csv')
print(df.shape)
df = df.sort_values('pnr',ascending=True)
df.drop_duplicates(['pnr'],inplace=True)
print(df.shape)
print(df.columns)
#type(df['date'][0])


# In[258]:


L,U,M,SL,SU = (36,36,36,36,36)
# Seat numbers
lower=[i for i in range(1,181) if i%5==1]
l=0
upper=[i for i in range(1,181) if i%5==2]
u=0
middle=[i for i in range(1,181) if i%5==3]
m=0
side_lower=[i for i in range(1,181) if i%5==4]
sl=0
side_upper=[i for i in range(1,181) if i%5==0]
su=0


# In[259]:


temp = df.sort_values(['date','time'])
temp.shape


# In[260]:


total_seats=180
no_of_bookings = temp.shape[0]
if total_seats < no_of_bookings:
    df = temp.iloc[:total_seats,:]
    waiting_list = temp.iloc[total_seats:,:]
else:
    df = temp.iloc[:no_of_bookings,:]
    waiting_list = []

print(df.shape)
if(len(waiting_list)!=0):
    print(waiting_list.shape)


# In[261]:



preg_women = df[df['pregnant']==1]
df_dropped=df.drop(df[df['pregnant']==1].index)

#print(df_dropped.shape)
#print(preg_women.shape)

senior_citizen_M = df_dropped[(df_dropped['age'] >= 60) & (df_dropped['gender']=='M')]
df_dropped=df_dropped.drop(df_dropped[(df_dropped['age'] >= 60) & (df_dropped['gender']=='M')].index)

#print(df_dropped.shape)
#print(senior_citizen_M.shape)

senior_citizen_F = df_dropped[(df_dropped['age'] >= 40) & (df_dropped['gender']=='F')]
df_dropped=df_dropped.drop(df_dropped[(df_dropped['age'] >= 40) & (df_dropped['gender']=='F')].index)

#print(df_dropped.shape)
#print(senior_citizen_F.shape)

rest = df_dropped

#print(df_dropped.shape)
#print(rest.shape)


# In[262]:


# Final Seats allocation
seat_no=[]
pnr=[]
berth=[]
gender=[]
age=[]
pregnant=[]


# In[263]:


def allocate_special(category,l,sl,m,u,su):
    for i in range(len(category)):
        if(l<L):
            seat_no.append(lower[l])
            berth.append('L')
            l=l+1
        elif(sl<SL):
            seat_no.append(side_lower[sl])
            berth.append('SL')
            sl=sl+1
        elif(m<M):
            seat_no.append(middle[m])
            berth.append('M')
            m=m+1
        elif(u<U):
            seat_no.append(upper[u])
            berth.append('U')
            u=u+1
        else:
            seat_no.append(side_upper[su])
            berth.append('SU')
            su=su+1

        pnr.append(category.iloc[i,0])
        gender.append(category.iloc[i,1])
        age.append(category.iloc[i,3])
        pregnant.append(category.iloc[i,2])
        
    return (l,sl,m,u,su)

def allocate_normal(category,l,sl,m,u,su):
    for i in range(len(category)):
        if(category.iloc[i,6]=='L' and l<L):
            seat_no.append(lower[l])
            berth.append('L')
            l=l+1
        elif(category.iloc[i,6]=='M' and m<M):
            seat_no.append(middle[m])
            berth.append('M')
            m=m+1
        elif(category.iloc[i,6]=='SL' and sl<SL):
            seat_no.append(side_lower[sl])
            berth.append('SL')
            sl=sl+1
        elif(category.iloc[i,6]=='U' and u<U):
            seat_no.append(upper[u])
            berth.append('U')
            u=u+1
        elif(category.iloc[i,6]=='SU' and su<SU):
            seat_no.append(side_upper[su])
            berth.append('SU')
            su=su+1
        else:
            if(l<L):
                seat_no.append(lower[l])
                berth.append('L')
                l=l+1
            elif(sl<SL):
                seat_no.append(side_lower[sl])
                berth.append('SL')
                sl=sl+1
            elif(m<M):
                seat_no.append(middle[m])
                berth.append('M')
                m=m+1
            elif(u<U):
                seat_no.append(upper[u])
                berth.append('U')
                u=u+1
            else:
                seat_no.append(side_upper[su])
                berth.append('SU')
                su=su+1

        pnr.append(category.iloc[i,0])
        gender.append(category.iloc[i,1])
        age.append(category.iloc[i,3])
        pregnant.append(category.iloc[i,2])
        
    return (l,sl,m,u,su)


# In[264]:


#For pregnant women
l,sl,m,u,su=allocate_special(preg_women,l,sl,m,u,su)


# In[265]:


# For senior citizens(Female)
l,sl,m,u,su=allocate_special(senior_citizen_F,l,sl,m,u,su)

# In[266]:


# For senior citizens(Male)
l,sl,m,u,su=allocate_special(senior_citizen_M,l,sl,m,u,su)


# In[267]:


# For rest
l,sl,m,u,su=allocate_normal(rest,l,sl,m,u,su)


# In[270]:


from sklearn.utils import shuffle

seat_allocated = pd.DataFrame(list(zip(pnr,seat_no,berth,gender,age,pregnant)),columns=['pnr','seat_no','berth','gender','age','pregnant'])
seat_allocated = shuffle(seat_allocated)
seat_allocated.to_csv("confirmed_list.csv",index=False)
print(seat_allocated)


# In[269]:


print(waiting_list)
waiting_list.to_csv('waiting_list.csv',index=False)

