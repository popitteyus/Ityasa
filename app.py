import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

st.set_page_config(page_title="ITYASA OS Dashboard", layout="wide")
st.title("📊 ITYASA OS – Project Tracker")

# Info sidebar
st.sidebar.success("Terhubung ke Google Sheets")

# Menggunakan credentials dari Streamlit secrets
scope = ["https://www.googleapis.com/auth/spreadsheets"]

# Baca credentials dari secrets
try:
    creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    client = gspread.authorize(creds)

    # Buka spreadsheet
    spreadsheet = client.open("IVA_Project_Tracker")

    # Pilih sheet (misal sheet pertama)
    sheet = spreadsheet.get_worksheet(0)  # index 0 = sheet pertama
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    st.subheader("Data dari Sheet 1")
    st.dataframe(df, use_container_width=True)

    # Tampilkan statistik sederhana
    st.subheader("Ringkasan")
    st.write(f"Total baris: {len(df)}")
    st.write(f"Total kolom: {len(df.columns)}")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.info("Pastikan service account sudah dishare ke Google Sheet dan secrets sudah diatur dengan benar.")


