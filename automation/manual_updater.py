#!/usr/bin/env python3
"""
TerraLogic Tech - Manual Product Updater
Simple tool to update products without PA-API
"""

import yaml
import os
from website_updater import WebsiteUpdater

class ManualProductUpdater:
    """Updates website with manually configured products"""

    def __init__(self, manual_config_path: str = "automation/products-manual.yaml"):
        self.manual_config_path = manual_config_path
        self.products = self.load_manual_products()

    def load_manual_products(self):
        """Load manually configured products from YAML"""
        if not os.path.exists(self.manual_config_path):
            print(f"❌ Manual products file not found: {self.manual_config_path}")
            print("📝 Please create it using products-manual.example.yaml as a template")
            return {}

        try:
            with open(self.manual_config_path, 'r') as f:
                data = yaml.safe_load(f)
                return data.get('products', {})
        except Exception as e:
            print(f"❌ Error loading manual products: {e}")
            return {}

    def validate_product(self, product, category):
        """Validate that product has required fields"""
        required = ['name', 'asin', 'price_range', 'affiliate_url']
        missing = [field for field in required if not product.get(field)]

        if missing:
            print(f"⚠️  Warning: Product in {category} missing: {', '.join(missing)}")
            return False
        return True

    def generate_affiliate_url(self, asin: str, tag: str = None) -> str:
        """Generate Amazon affiliate URL from ASIN"""
        # Get tag from environment or config
        if not tag:
            tag = os.getenv('AMAZON_ASSOCIATE_TAG', 'yourname-20')

        return f"https://www.amazon.com/dp/{asin}?tag={tag}"

    def process_products(self):
        """Process and format products for website updater"""
        processed = {}

        for category, products in self.products.items():
            processed[category] = []

            for idx, product in enumerate(products, 1):
                # Skip invalid products
                if not self.validate_product(product, category):
                    continue

                # Auto-generate affiliate URL if not provided
                if not product.get('affiliate_url') and product.get('asin'):
                    tag = os.getenv('AMAZON_ASSOCIATE_TAG')
                    if tag:
                        product['affiliate_url'] = self.generate_affiliate_url(
                            product['asin'],
                            tag
                        )

                # Format product for website updater
                formatted = {
                    'name': product.get('name', 'Product Name'),
                    'asin': product.get('asin', ''),
                    'price': product.get('price_range', 'Check Amazon'),
                    'price_range': product.get('price_range', 'Check Amazon'),
                    'description': product.get('description', ''),
                    'features': product.get('features', []),
                    'image_url': product.get('image_url', ''),
                    'tier': product.get('tier', 'mid'),
                    'affiliate_url': product.get('affiliate_url', '#'),
                    'rating': product.get('rating', 4.5),
                    'review_count': product.get('review_count', 100)
                }

                processed[category].append(formatted)

            print(f"✅ Processed {len(processed[category])} products for {category}")

        return processed

    def update_website(self):
        """Update website HTML files with products"""
        print("=" * 60)
        print("Manual Product Updater - Updating Website")
        print("=" * 60)

        # Load products
        if not self.products:
            print("❌ No products to update. Please add products to products-manual.yaml")
            return

        # Process products
        processed_products = self.process_products()

        # Save to products.json (so website_updater can use it)
        import json
        from datetime import datetime

        output_data = {
            'last_updated': datetime.now().isoformat(),
            'products': processed_products,
            'source': 'manual'
        }

        products_file = "automation/products.json"
        with open(products_file, 'w') as f:
            json.dump(output_data, f, indent=2)

        print(f"\n✅ Saved products to {products_file}")

        # Use website updater to update HTML
        print("\n" + "=" * 60)
        print("Updating HTML Files")
        print("=" * 60)

        updater = WebsiteUpdater()
        updater.products_data = processed_products
        updater.update_all_categories()

        print("\n" + "=" * 60)
        print("✅ Website Updated Successfully!")
        print("=" * 60)
        print("\n📝 Next steps:")
        print("  1. Check your category pages to verify updates")
        print("  2. Commit and push changes to GitHub")
        print("  3. Wait 1-2 minutes for site to deploy")
        print("\nCommands to push:")
        print("  git add -A")
        print('  git commit -m "Update products manually"')
        print("  git push")


def main():
    """Main execution"""
    updater = ManualProductUpdater()
    updater.update_website()


if __name__ == "__main__":
    main()
