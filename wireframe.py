import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Sistem Informasi Pariwisata", page_icon="🏢", layout="wide")

# 2. STYLE MEWAH & ELEGAN
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #0f172a, #1e293b); color: #f8fafc; }
    h1, h2, h3 { color: #fbbf24 !important; font-family: 'Georgia', serif; }
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #b45309, #fbbf24);
        color: #000000; font-weight: bold; border-radius: 8px;
    }
    </style>
    """, unsafe_allow_index=True)

# 3. SIDEBAR
with st.sidebar:
    st.markdown("<h2 style='color: #fbbf24;'>SISTEM PUSAT</h2>", unsafe_allow_index=True)
    menu = st.radio("Navigasi:", ["🌐 Portal Utama", "📊 Dashboard", "🎫 Reservasi"])

# 4. DATA SIMULASI (Agar Link Publik Tetap Jalan Tanpa XAMPP)
df_dummy = pd.DataFrame({
    "Destinasi": ["Raja Ampat", "Borobudur", "Labuan Bajo", "Danau Toba"],
    "Kategori": ["Alam", "Budaya", "Alam", "Alam"],
    "Pengunjung": [450, 1200, 600, 850],
    "Harga": [500000, 50000, 450000, 25000]
})

# 5. LOGIKA MENU
if menu == "🌐 Portal Utama":
    st.title("Sistem Informasi Pariwisata Nusantara")
    st.image("https://images.unsplash.com/photo-1518548419970-58e3b4079ca1", use_container_width=True)
    st.subheader("Integrasi Layanan Wisata Nasional Secara Digital.")

elif menu == "📊 Dashboard":
    st.header("Analisis Strategis Destinasi")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df_dummy, x="Destinasi", y="Pengunjung", color_discrete_sequence=['#fbbf24'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#f8fafc")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.write("### Data Inventori")
        st.dataframe(df_dummy)

elif menu == "🎫 Reservasi":
    st.header("Portal Reservasi Terpadu")
    with st.form("res_form"):
        nama = st.text_input("Nama Lengkap")
        tujuan = st.selectbox("Pilih Destinasi", df_dummy["Destinasi"])
        jumlah = st.number_input("Jumlah Tiket", min_value=1)
        submit = st.form_submit_button("Hitung Biaya")
        
    if submit:
        harga_satuan = df_dummy[df_dummy["Destinasi"] == tujuan]["Harga"].values[0]
        total = harga_satuan * jumlah
        st.success(f"Invoice Berhasil Dibuat!")
        st.markdown(f"### Total Bayar: Rp {total:,}")