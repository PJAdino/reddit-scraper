import os
from dotenv import load_dotenv
import praw
from pymongo import MongoClient



# Step 1: Load environment variables
load_dotenv()

# Step 2: Connect to Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# Step 3: Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["reddit_scraper"]         # Database name
collection = db["posts"]     #collection name

# Step 4: Define what and where to search
subreddit = reddit.subreddit("jobs")        # Choose subreddit
search_query = "sidegig"                     # Keyword to search

# Step 5: Search posts
for post in subreddit.search(search_query, sort="new", limit=10):
    data = {
        "title": post.title,
        "content":post.selftext,
        "url": post.url,
        "score": post.score,
        "created_utc": post.created_utc,
        "id": post.id,
        "subreddit": post.subreddit.display_name
    }

# Step 6: Save to MongoDB
    collection.update_one({"id": post.id}, {"$set": data}, upsert=True)

print("✅ Scraping complete. Data stored in MongoDB.")    