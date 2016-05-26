starttime_dedup = datetime.datetime.now()
print "Process Start Time for De-duplication: %s" %starttime_dedup

## this piece of code will de-dup the records based on 'RCS_SECURITY' field
import pandas as pd
import csv
filein= r'hbs_jschreger_lab/Bond_RCS_Cols.csv'
toclean = pd.read_csv(filein,sep=',',error_bad_lines = False, index_col = False, dtype = 'unicode')
deduped = toclean.drop_duplicates(['RCS_SECURITY'])


## sort the file on RCS_SECURITY in ascending order
Sorted = deduped.sort(['RCS_SECURITY'],ascending = True)

##exporting the Dataframe to csv file 
Sorted.to_csv('hbs_jschreger_lab/Bond_Sorted.csv',index=False,header = True)

## counting the number of rows for deduped file
Count_Row_deduped=deduped.shape[0] #gives number of row count
print "Number of rows/lines in original file: %s"%Count_Row_deduped


end_time_dedup = datetime.datetime.now()
print "Process Ended for Deduplication: %s" %end_time_dedup

dedup_tt = end_time_dedup - starttime_dedup
print "Timetaken to for dedup process: %s" %(dedup_tt)