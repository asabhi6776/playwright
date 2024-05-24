import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opscribe.site/")
    page.get_by_role("link", name="Chaos Engineering: Building Resilient Systems Through Deliberate Disruption", exact=True).click()
    page.get_by_label("Getting Started with Chaos").click()
    page.get_by_role("heading", name="In Conclusion").click()
    page.get_by_label("Close sign in modal").click()
    page.get_by_role("link", name="Chaos Engineering", exact=True).click()
    page.get_by_text("Chaos Engineering: Building").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
