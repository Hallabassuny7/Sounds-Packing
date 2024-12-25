# import os
# import shutil
# from traceback import print_tb

    

#     def convert_to_seconds(time_str):
#         hours, minutes, seconds = time_str.split(':')
#         return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    
    
#     def readfile(folderdir):
#         file_data = {}
#         target_path = os.path.abspath(folderdir)
#         with open(target_path, 'r') as file:
#             num_entries = int(file.readline().strip())
    
#             for i in range(num_entries):
#                 line = file.readline().strip()
    
#                 filename, time_str = line.split()
    
#                 # key = int(filename.split('.')[0])
#                 key = filename
    
#                 value = convert_to_seconds(time_str)
    
#                 file_data[key] = value
    
#         return file_data


# def Output(src,dest,data1,funcname):
#     outputdir =os.path.join(os.path.abspath(dest), rf"OUTPUT\Sample{workingOn_testcase}")
#     os.makedirs(outputdir, exist_ok=True)
#     AbsPath = os.path.join(outputdir, funcname)
#     os.makedirs(AbsPath, exist_ok=True)
#     it = 1
#     for i in data1:
#         currentfolder = os.path.join(AbsPath, f"F{it}")
#         os.makedirs(currentfolder,exist_ok=True)
#         it+=1
#         for j in i:
#             #print(j[1])
#             sourcefile = os.path.join(os.path.abspath(src), j[0])
#             destfile = os.path.join(currentfolder, j[0])
#             #print(sourcefile)
#             #print(destfile)
#             try:
#                 shutil.copyfile(sourcefile, destfile)
#                 #print("File copied successfully.")

#             # If source and destination are same
#             except shutil.SameFileError:
#                 print("Source and destination represents the same file.")

#             # If destination is a directory.
#             except IsADirectoryError:
#                 print("Destination is a directory.")

#             # If there is any permission issue
#             except PermissionError:
#                 print("Permission denied.")

#             # For other errors
#             except:
#                 print("Error occurred while copying file.")

# workingOn_testcase = int(input("Enter Test case no. you would like to run: "))
# readfile(r"./Sample 1/INPUT/AudiosInfo.txt")


# if workingOn_testcase==1:
#     source = r"./Sample 1/INPUT/Audios"
# elif workingOn_testcase==2:
#     source = r"./Sample 2/INPUT/Audios"
# else:
#     source = r"./Sample 3/INPUT/Audios"

import os
import shutil
from traceback import print_tb

class FileHandlingClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FileHandlingClass, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            self.working_on_testcase = None

    def convert_to_seconds(self,time_str):
        hours, minutes, seconds = time_str.split(':')
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    def readfile(self, folderdir):
        file_data = {}
        target_path = os.path.abspath(folderdir)
        with open(target_path, 'r') as file:
            num_entries = int(file.readline().strip())

            for i in range(num_entries):
                line = file.readline().strip()
                filename, time_str = line.split()
                key = filename
                value = self.convert_to_seconds(time_str)
                file_data[key] = value

        return file_data

    def output(self, src, dest, data1, funcname):
        outputdir = os.path.join(os.path.abspath(dest), rf"OUTPUT\Sample{self.working_on_testcase}")
        os.makedirs(outputdir, exist_ok=True)
        abs_path = os.path.join(outputdir, funcname)
        os.makedirs(abs_path, exist_ok=True)
        it = 1
        for i in data1:
            currentfolder = os.path.join(abs_path, f"F{it}")
            os.makedirs(currentfolder, exist_ok=True)
            it += 1
            for j in i:
                sourcefile = os.path.join(os.path.abspath(src), j[0])
                destfile = os.path.join(currentfolder, j[0])
                try:
                    shutil.copyfile(sourcefile, destfile)
                except shutil.SameFileError:
                    print("Source and destination represent the same file.")
                except IsADirectoryError:
                    print("Destination is a directory.")
                except PermissionError:
                    print("Permission denied.")
                except Exception as e:
                    print(f"Error occurred while copying file: {e}")

    def set_testcase(self, testcase_no):
        self.working_on_testcase = testcase_no


# Singleton usage
file_processor = FileHandlingClass()

working_on_testcase = int(input("Enter Test case no. you would like to run: "))
file_processor.set_testcase(working_on_testcase)

if working_on_testcase == 1:
    source = r"/Sample 1/INPUT/Audios"
elif working_on_testcase == 2:
    source = r"/Sample 2/INPUT/Audios"
else:
    source = r".    /Sample 3/INPUT/Audios"

# Example usage
data = file_processor.readfile(r"./Sample 1/INPUT/AudiosInfo.txt")
file_processor.output(source, r"./Destination", data, "ProcessedData")
