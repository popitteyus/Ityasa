def get_css():
    return """
    <style>
        /* Import font Poppins dari Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        /* Terapkan font ke seluruh elemen */
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Latar belakang gradien halus */
        .stApp {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        /* Judul utama dengan gradasi warna ungu-biru */
        .main-header {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        
        /* Container/kotak dengan efek kaca (glassmorphism) */
        div.stContainer {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 1.5rem;
            border: 1px solid rgba(255,255,255,0.3);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        /* Efek hover pada container */
        div.stContainer:hover {
            transform: translateY(-5px);
        }
        
        /* Tombol dengan gradasi */
        .stButton>button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 30px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        /* Efek hover tombol */
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }
        
        /* Kartu metrik (angka statistik) */
        .stMetric {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 1.2rem;
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        /* Gaya untuk elemen chat */
        .stChatMessage {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        /* Header dari expander */
        .streamlit-expanderHeader {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(5px);
            border-radius: 15px;
        }
        
        /* Tab navigasi */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background: rgba(255,255,255,0.3);
            backdrop-filter: blur(5px);
            padding: 0.3rem;
            border-radius: 40px;
        }
        
        .stTabs [data-baseweb="tab"] {
            border-radius: 30px;
            padding: 0.3rem 1rem;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white !important;
        }
        
        /* Input teks dan text area */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            border-radius: 15px;
            border: 1px solid rgba(102, 126, 234, 0.3);
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(5px);
        }
        
        /* Garis pemisah gradien */
        hr {
            background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent);
            height: 2px;
            border: none;
        }
    </style>
    """
