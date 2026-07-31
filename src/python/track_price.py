from playwright.sync_api import sync_playwright
from datetime import datetime

url = "https://oilgroupbg.com/mazda-ultra-5w-30-1-%D0%BB%D0%B8%D1%82%D1%8A%D1%80.html"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    
    # Взимаме цената по селектор (проверен в браузър)
    price = page.query_selector(".product-price span").inner_text()
    print(datetime.now(), price)
    
    browser.close()
