# Manual Product Update Guide

Complete guide to manually managing products without Amazon PA-API.

---

## 📋 Overview

This system lets you update products **without PA-API access**. Perfect for:
- Getting started before you have 3 sales
- Testing your site with real products
- Building content and driving traffic
- Manual control over which products to show

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Create Your Products File

```bash
# Copy the example file
cp automation/products-manual.example.yaml automation/products-manual.yaml
```

### Step 2: Add Your First Product

Edit `automation/products-manual.yaml` and fill in product details (see below for how).

### Step 3: Update Your Site

```bash
python automation/manual_updater.py
```

### Step 4: Push to GitHub

```bash
git add -A
git commit -m "Add real products manually"
git push
```

**Done!** Your site updates in 1-2 minutes.

---

## 📝 How to Find and Add Products

### Finding Products on Amazon

1. **Go to Amazon.com**
2. **Search for products** (e.g., "ergonomic office chair")
3. **Filter by:**
   - Customer Reviews: 4 stars & up
   - Sort by: "Avg. Customer Review"
4. **Look for:**
   - ✅ 4+ star rating
   - ✅ 100+ reviews
   - ✅ "Amazon's Choice" or "Best Seller" badge
   - ✅ Prime eligible
   - ✅ Good photos

### Getting Product Information

For each product you want to add:

#### 1. **Get the ASIN**

The ASIN is Amazon's product ID. Find it in the URL:

```
https://www.amazon.com/Product-Name/dp/B08XYZ123/ref=...
                                      ^^^^^^^^^^
                                      This is the ASIN
```

Or on the product page:
- Scroll to "Product Information"
- Look for "ASIN: B08XYZ123"

#### 2. **Get Product Name**

Copy the main product title from the top of the page.

**Tip:** Shorten it if too long. Keep the brand and main features:
- ❌ "Executive Office Chair Big and Tall Computer Desk Chair Swivel Ergonomic High Back Leather Gaming Chair with Lumbar Support and Armrest, Black"
- ✅ "Executive Leather Office Chair with Lumbar Support"

#### 3. **Get Price**

Note the current price. Use a range:
- If $189.99 → Use "$150-200" or "$180-200"
- Ranges account for price fluctuations

#### 4. **Get Features**

Copy 4-5 key bullet points from the product description.

#### 5. **Generate Affiliate Link**

**Using Amazon SiteStripe:**

1. **Install SiteStripe** (if not visible):
   - Log into Amazon Associates
   - Browse any product on Amazon
   - You should see a black bar at the top

2. **Generate Link:**
   - On the product page, click **"Get Link"** in SiteStripe
   - Select **"Full Link"**
   - Copy the URL (automatically has your affiliate tag)

**Manual Method (if SiteStripe not available):**

```
https://www.amazon.com/dp/ASIN?tag=YOUR-AFFILIATE-TAG
```

Replace:
- `ASIN` with the product ASIN
- `YOUR-AFFILIATE-TAG` with your tag (e.g., `yourname-20`)

Example:
```
https://www.amazon.com/dp/B08XYZ123?tag=yourname-20
```

#### 6. **Optional: Get Image URL**

- Right-click the main product image
- Select "Copy Image Address"
- Paste into `image_url` field

**Or leave blank** - the site will use an emoji icon instead.

---

## 📄 Filling Out products-manual.yaml

### Template for Each Product

```yaml
- name: "Product Name Here"
  asin: "B08XYZ123"
  price_range: "$150-200"
  tier: "mid"  # budget, mid, or premium
  description: "2-3 sentence description. Highlight main benefits and who it's for."
  features:
    - "First key feature"
    - "Second key feature"
    - "Third key feature"
    - "Fourth key feature"
  image_url: ""  # Optional
  affiliate_url: "https://www.amazon.com/dp/B08XYZ123?tag=yourname-20"
  rating: 4.5
  review_count: 500
```

### Field Explanations

| Field | Description | Example |
|-------|-------------|---------|
| `name` | Product name (keep it concise) | "Ergonomic Mesh Office Chair" |
| `asin` | Amazon product ID | "B08XYZ123" |
| `price_range` | Approximate price range | "$150-200" |
| `tier` | Budget level (affects badge) | "budget", "mid", or "premium" |
| `description` | 2-3 sentences about the product | "Great for long work sessions..." |
| `features` | 4-5 key bullet points | List format |
| `image_url` | Product image URL (optional) | "https://..." or leave blank |
| `affiliate_url` | Your affiliate link | "https://amazon.com/dp/..." |
| `rating` | Star rating (out of 5) | 4.5 |
| `review_count` | Number of reviews | 500 |

### Tier Badges

Choose the right tier for each product:

| Tier | Badge Color | Price Range | Use For |
|------|-------------|-------------|---------|
| `budget` | Green | Under $200 | Affordable options |
| `mid` | Blue | $200-$500 | Most products |
| `premium` | Orange | $500+ | High-end picks |

---

## 🎯 Real Example

Let's say you found this chair on Amazon:

**Product:** Herman Miller Aeron Office Chair
**URL:** `https://www.amazon.com/dp/B00AZQKUV2`
**ASIN:** `B00AZQKUV2`
**Price:** $1,195
**Rating:** 4.3 stars
**Reviews:** 1,234

**Your YAML entry:**

```yaml
chairs:
  - name: "Herman Miller Aeron Ergonomic Office Chair"
    asin: "B00AZQKUV2"
    price_range: "$1,000-1,300"
    tier: "premium"
    description: "The gold standard in ergonomic office chairs. Fully adjustable with mesh back for breathability and all-day comfort. Investment piece built to last decades."
    features:
      - "PostureFit SL™ sacral support"
      - "8Z Pellicle® suspension"
      - "Fully adjustable arms, seat, and tilt"
      - "12-year warranty included"
    image_url: ""
    affiliate_url: "https://www.amazon.com/dp/B00AZQKUV2?tag=yourname-20"
    rating: 4.3
    review_count: 1234
```

---

## 🔄 Updating Products

### When to Update

- **Weekly:** Check if prices changed significantly
- **Monthly:** Add new products or remove discontinued ones
- **As needed:** When you find better options

### How to Update

1. Edit `automation/products-manual.yaml`
2. Run `python automation/manual_updater.py`
3. Push to GitHub:
   ```bash
   git add -A
   git commit -m "Update products"
   git push
   ```

---

## ⚙️ Running the Updater

### Basic Usage

```bash
cd "C:\Users\jaska\OneDrive\Desktop\TerraLogic Tech Website"
python automation/manual_updater.py
```

### What It Does

1. ✅ Reads your products-manual.yaml file
2. ✅ Validates product data
3. ✅ Generates products.json
4. ✅ Updates all category HTML files
5. ✅ Shows summary of changes

### Expected Output

```
============================================================
Manual Product Updater - Updating Website
============================================================
✅ Processed 6 products for chairs
✅ Processed 6 products for desks
✅ Processed 6 products for monitors
✅ Processed 6 products for lighting
✅ Processed 5 products for audio-video

✅ Saved products to automation/products.json

============================================================
Updating HTML Files
============================================================
Updating categories/chairs.html with 6 products...
  ✓ Updated categories/chairs.html
Updating categories/desks.html with 6 products...
  ✓ Updated categories/desks.html
...

✅ Website Updated Successfully!
```

---

## 🎨 Product Descriptions

### Writing Good Descriptions

**Formula:** Benefit + Feature + Who It's For

**Examples:**

✅ **Good:**
"A solid budget option with breathable mesh back, adjustable height, and lumbar support. Great for those starting their home office on a budget."

❌ **Bad:**
"This is a chair. It's good."

### Tips

1. **Be specific** - Mention key features
2. **Highlight benefits** - How does it help?
3. **Target audience** - Who is it for?
4. **Keep it short** - 2-3 sentences max
5. **Be honest** - Don't oversell

### Use AI to Help

Ask ChatGPT or me:

```
Write a 2-sentence product description for this office chair:
- Name: [Product Name]
- Key features: [List features]
- Price: [Price range]
Make it helpful and enthusiastic but honest.
```

---

## 📊 How Many Products to Add

### Recommended Numbers

| Category | Minimum | Recommended | Maximum |
|----------|---------|-------------|---------|
| Chairs | 3 | 6 | 10 |
| Desks | 3 | 6 | 10 |
| Monitors | 3 | 6 | 10 |
| Lighting | 3 | 6 | 10 |
| Audio-Video | 3 | 6 | 10 |

### Product Mix Strategy

For each category, include:
- **1-2 Budget options** ($50-200)
- **2-3 Mid-range options** ($200-500)
- **1-2 Premium options** ($500+)

This covers all buyer types!

---

## 🆘 Troubleshooting

### "File not found: products-manual.yaml"

**Solution:**
```bash
cp automation/products-manual.example.yaml automation/products-manual.yaml
```

### Products Not Showing on Site

**Checklist:**
1. Did you run `python automation/manual_updater.py`?
2. Did you see "✅ Website Updated Successfully!"?
3. Did you push to GitHub? (`git push`)
4. Wait 1-2 minutes for GitHub Pages to deploy
5. Hard refresh browser (Ctrl+Shift+R)

### Affiliate Links Not Working

**Check:**
- Link format: `https://www.amazon.com/dp/ASIN?tag=yourname-20`
- Replace `yourname-20` with YOUR actual affiliate tag
- Test link in browser - should go to Amazon with your tag

### YAML Syntax Error

**Common mistakes:**
```yaml
# ❌ Wrong (missing quotes)
name: My Product: The Best

# ✅ Right (use quotes)
name: "My Product: The Best"

# ❌ Wrong (inconsistent indentation)
features:
  - "Feature 1"
   - "Feature 2"

# ✅ Right (consistent indentation)
features:
  - "Feature 1"
  - "Feature 2"
```

**Validate your YAML:** https://www.yamllint.com/

---

## 🎯 Workflow Summary

### Daily Workflow

1. **Find products** on Amazon (10-15 min)
2. **Copy info** to products-manual.yaml (5 min per product)
3. **Run updater** (`python automation/manual_updater.py`)
4. **Push to GitHub** (`git push`)
5. **Verify** on live site (1-2 min later)

**Time investment: 30-60 minutes per category**

### Weekly Maintenance

- Check if any products out of stock
- Update prices if changed significantly
- Add 1-2 new products
- Remove discontinued items

**Time: 15-30 minutes per week**

---

## 🚀 Transition to Automation

### When You Get PA-API Access

**After your first 3 sales:**

1. Apply for PA-API
2. Get approved
3. Add credentials to GitHub Secrets
4. **Keep using manual system OR switch to automation**

**You can use both!**
- Manual for specific products you want to control
- Automation for everything else

---

## 💡 Pro Tips

### Finding Great Products

1. **Amazon Best Sellers** - Start here
2. **Amazon's Choice** - Algorithm picks
3. **4.5+ stars** - Quality threshold
4. **200+ reviews** - Enough data
5. **Prime eligible** - Faster shipping = more sales

### Optimizing for Conversions

1. **Show variety** - Different price points
2. **Highlight "best sellers"** - Use premium tier
3. **Update seasonally** - Back-to-school, holidays
4. **Test different products** - Track what sells

### Building Content

While adding products:
1. Note common questions from reviews
2. Turn into blog post topics
3. "Best chairs for back pain" (common issue)
4. "Standing desks for small spaces" (specific need)

---

## 📞 Need Help?

### Quick Reference

```bash
# Create products file
cp automation/products-manual.example.yaml automation/products-manual.yaml

# Update site
python automation/manual_updater.py

# Push changes
git add -A
git commit -m "Update products"
git push
```

### Common Issues

- **Python not found**: Install Python 3.x
- **Module not found**: `pip install -r automation/requirements.txt`
- **YAML errors**: Check indentation and quotes
- **Not showing on site**: Wait 2 min, hard refresh

---

## ✅ Checklist

First time setup:
- [ ] Copied products-manual.example.yaml to products-manual.yaml
- [ ] Found 3-6 products on Amazon for one category
- [ ] Copied ASIN, name, price for each
- [ ] Generated affiliate links
- [ ] Filled out YAML file
- [ ] Ran manual_updater.py successfully
- [ ] Pushed to GitHub
- [ ] Verified products showing on live site

---

**You're now manually managing products like a pro! Once you get PA-API access, you can switch to full automation. Until then, this system gives you complete control.**
