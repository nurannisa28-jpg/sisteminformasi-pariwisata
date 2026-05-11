import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA ELITE
# ==========================================
st.set_page_config(
    page_title="Nusantara Elite Travel | Wonderful Indonesia", 
    page_icon="🗺️", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# 2. CSS CUSTOM: MEWAH, JELAS, & CORPORATE STYLE
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600;700&display=swap');
    
    /* Font Dasar: Inter (Sangat Jelas & Modern) */
    html, body, [class*="css"] { 
        font-family: 'Inter', sans-serif; 
        color: #1e293b;
    }
    
    /* Font Judul: Playfair Display (Mewah & Klasik) */
    h1, h2, .luxury-header { 
        font-family: 'Playfair Display', serif; 
        font-weight: 700; 
        color: #0f172a !important; 
        margin-top: 0px;
    }
    h1 { font-size: 3.5rem !important; }
    h2 { font-size: 2.2rem !important; color: #0284c7 !important; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }
    h3 { font-size: 1.5rem !important; font-weight: 600; color: #0f172a; }

    .stApp { background-color: #f8fafc; }
    
    /* Container untuk Foto (Agar Rapi & Tidak Pecah) */
    .img-container {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }

    /* Card Styling */
    .stExpander {
        background-color: white;
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        margin-bottom: 15px;
    }
    
    /* Label Sidebar */
    .css-1d391kg { font-size: 1.1rem; font-weight: 600; color: #0f172a !important; }
    
    /* Custom Footer */
    .footer {
        text-align: center;
        padding: 30px 0;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. DATABASE DESTINASI SUPER SEMPURNA
# ==========================================
# Menggunakan link source.unsplash.com yang sangat stabil
destinasi_data = [
    {
        "id": "raja_ampat",
        "nama": "Raja Ampat",
        "provinsi": "Papua Barat",
        "tagline": "The Last Paradise on Earth",
        "desc": "Rumah bagi 75% spesies karang dunia. Pusat keanekaragaman hayati laut global di Segitiga Karang.",
        "images": [
            "https://source.unsplash.com/800x600/?ocean,indonesia",
            "https://source.unsplash.com/800x600/?coral,rajaampat"
        ],
        "kategori": "Bahari & Selam",
        "rating": "5.0 ★",
        "cost": "High-End"
    },
    {
        "id": "komodo",
        "nama": "Pulau Komodo",
        "provinsi": "NTT",
        "tagline": "Home of the Ancient Dragons",
        "desc": "Hanya di sini reptil purba terbesar di dunia hidup bebas di habitat aslinya. Nikmati keindahan Pantai Pink yang menawan.",
        "images": [
            "https://source.unsplash.com/800x600/?komododragon,island",
            "https://source.unsplash.com/800x600/?pinkbeach,indonesia"
        ],
        "kategori": "Konservasi & Alam",
        "rating": "4.9 ★",
        "cost": "Moderate-High"
    },
    {
        "id": "borobudur",
        "nama": "Candi Borobudur",
        "provinsi": "Jawa Tengah",
        "tagline": "The World's Largest Buddhist Temple",
        "desc": "Karya agung arsitektur abad ke-9, warisan dunia UNESCO yang memancarkan spiritualitas dan sejarah luhur.",
        "images": [
            "https://source.unsplash.com/800x600/?borobudur,temple",
            "https://source.unsplash.com/800x600/?sunrise,indonesia"
        ],
        "kategori": "Sejarah & Budaya",
        "rating": "4.8 ★",
        "cost": "Moderate"
    }
]

# ==========================================
# 4. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg", width=180)
    st.markdown("---")
    menu = st.radio("Sistem Navigasi:", ["🏢 Beranda Korporat", "🗺️ Katalog Pilihan Premium", "📊 Dashboard Data & Analitik"])
    st.markdown("---")
    st.info("Sistem Informasi Pariwisata v2.0 - Final Edition")

# ==========================================
# 5. LOGIKA HALAMAN
# ==========================================

# --- HALAMAN 1: BERANDA KORPORAT ---
if menu == "🏢 Beranda Korporat":
    col_main_1, col_main_2 = st.columns([2, 1])
    
    with col_main_1:
        st.title("Wonderful Indonesia Digital Gateway")
        st.markdown("### *Portal Eksklusif Informasi Destinasi Premium Nusantara*")
        st.write("Sertifikasi Wonderful Indonesia menjamin standar kualitas tertinggi dalam setiap pengalaman perjalanan Anda di Nusantara. Temukan kemewahan alam dan kekayaan budaya yang autentik.")
    
    with col_main_2:
        st.image("https://source.unsplash.com/600x400/?beach,luxury", use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Destinasi Premium", "20+", "✓ Certified")
    c2.metric("Rating Kepuasan Global", "96%", "↑ 1.2%")
    c3.metric("Kategori Wisata", "5 Utama", "✓ Beragam")

# --- HALAMAN 2: KATALOG PREMIUM (DENGAN TABS GAMBAR SEMPURNA) ---
elif menu == "🗺️ Katalog Pilihan Premium":
    st.header("Destinasi Unggulan Bersertifikat")
    st.write("Silakan pilih destinasi di bawah untuk melihat detail, galeri foto, dan informasi biaya.")

    for item in destinasi_data:
        # Menggunakan Expander agar rapi, dan menaruh Kategori & Rating di label agar elit
        expander_title = f"{item['nama']} - {item['provinsi']} ({item['cost']})"
        
        with st.expander(expander_title):
            st.markdown(f"**Tagline:** *{item['tagline']}*")
            st.write(item['desc'])
            
            # Sub-kolom di dalam expander
            col_inner_1, col_inner_2 = st.columns([2, 1])
            
            with col_inner_1:
                st.write("### Galeri Foto (Slide)")
                # TABS DI DALAM EXPANDER UNTUK SIMULASI SLIDE
                tab_titles = [f"Foto {i+1}" for i in range(len(item['images']))]
                tabs = st.tabs(tab_titles)
                for i, tab in enumerate(tabs):
                    with tab:
                        # TAMPILKAN GAMBAR DENGAN FUNGSI UNTUK MEMASTIKAN STABILITAS
                        try:
                            # Menambahkan 'try' untuk menangani jika link source unsplash gagal (sangat jarang)
                            st.markdown(f'<div class="img-container">', unsafe_allow_html=True)
                            st.image(item['images'][i], use_container_width=True, caption=f"{item['nama']} - Foto {i+1}")
                            st.markdown('</div>', unsafe_allow_html=True)
                        except Exception:
                            st.error("Gagal memuat gambar. Silakan refresh halaman.")

            with col_inner_2:
                st.write("### Informasi")
                st.markdown(f"**Kategori:** `{item['kategori']}`")
                st.markdown(f"**Rating:** `{item['rating']}`")
                
                if st.button(f"Cek Reservasi {item['nama']}", key=item['id']):
                    st.success(f"Permintaan informasi reservasi ke {item['nama']} telah dikirim!")

# --- HALAMAN 3: DASHBOARD DATA ---
elif menu == "📊 Dashboard Data & Analitik":
    st.header("Analisis Data Pariwisata Nusantara")
    
    # Dataframe Elit
    df = pd.DataFrame(destinasi_data).drop(columns=['id', 'images', 'desc'])
    
    col_db_1, col_db_2 = st.columns([1, 1])
    
    with col_db_1:
        st.write("### Daftar Destinasi Bersertifikat")
        st.dataframe(df, use_container_width=True)
        
    with col_db_2:
        st.write("### Distribusi Kategori")
        fig = px.pie(df, names='kategori', hole=.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 6. FOOTER
# ==========================================
st.markdown("""
    <div class="footer">
        <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Wonderful_Indonesia_logo.svg" width="100"><br>
        © 2026 PT. Pariwisata Nusantara Elit Digital Division. <br>
        Developed by Nur Annisa. Authorized Wonderful Indonesia Partner.
    </div>
    """, unsafe_allow_html=True)
