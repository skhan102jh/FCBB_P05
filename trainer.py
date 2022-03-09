import sys
import argparse

# Method to update counts in table given nucleotide and position 
def update_IMM(nucleotide, index, imm): 
    if (nucleotide == 'A'):
        imm[0][index] += 1
    if (nucleotide == 'C'):
        imm[1][index] += 1
    if (nucleotide == 'G'):
        imm[2][index] += 1
    if (nucleotide == 'T'):
        imm[3][index] += 1

# Make formatted imm model 
def format_imm(imm): 
    # Calculate number of data points
    num_samples = 0
    for i in range(len(imm)): 
        num_samples += imm[i][0]
    # Put counts into fraction form             
    for i in range(len(imm)):
        for j in range(len(imm[0])):
            imm[i][j] = str(imm[i][j]) + "/" + str(num_samples)

# Output a row of imm data to the correct outfile file format
def write_formatted_imm_line(output_file, nucleotide, arr_row):
    output_file.write(nucleotide)
    for element in arr_row: 
        output_file.write("\t" + element)
    output_file.write("\n")

# SET UP PARSING FOR COMMAND LINE
parser = argparse.ArgumentParser(description='Creating IMM from Training Data')
parser.add_argument('-f', '--traindata', required=True, help='Training data file')
parser.add_argument('-o', '--outputfile', required=True, help='Output file')
args = parser.parse_args()


traindata = open(args.traindata)

rows, cols = (4, 6)
imm = [[0 for i in range(cols)] for j in range(rows)]
for line in traindata:
    line = str.strip(line) 
    for i in range(len(line)): 
        update_IMM(line[i], i, imm)
format_imm(imm)

# Write the IMM to the specified output file 
output_file = open(args.outputfile,"w+")
output_file.write("Position\t1\t2\t3\t4\t5\t6\n")
write_formatted_imm_line(output_file, 'A', imm[0])
write_formatted_imm_line(output_file, 'C', imm[0])
write_formatted_imm_line(output_file, 'G', imm[0])
write_formatted_imm_line(output_file, 'T', imm[0])
