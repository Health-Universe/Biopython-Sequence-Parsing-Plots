import streamlit as st
import subprocess
import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import argparse
from Bio import SeqIO

from HistogramOfSequenceLengths import plot_sequence_lengths

st.title("Sequence Length Histogram")

# File upload
uploaded_file = st.file_uploader("Upload", type=["fasta"], help="**Input:** FASTA File.\n\n**Output:** PNG of Sequence Length Histogram")

# File Processing
if uploaded_file is not None:
    run_button = st.button("Run", help="Generating Histogram")
    if run_button:
        with st.spinner("Running"):
            temp_file_path = "temp.fasta"
            
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.read())
            

            sequences = SeqIO.parse(temp_file_path, "fasta")
            seq_lengths = [len(seq) for seq in sequences]
            
            # DataFrame
            data = pd.DataFrame({"Sequence Length (bp)": seq_lengths})
            
            # Interactive histogram via Plotly
            fig = px.histogram(data, x="Sequence Length (bp)", nbins=20, title="Sequence Length Histogram")
            
            # Display the Plotly
            st.plotly_chart(fig)
            
            # Matplotlib figure
            fig, ax = plt.subplots()
            
            # Generate Matplot histogram
            plot_sequence_lengths(temp_file_path)
            
            # Save plot to a BytesIO object
            output_buffer = BytesIO()
            plt.savefig(output_buffer, format="png")
            plt.close()

            # Download plot
            st.markdown("---")
            st.markdown("### Download")
            st.download_button(
                label="Download Sequence Length Histogram",
                data=output_buffer.getvalue(),
                file_name="sequencelength_histogram.png",
                mime="image/png",
            )





