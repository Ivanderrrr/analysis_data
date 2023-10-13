import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Membaca dataset
all_data1 = pd.read_csv("all_data1.csv")
all_data2 = pd.read_csv("all_data2.csv")

# Judul
st.header("Bike Sharing Collection Dashboard")
# Perkembangan Bike Sharing Setiap Bulan (2011)
st.subheader("Perkembangan Bike Sharing Setiap Bulan (2011)")
# Filter data 2011
month_2011 = all_data1[all_data1["dteday"].str.startswith('2011')].groupby(all_data1["dteday"].str[5:7])["cnt"].sum()
# Membuat plot
fig, ax = plt.subplots()
ax.plot(month_2011.index, month_2011.values, marker="o", linewidth=2, color="#33FF57")
ax.set_xticks(month_2011.index)
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], fontsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.set_ylabel("Penyewa Sepeda", fontsize=12)
ax.set_ylim(0)
ax.grid(True)
st.pyplot(fig)
plt.close(fig)

# judul
st.subheader("Perkembangan Bike Sharing Setiap Bulan (2012)")
# Filter data 2012
month_2012 = all_data1[all_data1["dteday"].str.startswith('2012')].groupby(all_data1["dteday"].str[5:7])["cnt"].sum()
# Membuat plot
fig, ax = plt.subplots()
ax.plot(month_2012.index, month_2012.values, marker="o", linewidth=2, color="#33FF57")
ax.set_xticks(month_2012.index)
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], fontsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.set_ylabel("Penyewa Sepeda", fontsize=12)
ax.set_ylim(0)
ax.grid(True)
st.pyplot(fig)
plt.close(fig)

# Judul
st.subheader("Jumlah Bike Sharing Berdasarkan Faktor Lingkungan (2011)")
# Filter data untuk tahun 2011
data_2011 = all_data2[all_data2["dteday"].str.startswith('2011')]
# Mengelompokkan data berdasarkan kondisi cuaca dan menghitung jumlah total penyewaan
weather_counts = data_2011.groupby("weathersit")["cnt"].sum()
weather_counts.index = ["Bagus", "Sedang", "Buruk", "Sangat Buruk"]
# Menampilkan grafik bar menggunakan Streamlit
st.bar_chart(weather_counts)

# Judul
st.subheader("Jumlah Bike Sharing Berdasarkan Faktor Lingkungan (2012)")
# Filter data untuk tahun 2012
data_2012 = all_data2[all_data2["dteday"].str.startswith('2012')]
# Mengelompokkan data berdasarkan kondisi cuaca dan menghitung jumlah total penyewaan
weather_counts = data_2012.groupby("weathersit")["cnt"].sum()
weather_counts.index = ["Bagus", "Sedang", "Buruk", "Sangat Buruk"]
# Menampilkan grafik bar menggunakan Streamlit
st.bar_chart(weather_counts)

# judul
st.subheader("Teknik Analisis Lanjutan Time Series Analysis")
# Mengatur dteday sebagai index (harus menggunakan inplace=True)
all_data1.set_index('dteday', inplace=True)
# Membuat line chart time series bike sharing menggunakan Streamlit
st.line_chart(all_data1["cnt"])

