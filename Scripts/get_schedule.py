import pandas as pd
import requests
from bs4 import BeautifulSoup
import time 
import os
import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout


#set up constants 
#Scrapes seasons from 2021 to 2025
Seasons = list(range(2022,2027))
#print(Seasons)

async def get_html(url, selector, sleep=5, retries=3):
    html = None
    for i in range(1, retries+1):
        time.sleep(sleep * i)
        
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                #esstenially creates a new tab
                page = await browser.new_page()
                await page.goto(url)
                print(await page.title())
                html = await page.inner_html(selector)
                
        except PlaywrightTimeout:
            print(f"Timeout on attempt {i} for URL: {url}")
            continue
        else:
            break
    return html
"""
Had to make the main function ascync to work with playwright 

""" 
async def main():
    season = 2024
    # make this loop over all seasons
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_games.html"
    html = await get_html(url, "#content .filter")
    #grabbing the html content 
    print(html)
        
if __name__ == "__main__":
    asyncio.run(main())


    
                 
        