# Python Web Scraping Script

This Python script scrapes data from URLs listed in an Excel file, extracting text, images, and links using BeautifulSoup and pandas libraries.

## Setup

1. **Dependencies:**
    - pandas
    - requests
    - BeautifulSoup

2. **Installation:**
    ```bash
    pip install pandas requests beautifulsoup4
    ```

3. **Usage:**
    - Ensure the Excel file path is correctly set in the script.
    - Run the script.

## Code Explanation

- The script reads an Excel file containing URLs.
- For each URL, it scrapes the HTML content using BeautifulSoup.
- It extracts text, images, and links from the HTML.
- Scraped data is stored in a list of dictionaries.
- Finally, the script saves the scraped data to both CSV and JSON formats.

## Files

- `scrape.py`: The main Python script.
- `Scrapping Python Assigment- Flair Insights.xlsx`: Sample Excel file containing URLs.
- `scraped_data.csv`: Output CSV file containing scraped data.
- `scraped_data.json`: Output JSON file containing scraped data.

## Execution

```bash
python scrape.py
