import os
import shutil

# Define the source and destination directories
source_dir = '/Users/anush/OneDrive/Documents/uni2023to2024/spring!/cse_182/ccle_hg38_classification_bed_files'  # Replace with the path to your source directory
destination_dir = '~/Users/anush/OneDrive/Documents/uni2023to2024/spring!/cse_182/ecDNAbedfiles'  # Replace with the desired path to your destination directory

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Iterate through the files in the source directory
for filename in os.listdir(source_dir):
    if 'ecDNA' in filename:
        # Construct full file paths
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        # Move the file to the destination directory
        shutil.move(source_file, destination_file)
        print(f'Moved: {filename}')

print('Filtering complete.')
