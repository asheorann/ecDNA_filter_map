![project_status](https://img.shields.io/badge/project%20status-stable-green)
![python](https://img.shields.io/badge/python-3.9.5-green)
# Frequencies of Genomic Regions in ecDNA BED Files
We are visualizing frequencies of genome regions in the BED files using a web framework trying to accomplish these tasks below:
1. Mine the data file to identify all genomic regions that participate in ecDNA formation
2. Plot these regions on the cartoon of a genome map
3. Identify the most frequent regions and genes that are on those intervals
4. Identify large genomic segments that are part of ecDNA bud do not contain genes
5. Try and identify any functional regions

## Table of Contents
* Installation Instructions
* Our Data
* Credits

 **_NOTE:_**  All citation and resources are located in the Credits.md file

Frequency_matrix has a 3 columns, the chromosome, the start positions (all at intervals currently set to 2,000,000) and the count at the interval.

In order to generate matrices at different intervals, change the intervl length in the get_freq.py file and it will create a new frequency_matrix file!
