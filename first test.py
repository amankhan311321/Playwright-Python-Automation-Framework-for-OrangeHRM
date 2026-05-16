#playwright python code to open a browers and print the title
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False)
   page = browser.new_page()
   page.goto('https://sites.google.com/view/bwowunisexsalon/home')
   print(page.title())
   browser.close()
