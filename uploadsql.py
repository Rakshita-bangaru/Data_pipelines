import pandas as pd
from sqlalchemy import create_engine
import urllib
import configparser as cp

def uploadtossms(df):
    config = cp.ConfigParser()
    config.read(r'C:\Users\Rakshita\Downloads\tasks\task4_my_sql\config.ini')
   
    DRIVER = config['ssms']['DRIVER']
    SERVER = config['ssms']['SERVER']
    DATABASE = config['ssms']['DATABASE']
    UID = config['ssms']['UID']
    PWD = config['ssms']['PWD']

    connection_string = (
        f'DRIVER={DRIVER};'
        f'SERVER={SERVER};'
        f'DATABASE={DATABASE};'
        f'UID={UID};'
        f'PWD={PWD};'
    )

    # Encode and build SQLAlchemy engine
    
    encoded = urllib.parse.quote_plus(connection_string)
    engine = create_engine(f'mssql+pyodbc:///?odbc_connect={encoded}')

    df.to_sql(name='scd3_transforms.csv', con=engine, if_exists='replace', index=False)
    

    print("uploaded to ssms")


    