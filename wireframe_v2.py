import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI ULTRA PREMIUM
st.set_page_config(page_title="Ultimate Nusantara Atlas", page_icon="🇮🇩", layout="wide")

# 2. CSS CUSTOM: MEWAH & SANGAT JELAS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #f1f5f9; }
    .luxury-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05); margin-bottom: 20px;
        border: 1px solid #e2e8f0; transition: 0.3s;
    }
    .luxury-card:hover { transform: translateY(-5px); border-color: #0284c7; }
    h1 { color: #0f172a; font-weight: 800; font-size: 3.5rem !important; text-align: center; }
    .island-badge {
        background: #0284c7; color: white; padding: 4px 12px;
        border-radius: 20px; font-size: 0.8rem; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE 38 PROVINSI LENGKAP (KOORDINAT & GAMBAR)
data_38 = [
    # SUMATERA
    {"nama": "Masjid Baiturrahman", "prov": "Aceh", "pulau": "Sumatera", "lat": 5.55, "lon": 95.32, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=600"},
    {"nama": "Danau Toba", "prov": "Sumatera Utara", "pulau": "Sumatera", "lat": 2.68, "lon": 98.88, "img": "https://images.unsplash.com/photo-1572458421035-7c858a74e503?w=600"},
    {"nama": "Jam Gadang", "prov": "Sumatera Barat", "pulau": "Sumatera", "lat": -0.30, "lon": 100.37, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=600"},
    {"nama": "Istana Siak", "prov": "Riau", "pulau": "Sumatera", "lat": 0.79, "lon": 102.04, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=600"},
    {"nama": "Jembatan Barelang", "prov": "Kepulauan Riau", "pulau": "Sumatera", "lat": 1.05, "lon": 104.05, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=600"},
    {"nama": "Sungai Batanghari", "prov": "Jambi", "pulau": "Sumatera", "lat": -1.61, "lon": 103.61, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Benteng Marlborough", "prov": "Bengkulu", "pulau": "Sumatera", "lat": -3.79, "lon": 102.25, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},
    {"nama": "Jembatan Ampera", "prov": "Sumatera Selatan", "pulau": "Sumatera", "lat": -2.99, "lon": 104.76, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},
    {"nama": "Pantai Tanjung Tinggi", "prov": "Bangka Belitung", "lat": -2.74, "lon": 107.63, "pulau": "Sumatera", "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},
    {"nama": "Menara Siger", "prov": "Lampung", "pulau": "Sumatera", "lat": -5.87, "lon": 105.75, "img": "https://images.unsplash.com/photo-1591017403286-fd8ba110ee04?w=600"},

    # JAWA
    {"nama": "Monumen Nasional", "prov": "DKI Jakarta", "pulau": "Jawa", "lat": -6.17, "lon": 106.82, "img": "https://images.unsplash.com/photo-1555899434-94d1368aa7af?w=600"},
    {"nama": "Gedung Sate", "prov": "Jawa Barat", "pulau": "Jawa", "lat": -6.90, "lon": 107.61, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=600"},
    {"nama": "Masjid Agung Banten", "prov": "Banten", "pulau": "Jawa", "lat": -6.03, "lon": 106.15, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=600"},
    {"nama": "Candi Borobudur", "prov": "Jawa Tengah", "pulau": "Jawa", "lat": -7.60, "lon": 110.20, "img": "https://images.unsplash.com/photo-1626202341512-a97a922a0887?w=600"},
    {"nama": "Malioboro", "prov": "DI Yogyakarta", "pulau": "Jawa", "lat": -7.79, "lon": 110.36, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Gunung Bromo", "prov": "Jawa Timur", "pulau": "Jawa", "lat": -7.94, "lon": 112.95, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},

    # BALI & NUSA TENGGARA
    {"nama": "Tanah Lot", "prov": "Bali", "pulau": "Bali-Nusa", "lat": -8.62, "lon": 115.08, "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600"},
    {"nama": "Mandalika", "prov": "NTB", "pulau": "Bali-Nusa", "lat": -8.89, "lon": 116.29, "img": "https://images.unsplash.com/photo-1512100356956-c1287eb0a1bc?w=600"},
    {"nama": "Labuan Bajo", "prov": "NTT", "pulau": "Bali-Nusa", "lat": -8.49, "lon": 119.87, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},

    # KALIMANTAN
    {"nama": "Tugu Khatulistiwa", "prov": "Kalimantan Barat", "pulau": "Kalimantan", "lat": 0.00, "lon": 109.33, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Pasar Terapung", "prov": "Kalimantan Selatan", "pulau": "Kalimantan", "lat": -3.31, "lon": 114.59, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Derawan", "prov": "Kalimantan Timur", "pulau": "Kalimantan", "lat": 2.25, "lon": 118.24, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=600"},
    {"nama": "Taman Nasional Tanjung Puting", "prov": "Kalimantan Tengah", "pulau": "Kalimantan", "lat": -2.83, "lon": 111.91, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=600"},
    {"nama": "Krayan", "prov": "Kalimantan Utara", "pulau": "Kalimantan", "lat": 3.92, "lon": 115.61, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},

    # SULAWESI
    {"nama": "Pantai Losari", "prov": "Sulawesi Selatan", "pulau": "Sulawesi", "lat": -5.14, "lon": 119.40, "img": "https://images.unsplash.com/photo-1546500840-ae38253aba9b?w=600"},
    {"nama": "Bunaken", "prov": "Sulawesi Utara", "pulau": "Sulawesi", "lat": 1.63, "lon": 124.77, "img": "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=600"},
    {"nama": "Wakatobi", "prov": "Sulawesi Tenggara", "pulau": "Sulawesi", "lat": -5.32, "lon": 123.58, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=600"},
    {"nama": "Pulau Togean", "prov": "Sulawesi Tengah", "pulau": "Sulawesi", "lat": -0.41, "lon": 121.84, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},
    {"nama": "Benteng Otanaha", "prov": "Gorontalo", "pulau": "Sulawesi", "lat": 0.54, "lon": 123.05, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=600"},
    {"nama": "Pantai Manakarra", "prov": "Sulawesi Barat", "pulau": "Sulawesi", "lat": -2.67, "lon": 118.88, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},

    # MALUKU & PAPUA (DENGAN PROVINSI BARU)
    {"nama": "Banda Neira", "prov": "Maluku", "pulau": "Papua-Maluku", "lat": -4.51, "lon": 129.90, "img": "https://images.unsplash.com/photo-1570789210967-2cac24afad44?w=600"},
    {"nama": "Pantai Ora", "prov": "Maluku Utara", "pulau": "Papua-Maluku", "lat": 0.73, "lon": 127.36, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=600"},
    {"nama": "Raja Ampat", "prov": "Papua Barat", "pulau": "Papua-Maluku", "lat": -0.23, "lon": 130.50, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=600"},
    {"nama": "Danau Sentani", "prov": "Papua", "pulau": "Papua-Maluku", "lat": -2.59, "lon": 140.48, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=600"},
    {"nama": "Lembah Baliem", "prov": "Papua Pegunungan", "pulau": "Papua-Maluku", "lat": -4.01, "lon": 138.92, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=600"},
    {"nama": "Hutan Mangrove", "prov": "Papua Selatan", "pulau": "Papua-Maluku", "lat": -8.49, "lon": 140.40, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Kepulauan Biak", "prov": "Papua Tengah", "pulau": "Papua-Maluku", "lat": -1.18, "lon": 136.06, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},
    {"nama": "Puncak Jaya", "prov": "Papua Barat Daya", "pulau": "Papua-Maluku", "lat": -0.87, "lon": 131.25, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"}
]
df = pd.DataFrame(data_38)

# 4. SIDEBAR & NAVIGASI
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=180)
    st.markdown("### **EXPLORE 38 PROVINCES**")
    menu = st.radio("Sistem Layanan:", ["🏠 Beranda Nasional", "🗺️ Peta Radar Interaktif", "🗂️ Direktori Provinsi"])
    st.info(f"Status Sistem: Online\nData: 38 Provinsi")

# 5. LOGIKA HALAMAN
if menu == "🏠 Beranda Nasional":
    st.title("Gedung Digital Pariwisata Indonesia")
    st.markdown("#### *Satu Pintu Menuju Pesona Seluruh Nusantara*")
    st.image("https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=1400", use_container_width=True)
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1: st.markdown('<div class="luxury-card"><h3>38 Provinsi</h3><p>Representasi lengkap dari ujung barat sampai ujung timur Indonesia.</p></div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="luxury-card"><h3>Navigasi Cerdas</h3><p>Pilih pulau atau wilayah untuk eksplorasi yang lebih fokus.</p></div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="luxury-card"><h3>Visual Akurat</h3><p>Dokumentasi foto terpilih untuk setiap destinasi ikonik provinsi.</p></div>', unsafe_allow_html=True)

elif menu == "🗺️ Peta Radar Interaktif":
    st.header("Peta Sebaran Destinasi 38 Provinsi")
    st.write("Zoom peta untuk melihat detail titik lokasi tiap provinsi di Indonesia.")
    
    fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="nama", hover_data=["prov", "pulau"],
                            color_discrete_sequence=["#0284c7"], zoom=3.8, height=650)
    fig.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

elif menu == "🗂️ Direktori Provinsi":
    st.header("Katalog Wisata Lengkap (38 Provinsi)")
    
    # FILTER PER PULAU
    pulau_pilihan = st.selectbox("Filter Berdasarkan Wilayah/Pulau:", ["Semua Wilayah", "Sumatera", "Jawa", "Bali-Nusa", "Kalimantan", "Sulawesi", "Papua-Maluku"])
    
    if pulau_pilihan != "Semua Wilayah":
        filtered_df = df[df["pulau"] == pulau_pilihan]
    else:
        filtered_df = df
        
    st.write(f"Menampilkan **{len(filtered_df)}** Destinasi")
    
    # GRID 3 KOLOM AGAR RAPI (Sangat Gacor)
    cols = st.columns(3)
    for i, row in filtered_df.reset_index().iterrows():
        with cols[i % 3]:
            st.markdown(f'''
                <div class="luxury-card">
                    <img src="{row['img']}" style="width:100%; border-radius:10px; height:180px; object-fit:cover;">
                    <div style="margin-top:10px;">
                        <span class="island-badge">{row['pulau']}</span>
                        <h3 style="margin:10px 0 5px 0; font-size:1.2rem;">{row['nama']}</h3>
                        <p style="color:#64748b; font-size:0.9rem;">📍 {row['prov']}</p>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
            with st.expander("Klik Detail"):
                st.write(f"Informasi resmi destinasi {row['nama']} yang menjadi ikon dari Provinsi {row['prov']}.")
                if st.button(f"Hubungi Admin: {row['nama']}", key=row['nama']):
                    st.success("Menghubungkan ke layanan informasi...")

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 Wonderful Indonesia Ultimate Atlas - Nur Annisa (Sistem Informasi UNJANI).</p>", unsafe_allow_html=True)
