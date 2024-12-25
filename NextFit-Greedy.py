import heapq 

def next_fit_greedy_with_heap(file_sizes, folder_capacity):
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
    

# Example usage
size_tst = {"file1": 70, "file2": 80, "file3": 20, "file4": 15, "file5": 15}  # O(n)
capacity_tst = 100 # O(1)
allocated_folders = next_fit_greedy_with_heap(size_tst, capacity_tst)  # O(n log k)


# Print the result as requested
print("Final folders:", allocated_folders)  # O(m)

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


