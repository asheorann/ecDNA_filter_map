input_filename = 'filtered_frequency_matrix_500k'  # Replace with the name of your input file

total_sum = 0

# Open the input file and read each line
with open(input_filename, 'r') as infile:
    for line in infile:
        # Split the line into columns
        columns = line.strip().split('\t')
        # Extract the value from the last column and add it to the total sum
        count = int(columns[3])
        total_sum += count

print(f'Total sum of the last column: {total_sum}')
