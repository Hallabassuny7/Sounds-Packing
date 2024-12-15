def folder_filling(files, folder_capacity):
    # dp function returns two things:
    # 1) Maximum value obtained by including or not including the current file
    # 2) List of files used to achieve this maximum value

    def dp(keys, index, capacity, memo):
        # Base case
        if index == len(keys) or capacity == 0:
            return 0, []
        
        # Check if result is already computed and stored in memo
        if (index, capacity) in memo:
            return memo[(index, capacity)]
        
        file_index = keys[index]
        file_size = files[file_index]
        
        # leave_value is the maximum value obtained by not including this file
        # leave_files is the list of files used to achieve leave_value
        leave_value, leave_files = dp(keys, index + 1, capacity, memo)
        take_value, take_files = 0, []
        
        if file_size <= capacity:
            # take_value is the maximum value obtained by including this file
            # take_files is the list of files used to achieve take_value
            take_value, take_files = dp(keys, index + 1, capacity - file_size, memo)
            take_value += file_size
            take_files = [(file_index, file_size)] + take_files
        
        # Choose the better option: including or not including the current file
        if leave_value > take_value:
            memo[(index, capacity)] = (leave_value, leave_files)
        else:
            memo[(index, capacity)] = (take_value, take_files)
        
        return memo[(index, capacity)]
    
    # Main logic of folder filling function
    folders = []
    file_keys = list(files.keys())
    
    while file_keys:
        memo = {}
        # Get the best subset of files for the current folder capacity
        _, files_in_a_folder = dp(file_keys, 0, folder_capacity, memo)
        if not files_in_a_folder:
            break
        folders.append(files_in_a_folder)
        
        # Remove the files that have been added to the current folder
        for file_name, _ in files_in_a_folder:
            file_keys.remove(file_name)
    
    return folders

# Example usage
files = {
    "mp3-1": 70, "mp3-2": 80, "mp3-3": 15, "mp3-4": 20, "mp3-5": 15,
    "mp3-6": 10, "mp3-7": 5, "mp3-8": 5, "mp3-9": 10, "mp3-10": 30
}
folder_capacity = 120
print(folder_filling(files, folder_capacity))
