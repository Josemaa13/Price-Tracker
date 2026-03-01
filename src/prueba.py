from playwright.sync_api import sync_playwright
import sqlite3
import time
import random
from datetime import datetime

URLS_FILE = "urls_zara.txt"
DB_NAME = "tracker.db"

def initialize_db():
    """Creates the SQLite database and table if they do not exist."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            price REAL,
            date TEXT,
            url TEXT
        )
    ''')
    connection.commit()
    return connection

def extract_zara_data(page, url):
    """Navigates to the web, avoids blocks, and extracts clean data."""
    page.goto(url, wait_until="domcontentloaded") 
    page.wait_for_selector("h1")
    
    # Raw extraction
    clothing = page.locator("h1").first.inner_text()
    price_str = page.locator(".money-amount__main").first.inner_text()
    
    # Data Cleaning
    clean_price = price_str.replace(" EUR", "").replace(",", ".")
    final_price = float(clean_price)
    
    return clothing, final_price

def save_to_db(connection, product, price, url):
    """Persists the mathematical data in the relational table."""
    cursor = connection.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO price_history (product, price, date, url)
        VALUES (?, ?, ?, ?)
    ''', (product, price, current_date, url))
    connection.commit()

def run():
    print("🚀 Starting Scraping Engine (Thesis Mode)...")
    
    # 1. Read URLs from external file
    try:
        with open(URLS_FILE, "r") as f:
            urls = [line.strip() for line in f.readlines() if line.strip()]
        print(f"📄 {len(urls)} URLs loaded for analysis.")
    except FileNotFoundError:
        print(f"❌ Error: File '{URLS_FILE}' not found. Create it and put URLs inside.")
        return

    connection = initialize_db()
    
    with sync_playwright() as p:
        # Add a real Chrome User-Agent for better camouflage
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        # 2. The Massive Loop with human-like waits
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] Analyzing URL...")
            try:
                product, price = extract_zara_data(page, url)
                save_to_db(connection, product, price, url)
                print(f"✅ Success: {product} | {price}€ saved to SQLite.")
                
            except Exception as e:
                print(f"⚠️ Non-critical failure on URL {i}. Skipping... (Error: {e})")
            
            # 3. Human Behavior: Random pause between 2 and 5 seconds
            if i < len(urls):
                wait_time = random.uniform(2.0, 5.0)
                print(f"⏳ Simulating human reading: waiting {wait_time:.2f}s...")
                time.sleep(wait_time)
        
        browser.close()
        connection.close()
        
    print("\n🏁 Process completed. Data secured in the relational database.")
    print("-" * 50)

if __name__ == "__main__":
    run()