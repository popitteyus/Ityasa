from supabase import create_client, Client
import os

# Inisialisasi Supabase (URL dan Key akan diambil dari environment variables)
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key) if url and key else None

# Fungsi untuk mengambil semua divisi
def get_divisi():
    if supabase:
        return supabase.table("divisi").select("*").execute().data
    return []

# Fungsi untuk mengambil semua proyek
def get_projects():
    if supabase:
        return supabase.table("projects").select("*").order("created_at", desc=True).execute().data
    return []

# Fungsi untuk menambah proyek baru
def insert_project(nama_proyek, nama_klien, brief):
    if supabase:
        data = {
            "nama_proyek": nama_proyek,
            "nama_klien": nama_klien,
            "brief": brief,
            "status": "brief"
        }
        return supabase.table("projects").insert(data).execute()
    return None

# Fungsi untuk mengambil tugas berdasarkan proyek
def get_tasks_by_project(project_id):
    if supabase:
        return supabase.table("tasks").select("*, divisi(*)").eq("project_id", project_id).order("created_at").execute().data
    return []

# Fungsi untuk menambah tugas
def insert_task(project_id, divisi_id, prompt):
    if supabase:
        data = {
            "project_id": project_id,
            "divisi_id": divisi_id,
            "prompt": prompt,
            "status": "pending"
        }
        return supabase.table("tasks").insert(data).execute()
    return None

# Fungsi untuk mengambil template prompt
def get_prompt_templates(divisi_id=None):
    if supabase:
        query = supabase.table("prompt_templates").select("*")
        if divisi_id:
            query = query.eq("divisi_id", divisi_id)
        return query.execute().data
    return []

# Fungsi untuk update output tugas (nanti dipanggil oleh AI)
def update_task_output(task_id, output):
    if supabase:
        return supabase.table("tasks").update({"output": output, "status": "selesai"}).eq("id", task_id).execute()
    return None

# Fungsi untuk update review
def update_task_review(task_id, status, notes):
    if supabase:
        return supabase.table("tasks").update({"status": status, "review_notes": notes}).eq("id", task_id).execute()
    return None
