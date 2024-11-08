In order to execute the periodic scraping logic please execute


```bash
python3 data_scraper.py
```

### 1. Why did you choose the specific scraping approach you used?

The scraping approach was chosen to ensure that we retrieve and effectively manage the data from a dynamic webpage like the one at https://crex.live/fixtures/match-list. The approach involves:

* Requests and BeautifulSoup: These libraries are powerful and easy to use for making HTTP requests and parsing HTML content.
* Modular Functions: Separation of concerns is maintained by creating modular functions (save_html, scrape_match_details, scrape_and_monitor). This improves readability and maintainability.
* Scheduling Library: By using the schedule library, the script can run at intervals, automatically scraping data and monitoring the page without the need for manual intervention.

### 2. How can we further optimize the resource usage of your system?

Resource usage can be optimized through several strategies:

* Asynchronous Requests: Utilize asynchronous HTTP requests (via libraries such as aiohttp and asyncio) to make non-blocking calls, which can significantly reduce waiting times and improve overall performance.
* Incremental Updates: Instead of re-downloading the entire page on each scrape, use techniques to check for updates and only fetch and parse new or changed data.
* Resource Limits: Limit the number of concurrent requests to avoid overloading the server or your local machine's resources.
* Caching: Implement caching strategies to store recently fetched data, thereby reducing repetitive requests for unchanged data.

### 3. Can the time consumption of your codebase be further reduced?

Yes, time consumption can be further reduced by:

* Parallel Processing: Leveraging parallel processing (using libraries like concurrent.futures or multi-threading) to handle multiple requests simultaneously.
* Efficient Parsing: Optimize the parsing logic in BeautifulSoup or consider using more performant parsers if necessary.
* Asynchronous Handling: As mentioned, using asyncio and aiohttp for the HTTP requests to allow parallelism.
* Selective Scraping: Instead of scraping all match details every time, implement logic to check which matches have started or finished and only scrape those.


