import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN UNIVERSAL
st.set_page_config(
    page_title="Pariwisata Nusantara | Portal Resmi",
    page_icon="🇮🇩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS CUSTOM UNTUK TAMPILAN PREMIUM & UNIVERSAL
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #f8fafc; }
    
    /* Card Style */
    .travel-card {
        background: white; padding: 0px; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
        margin-bottom: 25px; overflow: hidden;
    }
    .card-content { padding: 20px; }
    
    /* Typography */
    h1 { color: #0f172a; font-weight: 800; font-size: 3rem !important; text-align: center; }
    h2 { color: #0284c7; font-weight: 700; }
    .price-tag { color: #059669; font-weight: 700; font-size: 1.1rem; }
    
    /* Buttons */
    div.stButton > button:first-child {
        background: #0284c7; color: white; border-radius: 12px;
        border: none; padding: 10px 20px; width: 100%; font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE 38 PROVINSI (STABIL & AKURAT)
wisata_list = [
    # SUMATERA
    {"nama": "Masjid Baiturrahman", "prov": "Aceh", "kat": "Religi", "price": 0, "lat": 5.55, "lon": 95.32, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=600"},
    {"nama": "Danau Toba", "prov": "Sumatera Utara", "kat": "Alam", "price": 20000, "lat": 2.68, "lon": 98.88, "img": "https://images.unsplash.com/photo-1572458421035-7c858a74e503?w=600"},
    {"nama": "Jam Gadang", "prov": "Sumatera Barat", "kat": "Sejarah", "price": 5000, "lat": -0.30, "lon": 100.37, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=600"},
    {"nama": "Istana Siak", "prov": "Riau", "kat": "Sejarah", "price": 10000, "lat": 0.79, "lon": 102.04, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=600"},
    {"nama": "Jembatan Barelang", "prov": "Kepulauan Riau", "kat": "Modern", "price": 0, "lat": 1.05, "lon": 104.05, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=600"},
    {"nama": "Candi Muaro Jambi", "prov": "Jambi", "kat": "Budaya", "price": 10000, "lat": -1.61, "lon": 103.61, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Benteng Marlborough", "prov": "Bengkulu", "kat": "Sejarah", "price": 5000, "lat": -3.79, "lon": 102.25, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},
    {"nama": "Jembatan Ampera", "prov": "Sumatera Selatan", "kat": "Modern", "price": 0, "lat": -2.99, "lon": 104.76, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},
    {"nama": "Pantai Tanjung Tinggi", "prov": "Bangka Belitung", "kat": "Bahari", "price": 10000, "lat": -2.74, "lon": 107.63, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},
    {"nama": "Way Kambas", "prov": "Lampung", "kat": "Alam", "price": 15000, "lat": -5.00, "lon": 105.75, "img": "https://images.unsplash.com/photo-1591017403286-fd8ba110ee04?w=600"},

    # JAWA
    {"nama": "Monas", "prov": "DKI Jakarta", "kat": "Modern", "price": 15000, "lat": -6.17, "lon": 106.82, "img": "https://images.unsplash.com/photo-1555899434-94d1368aa7af?w=600"},
    {"nama": "Gedung Sate", "prov": "Jawa Barat", "kat": "Sejarah", "price": 5000, "lat": -6.90, "lon": 107.61, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=600"},
    {"nama": "Masjid Agung Banten", "prov": "Banten", "kat": "Religi", "price": 0, "lat": -6.03, "lon": 106.15, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=600"},
    {"nama": "Candi Borobudur", "prov": "Jawa Tengah", "kat": "Budaya", "price": 50000, "lat": -7.60, "lon": 110.20, "img": "https://images.unsplash.com/photo-1626202341512-a97a922a0887?w=600"},
    {"nama": "Candi Prambanan", "prov": "DI Yogyakarta", "kat": "Budaya", "price": 50000, "lat": -7.75, "lon": 110.49, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Gunung Bromo", "prov": "Jawa Timur", "kat": "Alam", "price": 35000, "lat": -7.94, "lon": 112.95, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},

    # BALI & NUSA TENGGARA
    {"nama": "Pura Uluwatu", "prov": "Bali", "kat": "Religi", "price": 30000, "lat": -8.82, "lon": 115.08, "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600"},
    {"nama": "Mandalika Circuit", "prov": "NTB", "kat": "Modern", "price": 50000, "lat": -8.89, "lon": 116.29, "img": "https://images.unsplash.com/photo-1512100356956-c1287eb0a1bc?w=600"},
    {"nama": "Pulau Komodo", "prov": "NTT", "kat": "Alam", "price": 200000, "lat": -8.49, "lon": 119.87, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},

    # KALIMANTAN
    {"nama": "Tugu Khatulistiwa", "prov": "Kalimantan Barat", "kat": "Sejarah", "price": 0, "lat": 0.00, "lon": 109.33, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "TN Tanjung Puting", "prov": "Kalimantan Tengah", "kat": "Alam", "price": 100000, "lat": -2.83, "lon": 111.91, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=600"},
    {"nama": "Pasar Terapung", "prov": "Kalimantan Selatan", "kat": "Budaya", "price": 0, "lat": -3.31, "lon": 114.59, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Derawan Island", "prov": "Kalimantan Timur", "kat": "Bahari", "price": 50000, "lat": 2.25, "lon": 118.24, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=600"},
    {"nama": "Krayan", "prov": "Kalimantan Utara", "kat": "Alam", "price": 0, "lat": 3.92, "lon": 115.61, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},

    # SULAWESI
    {"nama": "Bunaken", "prov": "Sulawesi Utara", "kat": "Bahari", "price": 50000, "lat": 1.63, "lon": 124.77, "img": "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=600"},
    {"nama": "Kepulauan Togean", "prov": "Sulawesi Tengah", "kat": "Bahari", "price": 25000, "lat": -0.41, "lon": 121.84, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},
    {"nama": "Pantai Losari", "prov": "Sulawesi Selatan", "kat": "Modern", "price": 0, "lat": -5.14, "lon": 119.40, "img": "https://images.unsplash.com/photo-1546500840-ae38253aba9b?w=600"},
    {"nama": "Wakatobi", "prov": "Sulawesi Tenggara", "kat": "Bahari", "price": 150000, "lat": -5.32, "lon": 123.58, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=600"},
    {"nama": "Benteng Otanaha", "prov": "Gorontalo", "kat": "Sejarah", "price": 5000, "lat": 0.54, "lon": 123.05, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=600"},
    {"nama": "Pantai Manakarra", "prov": "Sulawesi Barat", "kat": "Bahari", "price": 0, "lat": -2.67, "lon": 118.88, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},

    # MALUKU & PAPUA
    {"nama": "Banda Neira", "prov": "Maluku", "kat": "Sejarah", "price": 20000, "lat": -4.51, "lon": 129.90, "img": "https://images.unsplash.com/photo-1570789210967-2cac24afad44?w=600"},
    {"nama": "Benteng Tolukko", "prov": "Maluku Utara", "kat": "Sejarah", "price": 10000, "lat": 0.73, "lon": 127.36, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=600"},
    {"nama": "Danau Sentani", "prov": "Papua", "kat": "Alam", "price": 10000, "lat": -2.59, "lon": 140.48, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=600"},
    {"nama": "Raja Ampat", "prov": "Papua Barat", "kat": "Bahari", "price": 500000, "lat": -0.23, "lon": 130.50, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=600"},
    {"nama": "Pantai Nabire", "prov": "Papua Tengah", "kat": "Alam", "price": 0, "lat": -3.36, "lon": 135.48, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},
    {"nama": "Monumen Merauke", "prov": "Papua Selatan", "kat": "Modern", "price": 0, "lat": -8.49, "lon": 140.40, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Lembah Baliem", "prov": "Papua Pegunungan", "kat": "Budaya", "price": 50000, "lat": -4.01, "lon": 138.92, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=600"},
    {"nama": "Sorong City", "prov": "Papua Barat Daya", "kat": "Modern", "price": 0, "lat": -0.87, "lon": 131.25, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"}
]
df = pd.DataFrame(wisata_list)

# 4. SIDEBAR UNIVERSAL
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=180)
    st.markdown("### **PORTAL LAYANAN**")
    
    # Universal User Info
    st.markdown("""
    <div style="background:#f1f5f9; padding:15px; border-radius:12px; margin-bottom:20px; border: 1px solid #e2e8f0;">
        <p style="margin:0; font-weight:700; color:#0f172a;">👤 Pengguna Publik</p>
        <p style="margin:0; font-size:0.8rem; color:#64748b;">Sesi Aktif: Terverifikasi</p>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio("Sistem Navigasi:", ["🏠 Beranda Utama", "🗺️ Peta Lokasi (GIS)", "🗂️ Katalog Destinasi"])
    st.markdown("---")
    st.info(f"Integrasi 38 Provinsi Aktif")

# 5. LOGIKA HALAMAN
if menu == "🏠 Beranda Utama":
    st.title("Gerbang Pariwisata Digital Indonesia")
    st.markdown("#### *Eksplorasi Keindahan 38 Provinsi Secara Real-Time*")
    st.image("https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=1400", use_container_width=True)
    
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown('<div style="background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0; text-align:center;"><h3>38 Provinsi</h3><p>Cakupan data wilayah terlengkap di Indonesia.</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div style="background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0; text-align:center;"><h3>Peta GIS</h3><p>Visualisasi titik lokasi presisi berbasis koordinat.</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div style="background:white; padding:20px; border-radius:15px; border:1px solid #e2e8f0; text-align:center;"><h3>Universal</h3><p>Akses terbuka untuk seluruh wisatawan dunia.</p></div>', unsafe_allow_html=True)

elif menu == "🗺️ Peta Lokasi (GIS)":
    st.header("Sistem Informasi Geografis Destinasi")
    st.write("Arahkan kursor ke titik lokasi untuk melihat detail destinasi di setiap provinsi.")
    
    fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="nama", hover_data=["prov", "kat"],
                            color="kat", zoom=3.8, height=650)
    fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

elif menu == "🗂️ Katalog Destinasi":
    st.header("Direktori Destinasi Nasional")
    
    # Global Filter
    search = st.text_input("🔍 Cari destinasi atau provinsi...")
    kat_pilihan = st.multiselect("Saring Berdasarkan Kategori:", df["kat"].unique(), default=df["kat"].unique())
    
    filtered_df = df[df["kat"].isin(kat_pilihan)]
    if search:
        filtered_df = filtered_df[filtered_df["nama"].str.contains(search, case=False) | filtered_df["prov"].str.contains(search, case=False)]
    
    st.write(f"Menampilkan **{len(filtered_df)}** Lokasi Terverifikasi")
    
    # GRID DISPLAY
    cols = st.columns(3)
    for i, row in filtered_df.reset_index().iterrows():
        with cols[i % 3]:
            st.markdown(f'''
                <div class="travel-card">
                    <img src="{row['img']}" style="width:100%; height:200px; object-fit:cover;">
                    <div class="card-content">
                        <span style="background:#0284c7; color:white; padding:3px 10px; border-radius:20px; font-size:0.7rem; font-weight:600;">{row['kat']}</span>
                        <h3 style="margin:10px 0 5px 0; font-size:1.2rem;">{row['nama']}</h3>
                        <p style="color:#64748b; font-size:0.9rem; margin-bottom:10px;">📍 {row['prov']}</p>
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span class="price-tag">Rp {row['price']:,}</span>
                            <span style="color:#f59e0b; font-weight:600;">⭐ Terpopuler</span>
                        </div>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
            with st.expander("Informasi Selengkapnya"):
                st.write(f"Destinasi ini merupakan ikon wisata kategori **{row['kat']}** di Provinsi **{row['prov']}**.")
                st.write("Fasilitas: Area Parkir, Toilet, Spot Foto, dan Pusat Informasi.")
                if st.button(f"Ajukan Reservasi: {row['nama']}", key=row['nama']):
                    st.success("Sistem sedang memproses permintaan Anda. Harap tunggu konfirmasi.")

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 Portal Pariwisata Digital Indonesia. Lisensi Terbuka.</p>", unsafe_allow_html=True)
