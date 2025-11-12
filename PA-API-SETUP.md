# Amazon Product Advertising API Setup Guide

Step-by-step guide to get your Amazon PA-API credentials.

---

## What is Amazon PA-API?

The **Product Advertising API** (PA-API) is Amazon's official way for affiliates to:
- Search for products programmatically
- Get product details, images, prices
- Generate affiliate links automatically

**It's completely FREE** but requires maintaining sales activity.

---

## Prerequisites

Before applying for PA-API:

✅ **Amazon Associates account** (approved and active)
✅ **Live website with URL** (deploy to GitHub Pages first!)
✅ **Content about products** (your site qualifies)

---

## Step-by-Step Application

### Step 1: Access Associates Central

1. Go to: https://affiliate-program.amazon.com/
2. Log in with your Associates account
3. You should see your dashboard

### Step 2: Navigate to PA-API Section

1. In the top menu, hover over **Tools**
2. Click **Product Advertising API**

   **OR**

   Direct link: https://affiliate-program.amazon.com/assoc_credentials/home

### Step 3: Request API Access

You'll see one of two screens:

#### If You See "Get Started" or "Request Access"

1. Click the button to request access
2. Fill out the application form:

**Required Information:**

| Field | What to Enter |
|-------|---------------|
| **Website URL** | Your GitHub Pages URL (e.g., https://yourusername.github.io/terralogic-tech/) |
| **Application Name** | "TerraLogic Tech Automation" |
| **Description** | "Automated product discovery and recommendation system for home office products. Uses PA-API to find top-rated products in categories like office chairs, desks, monitors, and accessories." |
| **Use Case** | "Product recommendations and affiliate links" |

#### If You Already Have Access

You'll see your credentials displayed:
- Access Key (looks like: `AKIAI...`)
- Secret Key (long string)
- Your Associate Tag

**Skip to Step 5!**

### Step 4: Wait for Approval

- **Approval time:** Usually 1-3 business days
- **Email notification:** You'll receive confirmation
- **Check status:** Return to the PA-API page to see approval

**While waiting:** You can continue with deployment! The automation will use mock data until credentials are added.

### Step 5: Get Your Credentials

Once approved:

1. Return to **Product Advertising API** section
2. You should see three pieces of information:

```
Access Key:        AKIAIOSFODNN7EXAMPLE
Secret Key:        wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Associate Tag:     yourname-20
```

**⚠️ IMPORTANT:**
- Copy these immediately
- Store them securely
- Secret Key is only shown once!
- If lost, you'll need to regenerate

---

## Adding Credentials to Your Site

### For GitHub Actions (Automated Updates)

1. Go to your GitHub repository
2. Click **Settings** tab
3. In sidebar: **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add each credential:

**Secret 1:**
- Name: `AMAZON_ACCESS_KEY`
- Value: Your Access Key

**Secret 2:**
- Name: `AMAZON_SECRET_KEY`
- Value: Your Secret Key

**Secret 3:**
- Name: `AMAZON_ASSOCIATE_TAG`
- Value: Your Associate Tag (e.g., `yourname-20`)

### For Local Testing (Optional)

If you want to run automation on your computer:

1. Copy `automation/secrets.example.env` to `.env`
2. Edit `.env`:

```bash
AMAZON_ACCESS_KEY=your_actual_access_key_here
AMAZON_SECRET_KEY=your_actual_secret_key_here
AMAZON_ASSOCIATE_TAG=your_actual_tag_here
```

3. **NEVER commit .env to git!** (Already in .gitignore)

---

## PA-API Requirements & Restrictions

### To Keep Access Active

❗ **Critical:** You must maintain sales activity:

| Timeframe | Requirement |
|-----------|-------------|
| **First 30 days** | At least 3 qualifying sales |
| **After that** | At least 1 sale every 30 days |

If requirements not met:
- PA-API access is suspended
- Your site still works, but won't update products
- Can reapply after making required sales

### API Limits

- **Requests per day:** 8,640
- **Requests per second:** 1
- **Throttling:** Automatic with rate limits

**Your automation stays well under limits:**
- Runs once per week
- Makes ~6-10 API calls per run
- Total: ~40 calls per month

### Allowed Uses

✅ Product recommendations on your site
✅ Price comparisons
✅ Search functionality
✅ Automated affiliate links

❌ Data scraping for resale
❌ Creating product databases to sell
❌ Violating Amazon's ToS

---

## Testing Your API Access

### Test in GitHub Actions

1. After adding secrets, go to **Actions** tab
2. Select "Update Products Automatically"
3. Click **Run workflow** → **Run workflow**
4. Wait 2-3 minutes
5. Click on the workflow run to see logs

**If successful, you'll see:**
```
Finding products for: Office Chairs
  Found 6 products
Finding products for: Desks
  Found 6 products
...
✓ All category pages updated!
```

**If errors:**
- Check credentials are correct
- Verify PA-API is approved
- Check API quotas aren't exceeded

### Test Locally (Optional)

```bash
# Load environment variables
export $(cat .env | xargs)

# Run product finder
python automation/product_finder.py

# Check output
cat automation/products.json
```

---

## Common Issues

### "PA-API Access Denied"

**Causes:**
- Haven't been approved yet
- Credentials incorrect
- API access suspended (sales requirement)

**Solutions:**
1. Verify approval status in Associates Central
2. Check credentials match exactly (no extra spaces)
3. Check your sales activity (need 1 per month)

### "Invalid Signature"

**Cause:** Secret Key is incorrect

**Solution:**
- Regenerate credentials in Associates Central
- Update GitHub Secrets with new keys

### "Service Unavailable"

**Cause:** Temporary Amazon outage or rate limiting

**Solution:**
- Wait 1 hour and try again
- Check Amazon Associates announcements

### "Associate Tag Not Found"

**Cause:** Using wrong tag format

**Solution:**
- Should be: `yourname-20` (not full URL)
- Find in Associates → Account Settings

---

## What If I Don't Have PA-API Yet?

**Your site still works!**

Without PA-API:
- ✅ Website functions normally
- ✅ Automation runs on schedule
- ✅ Uses placeholder products
- ⚠️ No real product data
- ⚠️ No affiliate link generation

**Once PA-API is added:**
- Everything switches to real data automatically
- No code changes needed
- Just add the secrets!

---

## Alternative: Manual Mode

Don't want to apply for PA-API?

You can manually manage products:

1. Find products on Amazon yourself
2. Create affiliate links using Associates SiteStripe
3. Edit product data in HTML files directly
4. Skip the automation

**But you'll lose:**
- Automatic price updates
- Auto product discovery
- Scheduled refreshes

---

## API Documentation

Official Amazon PA-API docs:
- **Getting Started:** https://webservices.amazon.com/paapi5/documentation/
- **Troubleshooting:** https://webservices.amazon.com/paapi5/documentation/troubleshooting/
- **Associates Help:** https://affiliate-program.amazon.com/help/

---

## Checklist

Use this to track your PA-API setup:

- [ ] Amazon Associates account approved
- [ ] Website deployed with live URL
- [ ] Applied for PA-API access
- [ ] Received approval email
- [ ] Copied Access Key
- [ ] Copied Secret Key
- [ ] Copied Associate Tag
- [ ] Added all 3 secrets to GitHub
- [ ] Tested automation (manual run)
- [ ] Verified products updating
- [ ] Made at least 3 sales (first 30 days)

---

## Next Steps

1. ✅ **Got your credentials?** Add to GitHub Secrets
2. 🧪 **Test the automation** with manual run
3. 📈 **Monitor sales** to keep API active
4. 🎉 **Enjoy automated updates!**

---

**Once PA-API is set up, your site becomes fully automated!** Products update themselves weekly with zero manual work.
