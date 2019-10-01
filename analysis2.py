import pandas as pd
import csv
pd.read_csv("Super_store_purchase.csv")
dataframe = pd.DataFrame(pd.read_csv("Super_store_purchase.csv"), columns = ['Product_ID ', 'Gender', 'Age', 'Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Product_Category_1','Product_Category_2','Product_Category_3']) 



#products on demand:"a"
rslt_df = dataframe[dataframe['Age'] == "36-45"]
rslt_df = rslt_df[rslt_df['Gender']=="F"] 
pr1=rslt_df['Product_Category_1'].sum()
pr2=rslt_df['Product_Category_2'].sum()
pr3=rslt_df['Product_Category_3'].sum()
a=max(pr1,pr2,pr3)
if a==pr1:
    print("The product which are high in demand middle aged females : Product_Category_1")
if a==pr2:
    print("The product which are high in demand middle aged females : Product_Category_2")
if a==pr3:
    print("The product which are high in demand middle aged females : Product_Category_3")    

import pandas as pd
import csv
pd.read_csv("Super_store_purchase.csv")
dataframe = pd.DataFrame(pd.read_csv("Super_store_purchase.csv"), columns = ['Product_ID ', 'Gender', 'Age', 'Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Product_Category_1','Product_Category_2','Product_Category_3']) 



#Senior citizen:"f"
rslt_df = dataframe[dataframe['Age'] == "55+"]
pr1=rslt_df['Product_Category_1'].sum()
pr2=rslt_df['Product_Category_2'].sum()
pr3=rslt_df['Product_Category_3'].sum()
a=min(pr1,pr2,pr3)
if a==pr1:
    print("The product which are not interested by the Senior : Product_Category_1")
if a==pr2:
    print("The product which are not interested by the Senior : Product_Category_2")
if a==pr3:
    print("The product which are not interested by the Senior : Product_Category_3")    


#Not intersted by females: "d"
rslt_df = rslt_df[rslt_df['Gender']=="F"] 
pr1=rslt_df['Product_Category_1'].sum()
pr2=rslt_df['Product_Category_2'].sum()
pr3=rslt_df['Product_Category_3'].sum()
a=min(pr1,pr2,pr3)
if a==pr1:
    print("The product which are not interested by females : Product_Category_1")
if a==pr2:
    print("The product which are not interested by females : Product_Category_2")
if a==pr3:
    print("The product which are not interested by females : Product_Category_3")    





