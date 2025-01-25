import asyncio
import socket
import logging
from playwright.async_api import async_playwright, Browser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

remote_debugging_port = 9223
remote_host = "localhost"

async def is_browser_opened_in_debug_mode():
    """Check if the browser is opened in debug mode"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((remote_host, remote_debugging_port))
            return result == 0
    except (ConnectionRefusedError, OSError) as error:
        logger.error(f"Debug mode check error: {error}")
        return False

async def wait_for_browser_start(timeout=20, retry_interval=1):
    """Wait for the browser to start and listen on the debug port"""
    start_time = asyncio.get_event_loop().time()
    while not await is_browser_opened_in_debug_mode():
        if asyncio.get_event_loop().time() - start_time > timeout:
            raise TimeoutError(f"Timed out waiting for port {remote_debugging_port} to listen")
        await asyncio.sleep(retry_interval)

async def connect_browser() -> Browser:
    """Connect to the browser"""
    playwright = await async_playwright().start()

    
    endpoint_url = f"http://{remote_host}:{remote_debugging_port}"
    browser = await playwright.chromium.connect_over_cdp(endpoint_url)
    return browser

async def main():
    try:
        # Wait for browser to be available
        await wait_for_browser_start()
        logger.info("Browser is available on debug port")
        
        # Connect to browser
        browser = await connect_browser()
        logger.info("Connected to browser successfully")
        
        # Get first context and create new page
        context = browser.contexts[0]
        page = await context.new_page()
        logger.info("Created new page")
        
        # Navigate to Google
        await page.goto("https://www.facebook.com")
        logger.info("Navigated to Google")
        
        # Keep the script running briefly to see the result
        await asyncio.sleep(5)
        
        # Clean up
        await browser.close()
        logger.info("Closed browser connection")
        
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())