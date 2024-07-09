import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zenatix.com/")
    page.get_by_role("link", name="Partners", exact=True).click()
    page.get_by_role("button", name="Company ").click()
    page.get_by_role("link", name=" Careers").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

