import os
import time
import random
from playwright.sync_api import sync_playwright

# Import our custom modules
from database.db_manager import initialize_db, save_to_db
from scrapers.zara_scraper import extract_zara_data

URLS_FILE = os.path.join("input", "urls_zara.txt")

def run():
    print("🚀 Starting Scraping Engine (Modular Architecture)...")
    
    # 1. Read URLs
    try:
        with open(URLS_FILE, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
        print(f"📄 Successfully loaded {len(urls)} URLs from {URLS_FILE}.")
    except FileNotFoundError:
        print(f"❌ Error: File '{URLS_FILE}' not found.")
        return

    # 2. Initialize Database
    connection = initialize_db()
    
    # 3. Initialize Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0"
        )
        page = context.new_page()
        
        # 4. Main Loop
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Analyzing URL...")
            try:
                # Call the scraping module
                product, price = extract_zara_data(page, url)
                
                # Call the database module
                save_to_db(connection, product, price, url)
                
                print(f"✅ Success: {product} | {price}€ saved.")
            except Exception as e:
                print(f"⚠️ Warning: Failed on URL {i}. Skipping... (Error: {e})")
            
            # Human-like delay
            if i < len(urls):
                wait_time = random.uniform(2.0, 5.0)
                print(f"⏳ Waiting for {wait_time:.2f}s...")
                time.sleep(wait_time)
        
        browser.close()
        connection.close()
        
    print("\n🏁 Process completed successfully.")

if __name__ == "__main__":
    run()