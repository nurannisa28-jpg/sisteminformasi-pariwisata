import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI ELITE
st.set_page_config(page_title="Nusantara Premium Travel", layout="wide")

# 2. CSS UNTUK TAMPILAN PREMIUM & HURUF JELAS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main { background-color: #fcfcfc; }
    .stHeader { background-color: #0284c7; }
    
    /* Card Styling */
    .destination-card {
        border-radius: 15px;
        padding: 20px;
        background: white;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        border: 1px solid #f1f5f9;
    }
    
    h1 { color: #0f172a; font-weight: 800; font-size: 3rem !important; }
    .price-tag { color: #0284c7; font-weight: bold; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE DESTINASI (DENGAN SLIDE GAMBAR)
destinasi_list = [
    {
        "nama": "Raja Ampat",
        "provinsi": "Papua Barat",
        "desc": "Surga terakhir di bumi dengan keanekaragaman hayati laut tertinggi.",
        "images": [
            "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=800",
            "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=800"
        ],
        "harga": "Rp 5.000.000"
    },
    {
        "nama": "Pulau Komodo",
        "provinsi": "NTT",
        "desc": "Rumah bagi kadal purba terbesar di dunia dan Pantai Pink yang ikonik.",
        "images": [
            "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=800",
            "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800"
        ],
        "harga": "Rp 3.500.000"
    },
    {
        "nama": "Candi Borobudur",
        "provinsi": "Jawa Tengah",
        "desc": "Monumen Buddha terbesar di dunia dan warisan budaya UNESCO.",
        "images": [
            "https://images.unsplash.com/photo-1626202341512-a97a922a0887?w=800",
            "https://images.unsplash.com/photo-1616422285623-13ff0167c95c?w=800"
        ],
        "harga": "Rp 750.000"
    }
    # (Kamu bisa tambah sampai 20 destinasi dengan pola yang sama)
]

# 4. SIDEBAR
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=150)
    menu = st.radio("Navigasi Elit:", ["🏠 Home Experience", "🗺️ Katalog Destinasi", "📈 Analitik Wisata"])

# 5. LOGIKA HALAMAN
if menu == "🏠 Home Experience":
    st.title("Jelajahi Kemurnian Nusantara")
    st.markdown("#### *Standar Baru dalam Pengalaman Perjalanan Indonesia*")
    st.image("https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=1200", use_container_width=True)
    
elif menu == "🗺️ Katalog Destinasi":
    st.header("Destinasi Pilihan Premium")
    st.write("Klik tanda '+' pada destinasi untuk melihat slide foto.")
    
    for item in destinasi_list:
        with st.expander(f"✨ {item['nama']} - {item['provinsi']}"):
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Simulasi Slide dengan Tabs di dalam Expander
                img_tabs = st.tabs([f"Foto {i+1}" for i in range(len(item['images']))])
                for i, tab in enumerate(img_tabs):
                    with tab:
                        st.image(item['images'][i], use_container_width=True)
            
            with col2:
                st.subheader(item['nama'])
                st.write(item['desc'])
                st.markdown(f"<p class='price-tag'>Estimasi Biaya: {item['harga']}</p>", unsafe_allow_html=True)
                if st.button(f"Pesan Tiket {item['nama']}"):
                    st.success(f"Permintaan reservasi ke {item['nama']} dikirim!")

elif menu == "📈 Analitik Wisata":
    st.header("Data Statistik Pengunjung")
    # Contoh Grafik
    df = pd.DataFrame({
        "Destinasi": ["Raja Ampat", "Komodo", "Borobudur", "Bali", "Toba"],
        "Pengunjung": [450, 600, 1200, 2500, 800]
    })
    fig = px.pie(df, values='Pengunjung', names='Destinasi', hole=.3, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: #94a3b8;'>© 2026 PT. Pariwisata Nusantara Elit. Dibuat oleh Nur Annisa.</p>", unsafe_allow_html=True)
