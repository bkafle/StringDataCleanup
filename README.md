# CommercialData_Jesse
This Project is related to finding CUSIP6 code for the Security, especially Bond in this case. 
The code is related to string matching using Python Dictionary, and utilizes pandas and dataframe python packages.
The version of the Python and Pandas -
Python version: 2.7.6 |Anaconda 1.9.1 (64-bit)| (default, Nov 11 2013, 10:49:15) [MSC v.1500 64 bit (AMD64)]
Pandas version: 0.13.1


Two separate files are created at the very end. The first file holds all the records whose CUSIP6 merge value was found
in the MasterCusip file.  The second file will have all the records whose CUSIP6 merge value couldn't be found.


Order of Execution for this project - 
a) filecreation.py ---> creates file from RAW Original file by copying only few columns needed for merging.
b) security_clean.py ---> cleans security string removing special characters and extracting dates, coupon.
c) dedup.py ---> removes duplicates.
d) derivatives_removal.py ---> removes any security which are derivatives.
e) abbreviation_normalize.py ---> abbreviates string as per abbreviations.csv file.
f) dedup_cusip.py ---> remove duplicates from MasterCusip file if there is any.
g) cusip_merge.py ---> Merge CUSIP6 from MasterCusip 