#
# Adapted from:
#   http://pbpython.com/pandas-google-forms-part1.html
#
from __future__ import print_function
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json

SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "../../SIAG-key.json"
SPREADSHEET = "SIAG LA conference announcement (Responses)"

# Based on docs here - http://gspread.readthedocs.org/en/latest/oauth2.html
# Load in the secret JSON key (must be a service account)
json_key = json.load(open(SECRETS_FILE))

# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)

gc = gspread.authorize(credentials)
print("The following sheets are available")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))

# Open up the workbook based on the spreadsheet name
workbook = gc.open(SPREADSHEET)

# Get the first sheet
sheet = workbook.sheet1

# Extract all data into a dataframe
data = pd.DataFrame(sheet.get_all_records())

for idx, row in data.iterrows():

    info   = row['Conference information (Markdown format)']
    name   = row['Conference Name']
    tag    = row['Short Name']
    dstart = pd.to_datetime(row['Start Date']).replace(hour=12)
    dend   = pd.to_datetime(row['End Date']).replace(hour=12)
    venue  = row['Venue']
    page   = row['Web Page']

    mdname = "{0:%Y-%m-%d}-{1}.md".format(dstart, tag)
    with open(mdname, "w") as f:
        print("Generating {0}".format(mdname))
        f.write('---\n')
        f.write('title: {0}\n'.format(name))
        f.write('page: {0}\n'.format(page))
        f.write('start_date: {0}\n'.format(dstart))
        f.write('end_date: {0}\n'.format(dend))
        f.write('where: {0}\n'.format(venue))
        f.write('---\n')
        f.write(info)
