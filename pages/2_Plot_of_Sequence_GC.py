import streamlit as st
import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import argparse
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title("Sequence GC% Plot")

# File upload
uploaded_file = st.file_uploader("Upload", type=["fasta"], help="**Input:** FASTA File.\n\n**Output:** PNG of Sequence GC% Plot")

# Function to plot GC content via Plotly
def plot_gc_content_plotly(input_file):
    gc_values = sorted(
        100 * gc_fraction(rec.seq) for rec in SeqIO.parse(input_file, "fasta")
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=list(range(1, len(gc_values)+1)), y=gc_values, mode="lines", name="GC%"))
    fig.update_layout(
        title="%i sequences\nGC%% %0.1f to %0.1f" % (len(gc_values), min(gc_values), max(gc_values)),
        xaxis_title="Genes",
        yaxis_title="GC%",
        yaxis2=dict(title="GC%", overlaying="y", side="right")
    )
    
    return fig

# File Processing
if uploaded_file is not None:
    run_button = st.button("Run", help="Generating Plot")
    if run_button:
        with st.spinner("Running"):
            temp_file_path = "temp.fasta"
            
            with open(temp_file_path, "wb") as temp_file:
                temp_file.write(uploaded_file.read())
            
            # Generate Plotly figure
            fig = plot_gc_content_plotly(temp_file_path)
            st.plotly_chart(fig)
            
            # Download plot
            st.markdown("---")
            st.markdown("### Download")
            
            # Save plot to BytesIO object
            output_buffer = BytesIO()
            fig.write_image(output_buffer, format="png")
            
            st.download_button(
                label="Download Sequence GC Plot",
                data=output_buffer.getvalue(),
                file_name="sequenceGC_plot.png",
                mime="image/png",
            )
