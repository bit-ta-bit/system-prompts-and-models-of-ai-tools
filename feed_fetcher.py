import feedparser
import time

# List of RSS feed URLs
# Note: The X/Twitter URLs are placeholders and need to be replaced by the user.
FEED_URLS = [
    # YouTube
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCvasqcd8NP0YGKTaKYPb34A", # kkp_news
    "https://www.youtube.com/feeds/videos.xml?channel_id=UC8yHePe_RgUBE-waRWy6olw", # pivot00
    "https://www.youtube.com/feeds/videos.xml?channel_id=UC_kdDsYNfszgVtuxr3rXZzw", # tottekuu
    # X (Twitter) - Placeholders
    # "https://rss.app/feeds/placeholder-emollick.xml", # Placeholder for emollick
    # "https://rss.app/feeds/placeholder-simpsoka.xml", # Placeholder for simpsoka
    # "https://rss.app/feeds/placeholder-philschmid.xml", # Placeholder for _philschmid
    # Reddit
    "https://www.reddit.com/r/Bard/.rss",
]

def fetch_feeds():
    """
    Fetches and parses multiple RSS feeds.

    Returns:
        A list of entries from all feeds, where each entry is a dictionary.
    """
    all_entries = []
    for url in FEED_URLS:
        print(f"Fetching feed: {url}")
        try:
            feed = feedparser.parse(url)
            source_title = feed.feed.title

            for entry in feed.entries:
                all_entries.append({
                    'source': source_title,
                    'title': entry.title,
                    'link': entry.link,
                    # published_parsed is a time.struct_time object
                    'published_parsed': entry.get('published_parsed', time.gmtime()),
                })
        except Exception as e:
            print(f"Error fetching or parsing feed {url}: {e}")

    return all_entries

# Main block to test the function
if __name__ == "__main__":
    print("Starting feed fetching test...")
    entries = fetch_feeds()

    if entries:
        # Sort entries by date, newest first
        entries.sort(key=lambda x: x['published_parsed'], reverse=True)

        print(f"\nSuccessfully fetched {len(entries)} entries.")
        print("\n--- Latest 5 Entries ---")
        for entry in entries[:5]:
            # Convert struct_time to a readable string
            published_str = time.strftime('%Y-%m-%d %H:%M:%S', entry['published_parsed'])
            print(f"Source: {entry['source']}")
            print(f"  Title: {entry['title']}")
            print(f"  Link: {entry['link']}")
            print(f"  Published: {published_str}")
            print("-" * 20)
    else:
        print("No entries found.")
