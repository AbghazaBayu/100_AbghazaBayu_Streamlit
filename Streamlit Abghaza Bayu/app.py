import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi Streamlit
st.set_page_config(page_title='Statistik', layout='wide')

# Fungsi untuk menghasilkan data acak dengan distribusi normal
def generate_data(n_samples):
    np.random.seed(42)
    data = np.random.randn(n_samples)
    return data

# Menghasilkan data acak awal
data = generate_data(1000)

# Sidebar
st.sidebar.title('Geser Sendiri ya !!!')
n_samples = st.sidebar.slider('Pilih Sampelnya', min_value=100, max_value=5000, value=1000, step=100)

# Menghasilkan data baru jika jumlah sampel diubah
if n_samples != len(data):
    data = generate_data(n_samples)

# Menampilkan deskripsi statistik
st.subheader('Tabel Statistik')
stats = pd.DataFrame(data, columns=['Data'])
st.write(stats.describe())

# Visualisasi Histogram
st.subheader('Histogram')
fig, ax = plt.subplots()
ax.hist(data, bins='auto', color='skyblue', alpha=0.7)
ax.set_xlabel('Nilai')
ax.set_ylabel('Frekuensi')
st.pyplot(fig)

# Visualisasi Boxplot
st.subheader('Boxplot')
fig, ax = plt.subplots()
ax.boxplot(data, vert=False)
ax.set_xlabel('Nilai')
st.pyplot(fig)

# Visualisasi Q-Q Plot
st.subheader('Q-Q Plot')
fig, ax = plt.subplots()
ax.set_title('Q-Q Plot')
sorted_data = np.sort(data)
expected_data = np.random.normal(0, 1, n_samples)
ax.plot(expected_data, sorted_data, 'o')
ax.plot([-4, 4], [-4, 4], color='red', linestyle='--')
ax.set_xlabel('Quantiles Teoritis')
ax.set_ylabel('Quantiles Data')
st.pyplot(fig)
