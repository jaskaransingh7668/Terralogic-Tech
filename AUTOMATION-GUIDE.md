# TerraLogic Tech - Automation Guide

Complete guide to the fully automated affiliate website system.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Setup Instructions](#setup-instructions)
4. [Configuration](#configuration)
5. [Running Manually](#running-manually)
6. [Troubleshooting](#troubleshooting)
7. [Customization](#customization)

---

## Overview

Your TerraLogic Tech website now has **fully automated product management**:

### What's Automated ✅
- Finding top-rated products on Amazon
- Fetching product data (names, prices, images, ratings)
- Generating your affiliate links
- Updating HTML files with products
- Deploying changes to live site
- Running on a schedule (every Monday)

### What's Manual ✍️
- Writing custom product descriptions (optional)
- Creating blog posts with AI help
- Approving which products to show

---

## How It Works

### Architecture

```
┌─────────────────────────────────────────┐
│  GitHub Actions (Runs Every Monday)    │
└──────────────┬──────────────────────────┘
               │
               ▼
      ┌────────────────────┐
      │ product_finder.py  │  ← Finds products via Amazon PA-API
      └────────┬───────────┘
               │
               ▼
      ┌────────────────────┐
      │  products.json     │  ← Saves product data
      └────────┬───────────┘
               │
               ▼
      ┌────────────────────┐
      │ website_updater.py │  ← Updates HTML files
      └────────┬───────────┘
               │
               ▼
      ┌────────────────────┐
      │   categories/*.html│  ← Updated pages
      └────────┬───────────┘
               │
               ▼
      ┌────────────────────┐
      │  GitHub Pages      │  ← Live website auto-updates
      └────────────────────┘
```

### The Process

1. **Every Monday at midnight**:
   - GitHub Actions runs automatically
   - Connects to Amazon PA-API with your credentials
   - Searches for products in each category
   - Filters by rating (4.0+) and reviews (100+)
   - Finds 6 best products per category

2. **Product data is fetched**:
   - Product name
   - Current price
   - Product image
   - Customer rating & review count
   - Key features
   - Your affiliate link (with your tag)

3. **Website is updated**:
   - HTML files are modified with new products
   - Product cards are generated automatically
   - Prices are refreshed
   - Changes are committed to GitHub

4. **Site goes live**:
   - GitHub Pages automatically deploys
   - Your visitors see updated products
   - No manual work needed!

---

## Setup Instructions

### Prerequisites

✅ GitHub account (free)
✅ Amazon Associates account (approved)
✅ Amazon PA-API credentials (approved)

### Step 1: Add Amazon Credentials to GitHub

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add three secrets:

| Name | Value |
|------|-------|
| `AMAZON_ACCESS_KEY` | Your PA-API Access Key |
| `AMAZON_SECRET_KEY` | Your PA-API Secret Key |
| `AMAZON_ASSOCIATE_TAG` | Your affiliate tag (e.g., yourname-20) |

### Step 2: Enable GitHub Actions

1. Go to **Actions** tab in your repository
2. Enable workflows if prompted
3. Find "Update Products Automatically"
4. Click **Enable workflow**

### Step 3: Test the Automation

**Option A: Manual Test**
1. Go to **Actions** tab
2. Click "Update Products Automatically"
3. Click **Run workflow** → **Run workflow**
4. Wait 2-3 minutes
5. Check if products updated!

**Option B: Wait for Schedule**
- It runs automatically every Monday at midnight UTC
- Check your site Monday morning!

---

## Configuration

### Customize Product Search

Edit `automation/config.yaml`:

```yaml
categories:
  chairs:
    name: "Office Chairs"
    keywords: "ergonomic office chair"  # ← Change search terms
    max_products: 6                     # ← Change number of products
    filters:
      min_rating: 4.0                   # ← Minimum star rating
      min_reviews: 100                  # ← Minimum review count
      price_min: 100                    # ← Minimum price
      price_max: 1000                   # ← Maximum price
```

### Change Update Schedule

Edit `.github/workflows/update-products.yml`:

```yaml
schedule:
  - cron: '0 0 * * 1'  # Every Monday at midnight
  # - cron: '0 0 * * *'  # Daily
  # - cron: '0 0 1 * *'  # First day of month
```

### Add Custom Product Descriptions

1. Run the automation (products found)
2. Check `automation/products.json` for product names
3. Ask ChatGPT/Claude to write descriptions (see `content/prompts.md`)
4. Add to `content/product-descriptions.yaml`:

```yaml
ergonomic_mesh_office_chair: "Your AI-generated description here"
```

5. Next automation run will use your custom descriptions!

---

## Running Manually

### On Your Computer (Optional)

If you want to run locally instead of GitHub:

```bash
# 1. Install Python dependencies
pip install -r automation/requirements.txt

# 2. Create .env file with your credentials
cp automation/secrets.example.env .env
# Edit .env and add your Amazon credentials

# 3. Load environment variables
export $(cat .env | xargs)

# 4. Run product finder
python automation/product_finder.py

# 5. Update website
python automation/website_updater.py

# 6. Commit and push
git add -A
git commit -m "Manual product update"
git push
```

---

## Troubleshooting

### Products Not Updating

**Check GitHub Actions logs:**
1. Go to **Actions** tab
2. Click latest workflow run
3. Read error messages

**Common issues:**

| Problem | Solution |
|---------|----------|
| "Amazon credentials not found" | Add secrets in GitHub Settings → Secrets |
| "PA-API request failed" | Check if your PA-API access is still active (need 1 sale/month) |
| "Rate limit exceeded" | Wait 24 hours, Amazon has daily limits |
| "No products found" | Adjust search keywords or filters in config.yaml |

### GitHub Actions Not Running

1. Check if Actions are enabled: **Settings** → **Actions** → **Allow all actions**
2. Check workflow file exists: `.github/workflows/update-products.yml`
3. Check cron schedule is correct

### Products Show But Links Don't Work

- Verify `AMAZON_ASSOCIATE_TAG` secret is your actual affiliate ID
- Check format: `yourname-20` (not a URL)

---

## Customization

### Add New Product Category

1. Create new HTML file: `categories/new-category.html`
2. Add category to `automation/config.yaml`:

```yaml
categories:
  new-category:
    name: "New Category"
    keywords: "search terms here"
    max_products: 6
    filters:
      min_rating: 4.0
      min_reviews: 50
      price_min: 50
      price_max: 500
    emoji: "🎁"
```

3. Next automation run will populate it!

### Change Product Count

In `automation/config.yaml`, change `max_products` for any category:

```yaml
chairs:
  max_products: 10  # Show 10 products instead of 6
```

### Adjust Price Ranges

```yaml
chairs:
  filters:
    price_min: 200    # Only show products $200+
    price_max: 1500   # Up to $1500
```

---

## What Happens Without PA-API?

If you haven't set up Amazon PA-API yet:

- ✅ Automation still runs
- ✅ Uses mock/placeholder data
- ✅ Shows generic products
- ⚠️ No real affiliate links yet
- ⚠️ No real prices

**Once you add PA-API credentials, everything switches to real data automatically!**

---

## File Structure

```
TerraLogic Tech Website/
├── automation/
│   ├── product_finder.py       ← Finds products
│   ├── website_updater.py      ← Updates HTML
│   ├── config.yaml             ← Settings
│   ├── products.json           ← Generated product data
│   ├── requirements.txt        ← Python packages
│   └── secrets.example.env     ← Credentials template
├── content/
│   ├── product-descriptions.yaml  ← Custom descriptions
│   ├── blog-template.html         ← Blog post template
│   └── prompts.md                 ← AI prompts
├── .github/
│   └── workflows/
│       └── update-products.yml    ← Automation schedule
├── categories/
│   ├── chairs.html             ← Auto-updated
│   ├── desks.html              ← Auto-updated
│   └── ...
└── index.html
```

---

## Next Steps

1. ✅ **You've built the automation!**
2. 📝 Apply for Amazon PA-API (see PA-API-SETUP.md)
3. 🔑 Add credentials to GitHub Secrets
4. 🚀 Deploy to GitHub Pages (see DEPLOYMENT-GUIDE.md)
5. ✨ Watch it run automatically!

---

## Support

- **Automation errors?** Check GitHub Actions logs
- **Need help?** Review this guide and other docs
- **Want to customize?** Edit `automation/config.yaml`

**Your affiliate site now runs itself! 🎉**
