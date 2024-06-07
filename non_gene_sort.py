from non_gene_ecDNA import load_ecDNA

# Load the filtered ecDNA rows
ecDNA_file = 'all_non_gene_ecDNA_rows' # change relative path if needed
ecDNAs = load_ecDNA(ecDNA_file)

# sort by chromosome
ecDNAs.sort(key=lambda a: (a[0], a[1], a[2]))

# Output file for filtered intervals
output_file = 'all_non_gene_ecDNA_sorted'

# Open the output file
with open(output_file, 'w') as outfile:
    for ecDNA in ecDNAs:
        # Convert ecDNA tuple to tab-delimited string
        ecDNA = '\t'.join(map(str, ecDNA))
        outfile.write(f"{ecDNA}\n")