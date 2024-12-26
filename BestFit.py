#_Code Analysis__________________________________
import heapq                                                                          #   O(1)
def best_fit_with_priority_queue(file_sizes, folder_capacity):                        #   O(1)
    # Sort files by size in descending order
    sorted_files = sorted(file_sizes.items(), key=lambda item: item[1], reverse=True)# item()-> O(1) ,sorted()->O(nlogn)"timsort" , total complexity->O(nlogn)

    folders = []                                                                     # O(1)

    for file_name, size in sorted_files:                                             # for loop indexing ->O(n)  , the total complexity -> O(n * (m  + k)) ,Simplification: O(n * m) .
        # Skip if file is larger than folder capacity
        if size > folder_capacity:                                                   #O(1)
            raise ValueError(f"File '{file_name}' with size {size} exceeds folder capacity {folder_capacity}.") # raise ValueError() ->O(1)
        # Find the best folder for the current file
        best_fit_index = -1                                                          #O(1)
        min_remaining_space = float('inf')                                           #O(1)

        # Check for the folder with the smallest remaining space that can fit the file
        for i in range(len(folders)):                                               # O(m) "where m is the number of folders"
            remaining_capacity, files = folders[i]                                  #O(1)
            if remaining_capacity >= size and (remaining_capacity - size) < min_remaining_space:#O(1)
                best_fit_index = i                                                  #O(1)
                min_remaining_space = remaining_capacity - size                     #O(1)

        # If no suitable folder was found, create a new one
        if best_fit_index == -1:                                                   #O(1) ,total if complexity -> O(k)
            # Create a new folder with the current file
            heapq.heappush(folders, (folder_capacity - size, [(file_name, size)])) # O(log k)  "where k is the number of folders in heap (having remaining capacity)".
        else: 
            # Update the folder with the new file
            remaining_capacity, files = folders[best_fit_index]                    #O(1)
            files.append((file_name, size))                                        #append() -> O(1)
            folders[best_fit_index] = (remaining_capacity - size, files)           #O(1)
            heapq.heapify(folders)                                                 #O(k) "where k is the number of folders in the heap (having remaining capacity)"
            #Rebuilding the heap to restore the heap property after modifying the folder list.

    return [folders for _, folders in folders]



#_time complexity ______________
#total code complexity is O(n⋅m+nlogn) 
#worst case O(n^2) as m is equal to n
#best case o(nlogn) where m is equal 1
                                                                                
#_space complexity__________
# - The sorted_files list requires O(n) space where n is the number of files.
# - The folders list holds tuples of (remaining_capacity, files) for each folder.
#   In the worst case, this list can hold n folders, so the space complexity is O(n).
# - The heap used for managing the folders requires O(n) space because there could be up to n folders in the worst case.
# - Therefore, the total space complexity is O(n), where n is the number of files.

file_sizes = {
    "file1": 10,
    "file2": 15,
    "file3": 20,
    "file4": 5,
    "file5": 25,
    "file6": 10
}
folder_capacity = 30
result = best_fit_with_priority_queue(file_sizes, folder_capacity)


#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################
#code Analysis_#
def best_fit_dp(file_sizes, folder_capacity):                  # Total time complexity: O(n * C + n ^2)

    file_names = list(file_sizes.keys())          # O(n) - Extracting file names
    file_sizes_list = list(file_sizes.values())   # O(n) - Extracting file sizes
    n = len(file_sizes_list)                      # O(1) - Calculating number of files

    dp = [[False] * (folder_capacity + 1) for _ in range(n + 1)]  
                                                  # O(n * C) - Initializing the DP table (2D list of size n+1 by C+1)
    dp[0][0] = True                               # O(1) - Base case assignment
    # Build the DP table
    for i in range(1, n + 1):                     # O(n) - Looping through files
        for cap in range(folder_capacity + 1):    # O(C) - Looping through capacities
            dp[i][cap] = dp[i - 1][cap]           # O(1) - Excluding the current file
            if cap >= file_sizes_list[i - 1]:     # O(1) - Checking if the file can fit
                if dp[i - 1][cap - file_sizes_list[i - 1]]:  # O(1) - Checking previous DP value
                    dp[i][cap] = True             # O(1) - Marking this capacity as achievable

    # Backtracking 
    folders = []                                  # O(1) - Initialize list for  storing folders
    remaining_files = set(range(n))               # O(n) - Initialize set of all  files

    while remaining_files:                        # O(n) - Looping until all files are allocated
        cap = folder_capacity                     # O(1) - Reset folder capacity
        folder = []                               # O(1) - List to store current folder's files
        current_file_indices = set()              # O(1) - Set to track current folder's files

        for i in range(n, 0, -1):                # O(n) - Looping over files in reverse order
            if (i - 1) in remaining_files and dp[i][cap] and dp[i - 1][cap - file_sizes_list[i - 1]]:
                                                 # O(1) - Check if file fits and is available for allocation
                folder.append((file_names[i - 1], file_sizes_list[i - 1]))  # O(1) - Add file to folder
                cap -= file_sizes_list[i - 1]    # O(1) - Update folder capacity
                current_file_indices.add(i - 1)  # O(1) - Mark file as allocated

        # Ensure progress is made
        if not folder:                          # O(1) - Check if folder is empty (no files were allocated)
            print("Warning: No more files can be allocated to a folder. Exiting.")
            break                               # O(1) - Exit if no files can be allocated

        folders.append(folder)  
                                                # O(1) - Add folder to result

        # Remove the allocated files from the remaining files set
        remaining_files -= current_file_indices  # O(n) - Removing allocated files

    return folders                               # O(1) - Return the list of allocated folders


# Time complexity:
# Backtracking : O(n ^2)
# DP complexity: O(n * C)

# Space complexity:
# - DP table: O(n * C)
# - Folders and file sets: O(n)
# Total space complexity: O(n * C)
