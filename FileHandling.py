import os
import shutil
from traceback import print_tb


def convert_to_seconds(time_str):
    hours, minutes, seconds = time_str.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


def readfile(folderdir):
    file_data = {}
    target_path = os.path.abspath(folderdir)
    with open(target_path, 'r') as file:
        num_entries = int(file.readline().strip())

        for i in range(num_entries):
            line = file.readline().strip()

            filename, time_str = line.split()

            # key = int(filename.split('.')[0])
            key = filename

            value = convert_to_seconds(time_str)

            file_data[key] = value

    return file_data


def Output(src,dest,data1,funcname):
    outputdir =os.path.join(os.path.abspath(dest), rf"OUTPUT\Sample{workingOn_testcase}")
    os.makedirs(outputdir, exist_ok=True)
    AbsPath = os.path.join(outputdir, funcname)
    os.makedirs(AbsPath, exist_ok=True)
    it = 1
    for i in data1:
        currentfolder = os.path.join(AbsPath, f"F{it}")
        os.makedirs(currentfolder,exist_ok=True)
        it+=1
        for j in i:
            #print(j[1])
            sourcefile = os.path.join(os.path.abspath(src), j[0])
            destfile = os.path.join(currentfolder, j[0])
            #print(sourcefile)
            #print(destfile)
            try:
                shutil.copyfile(sourcefile, destfile)
                #print("File copied successfully.")

            # If source and destination are same
            except shutil.SameFileError:
                print("Source and destination represents the same file.")

            # If destination is a directory.
            except IsADirectoryError:
                print("Destination is a directory.")

            # If there is any permission issue
            except PermissionError:
                print("Permission denied.")

            # For other errors
            except:
                print("Error occurred while copying file.")

workingOn_testcase = int(input("Enter Test case no. you would like to run: "))
#readfile(r"..\testcases\Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
#print(file_data)

if workingOn_testcase==1:
    source = r"..\Sample Tests\Sample 1\INPUT\Audios"
elif workingOn_testcase==2:
    source = r"..\Sample Tests\Sample 2\INPUT\Audio"
else:
    source = r".. \Sample Tests\Sample 3\INPUT\Audios"
