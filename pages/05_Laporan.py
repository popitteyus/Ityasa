import streamlit as st
from utils.db import get_tasks_by_project
from datetime import datetime

st.set_page_config(page_title="Laporan", page_icon="📄", layout="wide")
from utils.styles import get_css
st.markdown(get_css(), unsafe_allow_html=True)

if 'selected_project' not in st.session_state:
    st.warning("Pilih proyek terlebih dahulu.")
    st.stop()

proyek = st.session_state['selected_project']
st.markdown(f"## 📄 Laporan Proyek: {proyek['nama_proyek']}")

tasks = get_tasks_by_project(proyek['id'])
approved_tasks = [t for t in tasks if t['status'] == 'disetujui']

if not approved_tasks:
    st.info("Belum ada output yang disetujui.")
else:
    for task in approved_tasks:
        with st.container(border=True):
            st.markdown(f"### 🧠 {task['divisi']['nama_divisi']}")
            st.write(task['output'])
            if task['review_notes']:
                st.caption(f"*Catatan Founder: {task['review_notes']}*")
    
    if st.button("📥 Generate Laporan Markdown"):
        laporan = f"""# Laporan Proyek: {proyek['nama_proyek']}
**Klien:** {proyek['nama_klien']}  
**Tanggal:** {datetime.now().strftime('%d %B %Y')}

## Brief Awal
{proyek['brief']}

## Hasil Pengerjaan
"""
        for task in approved_tasks:
            laporan += f"""
### Divisi {task['divisi']['nama_divisi']}
**Output:** {task['output']}
"""
            if task['review_notes']:
                laporan += f"*Catatan Founder: {task['review_notes']}*\n"
        
        st.download_button(
            label="💾 Download Laporan",
            data=laporan,
            file_name=f"laporan_{proyek['nama_proyek'].replace(' ', '_')}.md",
            mime="text/markdown"
        )
