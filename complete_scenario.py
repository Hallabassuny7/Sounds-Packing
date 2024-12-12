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

            key = filename

            value = convert_to_seconds(time_str)

            file_data[key] = value

    return file_data
def sortduration(audio):
    sorted_items = sorted(audio.items(), key=lambda item: item[1], reverse=True)
    sorted_Aura = dict(sorted_items)

    return sorted_Aura
def Output(src,dest,data1,funcname):
    outputdir =os.path.join(dest, rf"OUTPUT\Sample{workingOn_testcase}")
    os.makedirs(outputdir, exist_ok=True)
    AbsPath = os.path.join(outputdir, funcname)
    os.makedirs(AbsPath, exist_ok=True)
    it = 1
    for i in data1:
        currentfolder = os.path.join(AbsPath, f"F{it}")
        os.makedirs(currentfolder,exist_ok=True)
        it+=1
        for j in i:
            sourcefile = os.path.join(src, list(j.keys())[0])
            destfile = os.path.join(currentfolder, list(j.keys())[0])
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

# Loading Test Cases
# r means raw which treat backslashes as character not escape character
t1 = readfile(r"..\testcases\Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
t2 = readfile(r"..\testcases\Sample Tests\Sample 2\INPUT\AudiosInfo.txt")
t3 = readfile(r"..\testcases\Sample Tests\Sample 3\INPUT\AudiosInfo.txt")
workingOn_testcase = int(input("Enter Test case no. you would like to run: "))




def FirstFit (tracks,DDPF):
    #sorting
    sortedtracks = sortduration(tracks)
    #########
    Folders = []
    FoldersSize = []
    #print(len(folders))
    for key,value in sortedtracks.items():
        #print(len(Folders))
        if len(Folders) == 0:
            Folders.append([{key:value}])
            FoldersSize.append(value)
        else:
            Found=False
            for i in range(len(Folders)):
                #print(Folders)
                if value <= (DDPF-FoldersSize[i]):
                    Folders[i].append({key:value})
                    FoldersSize[i]+=value
                    Found=True
                    break
            if not Found:
                Folders.append([{key:value}])
                FoldersSize.append(value)
    #print(Folders)
    Output(source,r"D:\Faculty\5th_Semester\Algo\Project\testcases\mytest",Folders,"[3] FolderFilling")



if workingOn_testcase==1:
    source = r"D:\Faculty\5th_Semester\Algo\Project\testcases\Sample Tests\Sample 1\INPUT\Audios"
    FirstFit(t1,100)
elif workingOn_testcase==2:
    source = r"D:\Faculty\5th_Semester\Algo\Project\testcases\Sample Tests\Sample 2\INPUT\Audios"
    FirstFit(t2,100)
else:
    source = r"D:\Faculty\5th_Semester\Algo\Project\testcases\Sample Tests\Sample 3\INPUT\Audios"
    FirstFit(t3,100)
#data2 = FirstFit(t2,100)
#data3 = FirstFit(t3,100)
#choose = input("Enter sample no. : ")
#if choose == "1":
#    Output(r"D:\Faculty\5th_Semester\Algo\Project\testcases\Sample Tests\Sample 1\INPUT\Audios",r"D:\Faculty\5th_Semester\Algo\Project\testcases\mytest","Sample1",data1,"[3] FolderFilling")
#else:
#   Output(r"D:\Faculty\5th_Semester\Algo\Project\testcases\Sample Tests\Sample 2\INPUT\Audios",r"D:\Faculty\5th_Semester\Algo\Project\testcases\mytest","Sample2",data2,"[3] FolderFilling")
