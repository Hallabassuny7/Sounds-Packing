def folder_filling(files, folder_capacity):
    # dp function returns two things:
    # 1) Maximum value obtained by including or not including the current file
    # 2) List of files used to achieve this maximum value

    def dp(names, index, remaining_duration, memo):                                                          #O(n*D)
        # Base case
        if index == len(names) or remaining_duration == 0:                                                   #len() is O(1)      -> O(1)
            return 0, []                                                                                     #                   -> O(1)
        
        # Check if result is already computed and stored in memo
        if (index, remaining_duration) in memo:                                                              #                   -> O(1)
            return memo[(index, remaining_duration)]                                                         #                   -> O(1)
        
        file_name = names[index]                                                                             #                   -> O(1)
        file_duration = files[file_name]                                                                     #                   -> O(1)
        
        # leave_value is the maximum value obtained by not including this file
        # leave_files is the list of files used to achieve leave_value
        leave_value, leave_files = dp(names, index + 1, remaining_duration, memo)                             
        take_value, taken_files = 0, []
        
        if file_duration <= remaining_duration:                                                              #O(1)
            # take_value is the maximum value obtained by including this file
            # take_files is the list of files used to achieve take_value
            take_value, taken_files = dp(names, index + 1, remaining_duration - file_duration, memo)
            take_value += file_duration                                                                      #O(1)
            taken_files = [(file_name, file_duration)] + taken_files                                         #O(1)
        
        # Choose the better option: including or not including the current file
        if leave_value > take_value:                                                                         #O(1)
            memo[(index, remaining_duration)] = (leave_value, leave_files)                                   #O(1)
        else:
            memo[(index, remaining_duration)] = (take_value, taken_files)                                    #O(1)
           #names.remove(file_name)                                                                          #O(1)
        return memo[(index, remaining_duration)]                                                             #O(1)
    
    # Main logic of folder filling function
    folders = []
    files_names = list(files.keys())
    
    while files_names:                                                                                       #O(n)
        memo = {}
        # Get the best subset of files for the current folder capacity
        _, files_in_a_folder = dp(files_names, 0, folder_capacity, memo)                                     #O(n*D)
        if not files_in_a_folder:                                                                            #O(1)
            break                                                                                            #O(1)
        folders.append(files_in_a_folder)                                                                    #O(1)
        
        # Remove the files that have been added to the current folder
        for file_name, _ in files_in_a_folder:                                                               #O(k)
            files_names.remove(file_name)                                                                    #O(n)
                                                                                                            #for loop complexity -> O(n*k)
    return folders                                                                                           #O(1)
    #Assume that k = 1, this is the worst case scenario that at each iteration we only remove 1 file so the n is reduced slowly
    #if k > 1 this means that n is reduced faster. So, when k = 1 the time complexity is upper bounded by O(n)

    # Total Time complexity of while loop : (O(n*D) + O(n))*O(n) = O(n^2 * D) + O(n^2) = O(n^2 * D)

# Time complexity of dp function without memoization: T(n) = 2T(n-1) + O(1)   -> O(2^n)
# Time complexity of dp function with memoization:    O(n*D)
