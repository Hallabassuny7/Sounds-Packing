import os
import shutil
from traceback import print_tb
import heapq
from FileHandling import *

filehandler = FileHandlingClass()

#Overall complexity for the function is O(N*M) + O(M) = O(N*M)
def WorstFit_LinearSearch(files,folder_size):         # O(1): Function definition
    folders=[]                                        # O(1): Initialize an empty list for folders
    outputlist=[]                                     # O(1): Initialize an empty list to store output
    #Overall complexity for the outer loop is N*M so it is O(N*M)
    for fileName,fileDuration in files.items():       # O(N): Loop through all files in the input dictionary where N = number of audio files
        if len(folders)==0:                           # O(1): Check if the folder list is empty
            folders.append([folder_size-fileDuration,[(fileName,fileDuration)]])  # O(1):Add a new folder
        else:
            worst_fit_index=-1                         # O(1): Initialize index for the worst fit
            largest_remaining_size=-1                  # O(1): Track the largest remaining size
            #Overall complexity for the inner loop is M*1 so it is O(M)
            for i in range(len(folders)):              # O(M): Iterate over all folders where M = number of folders. 
                folder = folders[i]                    # O(1): Access folder by index
                if folder[0] >= fileDuration and folder[0] > largest_remaining_size:  # O(1): Check folder capacity
                    worst_fit_index= i                  # O(1): Update worst fit index
                    largest_remaining_size = folder[0]  # O(1): Update largest remaining size

            if worst_fit_index==-1:                     # O(1): If no folder can accommodate the file
                folders.append([folder_size-fileDuration,[(fileName,fileDuration)]])  # O(1): Add new folder
            else:
                folders[worst_fit_index][0]-=fileDuration      # O(1): Update remaining space in the folder
                folders[worst_fit_index][1].append((fileName,fileDuration)) # O(1): Add file to the folder

    for folder in folders: # O(M): Loop through all folders
        outputlist.append(folder[1])  # O(1): Add folder content to the output list
        
    return outputlist                   # O(1): Return the final output lis

#Overall complexity of the function = O(N log M) +  O(M*log M) = O(N log M) -->Because N log M is much larger relative to M log M.
def WorstFit_PriorityQueue(files,folder_size):          # O(1): Function definition
    folders=[]                                          # O(1): Initialize an empty list to represent the priority queue
    outputlist=[]                                       # O(1): Initialize an empty list for the output
    #Overall complexity for this loop = N * 3*log M = O(N log M)
    for fileName,fileDuration in files.items():         # O(N): Iterate through all files where N = number of audio files
        if len(folders)==0:                             # O(1): Check if priority queue is empty
            heapq.heappush(folders,[-folder_size + fileDuration,[(fileName,fileDuration)]])  #O(log M): Add folder where M = number of folders
        else:
            folder=folders[0]                           # O(1): Access the folder with the largest space
            largest_remaining_size=-folder[0]           # O(1): Convert negative size back to positive
            if largest_remaining_size >= fileDuration:  # O(1): Check if file fits in the folder
                heapq.heappop(folders)                  # O(log M): Remove folder from the priority queue
                folder[1].append((fileName,fileDuration))    # O(1): Add file to folder
                heapq.heappush(folders,[-largest_remaining_size + fileDuration,folder[1]])   # O(log M): Update folder

            else:
                heapq.heappush(folders,[-folder_size + fileDuration,[(fileName,fileDuration)]]) # O(log M): Add new folder
#Overall complexity for this loop = M * log M = O(M*log M)
    while folders:                               # O(M): Loop through all folders
        folder=heapq.heappop(folders)            # O(log M): Remove folder with the largest space
        outputlist.append(folder[1])             # O(1): Add folder content to output list

    return outputlist                             

#Overall complexity for this function = O(max(NlogN , N*M)) + O(M) which we can ignore because it is very small = O(max(NlogN , N*M))
def WorstFit_LinearSearch_Decreasing(files,folder_size):            # O(1): Function definition
    folders=[]                                                  # O(1): Initialize an empty list for folders
    outputlist=[]                                               # O(1): Initialize an empty list for output
    sorted_files=filehandler.sortduration(files)                            # O(N log N): Sort files in descending order by duration where N = number of audio files
#Overall comlexity for this outer loop = N * M = O(N*M)
    for fileName,fileDuration in sorted_files.items():          # O(N): Loop through sorted files 
        if len(folders)==0:                                     # O(1): Check if folders list is empty
            folders.append([folder_size-fileDuration,[(fileName,fileDuration)]])   # O(1): Add new folder
        else:
            worst_fit_index=-1                                  # O(1): Initialize worst fit index
            largest_remaining_size=-1                           # O(1): Track largest remaining space
            #Overall comlexity for this inner loop = O(M)
            for i in range(len(folders)):                       # O(M): Iterate through all folders
                folder = folders[i]                             # O(1): Access folder
                if folder[0] >= fileDuration and folder[0] > largest_remaining_size:   # O(1): Check space conditions
                    worst_fit_index= i                          # O(1): Update worst fit index
                    largest_remaining_size = folder[0]          # O(1): Update largest remaining space

            if worst_fit_index==-1:                             # O(1): If no folder fits the file
                folders.append([folder_size-fileDuration,[(fileName,fileDuration)]])   # O(1): Add new folder
            else:
                folders[worst_fit_index][0]-=fileDuration       # O(1): Reduce folder space
                folders[worst_fit_index][1].append((fileName,fileDuration))            # O(1): Add file to folder
#Overall complexity for this loop = O(M)
    for folder in folders:                             # O(M): Loop through all folders
        outputlist.append(folder[1])                   # O(1): Append folder content to output

    return outputlist                                  # O(1): Return the final output list

#Overall complexity of this function = O(N log M) + O(M log M) +  O(N log N) = O(N log N) beacuse it is much greater relative to the others. 
def WorstFit_PriorityQueue_Decreasing(files,folder_size):       # O(1): Function definition
    folders=[]                                              # O(1): Initialize an empty priority queue
    outputlist=[]                                           # O(1): Initialize an empty list for output
    sorted_files=sortduration(files)                        # O(N log N): Sort files by duration  where N = number of audio files
    #Overall complexity of this loop = N * 4 log M = O(N log M)
    for fileName,fileDuration in sorted_files.items():      # O(N): Iterate through sorted files
        if len(folders)==0:                                 # O(1): Check if priority queue is empty
            heapq.heappush(folders,[-folder_size + fileDuration,[(fileName,fileDuration)]])   # O(log M): Add folder
        else:
            folder=folders[0]                               # O(1): Access folder with largest space
            largest_remaining_size=-folder[0]               # O(1): Convert negative size back to positive
            if largest_remaining_size >= fileDuration:      # O(1): Check folder capacity
                heapq.heappop(folders)                      # O(log M): Remove folder
                folder[1].append((fileName,fileDuration))   # O(1): Add file
                heapq.heappush(folders,[-largest_remaining_size + fileDuration,folder[1]]) # O(log M): Update folder

            else:
                heapq.heappush(folders,[-folder_size + fileDuration,[(fileName,fileDuration)]])  # O(log M): Add new folder
#Overall complexity = O(M log M)
    while folders: # O(M) loop all folders
        folder=heapq.heappop(folders)  # O(log M): Remove folder
        outputlist.append(folder[1])   # O(1): Add folder content

    return outputlist                   # O(1): Return final output


#files=readfile(r"Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
#print(files)
#x=WorstFit_LinearSearch_Decreasing(files,100)
# print(x)
##Output(r"Sample Tests\Sample 1\INPUT\Audios",r"Sample Tests\Sample 1\test output",x,"worstfit_linearsearch")

# folders = WorstFit_LinearSearch_Decreasing(files, 100)
# for idx, folder in enumerate(folders, start=1):
#     print(f"Folder {idx}: {folder}")