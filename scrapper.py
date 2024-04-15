import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Read the Excel file
excel_file = "C:/Users/lenvo/Downloads/Scrapping Python Assigment- Flair Insights.xlsx"
sheet_name = 'Sheet1'
df = pd.read_excel(excel_file, sheet_name=sheet_name)


# Function to scrape data from a URL
def scrape_data(url):
    try:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract text
        text = soup.get_text()

        # Extract images
        images = [img['src'] for img in soup.find_all('img')]

        # Extract links
        links = [link['href'] for link in soup.find_all('a')]

        # Return the scraped data
        return {
            'url': url,
            'text': text,
            'images': images,
            'links': links
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None


# Scrape data for each URL in the Excel sheet
scraped_data = []
for index, row in df.iterrows():
    url = row[0]
    scraped_result = scrape_data(url)
    if scraped_result:
        scraped_data.append(scraped_result)

# Save the scraped data to CSV
csv_file = 'scraped_data.csv'
pd.DataFrame(scraped_data).to_csv(csv_file, index=False)

# Save the scraped data to JSON
json_file = 'scraped_data.json'
with open(json_file, 'w') as f:
    json.dump(scraped_data, f, indent=4)

print("Scraped data saved to CSV:", csv_file)
print("Scraped data saved to JSON:", json_file)
