import FileHandling
import os


def look_ahead(folders, sound, folder_capacity):  #complexity: O(k)
    bestFolder = None  #complexity:O(1)
    min_remaining_space=folder_capacity #complexity:O(1)

    for i, (capacity, _) in enumerate(folders): #complexity:O(k) , where k is the number of folders
        remaining_space=folder_capacity-capacity #complexity:O(1)

        if remaining_space>=sound[1] and remaining_space<min_remaining_space: #complexity:O(1)
            bestFolder= i #complexity:O(1)
            min_remaining_space=remaining_space #complexity:O(1)

    return bestFolder #complexity:O(1)

def pack(sounds: dict[str, int], folder_capacity: int) -> list[list[tuple[str, int]]]:
    folders = []  # Complexity: O(1)
    sorted_items = sorted(sounds.items(), key=lambda item: item[1], reverse=True)  # Complexity: O(nlogn)

    
    for sound in sorted_items: # Complexity: O(n*k) where n is the total number of sounds
        placed = False  #comlexity:O(1)
        bestFolder=look_ahead(folders,sound,folder_capacity) #complexity:O(k) 

        if bestFolder is not None: #complexity:O(1)
            capacity, content = folders[bestFolder] #complexity:O(1)
            folders[bestFolder] = (capacity + sound[1], content + [sound]) #complexity:O(1)
            placed = True #complexity:O(1)
      
        if not placed: #complexity:O(1)
            folders.append((sound[1], [sound])) #complexity:O(1)

    # Convert to list of lists of tuples format
    return [folder[1] for folder in folders]#complexity: O(k)


#total complexity: O(nlogn) + O(n*k) + O(k) = O(nlogn)+ O(n*k)

# Test case execution logic
if __name__ == "__main__":
    folder_capacity = 100
    packed_folders = None

    # Determine which test case to execute
    if FileHandling.workingOn_testcase == 1:
        source = r"./Sample Tests/Sample 1/INPUT/Audios"
        tracks_dict = FileHandling.t1  # Audio metadata
    elif FileHandling.workingOn_testcase == 2:
        source = r"./Sample Tests/Sample 2/INPUT/Audios"
        tracks_dict = FileHandling.t2
    elif FileHandling.workingOn_testcase == 3:
        source = r"./Sample Tests/Sample 3/INPUT/Audios"
        tracks_dict = FileHandling.t3
    else:
        source = r"./Complete Tests/Complete1/Audios" 
        tracks_dict=FileHandling.t4   

    try:
        audio_files = os.listdir(source)
    except FileNotFoundError:
        print(f"Directory not found: {source}")
        exit(1)

    # Process the audio metadata
    if tracks_dict:
        packed_folders = pack(tracks_dict, folder_capacity)
