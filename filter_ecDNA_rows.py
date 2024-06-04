import os

# Function to load intervals from a file
def load_intervals(filename):
    intervals = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('\t')
            chromosome = parts[0]
            start = int(parts[1])
            end = int(parts[2])
            count = int(parts[3])  # if needed, else ignore
            intervals.append((chromosome, start, end, count))
    return intervals

# Function to check if a position falls within an interval
def position_in_intervals(chromosome, position, intervals):
    for interval in intervals:
        if chromosome == interval[0] and interval[1] <= position <= interval[2]:
            return True
    return False

# Load the 47 intervals
intervals_file = 'filtered_frequency_matrix_500k'  # Replace with the name of your intervals file
intervals = load_intervals(intervals_file)

# Directory containing ecDNA bed files
bed_files_directory = 'ecDNAbedfiles'  # Replace with the actual directory containing BED files

# Output file for filtered intervals
output_file = 'filtered_ecDNA_rows'

# Open the output file
with open(output_file, 'w') as outfile:
    # Iterate through each BED file in the directory
    for bed_filename in os.listdir(bed_files_directory):
        if bed_filename.endswith('.bed'):  # Process only BED files
            bed_filepath = os.path.join(bed_files_directory, bed_filename)
            with open(bed_filepath, 'r') as bedfile:
                for line in bedfile:
                    parts = line.strip().split('\t')
                    bed_chromosome = parts[0]
                    bed_start = int(parts[1])
                    
                    # Check if the row falls within any of the 47 intervals
                    if position_in_intervals(bed_chromosome, bed_start, intervals):
                        # Write the matching row to the output file
                        outfile.write(line)
