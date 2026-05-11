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
    st.markdown("#### *Standar Baru dalam Pengalaman Perjalanan Indonesia*")
    st.image("https://images.unsplash.com/photo-1537996194471-e657df975ab4?q=80&w=2000", use_container_width=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="resort-card"><h3>Destinasi Premium</h3><p>Akses ke lebih dari 20+ lokasi wisata terbaik dunia yang ada di Indonesia.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="resort-card"><h3>Layanan Terpadu</h3><p>Sistem reservasi yang aman, cepat, dan terintegrasi secara digital.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="resort-card"><h3>Data Real-Time</h3><p>Informasi harga dan rating terbaru langsung dari otoritas pariwisata.</p></div>', unsafe_allow_html=True)

elif menu == "🌍 Galeri Destinasi":
    st.header("Katalog Destinasi Pilihan")
    
    # Filter System
    kat_filter = st.multiselect("Filter Berdasarkan Kategori:", df["Kategori"].unique(), default=df["Kategori"].unique())
    filtered_df = df[df["Kategori"].isin(kat_filter)]
    
    # Tampilan Tabs (Banyak Gambar)
    tab1, tab2, tab3 = st.tabs(["🌊 Wisata Bahari", "⛰️ Wisata Alam & Budaya", "🏙️ Wisata Kota & Sejarah"])
    
    with tab1:
        st.write("### Keajaiban Bawah Laut")
        c1, c2 = st.columns(2)
        c1.image("https://images.unsplash.com/photo-1589197331516-4d839633b42a?q=80&w=800", caption="Raja Ampat - Papua")
        c2.image("https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?q=80&w=800", caption="Wakatobi - Sultra")
        
    with tab2:
        st.write("### Kemegahan Alam & Warisan Luhur")
        c3, c4 = st.columns(2)
        c3.image("https://images.unsplash.com/photo-1626202341512-a97a922a0887?q=80&w=800", caption="Borobudur - Jawa Tengah")
        c4.image("https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?q=80&w=800", caption="Gunung Bromo - Jawa Timur")

    with tab3:
        st.write("### Jejak Sejarah & Dinamika Kota")
        st.dataframe(filtered_df[filtered_df["Kategori"].str.contains("Kota|Sejarah")], use_container_width=True)

elif menu == "📊 Analitik & Data":
    st.header("Dashboard Analisis Strategis")
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.write("### Top Rating Destinasi")
        st.table(df.sort_values(by="Rating", ascending=False).head(10)[["Nama", "Rating"]])
    
    with col_b:
        st.write("### Perbandingan Harga Tiket (IDR)")
        fig = px.bar(df, x="Nama", y="Harga_Tiket", color="Kategori", barmode="group", template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

elif menu == "💳 Reservasi Smart":
    st.header("Portal Reservasi Aman")
    
    with st.container():
        st.markdown('<div class="resort-card">', unsafe_allow_html=True)
        col_inv1, col_inv2 = st.columns(2)
        
        with col_inv1:
            nama = st.text_input("Nama Pemesan (Sesuai Identitas)")
            tujuan = st.selectbox("Pilih Destinasi", df["Nama"].tolist())
            email = st.text_input("Alamat Email")
        
        with col_inv2:
            tanggal = st.date_input("Rencana Kunjungan", datetime.now())
            jumlah = st.number_input("Jumlah Tiket", min_value=1, step=1)
            metode = st.radio("Metode Pembayaran", ["Transfer Bank", "E-Wallet", "Credit Card"])
            
        if st.button("PROSES INVOICE SEKARANG"):
            harga = df[df["Nama"] == tujuan]["Harga_Tiket"].values[0]
            total = harga * jumlah
            st.balloons()
            st.success(f"Pesanan atas nama {nama} telah diverifikasi!")
            
            # Tampilan Invoice
            st.markdown(f"""
            ---
            ### 🧾 E-INVOICE CONFIRMATION
            **No. Transaksi:** INV-{datetime.now().strftime('%Y%m%d%H%M')}  
            **Destinasi:** {tujuan}  
            **Total Pembayaran:** Rp {total:,}  
            ---
            *Silakan periksa email {email} untuk instruksi pembayaran.*
            """)
        st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2024 Wonderful Indonesia Digital Division. All Rights Reserved.</p>", unsafe_allow_html=True)
