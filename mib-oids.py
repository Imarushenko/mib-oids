# import the required libraries
import csv
import re   # a built-in module that provides support for regular expressions

# define file paths
mib_file_path = 'C:/develop/files/Frontline_ALLOT-MIB.mib'
csv_file_path = 'C:/develop/files/extracted-oids.csv'

# read the MIB file
with open(mib_file_path, 'r') as file:
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
    # curr_oid = OBJECT IDENTIFIER in the MIB file
    # alternative_oid = -- in the MIB
    # prev_oid = -- in the MIB inner lines
    curr_oid, inner_oid, alternative_oid = match
    if curr_oid:
        oids.append(curr_oid)
    elif inner_oid:
        oids.append(inner_oid)
    elif alternative_oid:
        oids.append(alternative_oid)

# write the OIDs to CSV file
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Object Identifier (OID)'])
    writer.writerows([(oid,) for oid in oids])

# prints
print(f"All OIDs extracted from {mib_file_path} and saved to {csv_file_path} successfully!")
print(f"Found {len(oids)} oids in {mib_file_path}.")
