                                                  #_______________________code Analysis____________________________#
def best_fit_dp(file_sizes, folder_capacity):                  # Total time complexity: O(n * C)

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

        folders.append((folder_capacity - cap, folder))  
                                                # O(1) - Add folder to result

        # Remove the allocated files from the remaining files set
        remaining_files -= current_file_indices  # O(n) - Removing allocated files

    return folders                               # O(1) - Return the list of allocated folders


# Time complexity:
# - Extracting file names and sizes: O(n)
# - DP table initialization: O(n * C)
# - Building the DP table: O(n * C)
# - Backtracking and allocating files: O(n * C)
# - Removing allocated files: O(n)
# Total time complexity: O(n * C)
# Worst-case time complexity: O(n * C)
# best-case time complexity: O(n * C)

# Space complexity:
# - DP table: O(n * C)
# - Folders and file sets: O(n)
# Total space complexity: O(n * C)

 # Test case:
file_sizes = {
    "file1": 10,
    "file2": 15,
    "file3": 20,
    "file4": 5,
    "file5": 25,
    "file6": 10
}
folder_capacity = 30
result = best_fit_dp(file_sizes, folder_capacity)

# Output the result
for idx, (used_capacity, folder_content) in enumerate(result):
     print(f"Folder {idx + 1}: Used Capacity = {used_capacity}, Files = {folder_content}")