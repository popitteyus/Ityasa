import streamlit as st
from utils.styles import get_css
from utils.db import get_divisi
import time

st.set_page_config(
    page_title="IVA - Ityasa Virtual Agency",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Pasang CSS dari file styles.py
st.markdown(get_css(), unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    try:
        st.image("logo.png", use_column_width=True)
    except:
        st.image("https://via.placeholder.com/150x50?text=IVA", use_column_width=True)
    
    st.markdown("## 🧠 **Ityasa Virtual Agency**")
    st.markdown("Ruang kendali kreatif dengan sentuhan manusia")
    st.markdown("---")
    
    st.markdown("### 🤖 Divisi AI Aktif")
    divisi = get_divisi()
    if divisi:
        for d in divisi:
            st.markdown(f"- **{d['nama_divisi']}**")
            st.caption(f"  {d['deskripsi']}")
    else:
        st.write("(koneksi database...)")
    
    st.markdown("---")
    st.caption(f"v2.0 - Ityasa OS • {time.strftime('%Y')}")
    
    # Animasi kecil (tanpa emoji untuk menghindari error)
    st.markdown('<div style="text-align: center; margin-top: 20px;"><span style="font-size: 0.8rem; color: #888;">Crafted with precision</span></div>', unsafe_allow_html=True)

# ========== MAIN PAGE ==========
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<h1 class="main-header">🏢 IVA</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Ityasa Virtual Agency — di mana AI bekerja, Anda yang memimpin.</p>', unsafe_allow_html=True)
with col2:
    st.markdown("### 👋 **Halo, Human**")
    if st.button("🔄 Refresh Data"):
        st.rerun()

st.markdown("---")

# ========== METRICS ==========
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Divisi AI", len(divisi) if divisi else 0, delta="6 Gems siap")
with col2:
    st.metric("Proyek Aktif", "—", delta="0")
with col3:
    st.metric("Tugas Selesai", "—", delta="0")
with col4:
    st.metric("Template", "—", delta="0")

st.markdown("---")

# ========== QUICK ACTIONS ==========
st.markdown("### 🚀 **Aksi Cepat**")

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("➕ Proyek Baru", use_container_width=True):
        st.switch_page("pages/01_Input_Proyek.py")
with col2:
    if st.button("📋 Lihat Proyek", use_container_width=True):
        st.switch_page("pages/02_Daftar_Proyek.py")
with col3:
    if st.button("⚙️ Tugas Divisi", use_container_width=True):
        st.switch_page("pages/03_Tugas_Divisi.py")
with col4:
    if st.button("📚 Template", use_container_width=True):
        st.switch_page("pages/06_Kelola_Template.py")

# ========== RECENT ACTIVITY ==========
st.markdown("---")
st.markdown("### 📌 **Aktivitas Terkini**")

with st.container(border=True):
    st.info("Belum ada aktivitas. Mulai dengan input proyek baru.")

# Footer
st.markdown('<div style="text-align: center; color: #718096; font-size: 0.9rem; margin-top: 3rem; padding: 1rem;">IVA — Where creativity meets artificial intelligence, guided by human wisdom.</div>', unsafe_allow_html=True)
