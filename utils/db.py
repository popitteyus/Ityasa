from supabase import create_client, Client
import os
import streamlit as st

# Inisialisasi Supabase (URL dan Key akan diambil dari environment variables)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = None
if url and key:
    try:
        supabase: Client = create_client(url, key)
        print("Supabase client created successfully")
    except Exception as e:
        st.error(f"Gagal membuat klien Supabase: {e}")
        supabase = None
else:
    st.error("URL atau KEY Supabase tidak ditemukan di Secrets")

# Fungsi untuk mengambil semua divisi
def get_divisi():
    if supabase:
        try:
            return supabase.table("divisi").select("*").execute().data
        except Exception as e:
            st.error(f"Error get_divisi: {e}")
            return []
    return []

# Fungsi untuk mengambil semua proyek
def get_projects():
    if supabase:
        try:
            return supabase.table("projects").select("*").order("created_at", desc=True).execute().data
        except Exception as e:
            st.error(f"Error get_projects: {e}")
            return []
    return []

# Fungsi untuk menambah proyek baru
def insert_project(nama_proyek, nama_klien, brief):
    if not supabase:
        st.error("Koneksi Supabase tidak tersedia")
        return None
    try:
        data = {
            "nama_proyek": nama_proyek,
            "nama_klien": nama_klien,
            "brief": brief,
            "status": "brief"
        }
        result = supabase.table("projects").insert(data).execute()
        return result
    except Exception as e:
        st.error(f"Error insert_project: {e}")
        return None

# Fungsi untuk mengambil tugas berdasarkan proyek
def get_tasks_by_project(project_id):
    if supabase:
        try:
            return supabase.table("tasks").select("*, divisi(*)").eq("project_id", project_id).order("created_at").execute().data
        except Exception as e:
            st.error(f"Error get_tasks_by_project: {e}")
            return []
    return []

# Fungsi untuk menambah tugas
def insert_task(project_id, divisi_id, prompt):
    if supabase:
        try:
            data = {
                "project_id": project_id,
                "divisi_id": divisi_id,
                "prompt": prompt,
                "status": "pending"
            }
            return supabase.table("tasks").insert(data).execute()
        except Exception as e:
            st.error(f"Error insert_task: {e}")
            return None
    return None

# Fungsi untuk mengambil template prompt
def get_prompt_templates(divisi_id=None):
    if supabase:
        try:
            query = supabase.table("prompt_templates").select("*")
            if divisi_id:
                query = query.eq("divisi_id", divisi_id)
            return query.execute().data
        except Exception as e:
            st.error(f"Error get_prompt_templates: {e}")
            return []
    return []

# Fungsi untuk update output tugas (nanti dipanggil oleh AI)
def update_task_output(task_id, output):
    if supabase:
        try:
            return supabase.table("tasks").update({"output": output, "status": "selesai"}).eq("id", task_id).execute()
        except Exception as e:
            st.error(f"Error update_task_output: {e}")
            return None
    return None

# Fungsi untuk update review
def update_task_review(task_id, status, notes):
    if supabase:
        try:
            return supabase.table("tasks").update({"status": status, "review_notes": notes}).eq("id", task_id).execute()
        except Exception as e:
            st.error(f"Error update_task_review: {e}")
            return None
    return None
