import random
import time
import pandas as pd
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AmazonScraper:
    def __init__(self):
        self.driver = self.setup_driver()

    def setup_driver(self):
        """Set up the Selenium WebDriver with headless mode and randomized User-Agent."""
        chrome_options = Options()
        chrome_options.add_argument("--headless") 
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        ]
        chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

        return webdriver.Chrome(service=ChromeService(), options=chrome_options)

    def search_amazon(self, product_title):
        """Search for the product on Amazon and return its link and ASIN."""
        search_url = f"https://www.amazon.com/s?k={'+'.join(product_title.split())}"
        self.driver.get(search_url)

        try:
            # Wait until the search results are loaded
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]'))
            )

            product = self.driver.find_element(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
            product_link = product.find_element(By.CSS_SELECTOR, 'a.a-link-normal').get_attribute('href')

            # Ensure we properly extract the ASIN
            asin = product_link.split('/dp/')[1].split('/')[0] if '/dp/' in product_link else None

            if asin is None:
                logging.warning(f"ASIN not found for product: {product_title}")

        except Exception as e:
            logging.error(f"Error processing {product_title}: {e}")
            return None, None  # Always return two values

        # Log the return values for debugging
        logging.info(f"Returning: Link: {product_link}, ASIN: {asin} for {product_title}")
        
        return product_link, asin 


    def close_driver(self):
        """Close the Selenium WebDriver."""
        self.driver.quit()