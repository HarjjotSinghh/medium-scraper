import time
from scrape import scrape_medium_blog


def job():
    """
    Periodically scrape Medium posts for the user 'gdg.gtbit' and print the results.
    """
    url = "https://medium.com/@gdg.gtbit"
    posts = scrape_medium_blog(url)
    print("Scraped posts:")
    for post in posts:
        print(post)


if __name__ == "__main__":
    # Run the job every 10 minutes (600 seconds)
    while True:
        job()
        time.sleep(600)
