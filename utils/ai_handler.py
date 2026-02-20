# utils/ai_handler.py
import google.generativeai as genai
import os
import streamlit as st
from utils.gem_configs import GEMS_CONFIG

# Ambil API key dari secrets
api_key = os.environ.get("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("GEMINI_API_KEY tidak ditemukan. Tambahkan di Secrets Streamlit.")

def panggil_gem(divisi_nama, prompt, brief=""):
    """
    Memanggil Gemini sesuai divisi dengan konfigurasi yang sudah ditentukan.
    """
    if not api_key:
        return "Error: API key tidak tersedia"
    
    if divisi_nama not in GEMS_CONFIG:
        return f"Error: Divisi '{divisi_nama}' tidak dikenali."
    
    config = GEMS_CONFIG[divisi_nama]
    
    try:
        model = genai.GenerativeModel(
            model_name=config["model"],
            generation_config={"temperature": config["temperature"]}
        )
        
        full_prompt = f"""{config['system_prompt']}

Berdasarkan brief proyek berikut:
{brief}

Tugas spesifik Anda:
{prompt}

Berikan output yang profesional, siap pakai, dalam bahasa Indonesia.
"""
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error saat memanggil AI: {str(e)}"
