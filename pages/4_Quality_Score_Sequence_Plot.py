import streamlit as st
import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt
from io import BytesIO

st.title("Quality Scores of Sequencing Read Data Plot")

# File upload
uploaded_file1 = st.file_uploader("Upload FASTQ File 1", type=["fastq"], help="**Input:** FASTQ File.\n\n**Output:** PNG of PHRED Quality Score Plot")
uploaded_file2 = st.file_uploader("Upload FASTQ File 2", type=["fastq"], help="**Input:** FASTQ File.\n\n**Output:** PNG of PHRED Quality Score Plot")

if uploaded_file1 is not None and uploaded_file2 is not None:
    run_button = st.button("Run", help="Generating Plot")
    if run_button:
        with st.spinner("Running"):
            temp_file1_path = "temp_seq1.fastq"
            temp_file2_path = "temp_seq2.fastq"

            with open(temp_file1_path, "wb") as temp_file1:
                temp_file1.write(uploaded_file1.read())

            with open(temp_file2_path, "wb") as temp_file2:
                temp_file2.write(uploaded_file2.read())

            # Load sequences from FASTQ files
            with open(temp_file1_path) as in_handle:
                rec_one = next(SeqIO.parse(in_handle, "fastq"))

            with open(temp_file2_path) as in_handle:
                rec_two = next(SeqIO.parse(in_handle, "fastq"))

            # Create quality score plots using Matplotlib
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 2, 1)
            for i, record in enumerate(SeqIO.parse(temp_file1_path, "fastq")):
                if i >= 50:
                    break
                plt.plot(record.letter_annotations["phred_quality"])
            plt.ylim(0, 45)
            plt.ylabel("PHRED quality score")
            plt.xlabel("Position")
            plt.title("FASTQ File 1")

            plt.subplot(1, 2, 2)
            for i, record in enumerate(SeqIO.parse(temp_file2_path, "fastq")):
                if i >= 50:
                    break
                plt.plot(record.letter_annotations["phred_quality"])
            plt.ylim(0, 45)
            plt.ylabel("PHRED quality score")
            plt.xlabel("Position")
            plt.title("FASTQ File 2")

            plt.tight_layout()

            # Save plot to a BytesIO object
            output_buffer = BytesIO()
            plt.savefig(output_buffer, format="png")
            plt.close()

            # Display the plot
            st.image(output_buffer.getvalue())

            # Download the plot
            st.markdown("---")
            st.markdown("### Download")
            st.download_button(
                label="Download Sequence Quality Score Plot",
                data=output_buffer.getvalue(),
                file_name="SequenceQualityScorePlot.png",
                mime="image/png",
            )
