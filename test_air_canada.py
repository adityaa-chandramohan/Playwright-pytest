import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def page():
    with sync_playwright() as p:
        # Set headless=False to see the browser window
        browser = p.chromium.launch(headless=False)
        
        # Optional: Set viewport size
        context = browser.new_context(viewport={'width': 1280, 'height': 720})
        
        # Optional: Add slow motion to see what's happening
        context.set_default_timeout(30000)  # 30 seconds timeout
        
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_air_canada_redirect(page):
    page.goto("https://www.aircanada.com/home/ca/en/aco/flights")
    
    # Optional: Add a small delay to see the page
    page.wait_for_timeout(1000)  # 1 second
    
    page.get_by_role("button", name="YYZ Toronto").click()
    page.get_by_role("button", name="Clear").click()
    page.get_by_role("combobox", name="From").fill("MONTREAL")
    page.get_by_role("button", name="Arriving in").click()
    page.get_by_role("combobox", name="To").fill("FRANK")
    page.get_by_role("combobox", name="Departure date").click()
    page.get_by_role("gridcell", name="May 27,").locator("p").click()
    page.locator("#bkmg-desktop_travelDates-date-2025-06-06").click()
    page.get_by_role("button", name="Select", exact=True).click()
    page.locator("#bkmg-desktop_findButton").click()
    page.wait_for_url("**/availability/rt/outbound**")
    
    assert "https://www.aircanada.com/booking/ca/en/aco/availability/rt/outbound" in page.url