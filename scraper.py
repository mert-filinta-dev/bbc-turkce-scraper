import requests
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime


def scrape_bbc_turkce():
    url = "https://www.bbc.com/turkce"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    articles = []

    for item in soup.find_all("a", href=True):
        title = item.get_text(strip=True)
        link = item["href"]

        if not title or len(title) < 20:
            continue
        if "/turkce/" not in link:
            continue
        if not link.startswith("http"):
            link = "https://www.bbc.com" + link

        articles.append({
            "title": title,
            "link": link,
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    # Remove duplicates
    seen = set()
    unique_articles = []
    for a in articles:
        if a["link"] not in seen:
            seen.add(a["link"])
            unique_articles.append(a)

    # Save to Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "BBC Türkçe Haberler"
    ws.append(["Başlık", "Link", "Tarih"])

    for article in unique_articles:
        ws.append([article["title"], article["link"], article["scraped_at"]])

    filename = f"bbc_haberler_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
    wb.save(filename)

    print(f"{len(unique_articles)} haber bulundu.")
    print(f"Kaydedildi: {filename}")


if __name__ == "__main__":
    scrape_bbc_turkce()
