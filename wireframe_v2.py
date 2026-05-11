import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="Wonderful Indonesia | Official 38 Provinces", page_icon="🇮🇩", layout="wide")

# 2. CSS CUSTOM UNTUK TAMPILAN ELITE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #f8fafc; }
    .travel-card {
        background: white; border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
        margin-bottom: 25px; overflow: hidden; transition: 0.3s;
    }
    .card-content { padding: 20px; }
    h1 { color: #0f172a; font-weight: 800; font-size: 3rem !important; text-align: center; }
    h2 { color: #0284c7; font-weight: 700; border-bottom: 3px solid #0284c7; padding-bottom: 10px; }
    .price-tag { color: #059669; font-weight: 700; font-size: 1.2rem; }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #0284c7 0%, #0ea5e9 100%);
        color: white; border-radius: 12px; border: none; padding: 12px 25px; font-weight: 700;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE 38 PROVINSI LENGKAP (URUT BERDASARKAN WILAYAH)
wisata_data = [
    # SUMATERA
    {"nama": "Masjid Baiturrahman", "prov": "Aceh", "kat": "Religi", "harga": 0, "lat": 5.55, "lon": 95.32, "img": "https://images.unsplash.com/photo-1590278035755-927807604929?w=600"},
    {"nama": "Danau Toba", "prov": "Sumatera Utara", "kat": "Alam", "harga": 25000, "lat": 2.68, "lon": 98.88, "img": "https://images.unsplash.com/photo-1572458421035-7c858a74e503?w=600"},
    {"nama": "Jam Gadang", "prov": "Sumatera Barat", "kat": "Sejarah", "harga": 5000, "lat": -0.30, "lon": 100.37, "img": "https://images.unsplash.com/photo-1635345638426-5b4815456f93?w=600"},
    {"nama": "Istana Siak", "prov": "Riau", "kat": "Sejarah", "harga": 15000, "lat": 0.79, "lon": 102.04, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=600"},
    {"nama": "Jembatan Barelang", "prov": "Kepulauan Riau", "kat": "Modern", "harga": 0, "lat": 1.05, "lon": 104.05, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=600"},
    {"nama": "Candi Muaro Jambi", "prov": "Jambi", "kat": "Budaya", "harga": 10000, "lat": -1.61, "lon": 103.61, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Benteng Marlborough", "prov": "Bengkulu", "kat": "Sejarah", "harga": 5000, "lat": -3.79, "lon": 102.25, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},
    {"nama": "Jembatan Ampera", "prov": "Sumatera Selatan", "kat": "Modern", "harga": 0, "lat": -2.99, "lon": 104.76, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},
    {"nama": "Pantai Parai", "prov": "Bangka Belitung", "kat": "Bahari", "harga": 20000, "lat": -2.74, "lon": 107.63, "img": "https://images.unsplash.com/photo-1621644787508-41076f80907d?w=600"},
    {"nama": "Way Kambas", "prov": "Lampung", "kat": "Alam", "harga": 20000, "lat": -5.00, "lon": 105.75, "img": "https://images.unsplash.com/photo-1581852017103-68ac65514cf7?w=600"},
    
    # JAWA
    {"nama": "Monas", "prov": "DKI Jakarta", "kat": "Modern", "harga": 15000, "lat": -6.17, "lon": 106.82, "img": "https://images.unsplash.com/photo-1555899434-94d1368aa7af?w=600"},
    {"nama": "Gedung Sate", "prov": "Jawa Barat", "kat": "Sejarah", "harga": 5000, "lat": -6.90, "lon": 107.61, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=600"},
    {"nama": "Masjid Agung Banten", "prov": "Banten", "kat": "Religi", "harga": 0, "lat": -6.03, "lon": 106.15, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=600"},
    {"nama": "Candi Borobudur", "prov": "Jawa Tengah", "kat": "Budaya", "harga": 50000, "lat": -7.60, "lon": 110.20, "img": "https://images.unsplash.com/photo-1626202341512-a97a922a0887?w=600"},
    {"nama": "Keraton Yogyakarta", "prov": "DI Yogyakarta", "kat": "Budaya", "harga": 15000, "lat": -7.79, "lon": 110.36, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Gunung Bromo", "prov": "Jawa Timur", "kat": "Alam", "harga": 35000, "lat": -7.94, "lon": 112.95, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},

    # BALI & NUSA TENGGARA
    {"nama": "Pura Besakih", "prov": "Bali", "kat": "Religi", "harga": 30000, "lat": -8.37, "lon": 115.45, "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=600"},
    {"nama": "Sirkuit Mandalika", "prov": "NTB", "kat": "Modern", "harga": 50000, "lat": -8.89, "lon": 116.29, "img": "https://images.unsplash.com/photo-1625232930267-2856403565e3?w=600"},
    {"nama": "Pink Beach", "prov": "NTT", "kat": "Bahari", "harga": 50000, "lat": -8.49, "lon": 119.87, "img": "https://images.unsplash.com/photo-1616422285623-13ff0167c95c?w=600"},

    # KALIMANTAN
    {"nama": "Tugu Khatulistiwa", "prov": "Kalimantan Barat", "kat": "Sejarah", "harga": 0, "lat": 0.00, "lon": 109.33, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Sungai Kahayan", "prov": "Kalimantan Tengah", "kat": "Alam", "harga": 0, "lat": -2.21, "lon": 113.91, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=600"},
    {"nama": "Pasar Terapung", "prov": "Kalimantan Selatan", "kat": "Budaya", "harga": 0, "lat": -3.31, "lon": 114.59, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=600"},
    {"nama": "Pulau Derawan", "prov": "Kalimantan Timur", "kat": "Bahari", "harga": 50000, "lat": 2.25, "lon": 118.24, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=600"},
    {"nama": "Krayan", "prov": "Kalimantan Utara", "kat": "Alam", "harga": 0, "lat": 3.92, "lon": 115.61, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"},

    # SULAWESI
    {"nama": "Bunaken", "prov": "Sulawesi Utara", "kat": "Bahari", "harga": 50000, "lat": 1.63, "lon": 124.77, "img": "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=600"},
    {"nama": "Togean", "prov": "Sulawesi Tengah", "kat": "Bahari", "harga": 25000, "lat": -0.41, "lon": 121.84, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},
    {"nama": "Pantai Losari", "prov": "Sulawesi Selatan", "kat": "Modern", "harga": 0, "lat": -5.14, "lon": 119.40, "img": "https://images.unsplash.com/photo-1546500840-ae38253aba9b?w=600"},
    {"nama": "Wakatobi", "prov": "Sulawesi Tenggara", "kat": "Bahari", "harga": 150000, "lat": -5.32, "lon": 123.58, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=600"},
    {"nama": "Benteng Otanaha", "prov": "Gorontalo", "kat": "Sejarah", "harga": 5000, "lat": 0.54, "lon": 123.05, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=600"},
    {"nama": "Pantai Manakarra", "prov": "Sulawesi Barat", "kat": "Bahari", "harga": 0, "lat": -2.67, "lon": 118.88, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=600"},

    # MALUKU & PAPUA
    {"nama": "Banda Neira", "prov": "Maluku", "kat": "Sejarah", "harga": 20000, "lat": -4.51, "lon": 129.90, "img": "https://images.unsplash.com/photo-1570789210967-2cac24afad44?w=600"},
    {"nama": "Benteng Tolukko", "prov": "Maluku Utara", "kat": "Sejarah", "harga": 10000, "lat": 0.73, "lon": 127.36, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=600"},
    {"nama": "Danau Sentani", "prov": "Papua", "kat": "Alam", "harga": 10000, "lat": -2.59, "lon": 140.48, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=600"},
    {"nama": "Raja Ampat", "prov": "Papua Barat", "kat": "Bahari", "harga": 500000, "lat": -0.23, "lon": 130.50, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=600"},
    {"nama": "Lembah Baliem", "prov": "Papua Pegunungan", "kat": "Budaya", "harga": 100000, "lat": -4.01, "lon": 138.92, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=600"},
    {"nama": "Nabire", "prov": "Papua Tengah", "kat": "Alam", "harga": 20000, "lat": -3.36, "lon": 135.48, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=600"},
    {"nama": "Merauke", "prov": "Papua Selatan", "kat": "Modern", "harga": 0, "lat": -8.49, "lon": 140.40, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=600"},
    {"nama": "Sorong", "prov": "Papua Barat Daya", "kat": "Modern", "harga": 0, "lat": -0.87, "lon": 131.25, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=600"}
]
df = pd.DataFrame(wisata_data)

# 4. SIDEBAR NAVIGATION
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=180)
    st.markdown("---")
    menu = st.radio("Layanan Utama:", ["🏠 Beranda", "📊 Analitik Wisata", "🗺️ Peta Lokasi (GIS)", "🛒 Reservasi & QR Tiket"])
    st.info(f"Database: 38 Provinsi Aktif")

# 5. LOGIKA HALAMAN
if menu == "🏠 Beranda":
    st.title("Wonderful Indonesia Digital Atlas")
    st.image("https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=1400", use_container_width=True)
    st.markdown("### *Portal Eksplorasi 38 Provinsi Nusantara*")

elif menu == "📊 Analitik Wisata":
    st.header("Dashboard Analitik Pariwisata")
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Sebaran Kategori")
        fig_pie = px.pie(df, names='kat', hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_pie, use_container_width=True)
    with c2:
        st.write("### Perbandingan Harga Tiket")
        fig_bar = px.bar(df, x='nama', y='harga', color='kat', template="plotly_white")
        st.plotly_chart(fig_bar, use_container_width=True)

elif menu == "🗺️ Peta Lokasi (GIS)":
    st.header("Sistem Informasi Geografis Destinasi")
    fig_map = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="nama", hover_data=["prov", "kat", "harga"],
                                color="kat", zoom=3.8, height=650)
    fig_map.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)

elif menu == "🛒 Reservasi & QR Tiket":
    st.header("Pusat Reservasi & E-Ticketing")
    col_a, col_b = st.columns([1.2, 1])
    with col_a:
        pilih = st.selectbox("Pilih Destinasi Wisata:", df["nama"].tolist())
        sel = df[df["nama"] == pilih].iloc[0]
        st.markdown(f"""
            <div class="travel-card">
                <img src="{sel['img']}" style="width:100%; height:250px; object-fit:cover;">
                <div class="card-content">
                    <h2>{sel['nama']}</h2>
                    <p>📍 {sel['prov']}</p>
                    <p class="price-tag">Harga: Rp {sel['harga']:,}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.write("### Form Reservasi")
        nama = st.text_input("Nama Lengkap")
        jml = st.number_input("Jumlah Tiket", min_value=1, value=1)
        total = sel['harga'] * jml
        st.write(f"#### Total Bayar: Rp {total:,}")
        if st.button("TERBITKAN TIKET"):
            if nama == "": st.error("Isi Nama!")
            else:
                st.balloons()
                st.success("Pembayaran Sukses!")
                st.markdown("---")
                qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=TIKET-{pilih}-{nama}"
                st.image(qr_url, caption="QR-Code Tiket Anda")
                st.write(f"Nama: {nama} | Destinasi: {pilih} | Status: LUNAS")

# FOOTER
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>© 2026 Portal Pariwisata Digital Indonesia - Dibuat oleh Nur Annisa Bangka.</p>", unsafe_allow_html=True)
