import pandas as pd
order_items_df= pd.read_csv(r"C:\Users\tatty\OneDrive\Desktop\DATA ENGINEERING PROJECT\DATA\order_items.csv")
order_items_df = order_items_df[
    (order_items_df['quantity'] > 0) &
    (order_items_df['unit_price'] > 0)
]
order_items_df = order_items_df.reset_index(drop=True)

print(order_items_df)