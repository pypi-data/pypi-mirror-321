# Arı WebScraper

This is simple web scraping library that can be used to scrape data from websites. It is built using Python and BeautifulSoup.

## Installation
Standard:
```bash
pip install ariwebscraper
```
Jupyter Notebook:
```bash
!pip install ariwebscraper
```

## Usage
```python
from webscraper import Scraper

scraper = Scraper()
url = "https://www.example.com"
html = scraper.fetch(url)

if html:
    data = scraper.extract(html, "h1")
    print("Extracted: ", data)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
```
MIT License
Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
```