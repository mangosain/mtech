import os

# Path to the folder containing images
folder_path = 'dataset/false'

# Initialize count for renaming
count = 0

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (you can modify this to include other formats if needed)
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        # Construct the new file name
        new_name = f'NP_{count}.jpg'
        
        # Build full file paths
        source = os.path.join(folder_path, filename)
        destination = os.path.join(folder_path, new_name)
        
        # Rename the file
        os.rename(source, destination)
        print(f'Renamed: {filename} -> {new_name}')
        
        # Increment the count for the next image
        count += 1

print('Renaming completed.')
