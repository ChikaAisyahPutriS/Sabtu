import streamlit as st

# Ini bagian heading aplikasi Streamlit
st.title("Kuliah Praktik Big Data")
st.write("chika")
st.write("# Heading 1") 
st.write("## Heading 2")
st.write("### Heading 3")
#kira-kira max 6 heading

#Kinerja unit
st.metric("Kinerja", 40, -1)
st.metric("Response Time", 30, 20)
st.metric("Saham", 100,20)

#Pilihan
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2) 

"""
Ini untuk memunculkan text
"""

Makanan = st.radio('Makanan kesukaan',['Bakso', 'Nasi goreng', 'Mie ayam'])

st.write(Makanan)

Minuman = st.selectbox('Pilih minuman yang akan dipesan', ['Es teh', 'Kopi', 'Jus'])

st.write(Minuman)

Bayar = st.multiselect('Bayar pakai:', ['Tunai', 'Ovo','Gopay'])

st.write(Bayar)
