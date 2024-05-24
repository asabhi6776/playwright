import asyncio
import os
from playwright.async_api import async_playwright
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://mail.google.com")

        # Wait for the email input field and type the email
        await page.fill('input[type="email"]', os.getenv('GMAIL_USERNAME'))
        await page.click('button:has-text("Next")')
        
        # Wait for the password input field and type the password
        await page.wait_for_selector('input[type="password"]', state='visible')
        await page.fill('input[type="password"]', os.getenv('GMAIL_PASSWORD'))
        await page.click('button:has-text("Next")')

        # Add any other interactions with the page here if necessary
        # For example, you can navigate through the Gmail interface

        # Keep the browser open for a while to see the result
        await asyncio.sleep(30)
        await browser.close()

asyncio.run(main())

