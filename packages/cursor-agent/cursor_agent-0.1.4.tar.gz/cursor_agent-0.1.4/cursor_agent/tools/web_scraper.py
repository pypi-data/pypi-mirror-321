#!/usr/bin/env /workspace/tmp_windsurf/venv/bin/python3

import asyncio
import argparse
import sys
import os
from typing import List, Optional
from playwright.async_api import async_playwright
import html5lib
from multiprocessing import Pool
import time
from urllib.parse import urlparse
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

async def fetch_page(url):
    try:
        async with async_playwright() as p:
            # Launch WebKit with minimal options
            browser = await p.webkit.launch(
                headless=True,
                args=['--no-startup-window']  # WebKit-specific argument
            )
            
            # Create a context with basic settings
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 720},
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15'
            )
            
            # Create a new page
            page = await context.new_page()
            
            try:
                # Try different navigation strategies
                for wait_until in ['domcontentloaded', 'load', 'networkidle']:
                    try:
                        await page.goto(url, wait_until=wait_until, timeout=30000)
                        content = await page.content()
                        return content
                    except Exception as e:
                        logger.warning(f"Navigation failed with {wait_until}: {str(e)}")
                        continue
                
                # If all strategies fail, try one last time with minimal options
                await page.goto(url)
                content = await page.content()
                return content
                
            except Exception as e:
                logger.error(f"Error fetching {url}: {str(e)}")
                return None
            finally:
                await browser.close()
    except Exception as e:
        logger.error(f"Error fetching {url}: {str(e)}")
        return None

def parse_html(html_content: Optional[str]) -> str:
    """Parse HTML content and extract text with hyperlinks in markdown format."""
    if not html_content:
        return ""
    
    try:
        document = html5lib.parse(html_content)
        result = []
        seen_texts = set()  # To avoid duplicates
        
        def should_skip_element(elem) -> bool:
            """Check if the element should be skipped."""
            # Skip script and style tags
            if elem.tag in ['{http://www.w3.org/1999/xhtml}script', 
                          '{http://www.w3.org/1999/xhtml}style']:
                return True
            # Skip empty elements or elements with only whitespace
            if not any(text.strip() for text in elem.itertext()):
                return True
            return False
        
        def process_element(elem, depth=0):
            """Process an element and its children recursively."""
            if should_skip_element(elem):
                return
            
            # Handle text content
            if hasattr(elem, 'text') and elem.text:
                text = elem.text.strip()
                if text and text not in seen_texts:
                    # Check if this is an anchor tag
                    if elem.tag == '{http://www.w3.org/1999/xhtml}a':
                        href = None
                        for attr, value in elem.items():
                            if attr.endswith('href'):
                                href = value
                                break
                        if href and not href.startswith(('#', 'javascript:')):
                            # Format as markdown link
                            link_text = f"[{text}]({href})"
                            result.append("  " * depth + link_text)
                            seen_texts.add(text)
                    else:
                        result.append("  " * depth + text)
                        seen_texts.add(text)
            
            # Process children
            for child in elem:
                process_element(child, depth + 1)
            
            # Handle tail text
            if hasattr(elem, 'tail') and elem.tail:
                tail = elem.tail.strip()
                if tail and tail not in seen_texts:
                    result.append("  " * depth + tail)
                    seen_texts.add(tail)
        
        # Start processing from the body tag
        body = document.find('.//{http://www.w3.org/1999/xhtml}body')
        if body is not None:
            process_element(body)
        else:
            # Fallback to processing the entire document
            process_element(document)
        
        # Filter out common unwanted patterns
        filtered_result = []
        for line in result:
            # Skip lines that are likely to be noise
            if any(pattern in line.lower() for pattern in [
                'var ', 
                'function()', 
                '.js',
                '.css',
                'google-analytics',
                'disqus',
                '{',
                '}'
            ]):
                continue
            filtered_result.append(line)
        
        return '\n'.join(filtered_result)
    except Exception as e:
        logger.error(f"Error parsing HTML: {str(e)}")
        return ""

async def process_urls(urls):
    logger.info(f"Processing {len(urls)} URLs")
    results = {}
    
    for url in urls:
        logger.info(f"Starting browser for {url}")
        content = await fetch_page(url)
        
        if content:
            results[url] = content
        else:
            logger.warning(f"Failed to process {url}")
            results[url] = "Error: Failed to fetch content. This may happen with complex websites in Docker. Try running this command outside Docker for better compatibility."
    
    return results

def validate_url(url: str) -> bool:
    """Validate if the given string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def main():
    """Main function for the scrape command."""
    parser = argparse.ArgumentParser(description='Scrape web pages')
    parser.add_argument('urls', nargs='+', help='URLs to scrape')
    args = parser.parse_args()

    # Validate URLs
    valid_urls = []
    for url in args.urls:
        if validate_url(url):
            valid_urls.append(url)
        else:
            logger.error(f"Invalid URL: {url}")

    if not valid_urls:
        logger.error("No valid URLs provided")
        sys.exit(1)

    try:
        results = asyncio.run(process_urls(valid_urls))
        for url, content in results.items():
            print(f"\n=== Content from {url} ===")
            print(content)
            print("=" * 80)
        sys.exit(0)
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main() 