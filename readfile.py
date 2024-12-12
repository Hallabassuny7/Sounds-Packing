def convert_to_seconds(time_str):
    hours, minutes, seconds = time_str.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)


# Initialize an empty dictionary to store the data
file_data = {}

# Open the file
with open(r"D:\Faculty\5th_Semester\Algo\Project\testcases\Complete1\AudiosInfo.txt", 'r') as file:
    num_entries = int(file.readline().strip())

    for i in range(num_entries):
        line = file.readline().strip()

        filename, time_str = line.split()

        key = int(filename.split('.')[0])

        value = convert_to_seconds(time_str)

        file_data[key] = value



