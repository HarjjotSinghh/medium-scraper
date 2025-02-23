# Medium Blog Scraper

A Python-based project to scrape Medium blog posts from user profiles. It provides both a RESTful API using FastAPI and a periodic cron job for continuous scraping.

## Features

- **REST API**:  
  `app.py` exposes an endpoint `/scrape/{username}` to scrape a Medium user's blog posts.  
- **Cron Job**:  
  `cron.py` periodically scrapes the Medium blog for a pre-configured username every 10 minutes.
- **Web Scraping Module**:  
  `scrape.py` implements the scraping logic using `requests` and `BeautifulSoup`.

## Project Structure

- **app.py**: Runs the FastAPI application on port `8080`.
- **cron.py**: Contains a loop to run the scraping job at regular intervals.
- **scrape.py**: Contains the code to scrape Medium blog posts.
- **requirements.txt**: Lists Python dependencies.
- **Dockerfile**: Docker image configuration for the project.
- **docker-compose.yml**: Defines services for running the FastAPI app and the cron job in Docker.

## Getting Started

### Using Docker

1. **Build and run containers with Docker Compose:**

   ```bash
   docker-compose up --build
   ```

2. **Access the API:**

   The FastAPI service will be available at [http://localhost:8080](http://localhost:8080).

3. **Cron Job Service:**

   The cron job runs concurrently in a separate container and scrapes the Medium posts every 10 minutes.

### Without Docker

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI Application:**

   ```bash
   python app.py
   ```

3. **Run the Cron Job (in a separate terminal):**

   ```bash
   python cron.py
   ```

## Author

[Harjot Singh Rana](https://harjotrana.com)