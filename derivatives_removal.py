#This code will remove any security which have any words as provided in the derivatives list
#indicating that it is a derivative and won't have a CUSIP value associated to it.
#It will create two separate files - a)Bond_NoDeri_Security which will be used for further processing to Merge Cusip Values.
#									b)Bond_Derivatives_Security which will have rows which indicate that it is derivative.
#									
#								

import re
import csv

st_remove_der= datetime.datetime.now()
print "Process Start Time for removing Derivatives: %s" %st_remove_der

derivatives=["derivative", "put", "put@", "put", "-put", "usd p", "usd rec",
"call"," call@", "cll", "-call", "usd c", "buy", 
"optn", "option", "libor", "euroibor", "euroyen", "eurodollar",
"forward", "fwd", "(fwd)", "cmdtyfut", "rtp", "rtr", "interest rate fut",
"future", "futures", "fut", "(fut)", " futr", "ftr", "ftrs", 
"swap", "swap:", "swp:", "swaption", "swp", "swp:", "swap", "swap", "swpn", "swptn", "swptn", 
"ccs", "irs", "iswp", "irs:", "trs", "trs:", "trswap", "trswap:",
"cds", "cds", "cds:", "cds(", "cds-", "cds", "iro", "otc", 
"designated currency contract", "american style", "strike price", "str", "expire", "sold credit", 
"receive a fixed rate", "recevie a fixed rate", "pay", "payb", "fswp", "fswp", "fswp"]



# the files
infile = "hbs_jschreger_lab/Bond_Sorted.csv"
outfile = "hbs_jschreger_lab/Bond_NoDeri_Security.csv"
derifile = "hbs_jschreger_lab/Bond_Derivatives_Security.csv"

# changing the case of words in derviates to Upper since our data is Upper
de = set(word.upper() for word in derivatives)


with open(infile, 'rb') as inFile, open(derifile,'wb') as dFile, open(outfile, 'wb') as outFile:
    reader = csv.reader(inFile, delimiter=',')
    writer = csv.writer(outFile, delimiter=',')
    writer1 = csv.writer(dFile, delimiter=',')
    for row in reader:
        readrow = re.split("[@_()-: ]+",row[1])## tokenizing the string in any of these character including space
        if not set(readrow) & set(de):
            writer.writerow(row) 
        else:
            writer1.writerow(row)

            
### Code to diplay the rowcount of file prepared ie Bond_NoDeri_Security
with open("hbs_jschreger_lab/Bond_NoDeri_Security.csv","rb") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
print "Number of rows present for NoDerivatives: %s"%row_count



### Time display and timetaken information
et_remove_der = datetime.datetime.now()
print "Process Ended for Sorting: %s" %et_remove_der

remove_tt = et_remove_der - st_remove_der
print "Timetaken to for sorting process: %s" %(remove_tt)
