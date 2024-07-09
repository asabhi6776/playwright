import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://asabhi6776.hashnode.dev/")
    page.get_by_test_id("blog-sub-header").get_by_role("link", name="home").click()
    page.get_by_role("link", name="Integrating NFS as a storage class in Kubernetes cluster", exact=True).click()
    page.get_by_label("Like this article").dblclick()
    page.get_by_label("Close sign in modal").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

