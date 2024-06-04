#filtering

#DONE:determine interval length 
#DONE:determine peak threshold 
#DONE:from our frequency matrix this would output a file with a list of chromosomes and intervals (ideally 10-15), 
    #ACTUAL: we counted ~40 peaks for 500k intervals (threshold: >=4), we found that for upto 250k intervals things were more distributed and so 500k seemed appropriate bucketing
#DONE:filter out from all ecDNA files and all ecDNA rows that fall in our 10-15 intervals -> hopefully gives around 300-500
#filter from these 300-500 which ones have no genes falling anywhere in the interval.. so literally take each gene and 
# check if gene start is after ecDNA start or gene end is before ecDNA end, then that ecDNA is removed
#lets see if we get anything

input_filename = 'frequency_matrix_500k_new'
output_filename = 'filtered_frequency_matrix_500k'

# Open the input file and the output file
with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
    for line in infile:
        # Split the line into columns
        columns = line.strip().split('\t')
        # Extract the chromosome, start, and count values
        chromosome = columns[0]
        start = int(columns[1])
        count = int(columns[2])
        
        # Filter rows where the count is 4 or greater
        if count >= 4:
            # Calculate the end position
            end = start + 500000
            # Write the new line to the output file
            outfile.write(f'{chromosome}\t{start}\t{end}\t{count}\n')

