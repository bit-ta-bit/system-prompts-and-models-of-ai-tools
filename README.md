# Social Media & News Dashboard

This project is a simple, locally-run web dashboard that aggregates posts from specified X (formerly Twitter) accounts, YouTube channels, and Reddit communities. It presents the latest updates in a clean, tile-based card layout, sorted by publication date.

## Prerequisites

- Python 3.6 or newer
- `pip` for installing packages

## Setup Instructions

1.  **Clone the repository or download the files.**

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **(IMPORTANT) Configure X/Twitter RSS Feeds:**

    This application uses RSS feeds to get updates. While YouTube and Reddit provide standard RSS feeds, X/Twitter does not. To get feeds for X, you need to use a third-party service. We recommend [RSS.app](https://rss.app/).

    - Go to the [X / Twitter RSS Feed generator](https://rss.app/rss-feed/create-twitter-rss-feed).
    - Enter the URL of an X profile you want to follow (e.g., `https://x.com/emollick`) and generate the feed URL.
    - Open the `feed_fetcher.py` file in a text editor.
    - Find the `FEED_URLS` list and uncomment the placeholder X/Twitter URLs.
    - **Replace the placeholder URLs** with the ones you generated from RSS.app.

    For example, change this:
    ```python
    # "https://rss.app/feeds/placeholder-emollick.xml",
    ```
    To something like this (your generated URL will be different):
    ```python
    "https://rss.app/feeds/AbCdEfGhIjKlMnOp.xml",
    ```
    Repeat this for all the X accounts you wish to track.

## Running the Application

1.  **Start the Flask web server:**
    ```bash
    python app.py
    ```

2.  **View the dashboard:**
    Open your web browser and navigate to:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

You should see the dashboard populated with the latest posts from your configured sources. The application will fetch new data every time you load or refresh the page.
