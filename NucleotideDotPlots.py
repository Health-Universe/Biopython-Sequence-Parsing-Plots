import argparse
from Bio import SeqIO
import pylab

# Argument parsing
parser = argparse.ArgumentParser(description="Create a dot plot from two FASTA sequence files.")
parser.add_argument("fasta1", help="Path to the first FASTA sequence file")
parser.add_argument("fasta2", help="Path to the second FASTA sequence file")
parser.add_argument("--window", type=int, default=7, help="Window size for matching (default: 7)")
args = parser.parse_args()

# Load sequences from the provided FASTA files
with open(args.fasta1) as in_handle:
    rec_one = next(SeqIO.parse(in_handle, "fasta"))

with open(args.fasta2) as in_handle:
    rec_two = next(SeqIO.parse(in_handle, "fasta"))

window = args.window
dict_one = {}
dict_two = {}
for (seq, section_dict) in [
    (rec_one.seq.upper(), dict_one),
    (rec_two.seq.upper(), dict_two),
]:
    for i in range(len(seq) - window):
        section = seq[i : i + window]
        try:
            section_dict[section].append(i)
        except KeyError:
            section_dict[section] = [i]

# Find matching sub-sequences
matches = set(dict_one).intersection(dict_two)
print("%i unique matches" % len(matches))

# Create lists of x and y coordinates for scatter plot
x = []
y = []
for section in matches:
    for i in dict_one[section]:
        for j in dict_two[section]:
            x.append(i)
            y.append(j)

# Create the dot plot using matplotlib
pylab.cla()  # clear any prior graph
pylab.gray()
pylab.scatter(x, y)
pylab.xlim(0, len(rec_one) - window)
pylab.ylim(0, len(rec_two) - window)
pylab.xlabel("%s (length %i bp)" % (rec_one.id, len(rec_one)))
pylab.ylabel("%s (length %i bp)" % (rec_two.id, len(rec_two)))
pylab.title("Dot plot using window size %i\n(allowing no mis-matches)" % window)
pylab.show()
