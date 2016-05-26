## this code formats the date of MasterCusip to align with the MaturityDate present in DataFile
## this code was written to see if maturity date and Coupon in MasterCusip might come in handy for secondary lookups
import csv
import os
import datetime

starttime_df = datetime.datetime.now()
print "Process Start Time: %s" %starttime_df

inputfile = ('Jesse_Project/WORK_CONSOLIDATED_CUSIPS.csv')
outputfile = ('Jesse_Project/Master_Cusip_Dateformat.csv')

with open(inputfile, 'rb') as inFile, open(outputfile, 'wb') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)
    
    # process the date and copy into a new file
    for row in r:
        if row[6] != " ":
            try:
                rcs_date = datetime.datetime.strptime(row[6],'%Y%m%d').strftime('%m/%d/%Y')
            except:
                rcs_date = row[6]
        else:
            rcs_date = row[6]
                
        row[6] = rcs_date
        w.writerow(row)


end_time_dtformat = datetime.datetime.now()
print "Process Ended: %s" %(end_time_dtformat - starttime_df)