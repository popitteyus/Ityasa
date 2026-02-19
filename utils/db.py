from supabase import create_client, Client
import os
import streamlit as st

# Inisialisasi Supabase (URL dan Key akan diambil dari environment variables)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# Variabel internal, jangan diekspor
_supabase = None
if url and key:
    try:
        _supabase: Client = create_client(url, key)
    except Exception as e:
        st.error(f"Gagal membuat klien Supabase: {e}")
        _supabase = None
else:
    st.error("URL atau KEY Supabase tidak ditemukan di Secrets. Pastikan sudah diisi di Streamlit Cloud.")

# Fungsi untuk mengambil semua divisi
def get_divisi():
    if _supabase:
        try:
            return _supabase.table("divisi").select("*").execute().data
        except Exception as e:
            st.error(f"Error get_divisi: {e}")
            return []
    return []

# Fungsi untuk mengambil semua proyek
def get_projects():
    if _supabase:
        try:
            return _supabase.table("projects").select("*").order("created_at", desc=True).execute().data
        except Exception as e:
            st.error(f"Error get_projects: {e}")
            return []
    return []

# Fungsi untuk menambah proyek baru
def insert_project(nama_proyek, nama_klien, brief):
    if not _supabase:
        st.error("Koneksi Supabase tidak tersedia")
        return None
    try:
        data = {
            "nama_proyek": nama_proyek,
            "nama_klien": nama_klien,
            "brief": brief,
            "status": "brief"
        }
        result = _supabase.table("projects").insert(data).execute()
        return result
    except Exception as e:
        st.error(f"Error insert_project: {e}")
        return None

# Fungsi untuk mengambil tugas berdasarkan proyek
def get_tasks_by_project(project_id):
    if _supabase:
        try:
            return _supabase.table("tasks").select("*, divisi(*)").eq("project_id", project_id).order("created_at").execute().data
        except Exception as e:
            st.error(f"Error get_tasks_by_project: {e}")
            return []
    return []

# Fungsi untuk menambah tugas
def insert_task(project_id, divisi_id, prompt):
    if _supabase:
        try:
            data = {
                "project_id": project_id,
                "divisi_id": divisi_id,
                "prompt": prompt,
                "status": "pending"
            }
            return _supabase.table("tasks").insert(data).execute()
        except Exception as e:
            st.error(f"Error insert_task: {e}")
            return None
    return None

# Fungsi untuk mengambil template prompt (tanpa join divisi)
def get_prompt_templates(divisi_id=None):
    if _supabase:
        try:
            query = _supabase.table("prompt_templates").select("*")
            if divisi_id:
                query = query.eq("divisi_id", divisi_id)
            return query.execute().data
        except Exception as e:
            st.error(f"Error get_prompt_templates: {e}")
            return []
    return []

# Fungsi untuk mengambil template prompt beserta nama divisi (join manual)
def get_prompt_templates_with_divisi():
    if not _supabase:
        return []
    try:
        templates = _supabase.table("prompt_templates").select("*").execute().data
        if not templates:
            return []
        # Ambil semua divisi untuk referensi
        divisi = get_divisi()
        divisi_map = {d['id']: d['nama_divisi'] for d in divisi}
        for t in templates:
            t['nama_divisi'] = divisi_map.get(t['divisi_id'], 'Unknown')
        return templates
    except Exception as e:
        st.error(f"Error get_prompt_templates_with_divisi: {e}")
        return []

# Fungsi untuk menambah template
def insert_template(divisi_id, nama_template, template):
    if _supabase:
        try:
            data = {
                "divisi_id": divisi_id,
                "nama_template": nama_template,
                "template": template
            }
            return _supabase.table("prompt_templates").insert(data).execute()
        except Exception as e:
            st.error(f"Error insert_template: {e}")
            return None
    return None

# Fungsi untuk menghapus template
def delete_template(template_id):
    if _supabase:
        try:
            return _supabase.table("prompt_templates").delete().eq("id", template_id).execute()
        except Exception as e:
            st.error(f"Error delete_template: {e}")
            return None
    return None

# Fungsi untuk update output tugas (nanti dipanggil oleh AI)
def update_task_output(task_id, output):
    if _supabase:
        try:
            return _supabase.table("tasks").update({"output": output, "status": "selesai"}).eq("id", task_id).execute()
        except Exception as e:
            st.error(f"Error update_task_output: {e}")
            return None
    return None

# Fungsi untuk update review
def update_task_review(task_id, status, notes):
    if _supabase:
        try:
            return _supabase.table("tasks").update({"status": status, "review_notes": notes}).eq("id", task_id).execute()
        except Exception as e:
            st.error(f"Error update_task_review: {e}")
            return None
    return None
