# BBC Türkçe Haber Scraper

A Python web scraper that collects news from BBC Türkçe and exports to Excel.

## Features
- Scrapes latest news from BBC Türkçe homepage
- Extracts title, link, and timestamp
- Removes duplicate articles
- Exports data to timestamped Excel file

## Technologies
- Python 3
- requests
- BeautifulSoup4
- openpyxl

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python scraper.py
```

## Output
Generates an Excel file: `bbc_haberler_YYYYMMDD_HHMM.xlsx`

| Başlık | Link | Tarih |
|--------|------|-------|
| Haber başlığı | https://bbc.com/turkce/... | 2026-07-04 21:00 |
