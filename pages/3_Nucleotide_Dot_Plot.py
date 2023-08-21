import streamlit as st
import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import argparse
from Bio import SeqIO
import pylab

st.title("Nucleotide Dot Plot of Sequences")

# File upload
uploaded_file1 = st.file_uploader("Upload", type=["fasta"], help="**Input:** FASTA Sequence 1 File.\n\n**Output:** PNG of Nucleotide Dot Plot")

uploaded_file2 = st.file_uploader("Upload", type=["fasta"], help="**Input:** FASTA Sequence 2 File.\n\n**Output:** PNG of Nucleotide Dot Plot")

# Function to create a dot plot using Plotly Express
def create_dot_plot(seq1, seq2, window):
    data = []

    for i in range(len(seq1) - window):
        section = seq1[i : i + window]
        if section in seq2:
            for j in range(len(seq2) - window):
                if seq2[j : j + window] == section:
                    data.append({"x": i, "y": j})

    df = pd.DataFrame(data)
    fig = px.scatter(df, x="x", y="y", opacity=0.5)
    fig.update_layout(
        title=f"Nucleotide Dot Plot using window size {window}",
        xaxis_title=f"Sequence 1 (length {len(seq1)} bp)",
        yaxis_title=f"Sequence 2 (length {len(seq2)} bp)",
    )
    return fig

# File Processing
if uploaded_file1 is not None and uploaded_file2 is not None:
    window = st.slider("Window Size", min_value=1, max_value=30, value=7, help="Window size for matching")

    run_button = st.button("Run", help="Generating Dot Plot")
    if run_button:
        with st.spinner("Running"):
            temp_file1_path = "temp_seq1.fasta"
            temp_file2_path = "temp_seq2.fasta"

            with open(temp_file1_path, "wb") as temp_file1:
                temp_file1.write(uploaded_file1.read())

            with open(temp_file2_path, "wb") as temp_file2:
                temp_file2.write(uploaded_file2.read())

            # Load sequences from FASTA files
            with open(temp_file1_path) as in_handle:
                rec_one = next(SeqIO.parse(in_handle, "fasta"))

            with open(temp_file2_path) as in_handle:
                rec_two = next(SeqIO.parse(in_handle, "fasta"))

            # Create dot plot
            fig = create_dot_plot(rec_one.seq.upper(), rec_two.seq.upper(), window)

            # Display Plotly figure using st.plotly_chart
            st.plotly_chart(fig)

            # Save plot to a BytesIO object
            output_buffer = BytesIO()
            fig.write_image(output_buffer, format="png")
            st.markdown("---")
            st.markdown("### Download")
            st.download_button(
                label="Download Nucleotide Dot Plot",
                data=output_buffer.getvalue(),
                file_name="NucleotideDotPlot.png",
                mime="image/png",
            )





