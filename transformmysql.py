import pandas as pd
def transforms(df):
    df=df.drop_duplicates()
    df=df.sort_values(by='registration_date',ascending=True)
    df['customer_status']=df.groupby('loyalty_status')['customer_id'].transform('count')
    return df

   