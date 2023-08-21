import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt

def plot_sequence_lengths(input_file):
    sizes = [len(rec) for rec in SeqIO.parse(input_file, "fasta")]
    plt.hist(sizes, bins=20)
    plt.title(
        "%i sequences\nLengths %i to %i" % (len(sizes), min(sizes), max(sizes))
    )
    plt.xlabel("Sequence length (bp)")
    plt.ylabel("Count")
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Plot histogram of sequence lengths.")
    parser.add_argument("-f", "--file", required=True, help="Input FASTA file")
    args = parser.parse_args()

    plot_sequence_lengths(args.file)

if __name__ == "__main__":
    main()
