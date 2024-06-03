import os

def countFromBEDFiles(directory,chr):
    chrCount = 0
    
    # List all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a BED file
        if filename.endswith(".bed"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    # Ensure the line is stripped of leading/trailing spaces and split correctly
                    columns = line.strip().split()
                    if columns and columns[0] == chr:
                        #if chr == columns[0]:
                        #    print(filename)
                        chrCount += 1
                        #print(f"Counted row: {line.strip()}")
                        
    return chrCount

def countFromOurFile(file_path,chr):
    chrSum = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            # Ensure the line is stripped of leading/trailing spaces and split correctly
            columns = line.strip().split()
            if columns and columns[0] == chr:
                try:
                    chrSum += int(columns[-1])
                except ValueError:
                    print(f"Skipping row with invalid number: {line.strip()}")
                #print(f"Summed row: {line.strip()}")
                
    return chrSum

# Path to the uploaded file
file_path = 'frequency_matrix.txt'

# Specify the directory containing BED files
directory_path1 = "/Users/jung/Documents/GitHub/ecDNA_filter_map/ecDNAbedfiles"
directory_path2 = "/Users/jung/Documents/GitHub/ecDNA_filter_map/frequency_matrix.txt"
chr = "chr11"

chrCount = countFromBEDFiles(directory_path1,chr)
print(f"Total number of manually checking rows: {chrCount}")
chrSum = countFromOurFile(directory_path2,chr)
print(f"Total number of our calculated rows: {chrSum}")

