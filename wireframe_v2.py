import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN GACOR
st.set_page_config(page_title="Nusantara Elite Travel | Wonderful Indonesia", page_icon="💎", layout="wide")

# 2. CSS CUSTOM UNTUK TAMPILAN ELITE & HURUF JELAS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Background & Card Mewah */
    .stApp { background-color: #f0f4f8; }
    
    .main-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    
    /* Judul Gacor */
    h1 { color: #0f172a; font-weight: 800; font-size: 3.5rem !important; margin-bottom: 10px; }
    h2 { color: #0284c7; font-weight: 700; border-left: 6px solid #0284c7; padding-left: 15px; }
    
    /* Button & Interaction */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #0284c7 0%, #0ea5e9 100%);
        color: white; border: none; padding: 12px 35px;
        border-radius: 12px; font-weight: 700; width: 100%; transition: 0.3s;
    }
    div.stButton > button:first-child:hover { transform: scale(1.02); box-shadow: 0 8px 20px rgba(2, 132, 199, 0.3); }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE 20+ DESTINASI (STABIL & LENGKAP)
destinasi = [
    {"nama": "Raja Ampat", "loc": "Papua Barat", "kat": "Bahari", "img": "https://images.pexels.com/photos/3405151/pexels-photo-3405151.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Pulau Komodo", "loc": "NTT", "kat": "Alam", "img": "https://images.pexels.com/photos/11559868/pexels-photo-11559868.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Candi Borobudur", "loc": "Jawa Tengah", "kat": "Budaya", "img": "https://images.pexels.com/photos/2034335/pexels-photo-2034335.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Gunung Bromo", "loc": "Jawa Timur", "kat": "Alam", "img": "https://images.pexels.com/photos/4041131/pexels-photo-4041131.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Danau Toba", "loc": "Sumatera Utara", "kat": "Alam", "img": "https://images.pexels.com/photos/6129991/pexels-photo-6129991.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Tanah Lot", "loc": "Bali", "kat": "Budaya", "img": "https://images.pexels.com/photos/2166559/pexels-photo-2166559.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Wakatobi", "loc": "Sultra", "kat": "Bahari", "img": "https://images.pexels.com/photos/2324562/pexels-photo-2324562.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Pulau Belitung", "loc": "Babel", "kat": "Bahari", "img": "https://images.pexels.com/photos/5406560/pexels-photo-5406560.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Kawah Ijen", "loc": "Jawa Timur", "kat": "Alam", "img": "https://images.pexels.com/photos/14841643/pexels-photo-14841643.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Tana Toraja", "loc": "Sulsel", "kat": "Budaya", "img": "https://images.pexels.com/photos/12470703/pexels-photo-12470703.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Nusa Penida", "loc": "Bali", "kat": "Bahari", "img": "https://images.pexels.com/photos/3322129/pexels-photo-3322129.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Banda Neira", "loc": "Maluku", "kat": "Sejarah", "img": "https://images.pexels.com/photos/1010657/pexels-photo-1010657.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Bunaken", "loc": "Sulut", "kat": "Bahari", "img": "https://images.pexels.com/photos/33041/antelope-canyon-lower-canyon-arizona.jpg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Mandalika", "loc": "NTB", "kat": "Sport", "img": "https://images.pexels.com/photos/3802510/pexels-photo-3802510.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Likupang", "loc": "Sulut", "kat": "Bahari", "img": "https://images.pexels.com/photos/1450353/pexels-photo-1450353.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Derawan", "loc": "Kaltim", "kat": "Bahari", "img": "https://images.pexels.com/photos/1285625/pexels-photo-1285625.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Labuan Bajo", "loc": "NTT", "kat": "Alam", "img": "https://images.pexels.com/photos/16383633/pexels-photo-16383633.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Jakarta Old Town", "loc": "DKI", "kat": "Sejarah", "img": "https://images.pexels.com/photos/11053185/pexels-photo-11053185.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Prambanan", "loc": "DIY", "kat": "Budaya", "img": "https://images.pexels.com/photos/12474921/pexels-photo-12474921.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Garuda Wisnu", "loc": "Bali", "kat": "Budaya", "img": "https://images.pexels.com/photos/931007/pexels-photo-931007.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Pantai Ora", "loc": "Maluku", "kat": "Bahari", "img": "https://images.pexels.com/photos/1287441/pexels-photo-1287441.jpeg?auto=compress&cs=tinysrgb&w=800"},
    {"nama": "Danau Kelimutu", "loc": "NTT", "kat": "Alam", "img": "https://images.pexels.com/photos/4041131/pexels-photo-4041131.jpeg?auto=compress&cs=tinysrgb&w=800"}
]
df = pd.DataFrame(destinasi)

# 4. SIDEBAR MEWAH
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=180)
    st.markdown("### **PORTAL EKSEKUTIF**")
    menu = st.radio("Navigasi:", ["🌟 Home Experience", "🗺️ Katalog Destinasi", "📊 Analitik Data"])
    st.info(f"Total Destinasi: {len(df)} Lokasi")

# 5. LOGIKA HALAMAN
if menu == "🌟 Home Experience":
    st.title("Eksplorasi Kemurnian Nusantara")
    st.markdown("#### *Standar Baru dalam Pengalaman Perjalanan Indonesia*")
    st.image("https://images.pexels.com/photos/1450363/pexels-photo-1450363.jpeg?auto=compress&cs=tinysrgb&w=1600", use_container_width=True)
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="main-card"><h3>Premium Access</h3><p>Informasi eksklusif 20+ destinasi tersertifikasi.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="main-card"><h3>Verified Data</h3><p>Update harga dan fasilitas secara real-time.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="main-card"><h3>User Focused</h3><p>Desain antarmuka modern yang memanjakan mata.</p></div>', unsafe_allow_html=True)

elif menu == "🗺️ Katalog Destinasi":
    st.header("Katalog Wisata Premium (20+ Destinasi)")
    st.write("Jelajahi setiap lokasi dengan galeri gambar yang jernih.")
    
    # Menampilkan Destinasi dalam 2 Kolom agar Rapi
    cols = st.columns(2)
    for i, row in df.iterrows():
        with cols[i % 2]:
            st.markdown(f'<div class="main-card">', unsafe_allow_html=True)
            st.image(row['img'], use_container_width=True)
            st.subheader(f"📍 {row['nama']}")
            st.write(f"**Provinsi:** {row['loc']} | **Kategori:** {row['kat']}")
            
            # FITUR SLIDE (Simulasi dengan Expand)
            with st.expander("Lihat Detail & Slide Lainnya"):
                st.write(f"Nikmati keindahan {row['nama']} yang merupakan salah satu destinasi unggulan di {row['loc']}.")
                st.image(row['img'], caption=f"Tampilan Utama {row['nama']}", use_container_width=True)
                if st.button(f"Pesan Tiket {row['nama']}", key=f"btn_{i}"):
                    st.success(f"Permintaan reservasi ke {row['nama']} berhasil!")
            st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📊 Analitik Data":
    st.header("Statistik & Distribusi Wisata")
    c_a, c_b = st.columns(2)
    
    with c_a:
        st.write("### Porsi Kategori Wisata")
        fig1 = px.pie(df, names='kat', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig1, use_container_width=True)
        
    with c_b:
        st.write("### Data Table Lengkap")
        st.dataframe(df, use_container_width=True)

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 Wonderful Indonesia Digital Division. Powered by Nur Annisa.</p>", unsafe_allow_html=True)
