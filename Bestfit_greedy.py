import heapq 

def best_fit_greedy(file_sizes, folder_capacity): 
    # Sort files in descending order by size
    sorted_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)

    # Tracking the remaining capacities of the folders
    heap = []
    # List to store the actual folders
    folders = []
    
    for file_name, size in sorted_files:
        # (Greedy choice): Try to fit the file into an existing folder
        if heap and heap[0][0] >= size:
            # Subproblem: Find the best existing folder
            remaining_capacity, folder_index = heapq.heappop(heap)
            remaining_capacity -= size
            folders[folder_index].append((file_name, size))  # Append file as a tuple
            heapq.heappush(heap, (remaining_capacity, folder_index))
        else:
            # (Greedy choice): Create a new folder if no existing folder can fit the file
            new_remaining = folder_capacity - size
            folder_index = len(folders)
            folders.append([(file_name, size)])  # New folder as a list of tuples
            heapq.heappush(heap, (new_remaining, folder_index))

    return folders
