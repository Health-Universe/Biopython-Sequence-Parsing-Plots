import streamlit as st

st.title("Sequence Parsing Plots 🧬")

st.divider()

st.markdown("""
    [**Documentation**](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec399) 📖 |
    [**GitHub**](https://github.com/biopython/biopython) 💻
    """)
    
st.markdown("""Different methods of sequence parsing.""")
             
st.markdown("""
- **Home:** You are here!
- **Histogram of Sequence Lengths:** Generate histogram of the length distribution within a sequence dataset.
- **Plot of sequence GC%**: Generate a plot of the calculated quantity of a nucleotide sequence for GC%.
- **Nucleotide Dot Plot:** Generate dot plot to visually compare two nucleotide sequences for similarity to each other
- **Quality Scores of Sequencing Read Data Plot:** Generate plot of sequencing read quality scores for data assessment and analysis.
""")

st.divider()
st.markdown("""App Created by [Health Universe](https://www.healthuniverse.com) 🚀
            (Kinal Patel & Mitchell Parker)""")
