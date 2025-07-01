# 🔍 Reddit Job Scraper

This project is a simple, beginner-friendly Python scraper that uses the Reddit API to search for job-related posts in specific subreddits and stores them in a local MongoDB database.

---

## 🚀 What It Does

- Connects securely to Reddit using Reddit's official API via `PRAW`
- Searches for keywords like `job`, `internship`, or `freelance` in a chosen subreddit (e.g. r/forhire, r/jobs)
- Collects post details: title, link, date, score, and post ID
- Saves the scraped data to MongoDB using `PyMongo`

---

## 🧰 Technologies Used

- **Python 3**
- **PRAW** – Python Reddit API Wrapper
- **PyMongo** – For storing posts in MongoDB
- **MongoDB** – Local database to store scraped content
- **dotenv** – Loads API credentials securely from `.env` file

---

## 📦 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/PJAdino/reddit-job-scraper.git
cd reddit-job-scraper
