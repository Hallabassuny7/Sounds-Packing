def FirstFit(tracks, DDPF):
    # Sorting the tracks by duration in descending order using Timsort
    sortedtracks = sortduration(tracks)                                                             # O(N log N), Timsort complexity for sorting dictionary items,where N is the number of items in `tracks`

    Folders = []                                                                                    # O(1), 
    FoldersSize = []                                                                                # O(1), 

    for key, value in sortedtracks.items():                                                         # O(N), iterating over all items in the sorted dictionary.
        if len(Folders) == 0:                                                                       # O(1), 
            Folders.append([(key, value)])                                                          # O(1), 
            FoldersSize.append(value)                                                               # O(1), 
        else:
            Found = False                                                                           # O(1), 
            for i in range(len(Folders)):                                                           # O(M), iterating over the existing folders.
                if value <= (DDPF - FoldersSize[i]):                                                # O(1), 
                    Folders[i].append((key, value))                                                 # O(1), 
                    FoldersSize[i] += value                                                         # O(1), 
                    Found = True                                                                    # O(1), 
                    break                                                                           # O(1), 
            if not Found:                                                                           # O(1), 
                Folders.append([(key, value)])                                                      # O(1), 
                FoldersSize.append(value)                                                           # O(1),

    return Folders                                                                                  # O(1),
    # Overall Time Complexity: O(N log N + N × M)
    # - Sorting: O(N log N)
    # - Outer loop over tracks: O(N)
    # - Inner loop over folders: O(M)
    # - Combined looping complexity: O(N × M)
