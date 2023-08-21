import argparse
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import matplotlib.pyplot as plt

def plot_gc_content(input_file):
    gc_values = sorted(
        100 * gc_fraction(rec.seq) for rec in SeqIO.parse(input_file, "fasta")
    )

    plt.plot(gc_values)
    plt.title(
        "%i sequences\nGC%% %0.1f to %0.1f"
        % (len(gc_values), min(gc_values), max(gc_values))
    )
    plt.xlabel("Genes")
    plt.ylabel("GC%")
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Plot GC content of sequences.")
    parser.add_argument("-f", "--file", required=True, help="Input FASTA file")
    args = parser.parse_args()

    plot_gc_content(args.file)

if __name__ == "__main__":
    main()
