from fastapi import FastAPI
from scrape import scrape_medium_blog

app = FastAPI()


@app.get("/scrap")
def get_scraped_data():
    url = "https://medium.com/@gdg.gtbit"
    posts = scrape_medium_blog(url)
    return {"posts": posts}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
