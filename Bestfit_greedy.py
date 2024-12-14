import heapq 

def best_fit_greedy(file_sizes, folder_capacity): 
    
    # Sort files in dec order 
    sorted_files = sorted(file_sizes.items(), key=lambda x: x[1], reverse=True)

    # tracking the remaining capacities of the folders
    heap = []
    # List to store the actual folders
    folders = []
    
    for file_name, size in sorted_files:
     # (Greedy choice):Trying to fit the file into an existing folder
        if heap and heap[0][0] >= size:
            # Subproblem:Finding the best existing folde
            remaining_capacity, folder_index = heapq.heappop(heap)
            remaining_capacity -= size
            folders[folder_index][file_name] = size
            heapq.heappush(heap, (remaining_capacity, folder_index))
        else:
            #(Greedy choice):Create a new folder if no existing folder can fit the file
            new_remaining = folder_capacity - size
            folder_index = len(folders)
            folders.append({file_name: size})
            heapq.heappush(heap, (new_remaining, folder_index))

    return folders
