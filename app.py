from fastapi import FastAPI
from scrape import scrape_medium_blog

app = FastAPI()


@app.get("/scrape/{username}")
def get_scraped_data(username):
    """
    Scrape the Medium blog of the given username.

    When you make a GET request to this endpoint with a username,
    it constructs a Medium URL and uses the scraping function to retrieve posts.

    @param username: str - The Medium username (without the @ symbol).
    @return: dict - A dictionary with a key "posts" containing a list of posts.

    Example endpoint:
        GET http://localhost:8080/scrape/gdg.gtbit
    """
    url = f"https://medium.com/@{username}"
    posts = scrape_medium_blog(url)
    return {"posts": posts}


if __name__ == "__main__":
    import uvicorn

    # Launch the FastAPI server on host 0.0.0.0 and port 8080.
    uvicorn.run(app, host="0.0.0.0", port=8080)
