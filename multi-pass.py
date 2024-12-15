import FileHandling


    
def multi_pass_pack(sounds, folder_capacity): 
    folders = []
    sorted_items = sorted(sounds.items(), key=lambda item: item[1], reverse=True)
    print(sorted_items)
    
    # First Pass: Greedy Packing
    for sound in sorted_items:
        placed = False
        for i, folder in enumerate(folders):
            # Check if the sound can be added to this folder
            if sum(f[1] for f in folder) + sound[1] <= folder_capacity:
                folder.append(sound)
                placed = True
                break
        if not placed:
            # Create a new folder if the sound couldn't be placed
            new_folder = [sound]
            folders.append(new_folder)
    
    # Check for leftovers
    packed_sounds = [sound for folder in folders for sound in folder]
    leftovers = [sound for sound in sorted_items if sound not in packed_sounds]
    
    # Second Pass: Re-assess packing state
    if leftovers:
        for sound in leftovers:
            placed = False
            for folder in folders:
                # Check if the sound can be added to any existing folder
                if sum(f[1] for f in folder) + sound[1] <= folder_capacity:
                    folder.append(sound)
                    placed = True
                    break
            if not placed:
                # Create a new folder if the sound couldn't be placed
                new_folder = [sound]
                folders.append(new_folder)
    
    return folders

# Test case execution logic
if __name__ == "__main__":
    folder_capacity = 100

    # Determine which test case to execute
    if complete_scenario.workingOn_testcase == 1:
        source = r"./Sample Tests/Sample 1/INPUT/Audios"
        packed_folders = multi_pass_pack(FileHandling.t1, folder_capacity)
    elif complete_scenario.workingOn_testcase == 2:
        source = r"./Sample Tests/Sample 2/INPUT/Audios"
        packed_folders = multi_pass_pack(FileHandling.t2, folder_capacity)
    else:
        source = r"./Sample Tests/Sample 3/INPUT/Audios"
        packed_folders = multi_pass_pack(FileHandling.t3, folder_capacity)

    # Print the results
    for i, folder in enumerate(packed_folders):
        print(f"Folder {i + 1}: {folder}")
