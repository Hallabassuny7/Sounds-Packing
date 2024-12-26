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

################################################################################################################################################################


def next_fit_greedy(file_sizes, folder_capacity):
    # Sort files in descending order to place larger files first
    sorted_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
    # Explanation: Sorting the file sizes, where n is the number of files.

    # List to store the folders (represented as a list of tuples (file_name, size))
    folders = []  # O(1)
    
    # Min-heap to track the remaining capacity of folders
    heap =[]   # O(1)
    
    heapq.heapify(heap)
    
    for file_name, size in sorted_files:  # O(n)
     
      
        if heap:  # O(1)
        

            # Pop the folder with the largest remaining capacity
            remaining_capacity, folder_index = heapq.heappop(heap)  # O(log k)
           

            # If the file fits in the folder
            if remaining_capacity >= size:  # O(1)
               
                # Add file to the folder
                folders[folder_index].append((file_name, size))  # O(1)
              
                remaining_capacity -= size  # O(1)
                # Update the remaining capacity
             

                # Push the updated folder back into the heap
                heapq.heappush(heap, (remaining_capacity, folder_index))  # O(log k)
               

            else:
                # File does not fit in any existing folder, create a new folder
                new_folder_index = len(folders)  # O(1)
               

                folders.append([(file_name, size)])  # O(1)
             

                # Push the new folder's remaining capacity into the heap
                heapq.heappush(heap, (folder_capacity - size, new_folder_index))  # O(log k)
              
        else:  # O(1)
            # No folders yet, create the first folder
            new_folder_index = len(folders)  # O(1)
            
            folders.append([(file_name, size)])  # O(1)
           

            # Push the new folder's remaining capacity into the heap
            heapq.heappush(heap, (folder_capacity - size, new_folder_index))  # O(log k)
         

    return folders  # O(1)
    

# _____________________________________ Time Complexity_____________________________________#
# 1. Sorting files: O(n log n)
# 2. For each file (n iterations):
#    - Popping and pushing from the heap: O(log k)
# Total: O(n log n + n log k), simplified as O(n log n + n log k).

# _____________________________________ Worst-Case Complexity_____________________________________#
# The worst-case time complexity happens when:
# 1. Each file is placed in its own folder because no file fits into any existing folder.
# 2. This leads to the following operations:
#    - Sorting the files: O(n log n)
#    - For each file (n iterations), we are performing heap operations (popping and pushing):
#      - Popping and pushing from the heap: O(log n) since the maximum number of folders will be n.
# Total worst-case time complexity: O(n log n + n log n) = O(n log n).

# _____________________________________Space Complexity_____________________________________#
# 1. Storing folders: O(m), where m is the total number of folders.
# 2. Storing files: O(n), where n is the number of files.
# 3. Heap storage: O(k), where k is the maximum number of folders in the heap at any time.
# Total: O(n + m + k).


