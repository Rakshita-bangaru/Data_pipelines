import pandas as pd
def s1(df,newa):
    updateddf=df.merge(newa[['customer_id','email']],on='customer_id',how='left',suffixes=('','_new'))
    updateddf['email']=updateddf['email_new'].combine_first(updateddf['email'])
    updateddf.drop(columns=['email_new'],inplace=True)
    return updateddf
def s2(df):
    a={
        'customer_id':2,
        'email':'rakshitha@gamil.com'
    }
    b=df.loc[df['customer_id']==a['customer_id']].copy()
    b['email']=a['email']
    df=pd.concat([df,b],axis=0)
    return df
def s3(df,newa):
    updateddf=df.merge(newa[['customer_id','email']],on='customer_id',how='left',suffixes=('','_new'))
    return updateddf



