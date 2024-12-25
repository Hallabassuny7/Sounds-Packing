                                                                                      #________________________Code Analysis___________________________________
import heapq                                                                          #   O(1)
def best_fit_with_priority_queue(file_sizes, folder_capacity):                        #   O(1)
    # Sort files by size in descending order
    sorted_files = sorted(file_sizes.items(), key=lambda item: item[1], reverse=True)# item()-> O(1) ,sorted()->O(nlogn)"timsort" , total complexity->O(nlogn)

    folders = []                                                                     #O(1)

    for file_name, size in sorted_files:                                             #for loop indexing ->O(n)  , the total complexity -> O(n * (m  + k)) ,Simplification: O(n * m) .
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

    return folders                                                                  #O(1)



#_____________time complexity ______________
#total code complexity is O(n⋅m+nlogn) 
#worst case O(n^2) as m is equal to m 
#best case o(nlogn)
                                                                                    

#__________space complexity___________
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

# Output the result
for idx, (used_capacity, folder_content) in enumerate(result):
    print(f"Folder {idx + 1}: Used Capacity = {used_capacity}, Files = {folder_content}")
