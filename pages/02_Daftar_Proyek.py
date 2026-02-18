import streamlit as st
from utils.db import get_projects

st.set_page_config(page_title="Daftar Proyek", page_icon="📋", layout="wide")

st.markdown('<h1 style="font-size:2.5rem;">📋 Daftar Proyek</h1>', unsafe_allow_html=True)

projects = get_projects()

if projects:
    for proyek in projects:
        with st.container(border=True):
            cols = st.columns([3, 1, 1])
            with cols[0]:
                st.subheader(proyek['nama_proyek'])
                st.write(f"**Klien:** {proyek['nama_klien']}")
                st.caption(proyek['brief'][:100] + "..." if len(proyek['brief'])>100 else proyek['brief'])
            with cols[1]:
                st.metric("Status", proyek['status'].capitalize())
            with cols[2]:
                if st.button("🔍 Kelola", key=proyek['id']):
                    st.session_state['selected_project'] = proyek
                    st.switch_page("pages/03_Tugas_Divisi.py")
else:
    st.info("Belum ada proyek.")
