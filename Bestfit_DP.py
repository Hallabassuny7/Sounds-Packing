
def best_fit_DP(file_sizes, folder_capacity):#The bottom-up approach
   
    files = list(file_sizes.items())
    n = len(files)
    
    files.sort(key=lambda x: x[1], reverse=True)  

    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: no files, no folders

    for i in range(1, n + 1):  
        for j in range(1, n + 1): 
            
            if files[i - 1][1] <= folder_capacity:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1) #take (Adding the File to the Current Folder)

        
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)  #leave (Moving the File to a New Folder)

    #  backtracking the solution (Folder assignments)
    folders = []
    folder_index = 0
    for i in range(1, n + 1):
        folder = {}
        for j in range(folder_index, n + 1):
            folder[files[i - 1][0]] = files[i - 1][1]
            folder_index = j + 1
        folders.append(folder)

    return folders
