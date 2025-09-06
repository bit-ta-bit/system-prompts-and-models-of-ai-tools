from flask import Flask, render_template, jsonify
from feed_fetcher import fetch_feeds
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/feed')
def api_feed():
    """
    API endpoint to get the combined and sorted feed data.
    """
    # Fetch entries from all feeds
    entries = fetch_feeds()

    # Sort entries by date, newest first
    entries.sort(key=lambda x: x['published_parsed'], reverse=True)

    # Convert time.struct_time to a serializable string format
    for entry in entries:
        entry['published'] = time.strftime('%Y-%m-%d %H:%M:%S', entry['published_parsed'])
        del entry['published_parsed'] # Remove the non-serializable object

    return jsonify(entries)

if __name__ == '__main__':
    app.run(debug=True)
