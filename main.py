import requests
from bs4 import BeautifulSoup
import os
import time


def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ebay.com/',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',  # "Do Not Track" header to simulate a real browser
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # If there's an error, this will stop execution
    return BeautifulSoup(response.text, 'html.parser')


def get_comments_from_page(soup, comment_selector):
    comments = []
    comment_divs = soup.select(comment_selector)
    for div in comment_divs:
        comment_text = div.get_text(strip=True)
        if "Search" not in comment_text:
            comments.append(comment_text)
    return comments


def find_next_page(soup):
    # Locate the pagination navigation
    pagination_nav = soup.select_one("nav.pagination-warpper")
    if not pagination_nav:
        return None

    # Find the next page link
    next_button = pagination_nav.select_one("a[rel='next']")
    if next_button and next_button['href']:
        return next_button['href']  # Return the next page URL
    return None


def scrape_comments(url, comment_selector, max_pages=5):
    all_comments = []
    page_count = 0

    while url and page_count < max_pages:
        print(f"Scraping page {page_count + 1}: {url}")
        soup = get_soup(url)
        comments = get_comments_from_page(soup, comment_selector)
        all_comments.extend(comments)
        
        # Find the next page using the updated function
        url = find_next_page(soup)
        page_count += 1
        time.sleep(1)  # no overloading for the SERVER !!!

    return all_comments


def save_comments_to_file(comments, version_name, output_dir="comments"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.join(output_dir, f"{version_name}_comments.txt")
    with open(filename, 'w', encoding='utf-8') as f:
        for comment in comments:
            f.write(comment + '\n')
    print(f"Saved comments for {version_name} to {filename}")


def read_urls_from_file(filename):
    urls = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # Ignore empty lines
                version_name, url = line.strip().split(',', 1)  # Expecting "VersionName,URL" format
                urls[version_name.strip()] = url.strip()
    return urls


def main():
    # Read version URLs from a text file
    version_urls = read_urls_from_file("urls.txt")

    # CSS selectors for eBay product review pages
    comment_selector = ".ebay-review-section-r"  # Adjust this based on the page structure

    for version, url in version_urls.items():
        print(f"Scraping comments for {version}")
        comments = scrape_comments(url, comment_selector)
        save_comments_to_file(comments, version)


if __name__ == "__main__":
    main()
