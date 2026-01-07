# 📰 News Scraper
# By Kaushik 🚀

import requests
from bs4 import BeautifulSoup

def fetch_news():
    print("📰 Fetching latest headlines from BBC News...\n")

    URL = "https://www.bbc.com/news"
    response = requests.get(URL)

    if response.status_code != 200:
        print("⚠️ Failed to retrieve news!")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all("p")

    count = 0
    for h in headlines:
        title = h.get_text().strip()
        if title and len(title) > 20:  # Filter short tags
            count += 1
            print(f"{count}. 🗞️ {title}")
        if count >= 10:
            break

    print("\n✅ Top 10 news headlines fetched successfully!")

def main():
    print("🌍 Welcome to Python News Scraper 📰")
    fetch_news()

    while True:
        again = input("\n🔁 Fetch again? (y/n): ").lower()
        if again == 'y':
            fetch_news()
        else:
            print("👋 Goodbye, stay informed!")
            break

if __name__ == "__main__":
    main()
