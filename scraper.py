import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://crex.live/fixtures/match-list'

# Send a HTTP request to the URL
response = requests.get(url)

# Ensure we got a successful response
if response.status_code == 200:
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the page's HTML content
    page_content = soup.prettify()

    # Define the name of the output file
    output_file = 'scraped_page.html'

    # Open the file in write mode and save the content
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(page_content)

    print(f"Webpage content has been saved to {output_file}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")