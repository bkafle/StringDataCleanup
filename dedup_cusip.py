## This will dedup the original file-'MasterCusip' file so that it is relatively
## faster for processing the Merge.
## The original 'MasterCusip' have duplicates and we could remove them so that we can achieve some gain in processing time
import pandas as pd
import csv

## reading the file
file_cusip = r'hbs_jschreger_lab/WORK_CONSOLIDATED_CUSIPS.csv'

## creating a DF
toclean_cusip = pd.read_csv(file_cusip,sep=',',error_bad_lines = False, index_col = False, dtype = 'unicode')
deduped = toclean_cusip.drop_duplicates(['Alpha Description 1'])## removing duplicates

## sort the file in ascending order
Sorted_cusip = deduped.sort(['CUSIP Issuer Number'],ascending = True)

##Counting the number or records in the file
Count_Row_cusip=Sorted_cusip.shape[0] #gives number of row count
print "Number of rows/lines in Cusipfile: %s"%Count_Row_cusip


##exporting the Dataframe to csv file 
Sorted_cusip.to_csv('hbs_jschreger_lab/MasterCusip_Deduped.csv',index=False,header = True)