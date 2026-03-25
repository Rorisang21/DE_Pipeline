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

valid_customer_ids= orders_df ['customer_id'].unique()
orders_df = orders_df[orders_df['customer_id'].isin(valid_customer_ids)]
#Reset index 
orders_df = orders_df.reset_index(drop=True)

# View cleaned data
print(orders_df)
print(orders_df['customer_id'].dtype)
