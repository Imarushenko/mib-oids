# import the required modules
import csv
import re   # a built-in module that provides support for regular expressions

# setting file paths
mib_file = 'mib/file/path.mib'
csv_file = 'csv/file/path.csv'

# read the MIB file
with open(mib_file, 'r') as file:
    mib_content = file.read()

# regular expression pattern to match OIDs - sequence of digits separated by periods
pattern = r"DESCRIPTION\s+\"(.+?)\"[\s\S]*?--\s*([\d.]+)"

# find all matches of the pattern
matches = re.findall(pattern, mib_content, re.DOTALL)

# prepare the OIDs for writing to the CSV file
oids = [(oid, description.strip()) for description, oid in matches]

# save OIDs to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['OID', 'Description'])
    writer.writerows(oids)

# prints
print(f"All OIDs parsed from {mib_file} and saved to {csv_file} successfully.")
print(f"OIDs list size: {len(oids)}")
