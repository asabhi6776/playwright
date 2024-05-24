import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)  # Set headless=True if you don't want to open the browser window
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://mail.google.com")
        # Add any other interactions with the page here if necessary
        # For example, you can log in, navigate, etc.

        # Keep the browser open for a while to see the result
        await asyncio.sleep(30)
        await browser.close()

asyncio.run(main())

