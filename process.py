"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# TODO: Your code here

from main import covid_records
from tui import *
from datetime import *
import datetime


def process_total_records(list):
    num_records = len(list)
    return num_records


def serial_record(list_2):
    sno = serial_number() - 1
    return list_2[sno]


def process_obsrv_dates(dates):          # doesnt work yet

    list_to_return = []
    for user_date in dates:

        d1, m1, y1 = [int(x) for x in user_date.split('/')]
        date1 = (d1, m1, y1)

        for record in covid_records:         # something wrong in the loop

            d2, m2, y2 = [int(x) for x in record[1].split('/')]
            date2 = (d2, m2, y2)

            if date1 == date2:
                list_to_return.append(record)

    print(list_to_return)


def process_grouped_by_region():
    pass

def process_summary():
    pass