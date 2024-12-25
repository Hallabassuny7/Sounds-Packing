import heapq  
def next_fit_D_C(file_sizes, folder_capacity):  # Main function to allocate files into folders.
    # Convert file_sizes dictionary into a list of tuples (filename, size)
    file_list = list(file_sizes.items())  # Converts file_sizes into a list of tuples for easier processing. O(n)

    def allocate_files(file_list):  # Recursive function to allocate files using divide-and-conquer.
        # Base case: if there's only one file, allocate it in its own folder.
        if len(file_list) == 1:  
            return [[file_list[0]]]  # Single folder containing the file. O(1)

        # Divide: Split the file list into two halves.
        mid = len(file_list) // 2  
        left_files = file_list[:mid]  # Left half of the file list. O(n)
        right_files = file_list[mid:]  # Right half of the file list. O(n)
        
        print("Files before allocation (after divide and conquer):")
        print("Left files:", left_files)
        print("Right files:", right_files)
        print()

        # Conquer: Recursively allocate files in the left and right halves.
        left_folders = allocate_files(left_files)  # Recursive call for left half. O(log n)
        right_folders = allocate_files(right_files)  # Recursive call for right half. O(log n)

        # Combine: Merge the allocated folders from both halves.
        return merge_folders(left_folders, right_folders, folder_capacity)  # Combine results. O(m log m)

    def merge_folders(left_folders, right_folders, folder_capacity):  # Function to merge folders efficiently.
        folders = left_folders  # Start with the folders from the left half. O(1)

        # Create a min-heap for folder remaining capacities.
        folders_heap = [(folder_capacity - sum(size for _, size in folder), i) for i, folder in enumerate(folders)]  
        # Heap stores (remaining capacity, folder index) for each folder. O(n)

        heapq.heapify(folders_heap)  # Convert list to a min-heap. O(n)

        # Iterate through the folders in the right half.
        for folder in right_folders:  # O(m), where m is the total number of files in right_folders.
            for file_name, size in folder:  # Iterate through files in the current folder. O(k), where k is the number of files in a folder.
                placed = False  # Track whether the file is placed in an existing folder.

                while folders_heap:  # Check existing folders for available capacity. O(log n) per operation.
                    remaining_capacity, folder_index = heapq.heappop(folders_heap)  # Pop folder with the most available space. O(log n)

                    if size <= remaining_capacity:  # Check if the file fits in the folder. O(1)
                        folders[folder_index].append((file_name, size))  # Add file to folder. O(1)
                        remaining_capacity -= size  # Update remaining capacity. O(1)
                        heapq.heappush(folders_heap, (remaining_capacity, folder_index))  # Push updated folder back into the heap. O(log n)
                        placed = True  # Mark the file as placed. O(1)
                        break  # Exit the loop once the file is placed. O(1)

                if not placed:  # If the file couldn't be placed in any existing folder.
                    new_folder = [(file_name, size)]  # Create a new folder for the file. O(1)
                    folders.append(new_folder)  # Add the new folder to the list of folders. O(1)
                    heapq.heappush(folders_heap, (folder_capacity - size, len(folders) - 1))  # Push new folder into the heap. O(log n)

        return folders  # Return the merged list of folders. O(1)

    allocated_folders = allocate_files(file_list)  # Start the recursive allocation. O(n log n)
    #Output(source,"..\Karim\k",allocated_folders,"nextfit D&C")
    return allocated_folders  # Return the final allocation of folders. O(1)


# _____________________________________Time Complexity _____________________________________#
#   1. The `allocate_files` function has a time complexity of O(n log n) because it recursively divides the file list and merges the results.
#   2. The `merge_folders` function involves iterating through the right folder list (O(m)) and inserting/removing items from a heap (O(log n) for each file). This gives a complexity of O(m log n).
#   3. Thus, the total time complexity of the algorithm is O(n log n + m log m), where n is the number of files and m is the number of folders.


#_____________________________________Worst-Case Complexity_____________________________________#
# - The worst-case time complexity occurs when:
#   1. Every file requires its own folder because it doesn't fit into any existing folder.
#   2. The merging step involves checking all existing folders for each file, resulting in the maximum number of heap operations.
# - In this case, both the recursive allocation and the merging process each take O(n log n) time, leading to a worst-case total time complexity of **O(n log n)**


# _____________________________________Space Complexity_____________________________________#
# - Space used by the `file_list`: O(n) (for storing the file sizes).
# - Space used by the recursive call stack: O(log n) (due to the divide-and-conquer recursion).
# - Space used by the `folders` list: O(n) (for storing the allocated folders).
# - Space used by the min-heap `folders_heap`: O(n) (for managing the folder capacities).
# Total space complexity: O(n)

# Example
size_tst = {"file1": 70, "file2": 80, "file3": 20, "file4": 15, "file5": 15}  # Example file sizes.
capacity_tst = 100  # Example folder capacity.

allocated_folders = next_fit_D_C(size_tst, capacity_tst)  # Call the function with the test data.

print("Final folders:", allocated_folders)  # Print the final allocation of files into folders.










# import os
# import shutil
# from traceback import print_tb


# def convert_to_seconds(time_str):
#     hours, minutes, seconds = time_str.split(':')
#     return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


# def readfile(folderdir):
#     file_data = {}
#     target_path = os.path.abspath(folderdir)
#     with open(target_path, 'r') as file:
#         num_entries = int(file.readline().strip())

#         for i in range(num_entries):
#             line = file.readline().strip()

#             filename, time_str = line.split()

#             # key = int(filename.split('.')[0])
#             key = filename

#             value = convert_to_seconds(time_str)

#             file_data[key] = value

#     return file_data


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


# r =readfile(r"..\Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
# print (r)

# workingOn_testcase = int(input("Enter Test case no. you would like to run: "))
# #readfile(r"..\testcases\Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
# #print(file_data)

# if workingOn_testcase==1:
#     source = r"..\Sample Tests\Sample 1\INPUT\Audios"
#     next_fit_D_C(r,100)
# elif workingOn_testcase==2:
#     source = r"..\Sample Tests\Sample 2\INPUT\Audio"
#     next_fit_D_C(r,100)
# else:
#     source = r".. \Sample Tests\Sample 3\INPUT\Audios"
#     next_fit_D_C(r,100)

