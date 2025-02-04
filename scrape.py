import requests
from bs4 import BeautifulSoup
import json
import re


def scrape_medium_blog(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <article> tags (each blog post block)
    articles = soup.find_all("article")
    blog_posts = []
    for article in articles:
        # Look for the first <a> tag with an href (which should contain the blog link and title)
        a_tag = article.find("a", href=True)
        if not a_tag:
            continue

        raw_href = a_tag.get("href")
        # If the URL is relative, make it absolute
        if raw_href.startswith("/"):
            href = "https://medium.com" + raw_href
        else:
            href = raw_href

        # Extract the title text from the h2 tag inside the <a>
        title_tag = a_tag.find("h2")
        title = title_tag.get_text(strip=True) if title_tag else None

        # Extract the subtitle/description (if available) from an h3 tag
        subtitle_tag = a_tag.find("h3")
        subtitle = subtitle_tag.get_text(strip=True) if subtitle_tag else None

        # Try to extract a publication time like "10h ago", "1d ago" etc by searching the article text
        article_text = article.get_text(separator=" ", strip=True)
        pub_time_search = re.search(r"(\d+\s*[hdw] ago)", article_text)
        publication_time = pub_time_search.group(1) if pub_time_search else None

        blog_posts.append(
            {
                "title": title,
                "subtitle": subtitle,
                "url": href,
                "publication_time": publication_time,
            }
        )
    return blog_posts


if __name__ == "__main__":
    url = "https://medium.com/@gdg.gtbit"
    posts = scrape_medium_blog(url)
    print(json.dumps(posts, indent=4))
