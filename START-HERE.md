# 🚀 START HERE - Manual Product Management

**Your site is live, but you need 3 sales before PA-API access.**
**Use this manual system to get started TODAY!**

---

## ⚡ 5-Minute Quick Start

### 1. Create Products File (30 seconds)

```bash
cd "C:\Users\jaska\OneDrive\Desktop\TerraLogic Tech Website"
copy automation\products-manual.example.yaml automation\products-manual.yaml
```

### 2. Add Your First Product (3 minutes)

1. Go to Amazon.com
2. Search "ergonomic office chair"
3. Pick a 4+ star product
4. Copy the ASIN from URL (looks like: `B08XYZ123`)
5. Open `automation/products-manual.yaml` in Notepad
6. Fill in the template (see below)

### 3. Update Your Site (1 minute)

```bash
python automation\manual_updater.py
```

### 4. Push to GitHub (30 seconds)

```bash
git add -A
git commit -m "Add first products"
git push
```

**Done!** Check your live site in 2 minutes.

---

## 📝 Minimal Product Entry

**Fastest way to add a product:**

```yaml
chairs:
  - name: "Ergonomic Mesh Office Chair"
    asin: "B08XYZ123"  # ← Get from Amazon URL
    price_range: "$150-200"
    tier: "mid"
    description: "Comfortable chair with lumbar support. Great for home office use."
    features:
      - "Breathable mesh back"
      - "Adjustable height"
      - "Lumbar support"
      - "Smooth casters"
    image_url: ""
    affiliate_url: "https://www.amazon.com/dp/B08XYZ123?tag=YOURTAG-20"
    rating: 4.5
    review_count: 500
```

**Replace:**
- `B08XYZ123` with actual ASIN
- `YOURTAG-20` with your affiliate tag
- Fill in real product name, price, features

---

## 🎯 Your Week 1 Goal

**Add 3-6 products per category:**

- [ ] **Chairs** - 3 products minimum
- [ ] **Desks** - 3 products minimum
- [ ] **Monitors** - 3 products minimum
- [ ] **Lighting** - 3 products minimum
- [ ] **Audio-Video** - 3 products minimum

**Time needed: 2-3 hours total**

---

## 🔗 How to Get Affiliate Links

### Option 1: Amazon SiteStripe (Easiest)

1. Log into Amazon Associates
2. Browse product on Amazon
3. See black bar at top? That's SiteStripe
4. Click **"Get Link"** → **"Full Link"**
5. Copy and paste!

### Option 2: Manual Format

```
https://www.amazon.com/dp/[ASIN]?tag=[YOUR-TAG]
```

Example:
```
https://www.amazon.com/dp/B08XYZ123?tag=yourname-20
```

---

## 📚 Full Documentation

**For complete instructions:**
👉 **Read: `MANUAL-UPDATE-GUIDE.md`**

Covers:
- Finding products on Amazon
- Getting ASINs and product info
- Writing descriptions
- Troubleshooting
- Pro tips

---

## ❓ Quick Questions

### "Where do I find the ASIN?"

In the product URL:
```
https://www.amazon.com/Product-Name/dp/B08XYZ123/ref=...
                                      ^^^^^^^^^^
                                      This is it!
```

### "What's my affiliate tag?"

Check your Amazon Associates dashboard:
- Go to https://affiliate-program.amazon.com/
- Top right: Your tracking ID (like `yourname-20`)

### "How do I run Python scripts?"

Open Command Prompt (CMD) or PowerShell:
1. Navigate to website folder
2. Type: `python automation\manual_updater.py`
3. Press Enter

### "Products not showing?"

**Checklist:**
1. ✅ Ran `manual_updater.py` without errors?
2. ✅ Pushed to GitHub? (`git push`)
3. ✅ Waited 2 minutes?
4. ✅ Hard refreshed browser? (Ctrl+Shift+R)

---

## 🎯 Success Path

### Week 1-2: Setup
- ✅ Site live (DONE!)
- 📝 Add 3-6 products per category
- ✍️ Write 1-2 blog posts
- 📱 Share on social media

### Week 3-8: Growth
- ✍️ 1 blog post per week
- 📊 Track traffic
- 💬 Engage on Reddit/forums
- 🎯 Focus on SEO keywords

### Week 8-12: First Sales
- 💰 Get your 3 sales!
- 📝 Apply for PA-API
- 🔑 Add credentials
- 🤖 Switch to automation

### Week 12+: Autopilot
- 🤖 Full automation running
- ✍️ Occasional content updates
- 💵 Passive income!

---

## 🆘 Need Help?

### Documentation
- **`MANUAL-UPDATE-GUIDE.md`** - Complete manual system guide
- **`AUTOMATION-GUIDE.md`** - For when you get PA-API
- **`README.md`** - Overview of everything

### Commands Cheat Sheet

```bash
# Update products
python automation\manual_updater.py

# Push to GitHub
git add -A
git commit -m "Update products"
git push

# Check status
git status
```

---

## 💪 You've Got This!

**Your site is live and ready to make money.**
**Start adding products today, and you'll have your 3 sales in no time!**

**Next step:** Open `automation/products-manual.yaml` and add your first product! 🚀
