import pandas as pd
import streamlit as st
import altair as alt
# グラフ作成のライブラリ
from PIL import Image
# Python Imaging Library

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"


sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence
sequence = sequence[1:]
sequence
sequence = '\n'.join(sequence)
sequence

st.write("""
***
""")

# Prints the input DNA sequence
st.write('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Print dictionary
st.subheader('1. Print dictionary')


def dna_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d


X = dna_nucleotide_count(sequence)

X_label = list(X)
X_values = list(X.values())

X


# 2. Print text
st.subheader('There are  ' + str(X['A']) + ' adenine (A)')
st.subheader('There are  ' + str(X['T']) + ' thymine (T)')
st.subheader('There are  ' + str(X['G']) + ' guanine (G)')
st.subheader('There are  ' + str(X['C']) + ' cytosine (C)')


# 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)


# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)


p = p.properties(
    width=alt.Step(80)
)

st.write(p)
