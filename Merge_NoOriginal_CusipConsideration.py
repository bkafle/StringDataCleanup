## This code takes the cleaned version after fixing abbreviations and goes for Merging with CUSIP
## This code doesn't take consideration of Existing CUSIP values that were present from previous process
## File -- Bond_Merged_NoRAW.csv has all the Security with CUSIP6 populated after the lookup,and if multiple 
##             distinct CUSIP6 is found for firstN character all those CUSIP6 will be populated
## Write the Non-matching to a separate file 'Bond_NoMerge_NoRAW.csv'
import csv
import re
# Create Dictionary structure for CUSIP_MASTER file
with open("Jesse_Project/MasterCusip_Deduped.csv", "rb") as fp:
    dic_file = csv.reader(fp,)
    dict1 = {}
    for d in dic_file:
        d[1] = re.sub('[^A-Za-z0-9)]+','',d[1])
        dict1[d[1]] = d[0]


with open("Jesse_Project/Bond_Merged_NoRAW.csv", "wb") as fw1,open("Jesse_Project/Bond_NoMerge_NoRAW.csv", "wb") as fw2:
    with open("Jesse_Project/Abbreviated.csv", "r") as fr1:
        output = csv.writer(fw1, delimiter=",")
        writer1 = csv.writer(fw2,delimiter=",")
        read = csv.reader(fr1,)
            
        next(fr1, None)
            
        output.writerow(['FUNDID','RCS_SECURITY','RCS_COUPON',
                        'RCS_MATURITY','RCS_CUSIP6','MATCH TYPE','RCS_CUSIP8',
                'CUSIP','SECURITY','MATURITY','COUPON','CUSIP8'])
         
        writer1.writerow(['FUNDID','RCS_SECURITY','RCS_COUPON',
                        'RCS_MATURITY','RCS_CUSIP6','RCS_CUSIP8',
                'CUSIP','SECURITY','MATURITY','COUPON','CUSIP8'])   
        
        for row in read:
            row_c = re.sub('[^A-Za-z0-9)]+','',row[1])
            strip_20first = row_c[:20]
            strip_18first = row_c[:18]
            strip_16first = row_c[:16]
            strip_14first = row_c[:14]
            strip_12first = row_c[:12]

                
            found_ = False
            match = []
            for d in dict1:
                if d == row_c:     
                    if dict1[d] not in match:
                        match.append(dict1[d])
                    flag = 'Exact Match'
                    found_ = True
                    continue
                                 
                elif d[:20] == strip_20first:
                    if dict1[d] not in match:
                        match.append(dict1[d])
                    flag = 'First20_Match'
                    found_ = True
                    continue
                    
                    
                elif d[:18] == strip_18first:
                    if dict1[d] not in match:
                        match.append(dict1[d])
                    flag = 'First18_Match'
                    found_ = True
                    continue
                    
                    
                elif d[:16] == strip_16first:
                    if dict1[d] not in match:
                        match.append(dict1[d])
                    flag = 'First16_Match'
                    found_ = True
                    continue
                     
                        
                elif d[:14] == strip_14first:
                    if dict1[d] not in match:
                        match.append(dict1[d])
                    flag = 'First14_Match'
                    found_ = True
                    continue
                        
                elif d[:12] == strip_12first:
                    if dict1[d] not in match:
                        match.append(dict1[d])
                    flag = 'First12_Match'
                    found_ = True
                    continue
                        
                else:
                    pass
                    
            row[4] = ",".join(match)    
            if found_:    
                output.writerow([row[0],row[1],row[2],row[3],row[4],flag]+row[5:]) ## write only the matching ones
            else:
                writer1.writerow(row)