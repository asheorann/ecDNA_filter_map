import os

def count_chr8_in_bed_files(directory):
    chr8_count = 0
    
    # List all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a BED file
        if filename.endswith(".bed"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    # Check if the line contains "chr8"
                    if line.startswith("chr8"):
                        chr8_count += 1
                        
    return chr8_count

# Specify the directory containing BED files
directory_path = "/Users/jung/Documents/GitHub/ecDNA_filter_map/ecDNAbedfiles"

# Get the count of "chr8" rows
chr8_count = count_chr8_in_bed_files(directory_path)
print(f"Total number of 'chr8' rows: {chr8_count}")
