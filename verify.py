
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        pages_to_capture = ["index.html", "services.html", "about.html", "contact.html"]

        for page_name in pages_to_capture:
            await page.goto(f"http://localhost:8000/{page_name}")
            await page.screenshot(path=f"/home/jules/verification/{page_name.replace('.html', '.png')}")

        await browser.close()

asyncio.run(main())
