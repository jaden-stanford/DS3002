# ETL Data Processor
# Instructions: author a segment of an ETL pipeline that will ingest or process raw data
# Data processor should be able to ingest a pre-defined data source and perform at least 3 of:
# 1) fetch/download remote data by URL, S3 key, or ingest a local file
# 2) convert general format of data source (from TSV to CSV, CSV to JSON, JSON to SQL, etc)
# 3) Modify the number of columns from the source to the destination, reducing or adding columns
# 4) Converted/new file should be written to disk, or pushed to S3, or written to SQL database
# 5) Generate a brief summary of data file ingestion including number of records and number of columns
# Processor should produce informative errors should it be unable to complete operation

# importing required modules
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from sqlalchemy import create_engine


# authenticating kaggle api
api = KaggleApi()
api.authenticate()

# downloading dataset from kaggle.com/pratmo/dominos-pizza-stock-data
# This data set contains the Domino's stock market data for the past two years
api.dataset_download_file('pratmo/dominos-pizza-stock-data',
                          file_name='dominos_stock_data.csv',
                          path='./')

# reading csv data into DataFrame
dominos_df = pd.read_csv('Dominos_Stock_Data.csv')


# Adding a column 'Range,' that is the difference between the high stock price and low stock price of the day
dominos_df.insert(5, "Range", dominos_df['High'] - dominos_df['Low'], True)

# Printing details of data frame
print('The data set has',len(dominos_df) , 'rows')
print('The data set has',len(dominos_df.columns), 'columns')
print('')
print('A summary of the data table:')
print(dominos_df.info())
print('')
print('The first 5 rows of the dataset:')
print(dominos_df.head())

# Writing data frame to mysql
hostname = "localhost"
dbname = "dataproject1"
uname = "root"
pwd = "Sq!sanian4144"

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# Convert dataframe to sql table called dominos
dominos_df.to_sql('dominos', engine, index=False)
