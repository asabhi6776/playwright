import asyncio
from playwright.sync_api import sync_playwright

async def main():
    # Create a new Playwright instance
    playwright = await sync_playwright()

    # Launch Chrome (or another browser of your choice)
    browser = await playwright.chromium.launch(headless=False)

    # Create a new page
    page = await browser.new_page()

    # Navigate to Google
    await page.goto('https://www.google.com')

    # Enter search query
    await page.fill('[name="q"]', 'Sexy indian girl')

    # Submit the form
    await page.click('[type="submit"]')

    # Wait for the results page to load
    await page.waitForLoadState('networkidle2')

    # Close the browser
    await browser.close()

# Run the script
asyncio.run(main())

