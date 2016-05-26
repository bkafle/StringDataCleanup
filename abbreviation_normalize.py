## This takes the Security file and abbreviates any string according to cusip_abbreviations.csv
##if a string whose abbreviated form is present then it abbreviates
##  For example  AAMES MORTGAGE TRUST -----> AAMES MTG TR
import csv
import re
import string
# Create Dictionary structure of cusip_abbreviations.csv file 
with open("hbs_jschreger_lab/cusip_abbreviations.csv", "rb") as fp1:
    dic_file2 = csv.reader(fp1,)
    dict2 = {}
    for a in dic_file2:
        a[1] = re.sub('[^A-Za-z0-9)]+','',a[1])
        a[2] = re.sub('[^A-Za-z0-9)]+','',a[2])
        dict2[a[2]] = a[1]

            
with open("hbs_jschreger_lab/Bond_Abbreviated.csv", "wb") as fw1:
    with open("hbs_jschreger_lab/Bond_NoDeri_Security.csv", "r") as fr1:
        output = csv.writer(fw1, delimiter=",")
        writer1 = csv.writer(fw2,delimiter = ",")
        read = csv.reader(fr1,)
            
        next(fr1, None)
            
        output.writerow(['FUNDID','RCS_SECURITY','RCS_COUPON',
                        'RCS_MATURITY','RCS_CUSIP6','RCS_CUSIP8',
                'CUSIP','SECURITY','MATURITY','COUPON','CUSIP8']) 
           
        for row in read:
            row_split = row[1].split()
            abb_ = False
            new_row = row[1]
            for s in row_split:
                s = re.sub('[^A-Za-z0-9)]+','',s)
                for di in dict2:
                    if di == s:
                        new_row = string.replace(new_row,s,dict2[di])
                        abb_ = True
            if abb_:
                row[1] = re.sub('[^A-Za-z0-9 )]+','',new_row)# remove any special characters from string
                output.writerow(row)
            else:
                row[1] = re.sub('[^A-Za-z0-9 )]+','',row[1]) # remove any special characters from string
                output.writerow(row)


### Testing - Verify word with 'MORTGAGE' is not present in RCS_SECURITY, instead should be MTG.