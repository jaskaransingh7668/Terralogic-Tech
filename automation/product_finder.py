#!/usr/bin/env python3
"""
TerraLogic Tech - Amazon Product Finder
Automatically finds and fetches products from Amazon PA-API
"""

import os
import yaml
import json
import requests
import hashlib
import hmac
import time
from datetime import datetime
from urllib.parse import quote, urlencode
from typing import Dict, List, Optional

class AmazonProductFinder:
    """Handles Amazon Product Advertising API integration"""

    def __init__(self, config_path: str = "automation/config.yaml"):
        """Initialize with configuration"""
        self.config = self.load_config(config_path)
        self.access_key = os.getenv('AMAZON_ACCESS_KEY')
        self.secret_key = os.getenv('AMAZON_SECRET_KEY')
        self.associate_tag = os.getenv('AMAZON_ASSOCIATE_TAG')
        self.region = self.config.get('amazon', {}).get('region', 'us-east-1')
        self.marketplace = self.config.get('amazon', {}).get('marketplace', 'www.amazon.com')

    def load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            print(f"Warning: Config file not found at {config_path}")
            return {}

    def _sign_request(self, method: str, uri: str, query_params: Dict) -> str:
        """Sign the Amazon PA-API request"""
        timestamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        date_stamp = datetime.utcnow().strftime('%Y%m%d')

        # Add required parameters
        query_params.update({
            'Operation': 'SearchItems',
            'PartnerTag': self.associate_tag,
            'PartnerType': 'Associates',
            'Timestamp': timestamp
        })

        canonical_querystring = urlencode(sorted(query_params.items()))
        canonical_headers = f'host:{self.marketplace}\n'
        signed_headers = 'host'
        payload_hash = hashlib.sha256(''.encode('utf-8')).hexdigest()

        canonical_request = f'{method}\n{uri}\n{canonical_querystring}\n{canonical_headers}\n{signed_headers}\n{payload_hash}'

        algorithm = 'AWS4-HMAC-SHA256'
        credential_scope = f'{date_stamp}/{self.region}/ProductAdvertisingAPI/aws4_request'
        string_to_sign = f'{algorithm}\n{timestamp}\n{credential_scope}\n{hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()}'

        signing_key = self._get_signature_key(self.secret_key, date_stamp, self.region, 'ProductAdvertisingAPI')
        signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

        authorization_header = f'{algorithm} Credential={self.access_key}/{credential_scope}, SignedHeaders={signed_headers}, Signature={signature}'

        return authorization_header, canonical_querystring

    def _get_signature_key(self, key: str, date_stamp: str, region: str, service: str) -> bytes:
        """Derive signing key"""
        k_date = hmac.new(f'AWS4{key}'.encode('utf-8'), date_stamp.encode('utf-8'), hashlib.sha256).digest()
        k_region = hmac.new(k_date, region.encode('utf-8'), hashlib.sha256).digest()
        k_service = hmac.new(k_region, service.encode('utf-8'), hashlib.sha256).digest()
        k_signing = hmac.new(k_service, b'aws4_request', hashlib.sha256).digest()
        return k_signing

    def search_products(self, category: str, keywords: str, max_results: int = 10) -> List[Dict]:
        """
        Search for products using Amazon PA-API

        Args:
            category: Product category (e.g., 'Office Chairs')
            keywords: Search keywords
            max_results: Maximum number of results to return

        Returns:
            List of product dictionaries
        """
        if not all([self.access_key, self.secret_key, self.associate_tag]):
            print("Warning: Amazon PA-API credentials not set. Returning mock data.")
            return self._get_mock_products(category, max_results)

        try:
            # Prepare request parameters
            query_params = {
                'Keywords': keywords,
                'SearchIndex': 'OfficeProducts',
                'ItemCount': str(max_results),
                'Resources': 'Images.Primary.Large,ItemInfo.Title,ItemInfo.Features,Offers.Listings.Price'
            }

            # Sign and make request
            auth_header, query_string = self._sign_request('GET', '/paapi5/searchitems', query_params)

            url = f'https://{self.marketplace}/paapi5/searchitems?{query_string}'
            headers = {
                'Authorization': auth_header,
                'Content-Type': 'application/json'
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            return self._parse_products(data)

        except Exception as e:
            print(f"Error fetching products from Amazon: {e}")
            return self._get_mock_products(category, max_results)

    def _parse_products(self, api_response: Dict) -> List[Dict]:
        """Parse Amazon PA-API response into product dictionaries"""
        products = []

        items = api_response.get('SearchResult', {}).get('Items', [])

        for item in items:
            try:
                product = {
                    'asin': item.get('ASIN'),
                    'name': item.get('ItemInfo', {}).get('Title', {}).get('DisplayValue', 'Unknown Product'),
                    'price': self._extract_price(item),
                    'image_url': item.get('Images', {}).get('Primary', {}).get('Large', {}).get('URL', ''),
                    'features': item.get('ItemInfo', {}).get('Features', {}).get('DisplayValues', [])[:5],
                    'rating': item.get('CustomerReviews', {}).get('StarRating', {}).get('Value', 4.0),
                    'review_count': item.get('CustomerReviews', {}).get('Count', 100),
                    'affiliate_url': self._generate_affiliate_url(item.get('ASIN')),
                    'description': ''  # Will be filled manually or by AI
                }
                products.append(product)
            except Exception as e:
                print(f"Error parsing product: {e}")
                continue

        return products

    def _extract_price(self, item: Dict) -> str:
        """Extract price from API response"""
        try:
            price_info = item.get('Offers', {}).get('Listings', [{}])[0].get('Price', {})
            amount = price_info.get('Amount', 0)
            currency = price_info.get('Currency', 'USD')
            return f"${amount:.2f}" if currency == 'USD' else f"{amount:.2f} {currency}"
        except:
            return "$0.00"

    def _generate_affiliate_url(self, asin: str) -> str:
        """Generate Amazon affiliate URL"""
        if not asin or not self.associate_tag:
            return "#"
        return f"https://www.amazon.com/dp/{asin}?tag={self.associate_tag}"

    def _get_mock_products(self, category: str, count: int) -> List[Dict]:
        """Return mock product data when PA-API is not available"""
        print(f"Using mock data for category: {category}")

        mock_products = {
            'chairs': [
                {'name': 'Ergonomic Mesh Office Chair', 'price_range': '$150-200', 'tier': 'budget'},
                {'name': 'Executive Leather Chair', 'price_range': '$250-350', 'tier': 'mid'},
                {'name': 'Premium Ergonomic Task Chair', 'price_range': '$600-900', 'tier': 'premium'},
                {'name': 'Gaming Chair with Lumbar Support', 'price_range': '$200-300', 'tier': 'mid'},
                {'name': 'Drafting Stool for Standing Desk', 'price_range': '$150-250', 'tier': 'budget'},
                {'name': 'High-Back Executive Chair', 'price_range': '$300-400', 'tier': 'mid'},
            ],
            'desks': [
                {'name': 'Adjustable Standing Desk', 'price_range': '$300-500', 'tier': 'mid'},
                {'name': 'Budget L-Shaped Desk', 'price_range': '$150-250', 'tier': 'budget'},
                {'name': 'Premium Electric Standing Desk', 'price_range': '$700-1000', 'tier': 'premium'},
                {'name': 'Compact Computer Desk', 'price_range': '$100-150', 'tier': 'budget'},
                {'name': 'Executive Wood Desk', 'price_range': '$400-600', 'tier': 'mid'},
                {'name': 'Gaming Desk with LED', 'price_range': '$250-350', 'tier': 'mid'},
            ],
            'monitors': [
                {'name': '27" 4K Monitor', 'price_range': '$300-400', 'tier': 'mid'},
                {'name': '24" Budget Full HD Monitor', 'price_range': '$120-180', 'tier': 'budget'},
                {'name': '32" Curved Gaming Monitor', 'price_range': '$400-600', 'tier': 'premium'},
                {'name': 'Ultrawide 34" Monitor', 'price_range': '$500-700', 'tier': 'premium'},
                {'name': 'Portable USB-C Monitor', 'price_range': '$200-300', 'tier': 'mid'},
                {'name': 'Dual Monitor Mount', 'price_range': '$50-100', 'tier': 'budget'},
            ],
            'lighting': [
                {'name': 'LED Desk Lamp with USB', 'price_range': '$30-50', 'tier': 'budget'},
                {'name': 'Monitor Light Bar', 'price_range': '$80-120', 'tier': 'mid'},
                {'name': 'Smart LED Strip Lights', 'price_range': '$40-70', 'tier': 'mid'},
                {'name': 'Floor Lamp for Office', 'price_range': '$60-100', 'tier': 'mid'},
                {'name': 'Clamp Desk Lamp', 'price_range': '$25-40', 'tier': 'budget'},
                {'name': 'Ring Light for Video Calls', 'price_range': '$50-80', 'tier': 'mid'},
            ],
            'audio-video': [
                {'name': 'Wireless Noise-Cancelling Headset', 'price_range': '$150-250', 'tier': 'mid'},
                {'name': '1080p Webcam', 'price_range': '$60-100', 'tier': 'mid'},
                {'name': 'USB Condenser Microphone', 'price_range': '$80-120', 'tier': 'mid'},
                {'name': 'Budget Wired Headset', 'price_range': '$30-50', 'tier': 'budget'},
                {'name': 'Premium 4K Webcam', 'price_range': '$150-200', 'tier': 'premium'},
                {'name': 'Bluetooth Speaker', 'price_range': '$40-70', 'tier': 'budget'},
            ]
        }

        category_key = category.lower().replace(' ', '-')
        products_list = mock_products.get(category_key, mock_products['chairs'])

        return products_list[:count]

    def find_products_for_all_categories(self) -> Dict[str, List[Dict]]:
        """Find products for all configured categories"""
        all_products = {}

        categories = self.config.get('categories', {})

        for category_key, category_config in categories.items():
            print(f"\nFinding products for: {category_config['name']}")

            keywords = category_config.get('keywords', category_config['name'])
            max_products = category_config.get('max_products', 6)

            products = self.search_products(
                category=category_key,
                keywords=keywords,
                max_results=max_products
            )

            all_products[category_key] = products
            print(f"  Found {len(products)} products")

            # Rate limiting - be nice to Amazon API
            time.sleep(1)

        return all_products

    def save_products(self, products: Dict[str, List[Dict]], output_path: str = "automation/products.json"):
        """Save found products to JSON file"""
        output_data = {
            'last_updated': datetime.now().isoformat(),
            'products': products
        }

        with open(output_path, 'w') as f:
            json.dump(output_data, f, indent=2)

        print(f"\nProducts saved to {output_path}")


def main():
    """Main execution function"""
    print("=" * 60)
    print("TerraLogic Tech - Amazon Product Finder")
    print("=" * 60)

    # Initialize finder
    finder = AmazonProductFinder()

    # Find products for all categories
    all_products = finder.find_products_for_all_categories()

    # Save to JSON
    finder.save_products(all_products)

    # Print summary
    print("\n" + "=" * 60)
    print("Summary:")
    for category, products in all_products.items():
        print(f"  {category}: {len(products)} products")
    print("=" * 60)


if __name__ == "__main__":
    main()
