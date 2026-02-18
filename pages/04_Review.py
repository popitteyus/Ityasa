import streamlit as st
from utils.db import supabase, update_task_review

st.set_page_config(page_title="Review", page_icon="✅", layout="wide")

if 'selected_project' not in st.session_state:
    st.warning("Pilih proyek terlebih dahulu.")
    st.stop()

proyek = st.session_state['selected_project']
st.markdown(f"## ✅ Review Hasil: {proyek['nama_proyek']}")

tasks = supabase.table("tasks").select("*, divisi(*)").eq("project_id", proyek['id']).in_("status", ["selesai", "pending"]).execute().data

if not tasks:
    st.info("Tidak ada tugas yang perlu direview.")
else:
    for task in tasks:
        with st.expander(f"**{task['divisi']['nama_divisi']}** - {task['created_at'][:16]} - Status: {task['status']}", expanded=(task['status']=='selesai')):
            st.write("**Prompt:**", task['prompt'])
            if task['output']:
                st.write("**Output AI:**", task['output'])
            else:
                st.warning("Output belum ada.")
            
            with st.form(key=f"review_{task['id']}"):
                review_notes = st.text_area("Catatan Review", value=task.get('review_notes', ''))
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.form_submit_button("✅ Setujui"):
                        update_task_review(task['id'], "disetujui", review_notes)
                        st.success("Disetujui!")
                        st.rerun()
                with col2:
                    if st.form_submit_button("🔄 Minta Revisi"):
                        update_task_review(task['id'], "revisi", review_notes)
                        st.info("Revisi diminta.")
                        st.rerun()
                with col3:
                    if st.form_submit_button("❌ Tolak"):
                        update_task_review(task['id'], "ditolak", review_notes)
                        st.warning("Ditolak.")
                        st.rerun()
