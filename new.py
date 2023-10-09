import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
from dash import html
from dash import dcc

df=pd.read_csv(r'/Users/hritwik/Desktop/Diwali_SalesAnalysis/SalesData.csv')
df.drop(columns=['Status','unnamed1'],inplace=True)
df.dropna(inplace=True)

# Plotting using plotly

# Gender counts
gender_counts=px.histogram(data_frame=df,x='Gender',text_auto=True)

# Gender vs. Amount
gender_amount=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

gender_amounts=px.bar(data_frame=gender_amount,x='Gender',y='Amount',text_auto=True)

# Age counts

age_counts=px.histogram(data_frame=df,x='Age Group',text_auto=True,color='Gender')

# Age group vs, Amount
age_amount=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

age_amounts=px.bar(data_frame=age_amount,x='Age Group',y='Amount',text_auto=True)

# Marriage counts

marriage_counts=px.histogram(data_frame=df,x='Marital_Status',text_auto=True)

# Marriage vs. amount

marriage_amount=df.groupby(['Marital_Status'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
marriage_amounts=px.bar(data_frame=marriage_amount,x='Marital_Status',y='Amount',text_auto=True)

# State
stata_counts=px.histogram(data_frame=df,x='State',text_auto=True)

# State vs Amount
state_amount=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
state_amounts=px.bar(data_frame=state_amount,x='State',y='Amount',text_auto=True)

# Occupation counts
occupation_counts=px.histogram(data_frame=df,x='Occupation',text_auto=True)

# Occupation vs. Amount
occupation_amount=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
occupation_amounts=px.bar(data_frame=occupation_amount,x='Occupation',y='Amount',text_auto=True)

# Product count
product_counts=px.histogram(data_frame=df,x='Product_Category',text_auto=True)

# Product vs Amount
product_amount=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
product_amounts=px.bar(data_frame=product_amount,x='Product_Category',y='Amount',text_auto=True)

# top 10 orders in reference to product id
product_id_order=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
product_id_order=product_id_order.head(10)
product_id_orders=px.bar(data_frame=product_id_order,x='Product_ID',y='Orders',text_auto=True)

