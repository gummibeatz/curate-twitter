# -*- coding: UTF-8 -*-


# appends an additional column to csv signaling the user gender

import sexmachine.detector as gender
import sys
import io
from unicode_csv import *

def get_first_name(full_name):
    try:
        return full_name.split()[0].split('.')[0].split('_')[0]
    except:
        return "N/A"

twitter_handle = sys.argv[-1]

csv_file_in = "{0}/{1}_results.csv".format(twitter_handle, twitter_handle)
csv_file_out = "{0}/{1}_results_genderified.csv".format(twitter_handle, twitter_handle) 
d = gender.Detector(case_sensitive=False)

genderified_list = []
with io.open(csv_file_in, 'rb') as csv_data:
    reader = UnicodeReader(csv_data)

    for row in reader:
        row.append(d.get_gender(get_first_name(row[0])))
        genderified_list.append(row)

with io.open(csv_file_out, 'wb') as csv_data:
    writer = UnicodeWriter(csv_data)
    writer.writerows(genderified_list)
