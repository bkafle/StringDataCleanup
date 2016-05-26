# Import all related modules
import datetime
import csv
import string
import os
import re
import pandas as pd 
import sys 
from pandas import DataFrame, read_csv

print "Import Completed!"

### checking working directory and setting appropriately
os.getcwd()
os.chdir(r'hbs_jschreger_lab/RCS_temp')## this should be the path where you would like to work
## all the required files needed should be present inside the folder
## files that should be present are a) Porthold 1999 to 2014 - Type Code Q.csv b)cusip_abbreviations.csv c)


df_creation_start = datetime.datetime.now()

    # to read the CSV file as Dataframe in pandas
Location = r'hbs_jschreger_lab/Porthold 1999 to 2014 - Type Code Q.csv'
dfB = pd.read_csv(Location,sep=',',error_bad_lines = False, index_col = False, dtype = 'unicode')   
    
    ## Select the attributes you would need for analyzing the data
    ## this will make the file size smaller and processing will be much faster especially
    ## if there are too many unrequired attributes in source data
    
RCS_DF_B = dfB[['Fundid','cusip','security','maturity','coupon','cusip8']]

print "DF was created successfully!"

    ## counting the number of rows and columns in file
Count_Row=dfB.shape[0] #gives number of row count
print "Number of rows/lines in original file: %s"%Count_Row
Count_Col=dfB.shape[1] #gives number of col count
print "Number of columns in original file: %s"%Count_Col
    
    ## Download file as CSV with only few columns from Dataframe
RCS_DF_B.to_csv('hbs_jschreger_lab/Bond.csv',index=False,header = True)

end_df_creation_time = datetime.datetime.now()
df_tt = end_df_creation_time-df_creation_start
    
print "Timetaken to create processing from original file: %s" %(df_tt) 
## Testing - Validate the file is created and present in the location assigned