import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# 1. SETTING DASAR (Enterprise Level)
st.set_page_config(page_title="Wonderful Indonesia | Corporate Portal", layout="wide", initial_sidebar_state="expanded")

# 2. CSS CUSTOM UNTUK TAMPILAN MEWAH (Clean, Modern, & High-End)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    
    .stApp { background-color: #f8fafc; }
    
    /* Card Design */
    .resort-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border-left: 5px solid #0ea5e9;
    }
    
    /* Header Styling */
    h1 { color: #0f172a; font-weight: 700; font-size: 3.5rem !important; margin-bottom: 0px; }
    h2 { color: #0284c7; font-weight: 600; }
    
    /* Sidebar Luxury */
    .css-1d391kg { background-color: #0f172a !important; }
    
    /* Custom Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0284c7 0%, #0ea5e9 100%);
        color: white; border: none; padding: 12px 30px;
        border-radius: 10px; font-weight: 600; transition: 0.3s;
    }
    div.stButton > button:first-child:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(2, 132, 199, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE WISATA (20+ DESTINASI)
data_wisata = {
    "Nama": [
        "Raja Ampat", "Pulau Komodo", "Borobudur", "Danau Toba", "Gunung Bromo", 
        "Tanah Lot", "Wakatobi", "Derawan", "Belitung", "Tana Toraja",
        "Bunaken", "Banda Neira", "Kawah Ijen", "Nusa Penida", "Mandalika",
        "Likupang", "Jakarta Kota Tua", "Malang Batu", "Yogyakarta Malioboro", 
        "Bandung Lembang", "Makassar Losari", "Medan Istana Maimun"
    ],
    "Provinsi": [
        "Papua Barat", "NTT", "Jawa Tengah", "Sumatera Utara", "Jawa Timur", 
        "Bali", "Sultra", "Kaltim", "Bangka Belitung", "Sulsel",
        "Sulut", "Maluku", "Jawa Timur", "Bali", "NTB",
        "Sulut", "DKI Jakarta", "Jawa Timur", "DIY", 
        "Jawa Barat", "Sulsel", "Sumatera Utara"
    ],
    "Kategori": [
        "Alam/Laut", "Alam", "Budaya", "Alam", "Alam", 
        "Budaya/Laut", "Alam/Laut", "Alam/Laut", "Alam/Laut", "Budaya",
        "Alam/Laut", "Sejarah", "Alam", "Alam/Laut", "Alam/Laut",
        "Alam/Laut", "Sejarah", "Kota", "Budaya/Kota", 
        "Alam/Kota", "Kota", "Sejarah"
    ],
    "Harga_Tiket": [
        500000, 300000, 50000, 20000, 75000, 
        60000, 150000, 100000, 30000, 50000,
        50000, 20000, 25000, 75000, 50000,
        40000, 10000, 35000, 0, 
        25000, 0, 15000
    ],
    "Rating": [4.9, 4.8, 4.7, 4.6, 4.8, 4.7, 4.9, 4.8, 4.6, 4.7, 4.8, 5.0, 4.7, 4.8, 4.6, 4.5, 4.2, 4.5, 4.7, 4.6, 4.3, 4.4]
}
df = pd.DataFrame(data_wisata)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=200)
    st.markdown("---")
    menu = st.selectbox("Eksplorasi Portal", ["💎 Beranda Eksklusif", "🌍 Galeri Destinasi", "📊 Analitik & Data", "💳 Reservasi Smart"])
    st.markdown("---")
    st.info("Sistem Informasi Pariwisata Nusantara v2.0 (Revised Edition)")

# 5. LOGIKA HALAMAN
if menu == "💎 Beranda Eksklusif":
    # Hero Section
    st.title("Jelajahi Kemurnian Nusantara")
    st.markdown("####
