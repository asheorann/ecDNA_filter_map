import os

'''
Function: This is our function to keep track of the min starting point and the maximum ending point
'''
def update_min_max(chromosome, min_start, max_end):
    # Keep track of the minimum starting position
    if chromosome[0] is None or min_start < chromosome[0]:
        chromosome[0] = min_start
    # Keep track of the maximum ending position
    if chromosome[1] is None or max_end > chromosome[1]:
        chromosome[1] = max_end

'''
Function: This function allows us to process the BED files are retrieve the information we need.
This includes the chromosome number, the starting position, and the ending position.
'''
def process_files(directory):
    chromosome_dict = {} # Will hold the starting/ending positions of each chromosome
    co=0
    for file_name in os.listdir(directory):
        # Retrives the bed files
        if file_name.endswith(".bed"):  # You can adjust the extension as needed
            with open(os.path.join(directory, file_name), 'r') as file:
                for line in file:
                    # These files are tab separated
                    columns = line.strip().split('\t')

                    # Filters out the information to be added to the dictionary of list
                    chromosome = columns[0]
                    print(chromosome)
                    start = int(columns[1]) # Typecast the string to an int
                    end = int(columns[2]) # Typecast the string to an int

                    if chromosome not in chromosome_dict:
                        chromosome_dict[chromosome] = [None, None]
                    
                    # Update the min start and max end for every file we check
                    if chromosome=='chr8':
                        co+=1
                    update_min_max(chromosome_dict[chromosome], start, end)
    print("COUNT:", co)
    return chromosome_dict

# Example usage
directory = '/Users/anush/OneDrive/Documents/uni2023to2024/spring!/cse_182/ecDNAbedfiles'  # Replace with your actual directory path
chromosome_dict = process_files(directory)
#print(chromosome_dict)

# Define the interval length
interval_length = 50000

# Initialize the dictionary
intervals_dict = {}

# Function to initialize the intervals
def initialize_intervals(start, end, interval_length):
    intervals = []
    for position in range(start, end + 1, interval_length):
        intervals.append([position, 0])
    return intervals

# Initialize intervals for each chromosome
for chrom, (start, end) in chromosome_dict.items():
    intervals_dict[chrom] = initialize_intervals(start-1, end+1, interval_length)
    if chrom == 'chr1':
        print(len(intervals_dict[chrom]))
        print("START",start-end)

# Print the initialized dictionary
#print(intervals_dict['chr22'])
#print(len(intervals_dict['chr22']))
#for chrom, intervals in intervals_dict.items():
 #   print(f"{chrom}: {intervals}")

#==================================================

# Define the source directory containing the BED files
source_dir = '/Users/anush/OneDrive/Documents/uni2023to2024/spring!/cse_182/ecDNAbedfiles'  # Replace with the path to your ecDNAbedfiles directory

# Define the interval length
interval_length = 50000

# Function to update the intervals with counts from BED files
def update_intervals_from_bed(filepath):
    countchromone=0
    with open(filepath, 'r') as file:
        for line in file:
            columns = line.strip().split('\t')
            chrom = columns[0]
            if chrom=='chr1':
                countchromone+=1 
            start = int(columns[1])
            end = int(columns[2])
            if chrom in intervals_dict:
                index = ((end-start) // interval_length)
                #if index<len(intervals_dict[chrom]):
                intervals_dict[chrom][index][1] += 1
                #if chrom=='chr1' and index>len(intervals_dict[chrom]):
                 #   print("This index is out of bounds",index)
        return countchromone  
        print("count of one", countchromone)
# Iterate through each file in the source directory
count=0
for filename in os.listdir(source_dir):
    if filename.endswith('.bed'):
        filepath = os.path.join(source_dir, filename)
        count += update_intervals_from_bed(filepath)
print("total count", count)

# Example to print the updated intervals dictionary for a specific chromosome
#print(intervals_dict['chr22'])
#print(len(intervals_dict['chr22']))

'''
This is our code to write our frequencymatrix into a new file
'''
# Define the output file path
output_file = 'frequency_matrix_50k'

# Function to write intervals_dict to a file
def write_intervals_to_file(output_file, intervals_dict):
    with open(output_file, 'w') as file:
        for chrom, intervals in intervals_dict.items():
            for interval in intervals:
                start = interval[0]
                count = interval[1]
                file.write(f"{chrom}\t{start}\t{count}\n")

# Write the intervals_dict to the output file
write_intervals_to_file(output_file, intervals_dict)
