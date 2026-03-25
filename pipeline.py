import pandas as pd
customer_df= pd.read_csv(r"C:\Users\tatty\OneDrive\Desktop\DATA ENGINEERING PROJECT\DATA\Customers - Sheet1.csv")

customer_df ['email']= customer_df ['email'].str.lower()

#change the format of the signup date
customer_df['signup_date'] = pd.to_datetime(customer_df['signup_date'])

#keeping the earliest date firts 
customer_df = customer_df.sort_values(by=['signup_date', 'email'])

#dropping the duplicates
customer_df = customer_df.drop_duplicates(subset='email', keep='first')
#check email requiremnts 
customer_df = customer_df[
    customer_df['email'].str.contains('@') & 
    customer_df['email'].str.contains('\.')
]
customer_df = customer_df.reset_index(drop=True)
print (customer_df)


#ODER ITEMS 

order_items_df= pd.read_csv(r"C:\Users\tatty\OneDrive\Desktop\DATA ENGINEERING PROJECT\DATA\order_items.csv")
order_items_df = order_items_df[
    (order_items_df['quantity'] > 0) &
    (order_items_df['unit_price'] > 0)
]
order_items_df = order_items_df.reset_index(drop=True)

print(order_items_df)

#ORDERS

import pandas as pd


orders_df = pd.read_json(
    r"C:\Users\tatty\OneDrive\Desktop\DATA ENGINEERING PROJECT\DATA\oders.jsonl",
    lines=True
)


orders_df['status'] = orders_df['status'].str.lower()

#changed processing to placed
orders_df['status'] = orders_df['status'].replace('processing', 'placed')

#only Kept the statues that we needed 
valid_status = ['placed', 'shipped', 'cancelled', 'refunded']
orders_df = orders_df[orders_df['status'].isin(valid_status)]

#To convert to datetime in UTC (Assisted by AI)
orders_df['order_ts'] = pd.to_datetime(orders_df['order_ts'], errors='coerce', utc=True)

#removed inavlid timestamps
orders_df = orders_df[orders_df['order_ts'].notnull()]

valid_customer_ids= customer_df ['customer_id'].unique()
orders_df = orders_df[orders_df['customer_id'].isin(valid_customer_ids)]
#Reset index 
orders_df = orders_df.reset_index(drop=True)

valid_order_ids = orders_df['order_id'].unique()

order_items_df = order_items_df[
    order_items_df['order_id'].isin(valid_order_ids)
]

order_items_df = order_items_df.reset_index(drop=True)


print(orders_df)

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:Danamate21.@localhost:5432/postgres"
)

customer_df.to_sql('customers',engine, if_exists='append',index=False)
orders_df.to_sql('orders',engine,if_exists='append',index=False)
order_items_df.to_sql('order_items',engine,if_exists='append',index=False)
print('Data is loaded')