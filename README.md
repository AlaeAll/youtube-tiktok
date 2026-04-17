# 🎥 YouTube to TikTok Generator

## Déploiement sur Railway

### 1. Préparer votre repo GitHub
1. Créez un repo GitHub (public ou privé)
2. Uploadez ces fichiers :
   - `app.py`
   - `requirements.txt`
   - `nixpacks.toml`
   - `.streamlit/config.toml`

### 2. Déployer sur Railway
1. Allez sur [railway.app](https://railway.app) et connectez-vous avec GitHub
2. Cliquez **"New Project"** → **"Deploy from GitHub repo"**
3. Sélectionnez votre repo
4. Railway détecte automatiquement `nixpacks.toml` et installe ffmpeg + Python
5. Attendez le build (~3-5 min)
6. Cliquez sur **"Generate Domain"** pour obtenir votre URL publique

### C'est tout ! 🎉
Votre app sera accessible sur une URL du type :
`https://votre-app.up.railway.app`

## Notes
- Railway offre 500h/mois gratuitement (plan Hobby)
- Les vidéos générées sont temporaires (stockées en `/tmp`)
- yt-dlp se met à jour automatiquement si YouTube change son API
