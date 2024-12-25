import os
import concurrent.futures
from FileHandling import FileHandlingClass


def process_sound(name, duration_to_process): #complexity: O(1)
    """Mock process a sound file and print what would be done."""
    print(f"Processing {name} for {duration_to_process} seconds.") #complexity: O(1)

def fractional_packing(tracks, total_duration_available): #complexity: O(nlogn) + O(n) + O(k*n)

    sortedtracks = sorted(tracks.items(), key=lambda item: item[1], reverse=True) #complexity: O(nlogn)
    print(sortedtracks) #complexity: O(n)
    # List to store packed folders
    folders = []  #complexity: O(1)
    # Tracks in the current folder
    current_folder_tracks = []  #complexity:O(1)
    current_folder_duration = 0  #complexity:O(1)

    for sound_name, duration in sortedtracks: #complexity: O(n)
        if current_folder_duration + duration <= total_duration_available: #complexity: O(1)
            current_folder_tracks.append((sound_name, duration)) #complexity: O(1)
            current_folder_duration += duration #complexity: O(1)
        else:
            # calculates the fraction of the track that can fit into the remaining folder capacity.
            fraction_to_fit = (total_duration_available - current_folder_duration) / duration #complexity: O(1)
            fraction_duration = duration * fraction_to_fit #complexity: O(1)
            current_folder_tracks.append((sound_name, fraction_duration))  #complexity: O(1)
            
            # Store the remaining part in a new folder
            remaining_duration = duration - fraction_duration #complexity: O(1)
            folders.append(current_folder_tracks)  #complexity: O(1)
            current_folder_tracks = [(sound_name, remaining_duration)]  #complexity: O(1)         # Start new folder
            current_folder_duration = remaining_duration #complexity: O(1)          # Reset folder duration

    # Add the last folder if it has any tracks
    if current_folder_tracks: #complexity: O(1)
        folders.append(current_folder_tracks) #complexity: O(1)

    # Calculate fractions for each folder
    split_fractions = [] #complexity: O(n)
    for folder_tracks in folders: #complexity: O(k*n) , k is the number of iterations
        for track in folder_tracks: #complexity: O(n)
            fraction = track[1] / total_duration_available  #complexity: O(1)
            split_fractions.append((track[0], fraction)) #complexity: O(1)

    # Initialize ThreadPoolExecutor with the number of CPU cores, with: ensures proper cleanup of resources after block is exited
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor: #complexity: O(n)
        #list of objects representing the execution of async tasks
        futures = [
            executor.submit(
                process_sound,
                entry[0],
                #duration to process
                entry[1] * total_duration_available,
            )
            #submit the task for each entry
            for entry in split_fractions
        ] #complexity: O(n)
        for future in concurrent.futures.as_completed(futures): #complexity: O(n)
            future.result() #complexity: O(1)

    print("All tasks completed.") #complexity: O(1)
    return folders #complexity: O(1)

#total complexity: o(nlogn) + o(k*n) + o(n)= o(nlogn) + o(k*n) 
#worst case: number of files= number of folders, complexity= o(nlogn) + o(n^2)= o(n^2)

# Test case execution logic
if __name__ == "__main__":
    folder_capacity = 100
    packed_folders = None

fileHandling=FileHandlingClass()    

if fileHandling.working_on_testcase == 1:
        source = r"./Sample Tests/Sample 1/INPUT/Audios"
        tracks_dict = fileHandling.t1  # Access t1 from complete_scenario
elif fileHandling.working_on_testcase == 2:
        source = r"./Sample Tests/Sample 2/INPUT/Audios"
        tracks_dict = fileHandling.t2  # Access t2 from complete_scenario
elif fileHandling.working_on_testcase == 3:
        source = r"./Sample Tests/Sample 3/INPUT/Audios"
        tracks_dict = fileHandling.t3  # Access t3 from complete_scenario
elif fileHandling.working_on_testcase == 4:
        source = r"./Complete Tests/Complete1/Audios"
        tracks_dict = fileHandling.t4  # Access t4 from complete_scenario
elif fileHandling.working_on_testcase == 5:
        source = r"./Complete Tests/Complete2/Audios"
        tracks_dict = fileHandling.t5  # Access t5 from complete_scenario    

    # Ensure the directory contains the expected audio files
try:
        audio_files = os.listdir(source)
except FileNotFoundError:
        print(f"Directory not found: {source}")
        exit(1)

    # Process each audio file
if tracks_dict:  # Only process if tracks_dict is not None
        packed_folders = fractional_packing(tracks_dict, folder_capacity)

    # Print the results
if packed_folders:  # Only print if packed_folders has been assigned
        for i, folder in enumerate(packed_folders):
            print(f"Folder {i + 1}: {folder}")
