# MEMUAT MODEL

# Import library streamlit
import streamlit as st
# Import library pickle file ekstensi .pkl
import pickle

# Memuat model drug_classifier
with open('./drug_classifier/drug_classifier.pkl', 'rb') as file:
    model = pickle.load(file) #cek

# Tampilan judul dan kata pengantar
st.write("""
    # Drug Classifier App

    Memberikan obat yang tepat untuk pasien dengan data Umur, Jenis Kelamin, Tekanan Darah, Kolesterol,  Rasio Sodium dan Potasium dalam Darah
""")

# form input user
st.write("""
    ##### Masukkan data pasien
""")
umur = st.number_input('Umur', 0, value=25)
kelamin = st.radio('Jenis Kelamin', ['Laki-laki', 'Perempuan'])
darah = st.radio('Tekanan Darah', ['Rendah', 'Normal', 'Tinggi'])
kol = st.radio('Kolesterol', ['Normal', 'Tinggi'])
Na_to_K = st.number_input('Rasio Sodium dan Potasium dalam Darah', 0, value=15)

# Encoding Jenis Kelamin
if kelamin == 'Laki-laki' :
    kelamin = 1
else:
    kelamin = 0

# Encoding Tekanan Darah
if darah == 'Rendah' :
    darah = 1
elif darah == 'Normal' :
    darah = 2
else:
    darah = 3

# Encoding Kolesterol
if kol == 'Normal' :
    kol = 1
else:
    kol = 0

st.write("""
    ##### Prediksi
    Obat : 
""", '**', model.predict([[umur, kelamin, darah, kol, Na_to_K]])[0], '**')
