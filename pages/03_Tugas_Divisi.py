import streamlit as st
from utils.db import get_divisi, get_tasks_by_project, insert_task, get_prompt_templates

st.set_page_config(page_title="Tugas Divisi", page_icon="⚙️", layout="wide")

if 'selected_project' not in st.session_state:
    st.warning("⚠️ Belum ada proyek yang dipilih.")
    if st.button("📋 Ke Daftar Proyek"):
        st.switch_page("pages/02_Daftar_Proyek.py")
    st.stop()

proyek = st.session_state['selected_project']

st.markdown(f'<h1 style="font-size:2.5rem;">⚙️ Tugas Divisi</h1>', unsafe_allow_html=True)
st.markdown(f"### {proyek['nama_proyek']}  \n**Klien:** {proyek['nama_klien']}")
with st.expander("Lihat Brief"):
    st.write(proyek['brief'])

tasks = get_tasks_by_project(proyek['id'])

st.markdown("### 📌 Riwayat Tugas")
if tasks:
    for task in tasks:
        with st.chat_message(name="ai"):
            st.markdown(f"**Divisi {task['divisi']['nama_divisi']}**")
            st.caption(f"Status: {task['status']} | {task['created_at'][:16]}")
            st.write(f"**Prompt:** {task['prompt']}")
            if task['output']:
                st.write(f"**Output:** {task['output']}")
            if task['review_notes']:
                st.info(f"📝 Review: {task['review_notes']}")
else:
    st.info("Belum ada tugas.")

st.markdown("### ➕ Tugaskan ke Divisi AI")
with st.form("tugas_baru"):
    divisi_list = get_divisi()
    divisi_options = {d['nama_divisi']: d['id'] for d in divisi_list}
    selected_divisi = st.selectbox("Pilih Divisi", options=list(divisi_options.keys()))
    divisi_id = divisi_options[selected_divisi]
    
    templates = get_prompt_templates(divisi_id)
    template_options = {t['nama_template']: t['template'] for t in templates}
    selected_template = st.selectbox("Gunakan Template", options=[""] + list(template_options.keys()))
    
    prompt = st.text_area("Prompt", value=template_options.get(selected_template, ""), height=150)
    
    if st.form_submit_button("🚀 Kirim Tugas", use_container_width=True):
        if prompt.strip():
            with st.spinner("Mengirim..."):
                result = insert_task(proyek['id'], divisi_id, prompt)
                if result and result.data:
                    st.success("✅ Tugas berhasil dikirim!")
                    st.rerun()
                else:
                    st.error("❌ Gagal mengirim.")
        else:
            st.warning("Prompt tidak boleh kosong.")
