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

def harmonic_partitioning(files, folder_size):
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



def convert_to_seconds(time_str):
    hours, minutes, seconds = time_str.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

def readfile(folderdir):
    file_data = {}
    target_path = os.path.abspath(folderdir)
    with open(target_path, 'r') as file:
        num_entries = int(file.readline().strip())

        for i in range(num_entries):
            line = file.readline().strip()

            filename, time_str = line.split()

            # key = int(filename.split('.')[0])
            key = filename

            value = convert_to_seconds(time_str)

            file_data[key] = value

    return file_data





files=readfile(r"Sample Tests\Sample 1\INPUT\AudiosInfo.txt")
#print(files)
x=harmonic_partitioning(files,100)
print(x)



"""
Expected output:
Folder 1: [{'Track2': 80}]
Folder 2: [{'Track1': 70}]
Folder 3: [{'Track3': 20}, {'Track4': 15}, {'Track5': 15}]

Output:
Folder 1: [('Track2': 80),('Track1': 70)]
Folder 2: 
Folder 3: [('4.mp3', 15)], [('5.mp3', 15)], [('3.mp3', 20)] 
[
[[('1.mp3', 70)], [('2.mp3', 80)]], 
[], 
[[('4.mp3', 15)], [('5.mp3', 15)], [('3.mp3', 20)]]
]
"""

# folders = harmonic_partitioning(files, 100)
# for idx, folder in enumerate(folders, start=1):
#     print(f"Folder {idx}: {folder}")