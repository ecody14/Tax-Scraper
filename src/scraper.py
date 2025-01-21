import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited_urls = set()

    async def scrape_website(self, url):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)

            # Extract relevant content using BeautifulSoup
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            text = self.extract_text(soup)

            # Find and follow links to other relevant pages
            links = self.extract_links(soup, url)
            for link in links:
                if link not in self.visited_urls:
                    self.visited_urls.add(link)
                    text += await self.scrape_website(link)

            await browser.close()
            return text

    def extract_text(self, soup):
        # Extract text from relevant HTML elements
        text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'dt', 'dd'])
        text = ' '.join([el.get_text(strip=True) for el in text_elements])
        return text

    def extract_links(self, soup, url):
        # Extract links to other relevant pages
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and self.is_valid_link(href, url):
                absolute_url = urljoin(url, href)
                links.append(absolute_url)
        return links

    def is_valid_link(self, href, url):
        # Check if a link is valid and relevant
        parsed_href = urlparse(href)
        parsed_url = urlparse(url)
        return (
            parsed_href.scheme in ['http', 'https'] and
            parsed_href.netloc == parsed_url.netloc and
            'tax' in parsed_href.path.lower()  # Check if the link is tax-related
        )
