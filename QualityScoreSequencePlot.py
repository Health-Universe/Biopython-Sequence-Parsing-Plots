import argparse
import pylab
from Bio import SeqIO

def plot_fastq_quality(file1, file2):
    for subfigure, filename in enumerate([file1, file2], start=1):
        pylab.subplot(1, 2, subfigure)
        for i, record in enumerate(SeqIO.parse(filename, "fastq")):
            if i >= 50:
                break
            pylab.plot(record.letter_annotations["phred_quality"])
        pylab.ylim(0, 45)
        pylab.ylabel("PHRED quality score")
        pylab.xlabel("Position")
    pylab.show()  # Display the plot in a pop-up window

def main():
    parser = argparse.ArgumentParser(description="Plot PHRED quality scores from two fastq files.")
    parser.add_argument("--file1", required=True, help="Path to the first fastq file")
    parser.add_argument("--file2", required=True, help="Path to the second fastq file")
    args = parser.parse_args()

    plot_fastq_quality(args.file1, args.file2)

if __name__ == "__main__":
    main()
