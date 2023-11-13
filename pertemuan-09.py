import streamlit as st

st.title("Kuliah Praktik Big Data")
st.write("chika")
st.write("# Heading 1") 
st.write("## Heading 2") 
st.write("### Heading 3")

pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2) 

Makanan = st.radio('Makanan kesukaan',['Bakso', 'Nasi goreng', 'Mie ayam'])

st.write(Makanan)

Minuman = st.selectbox('Pilih minuman yang akan dipesan', ['Es teh', 'Kopi', 'Jus'])

st.write(Minuman)

Bayar = st.multiselect('Bayar pakai:', ['Tunai', 'Ovo','Gopay'])

st.write(Bayar)
