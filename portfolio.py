import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://iam-abhishek.netlify.app/")
    page.get_by_label("experience").click()
    page.get_by_role("tab", name="Netzary Infodynamics").click()
    with page.expect_popup() as page1_info:
        page.get_by_title("SES Mailtest").get_by_role("link").click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

