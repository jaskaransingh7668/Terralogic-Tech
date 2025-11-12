# GitHub Pages Deployment Guide

Complete guide to deploying your TerraLogic Tech site to GitHub Pages (free hosting).

---

## Why GitHub Pages?

✅ **Completely free** hosting
✅ **Automatic deployment** from GitHub
✅ **Fast CDN** (content delivery network)
✅ **Custom domain** support (optional)
✅ **HTTPS** included
✅ **No server management** needed

---

## Prerequisites

- GitHub account (free)
- Git installed on your computer
- Your TerraLogic Tech website files

---

## Step-by-Step Deployment

### Step 1: Create GitHub Repository

1. Go to https://github.com/
2. Log in to your account
3. Click the **+** icon (top right) → **New repository**
4. Fill in:

| Field | Value |
|-------|-------|
| **Repository name** | `terralogic-tech` (or your preferred name) |
| **Description** | "Home office affiliate product recommendations" |
| **Visibility** | Public (required for free GitHub Pages) |
| **Initialize** | ❌ Do NOT check any boxes |

5. Click **Create repository**

### Step 2: Initialize Git Locally

Open terminal/command prompt in your website folder:

```bash
# Navigate to your website folder
cd "/mnt/c/Users/jaska/OneDrive/Desktop/TerraLogic Tech Website"

# Initialize git repository
git init

# Add all files
git add -A

# Create first commit
git commit -m "Initial commit: TerraLogic Tech with automation"

# Set main branch
git branch -M main
```

### Step 3: Connect to GitHub

Replace `yourusername` with your actual GitHub username:

```bash
# Add remote repository
git remote add origin https://github.com/yourusername/terralogic-tech.git

# Push to GitHub
git push -u origin main
```

**If prompted for credentials:**
- Use your GitHub username
- For password, use a [Personal Access Token](https://github.com/settings/tokens)

### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll to **Pages** section (left sidebar)
4. Under **Source**:
   - Branch: Select `main`
   - Folder: Select `/ (root)`
5. Click **Save**

**Wait 1-2 minutes** for deployment!

### Step 5: Get Your Live URL

1. Refresh the Pages settings page
2. You'll see:
   ```
   Your site is live at https://yourusername.github.io/terralogic-tech/
   ```
3. Click the URL to visit your live site!

---

## Updating Your Site

### After Making Changes

Every time you update files locally:

```bash
# Check what changed
git status

# Add changes
git add -A

# Commit with message
git commit -m "Updated product descriptions"

# Push to GitHub
git push

# Site auto-updates in 1-2 minutes!
```

### Automated Updates

**Good news:** GitHub Actions handles this for you!

When automation runs:
1. Products are found
2. HTML is updated
3. Changes are committed automatically
4. GitHub Pages deploys automatically

**You don't need to manually push!**

---

## Custom Domain (Optional)

Want `terralogictech.com` instead of `yourusername.github.io`?

### Buy a Domain

Popular registrars:
- **Namecheap** (~$10/year)
- **Google Domains** (~$12/year)
- **Cloudflare** (~$10/year)

### Configure DNS

In your domain registrar:

**Add these DNS records:**

```
Type    Name    Value
A       @       185.199.108.153
A       @       185.199.109.153
A       @       185.199.110.153
A       @       185.199.111.153
CNAME   www     yourusername.github.io
```

### Set Custom Domain in GitHub

1. Repository → **Settings** → **Pages**
2. Under **Custom domain**, enter: `terralogictech.com`
3. Check **Enforce HTTPS** (after DNS propagates)
4. Wait 24-48 hours for DNS

---

## Fixing Path Issues

### If Your Site Looks Broken

**Problem:** CSS/JS not loading because of path issues

**Solution 1: Repository Name**

If your repo isn't named `terralogic-tech`, update paths:

In all HTML files, change:
```html
<link rel="stylesheet" href="css/styles.css">
```
To:
```html
<link rel="stylesheet" href="/your-repo-name/css/styles.css">
```

**Solution 2: Use Root Domain (Easier)**

Rename your repository to: `yourusername.github.io`

Then your URL becomes: `https://yourusername.github.io/`
(No subpath, simpler!)

---

## Troubleshooting

### Site Not Showing

**Check:**
1. Is repository public?
2. Is Pages enabled in Settings?
3. Did you push to `main` branch?
4. Wait 2-3 minutes and hard refresh (Ctrl+Shift+R)

**Check build status:**
- Repository → **Actions** tab
- Look for green checkmarks

### 404 Error

**Causes:**
- Wrong branch selected (should be `main`)
- index.html not in root folder
- Repository not public

### CSS Not Loading

**Check paths:**
- All CSS/JS paths should be relative or absolute
- Check browser console (F12) for errors
- If using subpath, update paths in HTML

### GitHub Actions Not Running

1. **Actions** tab → **Workflows**
2. Check if Actions are enabled
3. Look for errors in workflow runs
4. Verify secrets are added (Settings → Secrets)

---

## Directory Structure

Your deployed site structure:

```
https://yourusername.github.io/terralogic-tech/
├── index.html                          (Homepage)
├── about.html                          (About page)
├── contact.html                        (Contact)
├── privacy.html                        (Privacy policy)
├── affiliate-disclosure.html           (Disclosure)
├── css/
│   └── styles.css                      (Styles)
├── js/
│   └── main.js                         (JavaScript)
├── categories/
│   ├── chairs.html                     (Chairs category)
│   ├── desks.html                      (Desks category)
│   ├── monitors.html                   (Monitors category)
│   ├── lighting.html                   (Lighting category)
│   └── audio-video.html                (Audio-Video category)
└── colored-logo.png                    (Logo)
```

---

## GitHub Actions Secrets

After deployment, add Amazon credentials:

1. Repository → **Settings**
2. **Secrets and variables** → **Actions**
3. **New repository secret**
4. Add three secrets:

```
AMAZON_ACCESS_KEY       → Your PA-API access key
AMAZON_SECRET_KEY       → Your PA-API secret key
AMAZON_ASSOCIATE_TAG    → Your affiliate tag (yourname-20)
```

These allow automation to work!

---

## Monitoring Your Site

### Check Automation

- **Actions** tab → See workflow runs
- Green checkmark = success
- Red X = error (click to see logs)

### Site Analytics (Optional)

Add Google Analytics:

1. Create GA4 property
2. Get tracking code
3. Add to all HTML pages (before `</head>`)

### Monitor Affiliate Performance

- Amazon Associates dashboard
- Track clicks and sales
- See which products convert

---

## Development Workflow

### Recommended Process

```
Local Development
    ↓
Test Locally (open index.html)
    ↓
Commit Changes
    ↓
Push to GitHub
    ↓
GitHub Pages Auto-Deploys (1-2 min)
    ↓
Live Site Updated!
```

### Testing Before Push

```bash
# 1. Make changes locally
# 2. Open index.html in browser to preview
# 3. If looks good:
git add -A
git commit -m "Description of changes"
git push
```

---

## Cost Breakdown

| Service | Cost |
|---------|------|
| GitHub Pages | **FREE** |
| GitHub Actions | **FREE** (2,000 min/month) |
| Amazon PA-API | **FREE** (must maintain sales) |
| Domain (optional) | $10-15/year |
| **Total (without domain)** | **$0.00** |

---

## Next Steps After Deployment

1. ✅ **Site is live** at your GitHub Pages URL
2. 📝 **Apply for Amazon PA-API** using your live URL
3. 🔑 **Add PA-API secrets** to GitHub
4. 🧪 **Test automation** (Actions → Run workflow)
5. 📊 **Add analytics** (optional)
6. 🌐 **Get custom domain** (optional)
7. ✍️ **Create content** using AI prompts

---

## Quick Reference Commands

```bash
# Check status
git status

# Add all changes
git add -A

# Commit
git commit -m "Your message"

# Push to live site
git push

# Pull latest (if editing on GitHub)
git pull

# View commit history
git log --oneline
```

---

## Getting Help

### Deployment Issues

- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

### Common Fixes

```bash
# Reset to clean state
git clean -fd
git reset --hard

# Fix remote URL
git remote set-url origin https://github.com/yourusername/terralogic-tech.git

# Force push (use carefully!)
git push -f origin main
```

---

## Checklist

- [ ] GitHub account created
- [ ] Repository created
- [ ] Git initialized locally
- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Live URL works
- [ ] All pages load correctly
- [ ] CSS/JS working
- [ ] Images loading
- [ ] Links working
- [ ] Amazon secrets added
- [ ] Automation tested
- [ ] Custom domain configured (optional)

---

**Your site is now live and automatically managed by GitHub! 🚀**

Visit your URL anytime to see it in action.
