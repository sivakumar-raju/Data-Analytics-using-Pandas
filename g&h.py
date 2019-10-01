import pandas as pd
df=pd.read_csv('D:\\Super_store_purchase.csv')
df['Total']=df.iloc[:,-3:].sum(axis=1)
#for city A
am=df[df['City_Category']=='A']
am=am[am['Gender']=='M']
a_male=am['Total'].sum(axis=0)
af=df[df['City_Category']=='A']
af=af[af['Gender']=='F']
a_fmale=af['Total'].sum(axis=0)
#for city B
bm=df[df['City_Category']=='B']
bm=bm[bm['Gender']=='M']
b_male=bm['Total'].sum(axis=0)
bf=df[df['City_Category']=='B']
bf=bf[bf['Gender']=='F']
b_fmale=bf['Total'].sum(axis=0)
#For city c
cm=df[df['City_Category']=='C']
cm=cm[cm['Gender']=='M']
c_male=cm['Total'].sum(axis=0)
cf=df[df['City_Category']=='C']
cf=cf[cf['Gender']=='F']
c_fmale=cf['Total'].sum(axis=0)
#apllying conditions
if(a_male>a_fmale):
    print("Male are frequent customers in City A")
else:
    print("Female are frequent customers in City A")
if(b_male>b_fmale):
    print("Male are frequent customers in City B")
else:
    print("Female are frequent customers in City B")
if(c_male>c_fmale):
    print("Male are frequent customers in City C")
else:
    print("Female are frequent customers in City C")
# Frequent male shoppers
x= max(a_male,b_male,c_male)
if (a_male==x):
    print("male from A shop more")
elif (b_male==x):
    print("male from B shop more")
else:
    print("male from C shop more")
