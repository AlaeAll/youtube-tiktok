import streamlit as st
import subprocess
import tempfile
import os
import uuid
from moviepy.editor import VideoFileClip

st.set_page_config(page_title="YouTube to TikTok", page_icon="🎥")

st.markdown("# 🎥 YouTube to TikTok Generator")
st.markdown("**1min clip 9:16 prêt pour TikTok !**")

col1, col2 = st.columns([3, 1])
with col1:
    youtube_url = st.text_input("Lien YouTube:", placeholder="https://www.youtube.com/watch?v=...")
with col2:
    duration = st.number_input("Durée (sec):", min_value=15, max_value=180, value=60)

if st.button("🚀 Générer clip", type="primary"):
    if youtube_url:
        with st.spinner("⏳ Téléchargement et traitement en cours..."):
            try:
                tmp_input = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
                tmp_input.close()

                cmd = [
                    "yt-dlp",
                    "--no-playlist",
                    "-f", "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]",
                    "--merge-output-format", "mp4",
                    "-o", tmp_input.name,
                    "--force-overwrites",
                    youtube_url
                ]
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    st.error(f"Erreur yt-dlp: {result.stderr}")
                    st.stop()

                clip = VideoFileClip(tmp_input.name)
                dur = clip.duration
                start = 0 if dur < 120 else (dur / 2 - 30)
                end = min(dur, start + duration)
                sub = clip.subclip(start, end)

                # Recadrage TikTok 9:16
                target_ratio = 9 / 16
                current_ratio = sub.w / sub.h

                if current_ratio > target_ratio:
                    # Vidéo trop large → crop sur les côtés
                    new_w = int(sub.h * target_ratio)
                    x_center = sub.w / 2
                    sub = sub.crop(x_center=x_center, width=new_w)

                final = sub.resize((1080, 1920))

                tmp_out = f"/tmp/tiktok_{uuid.uuid4().hex[:8]}.mp4"
                final.write_videofile(
                    tmp_out,
                    codec="libx264",
                    audio_codec="aac",
                    fps=30,
                    preset="fast",
                    logger=None
                )

                clip.close()
                final.close()
                os.unlink(tmp_input.name)

                st.success("✅ Clip TikTok généré avec succès !")
                st.video(tmp_out)

                with open(tmp_out, "rb") as f:
                    st.download_button(
                        label="📥 Télécharger le clip TikTok",
                        data=f,
                        file_name="tiktok_clip.mp4",
                        mime="video/mp4"
                    )

            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")
    else:
        st.warning("⚠️ Veuillez entrer un lien YouTube.")

st.markdown("---")
st.markdown("*Perfect for BTC/XAUUSD trading analysis*")
