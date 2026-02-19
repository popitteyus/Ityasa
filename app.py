import streamlit as st
from utils.db import get_divisi

st.set_page_config(
    page_title="IVA Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Styling kustom (biar keren)
st.markdown("""
<style>
.main-header {
    font-size: 3rem;
    font-weight: 700;
    background: linear-gradient(90deg, #4F8BF9, #9D4F9F);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.sub-header {
    font-size: 1.2rem;
    color: #AAAAAA;
    margin-top: 0;
}
.stButton>button {
    border-radius: 30px;
    background: linear-gradient(90deg, #4F8BF9, #9D4F9F);
    color: white;
    border: none;
    padding: 0.5rem 2rem;
    font-weight: 600;
}
.stButton>button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("logo.png", use_column_width=True)
    st.markdown("## 🧠 IVA Agency")
    st.markdown("Ruang kendali kreatif")
    st.markdown("---")
    st.markdown("### Divisi Aktif")
    divisi = get_divisi()
    if divisi:
        for d in divisi:
            st.markdown(f"- {d['nama_divisi']}")
    else:
        st.write("(Koneksi database belum tersedia)")
    st.markdown("---")
    st.caption("v1.0 - Human-in-the-loop")

# Halaman utama
st.markdown('<h1 class="main-header">🏢 IVA (Ityasa Virtual Agency)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Selamat datang, Founder. Kelola agensi AI Anda dengan mulus.</p>', unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Divisi AI", len(divisi) if divisi else 0)
with col2:
    st.metric("Proyek Aktif", "?")  # nanti diisi dari db
with col3:
    st.metric("Tugas Selesai", "?")  # nanti diisi

st.markdown("### 🚀 Mulai Cepat")
if st.button("➕ Input Proyek Baru"):
    st.switch_page("pages/01_Input_Proyek.py")
if st.button("📋 Lihat Semua Proyek"):
    st.switch_page("pages/02_Daftar_Proyek.py")

