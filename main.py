import src.loasmysql as lms
import src.transformmysql as t
import src.scd as s
import src.uploadsql as lts
lms.load_csv_to_mysql("uscustomers","us_customer_data.csv")
df=lms.extract_table(table_name='uscustomers')
a=t.transforms(df)
newa = lms.extract_table(table_name='updatedtable')

b=s.s1(a,newa)
c=s.s2(b)
d=s.s3(df,newa)

a.to_csv('cleaned_data.csv',index=False)

lts.uploadtossms(a)

print("uploaded")