import os

# Function to load filtered ecDNA rows
def load_ecDNA(filename):
    # list of tuples of (chrom, start, end, count) for each ecDNA
    ecDNA = []
    with open(filename, 'r') as f:
        for line in f:
            row = line.strip().split('\t')
            chrom = row[0]
            start = int(row[1])
            end = int(row[2])
            ecDNA.append((chrom, start, end))
    return ecDNA

# Function to load gene file
def load_genes(filename):
    # list of tuples of (txStart, txEnd) for each gene
    genes = []
    with open(filename, 'r') as f:
        # first line is a header
        next(f)
        for line in f:
            row = line.strip().split('\t')
            chrom = row[1]
            start = int(row[3])
            end = int(row[4])
            genes.append((chrom, start, end))
    return genes

# Function to check if a gene overlaps with an ecDNA
# Returns True if there is overlap, returns False if not
def check_overlap(gene_start, gene_end, ec_start, ec_end):
    if gene_start >= ec_start and gene_start <= ec_end:
        return True
    elif gene_end >= ec_start and gene_end <= ec_end:
        return True
    else:
        return False

# Load the filtered ecDNA rows
ecDNA_file = 'combined_bed_file.bed' # change relative path if needed
ecDNAs = load_ecDNA(ecDNA_file)

# Load the gene file
genes_file = 'ucsc_genes.txt' # change relative path if needed
genes = load_genes(genes_file)

# Output file for filtered intervals
output_file = 'all_non_gene_ecDNA_rows'

# Open the output file
with open(output_file, 'w') as outfile:
    # Iterate through each ecDNA, only keep if doesn't have any overlapping genes
    for ecDNA in ecDNAs:
        ec_chrom = ecDNA[0]
        ec_start = ecDNA[1]
        ec_end = ecDNA[2]
        # var to keep track of if there is ever an overlap
        overlap = False
        for gene in genes:
            gene_chrom = gene[0]
            # only check for overlaps with genes in the same chromosome
            if gene_chrom == ec_chrom:
                gene_start = gene[1]
                gene_end = gene[2]
                if check_overlap(gene_start, gene_end, ec_start, ec_end) == True:
                    overlap = True
                    break
        # if there was never an overlap -> keep this ecDNA
        if overlap == False:
            # Convert ecDNA tuple to tab-delimited string
            ecDNA = '\t'.join(map(str, ecDNA))
            outfile.write(f"{ecDNA}\n")
