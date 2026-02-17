import streamlit as st
import gspread
import pandas as pd

st.set_page_config(page_title="ITYASA OS Dashboard", layout="wide")
st.title("📊 ITYASA OS – Project Tracker")

st.sidebar.success("Terhubung ke Google Sheets")

try:
    # Ambil informasi service account dari Streamlit Secrets
    # (sudah dalam bentuk dictionary karena format TOML)
    service_account_info = st.secrets["gcp_service_account"]
    
    # Gunakan gspread untuk otorisasi langsung dari dictionary
    gc = gspread.service_account_from_dict(service_account_info)
    
    # Buka spreadsheet berdasarkan nama
    sh = gc.open("IVA_Project_Tracker")
    
    # Ambil sheet pertama (index 0)
    worksheet = sh.get_worksheet(0)
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    
    st.subheader("Data dari Sheet 1")
    st.dataframe(df, use_container_width=True)
    
    st.subheader("Ringkasan")
    st.write(f"Total baris: {len(df)}")
    st.write(f"Total kolom: {len(df.columns)}")
    
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.info("Pastikan service account sudah diundang ke Google Sheet dan secrets sudah benar.")
