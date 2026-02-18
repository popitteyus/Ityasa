
import streamlit as st
from utils.db import insert_project
import time

st.set_page_config(page_title="Input Proyek", page_icon="📝", layout="wide")

st.markdown('<h1 style="font-size:2.5rem;">📝 Input Proyek Baru</h1>', unsafe_allow_html=True)

with st.form("form_proyek"):
    col1, col2 = st.columns(2)
    with col1:
        nama_proyek = st.text_input("Nama Proyek")
    with col2:
        nama_klien = st.text_input("Nama Klien")
    brief = st.text_area("Brief Klien", height=200)
    submitted = st.form_submit_button("🚀 Simpan Proyek", use_container_width=True)
    
    if submitted:
        if nama_proyek and nama_klien:
            with st.spinner("Menyimpan..."):
                result = insert_project(nama_proyek, nama_klien, brief)
                if result and result.data:
                    st.success("✅ Proyek berhasil disimpan!")
                    st.balloons()
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("❌ Gagal menyimpan.")
        else:
            st.warning("⚠️ Nama proyek dan klien harus diisi.")
