import re

def test_valid_link_format(link):
    """Test if the link is a valid Amazon product link."""
    pattern = r'https:\/\/www\.amazon\.com\/.*\/dp\/[A-Z0-9]{10}'
    assert re.match(pattern, link), f"Invalid link format: {link}"
    print(f"Valid link format: {link}")

def test_valid_asin_format(asin):
    """Test if the ASIN is valid (10 characters, alphanumeric)."""
    assert re.match(r'^[A-Z0-9]{10}$', asin), f"Invalid ASIN format: {asin}"
    print(f"Valid ASIN format: {asin}")

def test_product_details_retrieval(product):
    """Test if product details are correctly retrieved."""
    expected_keys = ['title', 'link', 'price', 'asin']
    for key in expected_keys:
        assert key in product, f"Missing expected key: {key}"
    print(f"Product details retrieved successfully: {product}")

# Example usage
if __name__ == "__main__":
    # Test data
    test_link = "https://www.amazon.com/Games-Workshop-Necromunda-Goliath-Gang/dp/B0779Q1K7P"
    test_asin = "B0779Q1K7P"
    test_product = {
        'title': 'Games Workshop - Necromunda Goliath Gang Miniature',
        'link': test_link,
        'price': 44.20,
        'asin': test_asin
    }

    test_valid_link_format(test_link)
    test_valid_asin_format(test_asin)
    test_product_details_retrieval(test_product)