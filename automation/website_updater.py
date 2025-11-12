#!/usr/bin/env python3
"""
TerraLogic Tech - Website Updater
Updates HTML files with product data from Amazon
"""

import os
import json
import yaml
import re
from datetime import datetime
from typing import Dict, List
from bs4 import BeautifulSoup


class WebsiteUpdater:
    """Updates website HTML files with product data"""

    def __init__(self, config_path: str = "automation/config.yaml"):
        """Initialize with configuration"""
        self.config = self.load_config(config_path)
        self.products_data = self.load_products()
        self.custom_descriptions = self.load_custom_descriptions()

    def load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Config file not found at {config_path}")
            return {}

    def load_products(self, products_path: str = "automation/products.json") -> Dict:
        """Load products from JSON file"""
        try:
            with open(products_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('products', {})
        except FileNotFoundError:
            print(f"Warning: Products file not found at {products_path}")
            return {}

    def load_custom_descriptions(self, desc_path: str = "content/product-descriptions.yaml") -> Dict:
        """Load custom product descriptions"""
        try:
            with open(desc_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        except FileNotFoundError:
            return {}

    def generate_product_card_html(self, product: Dict, index: int) -> str:
        """Generate HTML for a single product card"""

        # Determine badge
        tier = product.get('tier', '').lower()
        badge_html = ''
        if tier == 'budget':
            badge_html = '<div class="product-badge budget">Budget Pick</div>'
        elif tier == 'premium':
            badge_html = '<div class="product-badge premium">Premium Pick</div>'
        elif tier == 'mid':
            badge_html = '<div class="product-badge mid">Mid-Range</div>'

        # Get description (custom or from product data)
        product_key = product.get('name', '').lower().replace(' ', '_')[:30]
        description = self.custom_descriptions.get(product_key, product.get('description', 'Quality product for your home office.'))

        # Format features
        features = product.get('features', [])
        if not features:
            features = [
                'High-quality construction',
                'Great customer reviews',
                'Fast shipping available',
                'Reliable performance'
            ]

        features_html = '\n              '.join([f'<li>✓ {feature}</li>' for feature in features[:4]])

        # Product image or emoji
        if product.get('image_url'):
            image_html = f'<img src="{product["image_url"]}" alt="{product["name"]}" style="width: 100%; height: 100%; object-fit: cover;">'
        else:
            emoji = '🪑'  # Default emoji
            image_html = f'<span class="product-emoji">{emoji}</span>'

        html = f'''
        <!-- Product Card {index + 1} -->
        <div class="product-card">
          {badge_html}
          <div class="product-image-placeholder">
            {image_html}
          </div>
          <div class="product-content">
            <h3 class="product-name">{product.get('name', 'Product Name')}</h3>
            <div class="product-price">{product.get('price_range', product.get('price', 'Check Amazon'))}</div>
            <p class="product-description">{description}</p>
            <ul class="product-features">
              {features_html}
            </ul>
            <div class="product-footer">
              <a href="{product.get('affiliate_url', '#')}" class="btn btn-primary btn-block" data-affiliate="true" data-product-name="{product.get('name', 'Product')}">
                View on Amazon →
              </a>
            </div>
          </div>
        </div>'''

        return html

    def update_category_page(self, category_key: str, products: List[Dict]):
        """Update a category page with products"""

        category_config = self.config.get('categories', {}).get(category_key, {})
        category_file = f"categories/{category_key}.html"

        if not os.path.exists(category_file):
            print(f"Warning: Category file not found: {category_file}")
            return

        print(f"Updating {category_file} with {len(products)} products...")

        # Read the HTML file
        with open(category_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the products grid
        products_grid = soup.find('div', class_='products-grid')

        if not products_grid:
            print(f"  Warning: Could not find products-grid in {category_file}")
            return

        # Clear existing product cards
        products_grid.clear()

        # Add new product cards
        for idx, product in enumerate(products):
            card_html = self.generate_product_card_html(product, idx)
            card_soup = BeautifulSoup(card_html, 'html.parser')
            products_grid.append(card_soup)

        # Add update timestamp comment
        timestamp_comment = soup.new_string(f'\n    <!-- Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} by automation -->\n    ')
        products_grid.insert_before(timestamp_comment)

        # Write back to file
        with open(category_file, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

        print(f"  ✓ Updated {category_file}")

    def update_all_categories(self):
        """Update all category pages with products"""
        print("\n" + "=" * 60)
        print("Updating Category Pages")
        print("=" * 60)

        for category_key, products in self.products_data.items():
            self.update_category_page(category_key, products)

        print("\n✓ All category pages updated!")

    def update_homepage_stats(self):
        """Update homepage statistics"""
        print("\nUpdating homepage stats...")

        index_file = "index.html"

        if not os.path.exists(index_file):
            print("Warning: index.html not found")
            return

        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count total products
        total_products = sum(len(products) for products in self.products_data.values())

        # Update stat if needed (this is optional)
        # For now, we'll keep the existing stats as they are placeholders

        print("  ✓ Homepage stats reviewed")


def main():
    """Main execution function"""
    print("=" * 60)
    print("TerraLogic Tech - Website Updater")
    print("=" * 60)

    # Initialize updater
    updater = WebsiteUpdater()

    # Update all category pages
    updater.update_all_categories()

    # Update homepage if needed
    updater.update_homepage_stats()

    print("\n" + "=" * 60)
    print("Website Update Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
