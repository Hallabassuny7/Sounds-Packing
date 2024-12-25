import os

from bisect import bisect_left, insort

def FirstFit_BinarySearch(class_tracks, folder_size):
    FoldersWithSizes = []  # List of tuples: (folder_contents, remaining_space)

    for track_name, track_duration in class_tracks:
        # Extract remaining spaces for binary search
        FoldersRemainingSpace = [remaining_space for _, remaining_space in FoldersWithSizes]

        # Use binary search to find the first folder with enough remaining space
        idx = bisect_left(FoldersRemainingSpace, track_duration)

        if idx < len(FoldersWithSizes) and FoldersWithSizes[idx][1] >= track_duration:
            # Add track to the existing folder
            folder_contents, remaining_space = FoldersWithSizes.pop(idx)  # Remove folder
            folder_contents.append((track_name, track_duration))
            new_folder = (folder_contents, remaining_space - track_duration)
            insort(FoldersWithSizes, new_folder, key=lambda x: x[1])  # Reinsert to maintain sorted order
        else:
            # Create a new folder and insert it in sorted order
            new_folder = ([(track_name, track_duration)], folder_size - track_duration)
            insort(FoldersWithSizes, new_folder, key=lambda x: x[1])  # Maintain sorted order

    # Extract and return just the folder contents
    return [folder_contents for folder_contents, _ in FoldersWithSizes]

def Harmonic_Partitioning(files, folder_size):
    partitions = {
        "large": [],
        "medium": [],
        "small": []
    }

    # Thresholds for partitioning
    large_threshold = folder_size // 2
    medium_threshold = folder_size // 4

    # Categorize files into harmonic classes
    for fileName, fileDuration in files.items():
        if fileDuration > large_threshold:
            partitions["large"].append((fileName, fileDuration))
        elif fileDuration > medium_threshold:
            partitions["medium"].append((fileName, fileDuration))
        else:
            partitions["small"].append((fileName, fileDuration))

    # Sort tracks within each partition
    for partition_name in partitions:
        partitions[partition_name].sort(key=lambda x: x[1], reverse=True)

    # Process each partition using First Fit Binary Search
    all_folders = []
    for partition_name, class_tracks in partitions.items():
        folders = FirstFit_BinarySearch(class_tracks, folder_size)
        all_folders.extend(folders)  # Flatten the list of folders

    return all_folders
