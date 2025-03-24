from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
import os
import asyncio
import subprocess
import time

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
HN_USERNAME = os.getenv("HACKER_NEWS_USERNAME")
HN_PASSWORD = os.getenv("HACKER_NEWS_PASSWORD")

# Ensure credentials are available
if not HN_USERNAME or not HN_PASSWORD:
    raise ValueError("HN_USERNAME and HN_PASSWORD must be set in .env file")

llm = ChatOpenAI(model="gpt-4o")

async def main():
    # First make sure Chrome is closed
    subprocess.run(['killall', 'Google Chrome'], stderr=subprocess.DEVNULL)
    time.sleep(1)
    
    # Start Chrome with remote debugging enabled
    chrome_process = subprocess.Popen([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--remote-debugging-port=9222',
        '--user-data-dir=' + os.path.expanduser('~/ChromeProfile')
    ])
    
    # Wait for Chrome to start
    time.sleep(3)
    
    # Configure browser to connect to the debugging instance
    browser = Browser(
        config=BrowserConfig(
            headless=False,
            # We don't need to specify chrome_instance_path when connecting to an already running instance
            # that has remote debugging enabled
        )
    )
    
    # Create agent with the configured browser and specific instructions
    task_instructions = f"""
    Go to news.ycombinator.com.
    Click on 'login' in the top navigation bar.
    On the login page:
    - Enter the username: {HN_USERNAME}
    - Enter the password: {HN_PASSWORD}
    - Click the login button.
    After logging in, look for your username '{HN_USERNAME}' in the top navigation bar.
    Click on your username.
    On the profile page, find the number displayed next to the word 'karma' and report that number.
    """
    
    agent = Agent(
        task=task_instructions,
        llm=llm,
        browser=browser,
    )
    
    try:
        result = await agent.run()
        print(result)
    finally:
        # Clean up browser and Chrome process
        await browser.close()
        chrome_process.terminate()
        chrome_process.wait()

if __name__ == "__main__":
    asyncio.run(main()) 