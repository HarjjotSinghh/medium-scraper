import time
from scrape import scrape_medium_blog


def job():
    url = "https://medium.com/@gdg.gtbit"
    posts = scrape_medium_blog(url)
    print("Scraped posts:")
    for post in posts:
        print(post)


if __name__ == "__main__":
    while True:
        job()
        time.sleep(600)  # Sleep for 600 seconds (10 minutes)
