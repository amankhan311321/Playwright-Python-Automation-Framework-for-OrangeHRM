import re
from time import time
from playwright.sync_api import expect

def test_google_search(page):
    page.goto("https://www.google.com/ncr")
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept")

    page.get_by_role("combobox", name="Search").fill("playwright python")
    
    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("playwright", re.IGNORECASE))