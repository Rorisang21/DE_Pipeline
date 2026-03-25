import pandas as pd
customer_df= pd.read_csv(r"C:\Users\tatty\OneDrive\Desktop\DATA ENGINEERING PROJECT\DATA\Customers - Sheet1.csv")
 # transforimg the emails to lowercase 
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
