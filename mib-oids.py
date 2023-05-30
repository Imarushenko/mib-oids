# import the required libraries
import csv
import re   # a built-in module that provides support for regular expressions

# define file paths
mib_file = 'mib_file_path'
csv_file = 'csv_file_path'

# read the MIB file
with open(mib_file, 'r') as file:
    mib_content = file.read()

# regular expression pattern to match OIDs - sequence of digits separated by periods
# every group of regex is related to the 3 variables below in the loop, '?: ...' - related to each variable
pattern = r"(?:(\S+)\s+OBJECT\s+IDENTIFIER\s+--\s*([\d.]+)\s*\n|(?:^|\n)\s*--\s*([\d.]+)\s*\n)"

# find all matches of the pattern (OIDs) using re library, re.findall() function that finds all the matches in the
# MIB re.MULTILINE search the matches on each line
matches = re.findall(pattern, mib_content, re.MULTILINE)

oids = []
for match in matches:
    # define 3 variables to capture the values of corresponding groups from the regular expression match
    # oid = OBJECT IDENTIFIER in the MIB file
    # alternative_oid = -- in the MIB
    # preceding_oid = -- in the MIB inner lines
    preceding_oid, oid, alternative_oid = match
    if oid:
        oids.append(oid)
    elif preceding_oid:
        oids.append(preceding_oid)
    elif alternative_oid:
        oids.append(alternative_oid)

# write the OIDs to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Object Identifier (OID)'])
    writer.writerows([(oid,) for oid in oids])

# prints
print(f"All OIDs extracted from {mib_file} and saved to {csv_file} successfully!")
print(f"OIDs list size: {len(oids)}")
