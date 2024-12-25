import os
import shutil
from traceback import print_tb


def hms_to_seconds(time_str):
    hours, minutes, seconds = time_str.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"


def readfile(folderdir):
    file_data = {}
    target_path = os.path.abspath(folderdir)
    with open(target_path, 'r') as file:
        num_entries = int(file.readline().strip())

        for i in range(num_entries):
            line = file.readline().strip()

            filename, time_str = line.split()

            key = filename

            value = hms_to_seconds(time_str)

            file_data[key] = value

    return file_data

def sortduration(audio):
    # Sorting the items of the dictionary by their values in descending order using Timsort
    sorted_items = sorted(audio.items(), key=lambda item: item[1], reverse=True)
    # O(N log N), where N is the number of items in the audio dictionary.
    # - audio.items() creates a view of the dictionary items → O(N).
    # - sorted() sorts the items using Timsort → O(N log N).
    # - The lambda function extracts the value (item[1]) for sorting → O(1) per call, called N times.

    # Converting the sorted list of tuples back into a dictionary
    sorted_Aura = dict(sorted_items)
    # O(N), where N is the number of items in the list sorted_items.
    # - dict() iterates over the list and constructs a new dictionary.

    return sorted_Aura  # O(1), returning the sorted dictionary.

def Output(src,dest,folder,funcname,sample):
    #path
    outputdir =os.path.join(os.path.abspath(dest), rf"OUTPUT\{sample}",funcname)
    os.makedirs(outputdir, exist_ok=True)
    #//////////////////////////////////////////////////////////////////////////////
    it = 1
    #Display
    print("Folders Content:")
    for i in folder:
        # path
        currentfolder = os.path.join(outputdir, f"F{it}")
        os.makedirs(currentfolder,exist_ok=True)
        # //////////////////////////////////////////////////////////////////////////////
        # text file
        with open(os.path.join(outputdir,f"F{it}_METADATA.txt"), "w") as file:
            file.write(f"F{it}\n")
        # //////////////////////////////////////////////////////////////////////////////
        timesum = 0
        for j in i:
            sourcefile = os.path.join(os.path.abspath(src), j[0])
            destfile = os.path.join(currentfolder, j[0])
            #txt file
            #convert sec to time format
            time = seconds_to_hms(j[1])
            # Open the file in write mode ('w')
            with open(os.path.join(outputdir,f"F{it}_METADATA.txt"), "a") as file:
                file.write(f"{j[0]} {time}\n")
            timesum += j[1]

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
        # write to text file
        with open(os.path.join(outputdir,f"F{it}_METADATA.txt"), "a") as file:
            file.write(f"{seconds_to_hms(timesum)}\n")
        # //////////////////////////////////////////////////////////////////////////////
        with open(os.path.join(outputdir, f"F{it}_METADATA.txt"), "r") as file:
            # Read the file's content
            content = file.read()
            # Print the file's content
            print(content)
        it+=1
