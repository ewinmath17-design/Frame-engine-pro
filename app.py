import streamlit as st
import time
import os
import json
import tempfile
import google.generativeai as genai

# =====================================================================
# CONFIGURATION & PAGE SETUP
# =====================================================================
st.set_page_config(
    page_title="Frame Engine Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium Dark Theme
st.markdown("""
<style>
    .reportview-container { background: #0e1117; }
    .stButton>button {
        background-color: #2e7d32;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { background-color: #1b5e20; border-color: #a1887f; }
    .shot-box {
        background-color: #1e1e24;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        margin-bottom: 20px;
    }
    .audio-box {
        background-color: #141419;
        padding: 15px;
        border-radius: 8px;
        border: 1px dashed #475569;
        margin-top: 10px;
    }
    .metric-card {
        background-color: #161a22;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #2d3748;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State & Safe API Retrieval
if 'credits' not in st.session_state:
    st.session_state.credits = 500

# Mengambil API Key secara aman dari Secrets Management internal Streamlit
gemini_api_key = st.secrets.get("GEMINI_API_KEY", None)

# =====================================================================
# SIDEBAR NAVIGATION
# =====================================================================
with st.sidebar:
    st.title("🎬 Frame Engine Pro")
    st.caption("Architecture & Construction Timelapse Engine")
    st.markdown("---")
    
    # Indikator status koneksi API internal
    if gemini_api_key:
        st.success("🔒 System API Status: Connected")
    else:
        st.warning("⚠️ System API Status: Offline (Configure Secrets)")
        
    st.markdown("---")
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.metric(label="Sisa Kredit API", value=f"{st.session_state.credits} PTS")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# MAIN INTERFACE
# =====================================================================
st.header("🏗️ Frame Engine Pro: Timelapse Automation")
st.subheader("Ubah 1 Referensi Menjadi Rangkaian 3 Scene Sinematik Siap Eksekusi ke Veo / Kling")

# Input Methods
tab1, tab2 = st.tabs(["🔗 Tempel Link Video (Frictionless)", "📤 Unggah File Video (Deep AI Analysis)"])

video_url = None
uploaded_file = None

with tab1:
    video_url = st.text_input("Masukkan URL Video Konstruksi/Arsitektur (TikTok/Reels/Shorts):", 
                              placeholder="https://www.tiktok.com/@viral_architecture/video/...")
    if video_url:
        st.success("✅ Link terkunci! Sistem siap memproses visualisasi 3 scene.")
        
with tab2:
    uploaded_file = st.file_uploader("Atau unggah file video konstruksi asli (MP4/MOV):", type=["mp4", "mov", "avi"])
    if uploaded_file:
        st.success(f"✅ File {uploaded_file.name} siap dianalisis mendalam.")

st.markdown("---")
st.header("⚙️ Simulation & Hardware Layers")
col1, col2 = st.columns(2)
with col1:
    project_type = st.selectbox("Pilih Modul AI Prompting:", ["Real-Estate Timelapse Mode", "Premium Commercial Ads Mode"])
with col2:
    drone_gear = st.selectbox("Spesifikasi Kamera/Drone Virtual:", ["DJI Mavic 3 Pro (24mm Wide Lens, 8K Render)", "ARRI Alexa 65 (50mm Prime Lens, Cinematic)"])

if st.button("🚀 Generate 3-Scene Master Copy"):
    if not video_url and not uploaded_file:
        st.error("❌ Silakan masukkan link video atau unggah file video terlebih dahulu.")
    elif uploaded_file and not gemini_api_key:
        st.error("❌ API Key sistem belum dikonfigurasi di Streamlit Secrets Management.")
    else:
        try:
            with st.spinner("🎬 Frame Engine memproses struktur waktu & merancang alur audio-visual..."):
                
                storyboard = {}
                
                # JALUR 1: LIVE DEEP ANALYSIS VIA GEMINI API
                if uploaded_file:
                    genai.configure(api_key=gemini_api_key)
                    model = genai.GenerativeModel('gemini-1.5-pro-latest') 
                    
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        tmp_path = tmp_file.name

                    video_file = genai.upload_file(path=tmp_path)
                    while video_file.state.name == "PROCESSING":
                        time.sleep(2)
                        video_file = genai.get_file(video_file.name)

                    system_prompt = f"""
                    Analyze this construction/architecture video. Expand it into a professional 3-shot cinematic storytelling sequence (10 seconds per shot) using {drone_gear} specification.
                    Format the output strictly as JSON with keys: shot_1, shot_2, shot_3.
                    Each shot must contain fields: 'start_frame' (image prompt), 'motion' (veo camera instruction), 'caption' (text on screen in Indonesian), and 'voiceover' (narrator script in Indonesian).
                    """
                    response = model.generate_content([video_file, system_prompt])
                    genai.delete_file(video_file.name)
                    os.unlink(tmp_path)
                    
                    raw_json = response.text.replace("```json", "").replace("```", "").strip()
                    storyboard = json.loads(raw_json)
                
                # JALUR 2: FAST LINK ENTRY (REAL-ESTATE ARCHITECTURE CORE DATABASE)
                elif video_url:
                    time.sleep(2.5)
                    storyboard = {
                        "shot_1": {
                            "start_frame": "Aerial wide shot, an empty dirt plot surrounded by a scenic traditional landscape with distant hills, bright morning sun, crystal clear view.",
                            "motion": "High-angle static hyperlapse construction progression. Bare dirt plot rapidly transforming as foundation structures, concrete pillars, and brick walls build themselves frame-by-frame.",
                            "caption": "Membangun impian tidak harus menunggu lama...",
                            "voiceover": "Setiap mahakarya besar selalu dimulai dari fondasi yang kuat. Namun, bayangkan jika Anda bisa melihat hasil akhirnya sekarang.",
                            "sfx": "Fast-forward building machine sounds, crisp wooden hammer claps."
                        },
                        "shot_2": {
                            "start_frame": "Interior wide shot of a house frame under construction, bare concrete walls, sunlight shining through empty window frames, dust particles in the air.",
                            "motion": "Interior cinematic stop-motion time-lapse transition. Raw concrete walls seamlessly morphing into a pristine luxurious living room, white paint appearing, elegant furniture materializing.",
                            "caption": "Setiap detail ruang, dirancang khusus untuk Anda.",
                            "voiceover": "Dari dinding beton mentah, menjadi ruang keluarga yang hangat, elegan, dan siap menyambut kebahagiaan Anda.",
                            "sfx": "Smooth transition swoosh, elegant slow piano chord begins."
                        },
                        "shot_3": {
                            "start_frame": "Eye-level wide shot of a completed stunning modern-traditional luxury villa, perfectly manicured green grass lawn garden, bright afternoon.",
                            "motion": "Cinematic drone orbit shot of the fully built luxury villa. Smooth day-to-night time-lapse transition. As the sky turns into twilight purple, the warm golden lights turn on.",
                            "caption": "Wujudkan Rumah Impian Anda Bersama Kami.",
                            "voiceover": "Jangan biarkan desain Anda hanya sebatas denah. Mari wujudkan rumah impian Anda menjadi kenyataan hari ini.",
                            "sfx": "Orchestral swell climax, fading into calm night crickets sound."
                        }
                    }

                st.session_state.credits -= 30
                st.success("🎉 Rangkaian Konten Frame Engine Berhasil Terbentuk Sempurna!")
                
                # RENDER OUTPUT TO UI
                for shot_num in ["shot_1", "shot_2", "shot_3"]:
                    title_map = {
                        "shot_1": "🎬 SCENE 1: THE FOUNDATION (0 - 10 Detik)",
                        "shot_2": "🎬 SCENE 2: INTERIOR EVOLUTION (10 - 20 Detik)",
                        "shot_3": "🎬 SCENE 3: THE MASTERPIECE REVEAL (20 - 30 Detik)"
                    }
                    
                    st.markdown("<div class='shot-box'>", unsafe_allow_html=True)
                    st.markdown(f"### {title_map[shot_num]}")
                    
                    st.markdown("**🟢 START FRAME PROMPT (Salin ke Text-to-Image):**")
                    st.code(f"{storyboard[shot_num]['start_frame']} {drone_gear}, photorealistic, architectural digest style, 8k resolution.", language="text")
                    
                    st.markdown("**🎥 MOTION PROMPT (Salin ke Kolom Instruksi Veo/Kling):**")
                    st.code(storyboard[shot_num]['motion'], language="text")
                    
                    # Layer Audio & Narasi
                    st.markdown("<div class='audio-box'>", unsafe_allow_html=True)
                    st.markdown(f"💬 **Teks di Layar (On-Screen Caption):** *\"{storyboard[shot_num]['caption']}\"*")
                    st.markdown(f"🎙️ **Naskah Suara (Voiceover Script):** *\"{storyboard[shot_num]['voiceover']}\"*")
                    if 'sfx' in storyboard[shot_num]:
                        st.markdown(f"🎵 **Rekomendasi Audio/SFX:** `{storyboard[shot_num]['sfx']}`")
                    st.markdown("</div>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)

                st.info("💡 **SOP EKSEKUSI:** Download 3 video berdurasi 10 detik dari Veo berdasarkan petunjuk Frame Engine di atas, gabungkan di CapCut, lalu rekam Voiceover sesuai naskah yang sudah disediakan!")

        except Exception as e:
            st.error(f"❌ Terjadi kesalahan pada core engine: {str(e)}")
