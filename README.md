

# Goodreads Web Scraper

## Overview

This project involves scraping data from the "Best Books Ever" section of Goodreads.com using Scrapy. The spider collects information about 10,000 books, including their names, authors, votes, ratings, and average ratings. The scraped data is saved in a JSON file for further analysis and visualization using Python libraries.

## Features

- Scraped data from the "Best Books Ever" section of Goodreads.
- Collected the following information for each book:
  - Book Name
  - Author
  - Book Score
  - Book Votes
  - Book Ratings
  - Book Cover Link
- Data is stored in a structured JSON file.
- Visualized data using Jupyter Notebook with plots for insights.

## Technologies Used

- **Scrapy**: For web scraping.
- **Rotating User Agents**: To avoid being blocked while scraping.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib (plt)**: For creating visualizations.
- **Seaborn (sns)**: For enhanced visualizations.

## Spider Code

The main spider code is defined in `goodreads.py` as follows:

```python
import scrapy
from ..items import GoodreadItem

class GoodreadsSpider(scrapy.Spider):
    name = "goodreads"
    page_number = 2
    start_urls = ["https://www.goodreads.com/list/show/1.Best_Books_Ever"]

    def parse(self, response):
        items = GoodreadItem()

        book_name = response.css(".bookTitle span::text").extract()
        book_author = response.css(".authorName span::text").extract()
        book_score = response.css(".uitext a:nth-child(1)::text").extract()
        book_vote = response.css(".greyText+ a::text").extract()
        book_ratings = response.css(".minirating::text").extract()
        book_link = response.css(".bookCover::attr(src)").extract()

        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_score'] = book_score
        items['book_vote'] = book_vote
        items['book_ratings'] = book_ratings
        items['book_link'] = book_link

        yield items

        next_page = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page=" + str(GoodreadsSpider.page_number)
        
        if GoodreadsSpider.page_number <= 100:
            GoodreadsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devkverma/webscraing-goodreads.git
   cd webscraing-goodreads
   ```

2. Install the required packages:
   ```bash
   pip install scrapy pandas matplotlib seaborn
   ```

## Usage

1. **Run the Scrapy Spider**:
   To start the scraping process, navigate to the project directory and run the spider:
   ```bash
   scrapy crawl goodreads
   ```

2. **Visualize the Data**:
   Open the Jupyter Notebook:
   ```bash
   jupyter notebook visualization.ipynb
   ```
   In the notebook, you'll find various visualizations based on the scraped data.

## JSON Data Structure

The JSON file created during the scraping process contains a list of dictionaries, each representing a book with the following keys:
- `book_name`
- `author`
- `book_score`
- `book_vote`
- `book_ratings`
- `book_link`

## Conclusion

This project demonstrates the process of web scraping using Scrapy and the subsequent analysis of the collected data using Python's data visualization libraries. Feel free to explore and modify the code for your own data scraping and visualization projects!
