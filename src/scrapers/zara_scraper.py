def extract_zara_data(page, url):
    """Navigates to the Zara website and extracts clean data."""
    page.goto(url, wait_until="domcontentloaded") 
    page.wait_for_selector("h1")
    
    # Raw extraction
    product_name = page.locator("h1").first.inner_text()
    price_str = page.locator(".money-amount__main").first.inner_text()
    
    # Data Cleaning
    clean_price = price_str.replace(" EUR", "").replace(",", ".")
    final_price = float(clean_price)
    
    return product_name, final_price