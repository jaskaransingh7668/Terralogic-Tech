# TerraLogic Tech - Fully Automated Affiliate Website

A modern, professional affiliate marketing website for home office products with **complete automation**.

---

## 🎯 What You've Got

### Website Features ✅
- **Professional hero section** - Full-height with gradient background and animations
- **Value proposition** - 3 key reasons to trust your site
- **5 product categories** - Chairs, Desks, Monitors, Lighting, Audio-Video
- **Blog system** - Template for buying guides and content
- **Trust indicators** - Stats and badges
- **Fully responsive** - Perfect on all devices
- **Smooth animations** - Scroll effects and transitions
- **Mobile menu** - Works seamlessly on phones

### Automation Features 🤖
- **Automatic product discovery** - Finds top-rated products on Amazon
- **Auto-generated affiliate links** - Your tracking ID included
- **Price updates** - Refreshes weekly automatically
- **GitHub Actions integration** - Runs on schedule, no manual work
- **Self-updating** - Site updates itself with new products
- **Zero maintenance** - Set it and forget it!

---

## 📁 Project Structure

```
TerraLogic Tech Website/
├── index.html                    # Homepage
├── about.html                    # About page
├── contact.html                  # Contact form
├── privacy.html                  # Privacy policy
├── affiliate-disclosure.html     # FTC disclosure
├── categories/                   # Product category pages
│   ├── chairs.html              ← Auto-updated by automation
│   ├── desks.html               ← Auto-updated by automation
│   ├── monitors.html            ← Auto-updated by automation
│   ├── lighting.html            ← Auto-updated by automation
│   └── audio-video.html         ← Auto-updated by automation
├── css/
│   └── styles.css               # All styling
├── js/
│   └── main.js                  # JavaScript interactions
├── automation/                   # 🤖 Automation system
│   ├── product_finder.py        # Finds products via Amazon PA-API
│   ├── website_updater.py       # Updates HTML with products
│   ├── config.yaml              # Configuration & settings
│   ├── products.json            # Generated product data
│   ├── requirements.txt         # Python dependencies
│   └── secrets.example.env      # Credentials template
├── content/                      # Content management
│   ├── product-descriptions.yaml # Custom descriptions
│   ├── blog-template.html        # Blog post template
│   └── prompts.md                # AI content prompts
├── .github/
│   └── workflows/
│       └── update-products.yml   # GitHub Actions automation
├── .gitignore                    # Git ignore rules
├── AUTOMATION-GUIDE.md           # How automation works
├── PA-API-SETUP.md              # Amazon API setup guide
├── DEPLOYMENT-GUIDE.md          # Deployment instructions
└── README.md                    # This file
```

---

## 🚀 Quick Start Guide

### 1. Deploy to GitHub Pages

```bash
# Navigate to website folder
cd "TerraLogic Tech Website"

# Initialize git
git init
git add -A
git commit -m "Initial commit: TerraLogic Tech with automation"

# Push to GitHub
git remote add origin https://github.com/YOUR-USERNAME/terralogic-tech.git
git push -u origin main
```

**Then:** Enable GitHub Pages in repository Settings → Pages

📖 **Full guide:** See `DEPLOYMENT-GUIDE.md`

### 2. Apply for Amazon PA-API

1. Go to https://affiliate-program.amazon.com/
2. Navigate to Tools → Product Advertising API
3. Request API access
4. Use your GitHub Pages URL in application
5. Wait 1-3 days for approval

📖 **Full guide:** See `PA-API-SETUP.md`

### 3. Add Credentials to GitHub

Once PA-API is approved:

1. Go to your GitHub repo → Settings → Secrets → Actions
2. Add three secrets:
   - `AMAZON_ACCESS_KEY`
   - `AMAZON_SECRET_KEY`
   - `AMAZON_ASSOCIATE_TAG`

### 4. Test Automation

1. Go to Actions tab
2. Click "Update Products Automatically"
3. Click "Run workflow"
4. Wait 2-3 minutes
5. Your site updates with real products!

📖 **Full guide:** See `AUTOMATION-GUIDE.md`

---

## 🤖 How Automation Works

### The Process

```
Every Monday at Midnight (UTC)
         ↓
GitHub Actions Runs Automatically
         ↓
product_finder.py connects to Amazon PA-API
         ↓
Searches for top products (rating 4.0+)
         ↓
Generates affiliate links with your tag
         ↓
website_updater.py updates HTML files
         ↓
Changes committed to GitHub
         ↓
GitHub Pages auto-deploys
         ↓
Your Live Site is Updated! ✨
```

### What Gets Automated

✅ Finding products on Amazon
✅ Fetching product details (name, price, image, features)
✅ Generating your affiliate links
✅ Updating product cards on category pages
✅ Refreshing prices weekly
✅ Committing & deploying changes

### What's Manual

✍️ Writing custom product descriptions (optional)
✍️ Creating blog posts using AI prompts
✍️ Customizing categories/filters

---

## 💰 Cost Breakdown

| Service | Cost | Notes |
|---------|------|-------|
| **GitHub Pages** | FREE | Hosting |
| **GitHub Actions** | FREE | 2,000 min/month |
| **Amazon PA-API** | FREE | Must maintain 1 sale/month |
| **Domain (optional)** | $10-15/year | Custom domain |
| **Total** | **$0-15/year** | Practically free! |

---

## 📝 Content Creation Workflow

### For Product Descriptions

1. Automation finds products
2. Use prompts in `content/prompts.md` with ChatGPT/Claude
3. Add descriptions to `content/product-descriptions.yaml`
4. Next automation run uses your descriptions!

### For Blog Posts

1. Copy `content/blog-template.html`
2. Ask ChatGPT/Claude to write buying guide (use prompts)
3. Paste content into template
4. Save as `blog/your-post-title.html`
5. Commit and push

**See `content/prompts.md` for ready-to-use prompts!**

---

## ⚙️ Configuration

### Customize Product Search

Edit `automation/config.yaml`:

```yaml
categories:
  chairs:
    keywords: "ergonomic office chair"  # ← Change search terms
    max_products: 6                     # ← Number of products
    filters:
      min_rating: 4.0                   # ← Minimum stars
      min_reviews: 100                  # ← Minimum reviews
      price_min: 100                    # ← Min price
      price_max: 1000                   # ← Max price
```

### Change Automation Schedule

Edit `.github/workflows/update-products.yml`:

```yaml
schedule:
  - cron: '0 0 * * 1'  # Every Monday
  # - cron: '0 0 * * *'  # Daily
  # - cron: '0 0 1 * *'  # Monthly
```

---

## 🎨 Customization

### Colors & Branding

Edit `css/styles.css` (lines 5-20):

```css
:root {
  --primary-color: #f97316;     /* Main orange */
  --accent-color: #0ea5e9;      /* Accent blue */
  --text-primary: #1e293b;      /* Dark text */
  /* Customize these! */
}
```

### Add New Category

1. Create `categories/new-category.html` (copy existing)
2. Add to `automation/config.yaml`:

```yaml
categories:
  new-category:
    name: "New Category"
    keywords: "search terms"
    max_products: 6
```

3. Next automation run populates it!

---

## 🛠️ Technical Stack

### Frontend
- Pure HTML5/CSS3/JavaScript (no frameworks)
- CSS variables for easy theming
- Responsive design (mobile-first)
- Modern ES6+ JavaScript

### Automation
- Python 3.11+
- Amazon Product Advertising API
- BeautifulSoup for HTML parsing
- PyYAML for configuration

### Hosting & CI/CD
- GitHub Pages (hosting)
- GitHub Actions (automation)
- Git for version control

---

## 📚 Documentation

- **`AUTOMATION-GUIDE.md`** - Complete automation guide
- **`PA-API-SETUP.md`** - Amazon API setup
- **`DEPLOYMENT-GUIDE.md`** - GitHub Pages deployment
- **`content/prompts.md`** - AI content generation prompts

---

## 🎯 Features In Detail

### Design
- Full-screen hero with gradient background
- Smooth scroll animations (Intersection Observer)
- Hover effects on cards
- Mobile-responsive hamburger menu
- Back-to-top button
- Newsletter signup form
- Contact form with validation

### SEO & Performance
- Semantic HTML5
- Meta descriptions on all pages
- Fast loading (no external dependencies)
- Optimized animations (60fps)
- Mobile-first responsive
- Clean URL structure

### Affiliate Compliance
- FTC-required disclosure page
- Clear affiliate notices in footer
- Amazon Associates terms compliant
- Privacy policy included

---

## 🚦 Current Status

✅ Complete website (all pages)
✅ Full automation system built
✅ GitHub Actions configured
✅ Documentation complete
✅ Content templates ready
⏳ Awaiting deployment
⏳ Awaiting PA-API credentials

**Once deployed and PA-API added: Fully operational!**

---

## 🎓 How to Use This Site

### Day-to-Day Operation

**Week 1:**
- Deploy to GitHub Pages ✓
- Apply for Amazon PA-API ✓
- Add credentials to GitHub Secrets ✓
- Test automation ✓

**Ongoing (Automatic):**
- Every Monday: Products auto-update
- Every Monday: Prices refresh
- Zero maintenance required!

**As Needed (Manual):**
- Write blog posts (monthly)
- Customize product descriptions (optional)
- Monitor Amazon Associates dashboard
- Make design tweaks (rare)

**Time investment: ~1-2 hours per month** (mostly content writing)

---

## 💡 Tips for Success

### For Traffic & SEO
1. Write helpful buying guides (use AI prompts)
2. Target long-tail keywords ("best ergonomic chair for tall people")
3. Add Google Analytics to track performance
4. Share content on social media

### For Conversions
1. Keep product recommendations honest
2. Highlight different budget options
3. Write compelling product descriptions
4. Test different call-to-action text

### For Maintenance
1. Check automation logs weekly (GitHub Actions)
2. Monitor Amazon sales to keep PA-API active (1 sale/month)
3. Update content seasonally
4. Replace discontinued products as needed

---

## 🆘 Troubleshooting

### Automation Not Running

- Check GitHub Actions are enabled (Settings → Actions)
- Verify secrets are added correctly
- Check workflow file exists: `.github/workflows/update-products.yml`

### Products Not Updating

- Check PA-API credentials in GitHub Secrets
- Verify PA-API access is still active (need 1 sale/month)
- Check automation logs (Actions tab → latest run)

### Site Looks Broken

- Verify CSS path is correct (check repository name in URLs)
- Hard refresh browser (Ctrl+Shift+R)
- Check GitHub Pages is enabled and deployed

**Full troubleshooting in `AUTOMATION-GUIDE.md`**

---

## 📞 Next Steps

1. ✅ **Automation built** - You have everything!
2. 🚀 **Deploy site** - Follow `DEPLOYMENT-GUIDE.md`
3. 📝 **Apply for PA-API** - Follow `PA-API-SETUP.md`
4. 🔑 **Add credentials** - GitHub Settings → Secrets
5. 🧪 **Test automation** - Actions → Run workflow
6. ✍️ **Create content** - Use `content/prompts.md`
7. 📈 **Monitor & profit!**

---

## 🎉 Congratulations!

You now have a **fully automated affiliate website** that:
- Finds products automatically
- Updates itself weekly
- Generates affiliate links
- Requires minimal maintenance
- Costs $0-15/year to run

**Built with modern web standards and automation best practices.**

**Your passive income machine is ready! 🚀**
