import streamlit as st
import pandas as pd
import plotly.express as px

# 1. KONFIGURASI HALAMAN (TAMPILAN PREMIUM)
st.set_page_config(
    page_title="Sistem Informasi Pariwisata 38 Provinsi",
    page_icon="🇮🇩",
    layout="wide"
)

# 2. CUSTOM CSS (SESUAI FORMAT MASTERPIECE)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    .stApp { background-color: #fcfcfc; }
    .travel-card {
        background: white; border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #eee;
        margin-bottom: 20px; overflow: hidden;
    }
    .card-content { padding: 15px; }
    h1 { color: #1e293b; font-weight: 800; text-align: center; }
    .stButton>button { background: #0284c7; color: white; border-radius: 8px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE LENGKAP 38 PROVINSI (SESUAI FORMAT TERBARU)
wisata_data = [
    # SUMATERA (10)
    {"nama": "Masjid Baiturrahman", "prov": "Aceh", "kat": "Religi", "lat": 5.55, "lon": 95.32, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=400"},
    {"nama": "Danau Toba", "prov": "Sumatera Utara", "kat": "Alam", "lat": 2.68, "lon": 98.88, "img": "https://images.unsplash.com/photo-1572458421035-7c858a74e503?w=400"},
    {"nama": "Jam Gadang", "prov": "Sumatera Barat", "kat": "Sejarah", "lat": -0.30, "lon": 100.37, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=400"},
    {"nama": "Istana Siak", "prov": "Riau", "kat": "Sejarah", "lat": 0.79, "lon": 102.04, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=400"},
    {"nama": "Jembatan Barelang", "prov": "Kepulauan Riau", "kat": "Modern", "lat": 1.05, "lon": 104.05, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=400"},
    {"nama": "Candi Muaro Jambi", "prov": "Jambi", "kat": "Budaya", "lat": -1.61, "lon": 103.61, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=400"},
    {"nama": "Benteng Marlborough", "prov": "Bengkulu", "kat": "Sejarah", "lat": -3.79, "lon": 102.25, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=400"},
    {"nama": "Jembatan Ampera", "prov": "Sumatera Selatan", "kat": "Modern", "lat": -2.99, "lon": 104.76, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=400"},
    {"nama": "Pantai Laskar Pelangi", "prov": "Bangka Belitung", "kat": "Bahari", "lat": -2.74, "lon": 107.63, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=400"},
    {"nama": "Way Kambas", "prov": "Lampung", "lat": -5.00, "lon": 105.75, "kat": "Alam", "img": "https://images.unsplash.com/photo-1591017403286-fd8ba110ee04?w=400"},
    
    # JAWA (6)
    {"nama": "Monas", "prov": "DKI Jakarta", "kat": "Modern", "lat": -6.17, "lon": 106.82, "img": "https://images.unsplash.com/photo-1555899434-94d1368aa7af?w=400"},
    {"nama": "Gedung Sate", "prov": "Jawa Barat", "kat": "Sejarah", "lat": -6.90, "lon": 107.61, "img": "https://images.unsplash.com/photo-1590425028080-60b13576081d?w=400"},
    {"nama": "Pantai Anyer", "prov": "Banten", "kat": "Bahari", "lat": -6.03, "lon": 106.15, "img": "https://images.unsplash.com/photo-1571738205359-7d47bf47385f?w=400"},
    {"nama": "Candi Borobudur", "prov": "Jawa Tengah", "kat": "Budaya", "lat": -7.60, "lon": 110.20, "img": "https://images.unsplash.com/photo-1626202341512-a97a922a0887?w=400"},
    {"nama": "Keraton Yogyakarta", "prov": "DI Yogyakarta", "kat": "Budaya", "lat": -7.75, "lon": 110.49, "img": "https://images.unsplash.com/photo-1596402184320-417d7178b2cd?w=400"},
    {"nama": "Gunung Bromo", "prov": "Jawa Timur", "kat": "Alam", "lat": -7.94, "lon": 112.95, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=400"},

    # BALI & NUSA TENGGARA (3)
    {"nama": "Tanah Lot", "prov": "Bali", "kat": "Religi", "lat": -8.62, "lon": 115.08, "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=400"},
    {"nama": "Mandalika", "prov": "NTB", "kat": "Modern", "lat": -8.89, "lon": 116.29, "img": "https://images.unsplash.com/photo-1512100356956-c1287eb0a1bc?w=400"},
    {"nama": "Pulau Komodo", "prov": "NTT", "kat": "Alam", "lat": -8.49, "lon": 119.87, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=400"},

    # KALIMANTAN (5)
    {"nama": "Tugu Khatulistiwa", "prov": "Kalimantan Barat", "kat": "Sejarah", "lat": 0.00, "lon": 109.33, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=400"},
    {"nama": "Sungai Kahayan", "prov": "Kalimantan Tengah", "kat": "Alam", "lat": -2.21, "lon": 113.91, "img": "https://images.unsplash.com/photo-1627918546173-982862c95333?w=400"},
    {"nama": "Pasar Terapung", "prov": "Kalimantan Selatan", "kat": "Budaya", "lat": -3.31, "lon": 114.59, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=400"},
    {"nama": "Derawan", "prov": "Kalimantan Timur", "kat": "Bahari", "lat": 2.25, "lon": 118.24, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=400"},
    {"nama": "Krayan", "prov": "Kalimantan Utara", "kat": "Alam", "lat": 3.92, "lon": 115.61, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=400"},

    # SULAWESI (6)
    {"nama": "Bunaken", "prov": "Sulawesi Utara", "kat": "Bahari", "lat": 1.63, "lon": 124.77, "img": "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=400"},
    {"nama": "Togean", "prov": "Sulawesi Tengah", "kat": "Bahari", "lat": -0.41, "lon": 121.84, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=400"},
    {"nama": "Pantai Losari", "prov": "Sulawesi Selatan", "kat": "Modern", "lat": -5.14, "lon": 119.40, "img": "https://images.unsplash.com/photo-1546500840-ae38253aba9b?w=400"},
    {"nama": "Wakatobi", "prov": "Sulawesi Tenggara", "kat": "Bahari", "lat": -5.32, "lon": 123.58, "img": "https://images.unsplash.com/photo-1516690561799-46d8f74f9abf?w=400"},
    {"nama": "Benteng Otanaha", "prov": "Gorontalo", "kat": "Sejarah", "lat": 0.54, "lon": 123.05, "img": "https://images.unsplash.com/photo-1596708034500-1c944888be62?w=400"},
    {"nama": "Pantai Manakarra", "prov": "Sulawesi Barat", "kat": "Bahari", "lat": -2.67, "lon": 118.88, "img": "https://images.unsplash.com/photo-1540656012015-8447814b1049?w=400"},

    # MALUKU & PAPUA (8 - TERMASUK PEMEKARAN BARU)
    {"nama": "Banda Neira", "prov": "Maluku", "kat": "Sejarah", "lat": -4.51, "lon": 129.90, "img": "https://images.unsplash.com/photo-1570789210967-2cac24afad44?w=400"},
    {"nama": "Benteng Tolukko", "prov": "Maluku Utara", "kat": "Sejarah", "lat": 0.73, "lon": 127.36, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=400"},
    {"nama": "Raja Ampat", "prov": "Papua Barat", "kat": "Bahari", "lat": -0.23, "lon": 130.50, "img": "https://images.unsplash.com/photo-1589197331516-4d839633b42a?w=400"},
    {"nama": "Danau Sentani", "prov": "Papua", "kat": "Alam", "lat": -2.59, "lon": 140.48, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=400"},
    {"nama": "Pantai Nabire", "prov": "Papua Tengah", "kat": "Alam", "lat": -3.36, "lon": 135.48, "img": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=400"},
    {"nama": "Tugu Merauke", "prov": "Papua Selatan", "kat": "Modern", "lat": -8.49, "lon": 140.40, "img": "https://images.unsplash.com/photo-1544919931-15c613e51a6d?w=400"},
    {"nama": "Lembah Baliem", "prov": "Papua Pegunungan", "kat": "Budaya", "lat": -4.01, "lon": 138.92, "img": "https://images.unsplash.com/photo-1516939150577-16711756babf?w=400"},
    {"nama": "Sorong City", "prov": "Papua Barat Daya", "kat": "Modern", "lat": -0.87, "lon": 131.25, "img": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?w=400"}
]
df = pd.DataFrame(wisata_data)

# 4. SIDEBAR MENU
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=150)
    st.title("Sistem Informasi")
    menu = st.radio("Pilih Halaman:", ["🏠 Beranda", "🗺️ Peta Destinasi (GIS)", "🗂️ Direktori Wisata"])
    st.markdown("---")
    st.write("👤 **Profil: User Publik**")

# 5. LOGIKA HALAMAN
if menu == "🏠 Beranda":
    st.title("Wonderful Indonesia")
    st.write("### Eksplorasi 38 Provinsi")
    st.image("https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?w=1200", use_container_width=True)
    st.write("Sistem ini menyajikan data pariwisata lengkap dari 38 provinsi di Indonesia untuk kebutuhan informasi perjalanan Anda.")

elif menu == "🗺️ Peta Destinasi (GIS)":
    st.title("Sistem Informasi Geografis (Peta)")
    fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="nama", hover_data=["prov", "kat"],
                            color="kat", zoom=3, height=600)
    fig.update_layout(mapbox_style="open-street-map", margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)

elif menu == "🗂️ Direktori Wisata":
    st.title("Direktori Destinasi Nasional")
    
    # Filter
    kat_list = ["Semua"] + list(df["kat"].unique())
    pilihan = st.selectbox("Saring Kategori:", kat_list)
    
    if pilihan == "Semua":
        f_df = df
    else:
        f_df = df[df["kat"] == pilihan]

    # Grid Display
    rows = st.columns(3)
    for index, row in f_df.reset_index().iterrows():
        with rows[index % 3]:
            st.markdown(f"""
                <div class="travel-card">
                    <img src="{row['img']}" style="width:100%; height:180px; object-fit:cover;">
                    <div class="card-content">
                        <small>{row['kat']} | {row['prov']}</small>
                        <h4 style="margin:5px 0;">{row['nama']}</h4>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            if st.button("Lihat Detail", key=f"btn_{index}"):
                st.info(f"Informasi Lengkap: {row['nama']} berada di {row['prov']}. Tiket tersedia di lokasi.")

st.markdown("---")
st.markdown("<p style='text-align:center;'>© 2026 Portal Pariwisata Nusantara - 38 Provinsi</p>", unsafe_allow_html=True)
