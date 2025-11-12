# Quick Start Guide - Get Your Site Live in 30 Minutes

Follow these steps to deploy your fully automated affiliate website.

---

## ⏱️ Timeline

| Step | Time | Status |
|------|------|--------|
| 1. Deploy to GitHub Pages | 10 min | 🚀 Start here |
| 2. Apply for Amazon PA-API | 5 min | 📝 Then wait 1-3 days |
| 3. Add PA-API Credentials | 2 min | 🔑 After approval |
| 4. Test Automation | 3 min | ✅ Final step |

**Total active time: 20 minutes**
**Total wait time: 1-3 days** (Amazon approval)

---

## Step 1: Deploy to GitHub Pages (10 minutes)

### Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `terralogic-tech` (or your choice)
3. Make it **Public**
4. Click **Create repository**

### Push Your Code

Open terminal in your website folder:

```bash
# Initialize git
git init
git add -A
git commit -m "Initial commit: TerraLogic Tech automation"
git branch -M main

# Connect to GitHub (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/terralogic-tech.git
git push -u origin main
```

### Enable GitHub Pages

1. Go to your repo on GitHub
2. **Settings** → **Pages** (left sidebar)
3. **Source**: Select `main` branch, `/ (root)` folder
4. Click **Save**
5. Wait 1-2 minutes

### Get Your URL

Your site is now live at:
```
https://YOUR-USERNAME.github.io/terralogic-tech/
```

**✅ Step 1 Complete!** Your site is live (with placeholder products).

---

## Step 2: Apply for Amazon PA-API (5 minutes + wait)

### Prerequisites

- Amazon Associates account (already have it ✓)
- Live website URL (just got it ✓)

### Apply

1. Go to https://affiliate-program.amazon.com/
2. Log in
3. Navigate to: **Tools** → **Product Advertising API**
4. Click **Request Access**
5. Fill out form:
   - **Website URL**: Your GitHub Pages URL
   - **Application Name**: TerraLogic Tech Automation
   - **Description**: "Automated product recommendations for home office equipment"
6. Submit

### Wait for Approval

- **Time**: 1-3 business days
- **Notification**: Via email
- **Next**: Come back when approved!

---

## Step 3: Add PA-API Credentials (2 minutes)

**Do this after PA-API approval**

### Get Your Credentials

1. Go back to Product Advertising API page
2. You'll see:
   - Access Key
   - Secret Key
   - Associate Tag

### Add to GitHub

1. Go to your GitHub repo
2. **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add three secrets:

| Name | Value |
|------|-------|
| `AMAZON_ACCESS_KEY` | Paste your Access Key |
| `AMAZON_SECRET_KEY` | Paste your Secret Key |
| `AMAZON_ASSOCIATE_TAG` | Paste your Associate Tag (e.g., yourname-20) |

**✅ Step 3 Complete!** Automation is now armed and ready.

---

## Step 4: Test Automation (3 minutes)

### Run Manually First

1. Go to your repo's **Actions** tab
2. Click "Update Products Automatically"
3. Click **Run workflow** → **Run workflow**
4. Wait 2-3 minutes
5. Check the run logs (should see "✅ Products updated")

### Verify Updates

1. Go to your live site
2. Click on any category (Chairs, Desks, etc.)
3. You should see real products with:
   - Actual product names
   - Amazon product images
   - Current prices
   - Working affiliate links

**✅ Step 4 Complete!** Your site is fully operational!

---

## What Happens Next?

### Automatically (No Work Required)

- **Every Monday at midnight**: GitHub Actions runs
- **Products update**: Finds new top-rated products
- **Prices refresh**: Updates to current Amazon prices
- **Site deploys**: Changes go live automatically

### Optional (As Desired)

- **Write blog posts**: Use `content/prompts.md` with ChatGPT/Claude
- **Customize descriptions**: Add to `content/product-descriptions.yaml`
- **Check analytics**: Monitor traffic and clicks
- **Watch commissions**: Check Amazon Associates dashboard

---

## Troubleshooting

### "Git command not found"

Install Git:
- Windows: https://git-scm.com/download/win
- Mac: `brew install git`
- Linux: `sudo apt install git`

### "Permission denied" when pushing

Create Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select `repo` scope
4. Use token as password when git asks

### Automation fails with "credentials not found"

- Double-check secrets are added in GitHub
- Names must be exact: `AMAZON_ACCESS_KEY` (not `AMAZON-ACCESS-KEY`)
- No extra spaces in values

### Products not showing

- Wait 2-3 minutes after automation runs
- Hard refresh your browser (Ctrl+Shift+R)
- Check GitHub Actions logs for errors

---

## Next Steps (Beyond Basics)

### Week 1
- ✅ Site live
- ✅ Automation working
- ✍️ Write first blog post
- 📊 Add Google Analytics

### Month 1
- ✍️ Write 2-3 buying guides
- 📱 Share on social media
- 🎨 Customize product descriptions
- 📈 Monitor first sales

### Ongoing
- ✍️ 1-2 blog posts per month
- 📊 Check analytics weekly
- 💰 Monitor Amazon Associates monthly
- 🔄 Site updates automatically!

---

## Cost Summary

| Item | Cost | When |
|------|------|------|
| GitHub Pages | $0 | Forever |
| GitHub Actions | $0 | Forever (under 2,000 min/month) |
| Amazon PA-API | $0 | While maintaining 1 sale/month |
| Domain (optional) | $10-15 | Per year |
| **Total** | **$0-15/year** | |

---

## Support Resources

### Documentation
- `README.md` - Complete overview
- `AUTOMATION-GUIDE.md` - How automation works
- `DEPLOYMENT-GUIDE.md` - Detailed deployment help
- `PA-API-SETUP.md` - Amazon API details
- `content/prompts.md` - Content creation help

### Quick Commands

```bash
# Check what changed
git status

# Push updates
git add -A
git commit -m "Your update description"
git push

# Test automation locally (optional)
python automation/product_finder.py
python automation/website_updater.py
```

---

## Checklist

Use this to track your progress:

- [ ] GitHub repository created
- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Live URL working
- [ ] Applied for Amazon PA-API
- [ ] Received PA-API approval email
- [ ] Added 3 secrets to GitHub
- [ ] Ran automation test
- [ ] Verified products showing
- [ ] Site fully operational!

---

## You're Done! 🎉

Your fully automated affiliate website is now:
- ✅ Live on the internet
- ✅ Finding products automatically
- ✅ Updating prices weekly
- ✅ Generating affiliate commissions
- ✅ Running itself with zero maintenance

**Time to start creating content and driving traffic!**

**Questions?** Check the full documentation files for detailed help.
