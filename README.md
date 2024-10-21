# Project Part 2 for CS325" 

## Overview

In this project, we focused on scraping product reviews from an e-commerce website for a specific product of our choice. The objective was to gather reviews from various generations of the PlayStation console.

## Installation

To run this project, you only need to set up the environment using the requirements.yaml file. Ensure you have a working browser, as this is necessary for the web scraping process. No additional installations are required.

## Product

I chose to scrape reviews for PlayStation consoles, ranging from the PlayStation 2 to the PlayStation 5. This decision was made due to the abundance of available reviews and the widespread familiarity with PlayStation among consumers.

## Website

For scraping, I selected eBay as the target website. Initially, I attempted to scrape Amazon; however, their robust security measures hindered my efforts. After several unsuccessful attempts, I transitioned to eBay, where I encountered some challenges but ultimately found a way to navigate them. This allowed me to successfully access a wealth of reviews for the selected products.

## Key Code Components

This project utilizes the BeautifulSoup and requests libraries for web scraping. I chose these libraries due to their user-friendly documentation and the availability of numerous examples for web scraping on the internet.

### Scraping Mechanism

In my implementation, I provide a single URL for each PlayStation generation, and the scraper utilizes BeautifulSoup to navigate through the various pages of reviews. This approach eliminates the need for a large urls.txt file, simplifying the process. I opted for this method to minimize the manual effort of collecting individual URLs.

## Conclusion

This project successfully demonstrates the application of web scraping techniques to gather product reviews from an e-commerce platform. The choice of eBay allowed for a rich dataset of user opinions, which can be valuable for market analysis and consumer insights.



