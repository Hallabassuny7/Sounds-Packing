import os
import shutil
from traceback import print_tb


def convert_to_seconds(time_str):
    hours, minutes, seconds = time_str.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
def readfile(folderdir):
    target_path = os.path.abspath(folderdir)
    with open(target_path, 'r') as file:
        num_entries = int(file.readline().strip())

        for i in range(num_entries):
            line = file.readline().strip()

            filename, time_str = line.split()

            #key = int(filename.split('.')[0])
            key = filename

            value = convert_to_seconds(time_str)

            file_data[key] = value

    
    return file_data
file_data = {}
readfile(r"..\testcases\Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
print(file_data)
