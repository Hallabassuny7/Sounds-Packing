import os
from bisect import bisect_left, insort

# Overall complexity = O(N * (M + log M)) = O(Max (N*M , N log M)) 
def FirstFit_BinarySearch(class_tracks, folder_size):  # O(1): Function definition
    FoldersWithSizes = []  # O(1): Initialize an empty list for folders with their remaining spaces

    for track_name, track_duration in class_tracks:  # O(N): Loop through all tracks where N = number of tracks
        # Extract remaining spaces for binary search
        FoldersRemainingSpace = [remaining_space for _, remaining_space in FoldersWithSizes]  # O(M): Create a list of remaining spaces where M = number of folders

        # Use binary search to find the first folder with enough remaining space
        idx = bisect_left(FoldersRemainingSpace, track_duration)  # O(log M): Binary search for the first suitable folder

        if idx < len(FoldersWithSizes) and FoldersWithSizes[idx][1] >= track_duration:  # O(1): Check if a valid folder was found
            folder_contents, remaining_space = FoldersWithSizes.pop(idx)  # O(M): Remove the folder at the found index
            folder_contents.append((track_name, track_duration))  # O(1): Add the track to the folder
            new_folder = (folder_contents, remaining_space - track_duration)  # O(1): Update folder's remaining space
            insort(FoldersWithSizes, new_folder, key=lambda x: x[1])  # O(M): Reinsert the updated folder into the sorted list
        else:
            # Create a new folder and insert it in sorted order
            new_folder = ([(track_name, track_duration)], folder_size - track_duration)  # O(1): Create a new folder
            insort(FoldersWithSizes, new_folder, key=lambda x: x[1])  # O(M): Insert new folder into the sorted list

    # Extract and return just the folder contents
    return [folder_contents for folder_contents, _ in FoldersWithSizes]  # O(M): Extract folder contents

# Overall complexity = O(N + (K log K) + P * M) ≈ O(N log N + N * M)
def harmonic_partitioning(files, folder_size):  # O(1): Function definition
    partitions = {  # O(1): Initialize partitions dictionary
        "large": [],
        "medium": [],
        "small": []
    }

    # Thresholds for partitioning
    large_threshold = folder_size // 2  # O(1): Compute large threshold
    medium_threshold = folder_size // 4  # O(1): Compute medium threshold

    # Categorize files into harmonic classes
    for fileName, fileDuration in files.items():  # O(N): Loop through all files where N = number of files
        if fileDuration > large_threshold:  # O(1): Check if file belongs to "large" partition
            partitions["large"].append((fileName, fileDuration))  # O(1): Add to "large" partition
        elif fileDuration > medium_threshold:  # O(1): Check if file belongs to "medium" partition
            partitions["medium"].append((fileName, fileDuration))  # O(1): Add to "medium" partition
        else:
            partitions["small"].append((fileName, fileDuration))  # O(1): Add to "small" partition

    # Sort tracks within each partition
    for partition_name in partitions:  # O(1): Loop through partitions
        partitions[partition_name].sort(key=lambda x: x[1], reverse=True)  # O(K log K): Sort each partition (K = number of files in partition)

    # Process each partition using First Fit Binary Search
    all_folders = []  # O(1): Initialize list for all folders
    for partition_name, class_tracks in partitions.items():  # O(3 * P): Loop through partitions (P = average files per partition)
        folders = FirstFit_BinarySearch(class_tracks, folder_size)  # O(P * M): Process partition using First Fit Binary Search
        all_folders.extend(folders)  # O(P): Add partition folders to the result list

    return all_folders  # O(1): Return all folders



