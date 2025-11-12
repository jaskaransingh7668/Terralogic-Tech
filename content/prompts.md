# Content Generation Prompts

Use these prompts with ChatGPT or Claude to generate content for your affiliate site.

---

## Product Description Prompts

### For a Single Product

```
Write a compelling 2-3 sentence product description for an affiliate site about this product:

Product Name: [Product Name]
Category: [Category]
Price: [Price Range]
Key Features: [List 3-4 features]

The description should:
- Be enthusiastic but honest
- Highlight the main benefit
- Be 40-60 words
- Sound natural and helpful
```

### For Multiple Products at Once

```
I need product descriptions for my home office affiliate site. Write 2-3 sentence descriptions for each product below. Keep each around 50 words, enthusiastic but honest:

1. [Product 1 Name] - $[Price] - [1-2 key features]
2. [Product 2 Name] - $[Price] - [1-2 key features]
3. [Product 3 Name] - $[Price] - [1-2 key features]

Format: Just the descriptions, numbered
```

---

## Buying Guide Prompts

### Complete Buying Guide

```
Write a comprehensive buying guide blog post for my affiliate website about: "[Topic]"

Requirements:
- 800-1200 words
- SEO-friendly title
- Introduction explaining why this matters
- 5-7 key factors to consider when buying
- Budget vs premium comparisons
- Common mistakes to avoid
- Conclusion with clear next steps
- Friendly, helpful tone
- Focus on helping people make informed decisions

Target audience: Remote workers and home office professionals
```

### Quick Tips Section

```
Write 4-5 quick tips for "What to Look For in [Product Category]" for my home office affiliate site.

Format each as:
- Tip Title (2-4 words)
- 1-2 sentence explanation

Make them practical and easy to understand.
```

---

## Category Page Introductions

```
Write a 2-3 sentence intro for my [Product Category] page on a home office affiliate site.

Should:
- Welcome visitors
- Explain what they'll find on this page
- Mention variety of budgets/options
- Be encouraging and helpful
- 40-60 words total
```

---

## Blog Post Ideas Prompts

```
Generate 10 blog post title ideas for a home office affiliate website. Focus on:
- Buying guides
- Product comparisons
- Setup tips
- Productivity advice

Titles should be SEO-friendly and include numbers or "how-to" when possible.
```

---

## Meta Description Prompts

```
Write an SEO meta description (150-160 characters) for this page:

Page: [Page Name]
Topic: [Brief description]
Keywords: [1-2 main keywords]

Should: Describe the page, include keyword naturally, encourage clicks
```

---

## FAQ Prompts

```
Generate 5 frequently asked questions and answers for my page about "[Topic]" on a home office affiliate site.

Format:
Q: [Question]
A: [2-3 sentence answer]

Make them practical questions real buyers would ask.
```

---

## Example Workflow

### Step 1: Get Product Data
Run the automation to find products:
```bash
python automation/product_finder.py
```

### Step 2: Generate Descriptions
Copy product names from `automation/products.json` and use the prompt above with ChatGPT/Claude.

### Step 3: Add to Site
Paste descriptions into `content/product-descriptions.yaml`

### Step 4: Update Site
Run the updater:
```bash
python automation/website_updater.py
```

---

## Tips for Better AI Content

1. **Be specific**: The more context you give, the better the output
2. **Iterate**: Ask for revisions if the first version isn't quite right
3. **Add personality**: Ask Claude/ChatGPT to match your brand voice
4. **Stay honest**: Even with AI, keep descriptions truthful
5. **Batch work**: Generate multiple descriptions at once for efficiency

---

## Customization

Feel free to modify these prompts to match:
- Your brand voice
- Your target audience
- Your specific product categories
- Your preferred content style
