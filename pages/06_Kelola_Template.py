import streamlit as st
from utils.db import get_divisi, get_prompt_templates_with_divisi, insert_template, delete_template

st.set_page_config(page_title="Template", page_icon="📚", layout="wide")

st.markdown("## 📚 Kelola Template Prompt")

# Ambil daftar divisi
divisi_list = get_divisi()
if not divisi_list:
    st.error("Tidak dapat mengambil data divisi. Periksa koneksi database.")
    st.stop()

divisi_map = {d['id']: d['nama_divisi'] for d in divisi_list}

# Form tambah template
with st.form("template_baru"):
    divisi_id = st.selectbox("Divisi", options=list(divisi_map.keys()), format_func=lambda x: divisi_map[x])
    nama_template = st.text_input("Nama Template")
    template = st.text_area("Isi Template (gunakan {brief} sebagai placeholder)", height=150)
    submitted = st.form_submit_button("💾 Simpan Template")
    
    if submitted:
        if nama_template and template:
            with st.spinner("Menyimpan..."):
                result = insert_template(divisi_id, nama_template, template)
                if result and result.data:
                    st.success("Template disimpan!")
                    st.rerun()
                else:
                    st.error("Gagal menyimpan template. Lihat log untuk detail.")
        else:
            st.warning("Semua field harus diisi.")

# Tampilkan template yang ada
st.markdown("### Daftar Template")
templates = get_prompt_templates_with_divisi()
if templates:
    for t in templates:
        with st.expander(f"{t['nama_divisi']} - {t['nama_template']}"):
            st.code(t['template'])
            if st.button("🗑️ Hapus", key=t['id']):
                with st.spinner("Menghapus..."):
                    result = delete_template(t['id'])
                    if result and result.data:
                        st.success("Template dihapus!")
                        st.rerun()
                    else:
                        st.error("Gagal menghapus template.")
else:
    st.info("Belum ada template.")
