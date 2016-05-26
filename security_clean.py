# This code takes a csv input file and reads line by line.
# It adds five new columns based on columns in input file, and writes a new file with added columns
# Added Column 1 - 'RCS_CUSIP6' - fills with CUSIP present in input file
# Added Column 2 - 'RCS_CUSIP8' - fills with CUSIP8 present in input file
# Added Column 3 - 'RCS_COUPON' - fills with COUPON from security if COUPON is not present in input file
# ADded Column 4 -  'RCS_DATE' - fills with MATURITY_DATE from secrity if MATURITY_DATE is not present in input file
# Added Column 5 - 'RCS_SECURITY' - this is the stripped SECURITY without number and date on it

"""
****************************************************************************
The below code with filter Number and Date as below
a) If data = 'RCS 10/12/2016 7.5% ya' then RCS_SECURITY = 'RCS YA'; RCS_MATURITY = '10/12/2016';RCS_COUPON = '7.5%'
b) if data = 'RCS YAHO 20101212 768' then RCS_SECURITY = 'RCS YAHO';RCS_MATURITY = '12/12/2010'
c) if data = '679 YAHO 5477.32 RCS' then RCS_SECURITY = 'YAHO 5477.32 RCS'

*****************************************************************************
"""
## Display Starttime
import datetime
starttime_clean = datetime.datetime.now()
print "Process Start Time: %s" %starttime_clean

## importing library for reading CSV file 
import csv
import re  ## for Regular Expression

with open('hbs_jschreger_lab/Bond.csv', 'r') as infile:  
     with open('hbs_jschreger_lab/Bond_RCS_Cols.csv', 'wb') as outfile:
         reader = csv.reader(infile, delimiter=',')
         writer = csv.writer(outfile, delimiter=',')
         
            
         next(infile,None)## skip the old header
            
         ## write new header as below
         writer.writerow(['FUNDID','RCS_SECURITY','RCS_COUPON','RCS_MATURITY','RCS_CUSIP6','RCS_CUSIP8','CUSIP',
                'SECURITY','MATURITY','COUPON','CUSIP8'])
         
         ## process a row at a time line by line   
         for row in reader:
                
                rcs_cusip6 = row[1] # adding RCS_CUSIP6 a new column same as present in input file for now
                rcs_cusip8 = row[5] # adding RCS_cusip8 a new column same as present in input file for now
                
                ## related to extracting Security after removing numbers and date
                rcs_security_rstrip = row[2].rstrip('$+#?*@-0123456789.,%/ )( ') # removing trailing numbers and date from right side
                rcs_security_lstrip = rcs_security_rstrip.lstrip('$+#?*@-0123456789.,%/ )( ') # strip left side as well 
                rcs_security = rcs_security_lstrip.upper() ## convert security into UpperCase so that it's easy for comparison
                
                
                ## related to extracting coupon   
                if '%' in row[2]: ## if coupon is not present and security has % then
                    rcs_coupon1 = re.findall(r"[-+]?\d*\.[0-9]+%|[0-9]+%",row[2])
                    if not rcs_coupon1:
                        rcs_coupon = " ".join(str(c) for c in rcs_coupon1)
                    else:
                        rcs_coupon = str(rcs_coupon1[0])  
                        rcs_coupon = rcs_coupon.rstrip('% ')  ## removing % from coupon to have only number
                                            
                else:
                    rcs_coupon = row[4]  ## populates coupon with exiting values  if above conditions don't match
                              
                ## this part will populate MATRUITY DATE if already not present and present in Security
                if '/' in row[3] or  '-' in row[3]:  
                    rcs_date = row[3]
                    
                else:          
                    if '/' in row[2]:
                        
                        d = re.findall('(\d+[/]\d+[/]\d+)',row[2])
                        if not d:
                            rcs_date = " ".join(str(c) for c in d)
                        else:
                        ## handling dates in different format and converting to mm/dd/yyyy format
                            date = str(d[0])
                            try:
                                rcs_date = datetime.datetime.strptime(date,'%m-%d-%y').strftime('%m/%d/%Y')
                            except:
                                try:
                                    rcs_date = datetime.datetime.strptime(date,'%y-%m-%d').strftime('%m/%d/%Y')
                                except:
                                    rcs_date = date
                        
                    elif '-' in row[2]:
                        d = re.findall('(\d+[-]\d+[-]\d+)',row[2])
                        if not d:
                            rcs_date = " ".join(str(c) for c in d)
                        else:
                            date = str(d[0])
                        
                            try:
                                rcs_date = datetime.datetime.strptime(date,'%m-%d-%Y').strftime('%m/%d/%Y')
                            except:
                                try:
                                    rcs_date = datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%m/%d/%Y')
                                except:
                                    rcs_date = date
                  
                    else:
                        d = re.findall('(\d{4}\d{2}\d{2})',row[2])
                        if not d:
                            rcs_date = " ".join(str(c) for c in d)
                        else:
                            date = str(d[0])
                            try:
                                rcs_date = datetime.datetime.strptime(date,'%Y%m%d').strftime('%m/%d/%Y')
                            except:
                                try:
                                    rcs_date = datetime.datetime.strptime(date,'%m%d%Y').strftime('%m/%d/%Y')
                                except:
                                    rcs_date = date
                  
                
                      
                
                writer.writerow([row[0],rcs_security,rcs_coupon,rcs_date,rcs_cusip6,rcs_cusip8] +row[1:])

                
 # Display the endtime after program is completed
endtime_clean = datetime.datetime.now()
print "Process Ended: %s" %endtime_clean

## Display the time taken to run the job
clean_tt = endtime_clean - starttime_clean
print "Timetaken to process cleaning up data: %s" %clean_tt
"""
****************************************************************************
After the code has been executed
a) There will be no leading/trailing numbers or special characters
b) No number followed by % will be present in RCS_SECURITY
c) Date in any format if not originally populated and present in string will be populated in mm/dd/yyyy

*****************************************************************************
"""
