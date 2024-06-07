# Function to load frequent intervals file
def load_intervals(filename):
    # list of tuples of (chrom, start, end, count) for each ecDNA
    ecDNA = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip().split('\t')
            chrom = row[0]
            start = int(row[1])
            end = int(row[2])
            count = int(row[3])
            ecDNA.append((chrom, start, end, count))
    return ecDNA

# Load the frequent intervals
freq_intervals = 'filtered_frequency_matrix_500k' # change relative path if needed
intervals = load_intervals(freq_intervals)

# sort by chromosome
intervals.sort(key=lambda a: (a[0], -a[3], a[1], a[2]))

# Output file for filtered intervals
# currently contains frequent intervals from bin size 500k and count threshold >=4
output_file = 'freq_intervals_sorted'

# Open the output file
with open(output_file, 'w') as outfile:
    for interval in intervals:
        # Convert ecDNA tuple to tab-delimited string
        interval = '\t'.join(map(str, interval))
        outfile.write(f"{interval}\n")