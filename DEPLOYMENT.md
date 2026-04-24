# 🚀 Deployment Guide - AI Film Studio

## 📋 Overview

This guide covers deploying both the frontend and backend of AI Film Studio.

- **Frontend**: GitHub Pages (Static Next.js Export)
- **Backend**: Multiple options (Render, Railway, Vercel, etc.)

---

## 🎨 Frontend Deployment (GitHub Pages)

### Automatic Deployment

1. **Enable GitHub Pages**:
   - Go to your repo: `https://github.com/AI-Cloud-Tech-Inc/AI-Film-Studio`
   - Click **Settings** → **Pages**
   - Under "Source", select **GitHub Actions**

2. **Push to Main Branch**:
   ```bash
   git add .
   git commit -m "Add GitHub Pages deployment"
   git push origin main
   ```

3. **View Your Site**:
   - After ~2-3 minutes, visit: `https://ai-cloud-tech-inc.github.io/AI-Film-Studio/`
   - Check deployment status: **Actions** tab in GitHub

### Manual Build

```bash
cd frontend
npm run build
# Output will be in frontend/out/
```

---

## 🔧 Backend Deployment

### Option 1: Render.com (Recommended - Free Tier Available)

1. **Create Account**: Go to [render.com](https://render.com)

2. **New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Select `AI-Film-Studio`

3. **Configure**:
   ```
   Name: ai-film-studio-backend
   Region: Choose closest to you
   Branch: main
   Root Directory: backend
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

4. **Environment Variables** (Add in Render dashboard):
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///./ai_film_studio.db
   OPENAI_API_KEY=sk-...
   ANTHROPIC_API_KEY=sk-ant-...
   REPLICATE_API_KEY=r8_...
   ELEVENLABS_API_KEY=...
   ENVIRONMENT=production
   ```

5. **Deploy**: Click "Create Web Service"

6. **Get URL**: Your backend will be at `https://ai-film-studio-backend.onrender.com`

### Option 2: Railway.app

1. **Create Account**: [railway.app](https://railway.app)

2. **New Project**:
   - Click "New Project" → "Deploy from GitHub repo"
   - Select `AI-Film-Studio`

3. **Configure**:
   - Root Directory: `backend`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables** (same as Render)

5. **Deploy**: Automatic on push to main

### Option 3: Vercel (Serverless)

**Note**: Requires converting FastAPI to serverless functions

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Deploy:
   ```bash
   cd backend
   vercel
   ```

3. Follow prompts to configure

---

## 🔗 Connecting Frontend to Backend

After deploying backend, update frontend API URL:

1. **Edit**: `frontend/app/page.tsx` and `frontend/app/create/page.tsx`

2. **Replace**:
   ```typescript
   // Change from:
   fetch('http://localhost:8000/api/v1/autonomous/agent-status')
   
   // To:
   fetch('https://your-backend-url.onrender.com/api/v1/autonomous/agent-status')
   ```

3. **Or use Environment Variable** (Recommended):
   
   Create `frontend/.env.production`:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com
   ```
   
   Update code to use:
   ```typescript
   fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/v1/autonomous/agent-status`)
   ```

---

## 🛡️ Security & Configuration

### Backend (.env for production)

```bash
SECRET_KEY=use-strong-random-key-here
DATABASE_URL=postgresql://user:pass@host:5432/dbname  # For production DB
ENVIRONMENT=production
CORS_ORIGINS=https://ai-cloud-tech-inc.github.io

# API Keys (use secrets management in production)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
REPLICATE_API_KEY=r8_...
ELEVENLABS_API_KEY=...
```

### Frontend (Update CORS if needed)

In `backend/main.py`, update CORS origins:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001", 
        "https://ai-cloud-tech-inc.github.io"  # Add your GitHub Pages URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📊 Monitoring & Logs

### Frontend (GitHub Pages)
- Check build status: **Actions** tab
- View logs: Click on workflow run

### Backend (Render)
- Dashboard: `https://dashboard.render.com`
- Logs: Click your service → "Logs" tab
- Metrics: Built-in monitoring

### Backend (Railway)
- Dashboard: `https://railway.app/dashboard`
- Logs: Real-time in dashboard
- Metrics: Resource usage graphs

---

## 🔄 CI/CD Pipeline

The GitHub Action automatically:
1. ✅ Builds frontend on every push to main
2. ✅ Runs tests (if configured)
3. ✅ Deploys to GitHub Pages
4. ✅ Notifies on success/failure

Backend deploys automatically when connected to Render/Railway.

---

## 🆘 Troubleshooting

### Frontend Not Loading
- Check GitHub Actions logs
- Verify `basePath` in `next.config.js` matches repo name
- Ensure GitHub Pages is enabled

### Backend API Not Responding
- Check backend service logs
- Verify environment variables are set
- Test endpoints with: `https://your-backend.onrender.com/docs`

### CORS Errors
- Add frontend URL to CORS origins in backend
- Rebuild and redeploy backend

### Build Failures
- Check Node.js version (should be 22.x)
- Clear npm cache: `npm cache clean --force`
- Delete `node_modules` and reinstall

---

## 📚 Additional Resources

- **Next.js Deployment**: https://nextjs.org/docs/deployment
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **GitHub Pages**: https://docs.github.com/pages

---

## 🎬 Production Checklist

- [ ] Environment variables configured
- [ ] API keys secured (use secrets management)
- [ ] CORS origins updated
- [ ] Database configured (not SQLite for production)
- [ ] Error tracking setup (Sentry, etc.)
- [ ] Monitoring enabled
- [ ] SSL/HTTPS enabled (automatic on Render/Railway)
- [ ] Rate limiting configured
- [ ] Backup strategy in place

---

**Your URLs After Deployment**:
- 🎨 Frontend: `https://ai-cloud-tech-inc.github.io/AI-Film-Studio/`
- 🔧 Backend: `https://your-backend-name.onrender.com`
- 📖 API Docs: `https://your-backend-name.onrender.com/docs`
