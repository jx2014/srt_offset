# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:25:59 2021

@author: jx2014

Change subtitle timestamps with an offset

"""

from datetime import datetime
import re
import os

time_offset = -3 #in seconds

input_file = r'C:\random_directory\random_subtitle_file.srt'

def get_output_file(input_file):
    directory = os.path.dirname(input_file)
    filename = os.path.basename(input_file)
    filename, extension = os.path.basename(input_file).rsplit('.', 1)
    output_filename = filename + '_new'
    output_filename = '.'.join([output_filename, extension])
    return os.path.join(directory, output_filename)

output_file = get_output_file(input_file)



def sense_timestamps(line, time_offset):
    try:
        ts1, ts2 = re.findall('\d{2}:\d{2}:\d{2},\d{3}', line)
        ts1 = datetime.strptime(ts1,"%H:%M:%S,%f")
        ts2 = datetime.strptime(ts2,"%H:%M:%S,%f")
        ts1 = ts1.replace(second=ts1.second+time_offset)
        ts2 = ts2.replace(second=ts2.second+time_offset)
        ts1 = ts1.strftime("%H:%M:%S,%f")[:-3]
        ts2 = ts2.strftime("%H:%M:%S,%f")[:-3]
        return ts1 + ' --> ' + ts2 + '\n'
    except ValueError:
        return line
        

with open(input_file, 'r') as inFile:
    with open(output_file, 'w') as outFile:
        for inline in inFile:
            outFile.write(sense_timestamps(inline, time_offset))
    
    
