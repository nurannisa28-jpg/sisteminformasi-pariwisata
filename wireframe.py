import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Info Pariwisata Nusantara", layout="wide")

# 2. STYLE BARU (Bersih, Cerah, Profesional)
st.markdown("""
    <style>
    /* Latar belakang putih bersih */
    .stApp { background-color: #ffffff; color: #1e293b; }
    
    /* Font yang lebih tegas dan jelas */
    h1, h2, h3 { 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; 
        color: #0284c7 !important; 
        font-weight: 700;
    }
    
    /* Tombol yang lebih modern */
    div.stButton > button:first-child {
        background-color: #0284c7;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
    }
    
    /* Tabel agar lebih enak dilihat */
    .stDataFrame { border: 1px solid #e2e8f0; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR
with st.sidebar:
    st.title("Menu Utama")
    menu = st.radio("Pilih Halaman:", ["🏠 Beranda", "📊 Data Wisata", "💰 Cek Biaya"])

# 4. DATA CONTOH
data = {
    "Destinasi": ["Raja Ampat", "Borobudur", "Labuan Bajo", "Danau Toba", "Bali"],
    "Kategori": ["Alam", "Budaya", "Alam", "Alam", "Budaya"],
    "Pengunjung": [450, 1200, 600, 850, 2000],
    "Harga": [500000, 50000, 450000, 25000, 75000]
}
df = pd.DataFrame(data)

# 5. LOGIKA HALAMAN
if menu == "🏠 Beranda":
    st.title("Selamat Datang di Portal Pariwisata")
    st.write("Temukan informasi destinasi terbaik di Indonesia dengan data yang akurat.")
    
    # Menggunakan gambar pemandangan umum yang lebih stabil link-nya
    st.image("https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?q=80&w=1000", 
             caption="Eksplorasi Keindahan Nusantara", use_container_width=True)

elif menu == "📊 Data Wisata":
    st.header("Statistik Pengunjung Wisata")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("### Tabel Destinasi")
        st.dataframe(df, use_container_width=True)
        
    with col2:
        st.write("### Grafik Kunjungan")
        fig = px.bar(df, x="Destinasi", y="Pengunjung", 
                     color="Destinasi", 
                     color_discrete_sequence=px.colors.qualitative.Safe)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

elif menu == "💰 Cek Biaya":
    st.header("Kalkulator Estimasi Biaya")
    st.info("Silakan isi form di bawah untuk menghitung biaya tiket masuk.")
    
    with st.container():
        nama = st.text_input("Masukkan Nama Anda")
        tujuan = st.selectbox("Pilih Tujuan Wisata", df["Destinasi"])
        jumlah = st.number_input("Jumlah Tiket", min_value=1, step=1)
        
        if st.button("Hitung Sekarang"):
            harga_satuan = df[df["Destinasi"] == tujuan]["Harga"].values[0]
            total = harga_satuan * jumlah
            st.success(f"Halo {nama}, total biaya tiket ke {tujuan} adalah: Rp {total:,}")
