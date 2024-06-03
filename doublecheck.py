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
directory_path = "/Users/anush/OneDrive/Documents/uni2023to2024/spring!/cse_182/ecDNAbedfiles"

# Get the count of "chr8" rows
chr8_count = count_chr8_in_bed_files(directory_path)
print(f"Total number of 'chr8' rows: {chr8_count}")

def count_and_sum_chr8_from_file(file_path):
    chr8_count = 0
    chr8_sum = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            # Check if the line contains "chr8"
            if columns[0] == "chr8":
                chr8_count += 1
                chr8_sum += int(columns[-1])
                
    return chr8_count, chr8_sum

# Path to the uploaded file
file_path = 'frequency_matrix_1mb'

# Get the count and sum of "chr8" rows
chr8_count, chr8_sum = count_and_sum_chr8_from_file(file_path)
chr8_count, chr8_sum
print(chr8_count,chr8_sum)
