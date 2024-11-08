import requests
from bs4 import BeautifulSoup
import schedule
import time

# URL of the webpage to scrape
base_url = 'https://crex.live'
fixtures_url = f'{base_url}/fixtures/match-list'

def save_html(contents, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(contents)

def scrape_match_details(match_url):
    # Make request to the match URL
    response = requests.get(f'{base_url}{match_url}')

    if response.status_code != 200:
        print(f'Failed to retrieve the match details from {match_url}')
        return

    # Parse the match details page
    soup = BeautifulSoup(response.text, 'html.parser')
    match_details_content = soup.prettify()

    # Saving the scraped details
    filename = match_url.strip('/').replace('/', '_') + '.html'
    save_html(match_details_content, filename)
    print(f'Match details saved as {filename}')

def scrape_and_monitor():
    # Send a HTTP request to the URL
    response = requests.get(fixtures_url)

    if response.status_code != 200:
        print('Failed to retrieve the webpage.')
        return

    # Parsing the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Saving the main fixtures page
    save_html(soup.prettify(), 'fixtures_page.html')

    # Finding all upcoming match URLs
    match_urls = []
    for match_card in soup.select('a.match-card-wrapper'):
        match_url = match_card.get('href')
        if match_url:
            match_urls.append(match_url)

    # Scraping details for each match
    for match_url in match_urls:
        scrape_match_details(match_url)

# Schedule to run the scraper at the desired intervals
schedule.every(1).hours.do(scrape_and_monitor)

# Initial run
scrape_and_monitor()

# Keeping the script running to execute scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)