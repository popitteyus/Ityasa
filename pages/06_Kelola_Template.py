import streamlit as st
from utils.db import supabase, get_divisi

st.set_page_config(page_title="Template", page_icon="📚", layout="wide")

st.markdown("## 📚 Kelola Template Prompt")

divisi_list = get_divisi()
divisi_map = {d['id']: d['nama_divisi'] for d in divisi_list}

with st.form("template_baru"):
    divisi_id = st.selectbox("Divisi", options=list(divisi_map.keys()), format_func=lambda x: divisi_map[x])
    nama_template = st.text_input("Nama Template")
    template = st.text_area("Isi Template (gunakan {brief} sebagai placeholder)", height=150)
    if st.form_submit_button("💾 Simpan Template"):
        if nama_template and template:
            data = {"divisi_id": divisi_id, "nama_template": nama_template, "template": template}
            supabase.table("prompt_templates").insert(data).execute()
            st.success("Template disimpan!")
            st.rerun()
        else:
            st.warning("Semua field harus diisi.")

st.markdown("### Daftar Template")
templates = supabase.table("prompt_templates").select("*, divisi(*)").execute().data
if templates:
    for t in templates:
        with st.expander(f"{t['divisi']['nama_divisi']} - {t['nama_template']}"):
            st.code(t['template'])
            if st.button("🗑️ Hapus", key=t['id']):
                supabase.table("prompt_templates").delete().eq("id", t['id']).execute()
                st.rerun()
else:
    st.info("Belum ada template.")
