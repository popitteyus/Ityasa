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

st.markdown(get_css(), unsafe_allow_html=True)

# ========== CUSTOM CSS PREMIUM ==========
st.markdown("""
<style>
    /* Import font Poppins */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global styling */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Background gradient halus */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Sidebar styling - glass effect */
    .css-1d391kg, .css-12oz5g7 {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Header utama dengan gradasi emas */
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.3rem;
        color: #4a5568;
        margin-top: 0;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    /* Card styling - glassmorphism */
    div.stContainer {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.8rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    div.stContainer:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.6rem 2rem;
        font-weight: 500;
        font-size: 1rem;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
        background: linear-gradient(135deg, #5a67d8 0%, #6b46a0 100%);
    }
    
    /* Metric styling */
    .stMetric {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
    
    .stMetric label {
        color: #4a5568;
        font-weight: 500;
    }
    
    .stMetric div {
        color: #2d3748;
        font-weight: 700;
        font-size: 2rem;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(5px);
        border-radius: 15px;
        font-weight: 600;
        color: #2d3748;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
        background: rgba(255,255,255,0.3);
        backdrop-filter: blur(5px);
        padding: 0.5rem 1rem;
        border-radius: 40px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 30px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        color: #4a5568;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
    }
    
    /* Form styling */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 15px;
        border: 1px solid rgba(102, 126, 234, 0.3);
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(5px);
        padding: 0.8rem 1rem;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Selectbox styling */
    .stSelectbox>div>div {
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
    
    /* Success/warning/info messages */
    .stAlert {
        border-radius: 15px;
        border: none;
        backdrop-filter: blur(5px);
    }
    
    /* Divider */
    hr {
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
        height: 2px;
        border: none;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #718096;
        font-size: 0.9rem;
        margin-top: 3rem;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

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
    
    # Animasi kecil
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <span style="font-size: 0.8rem; color: #888;">✨ Crafted with precision</span>
    </div>
    """, unsafe_allow_html=True)

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
st.markdown('<div class="footer">IVA — Where creativity meets artificial intelligence, guided by human wisdom.</div>', unsafe_allow_html=True)



