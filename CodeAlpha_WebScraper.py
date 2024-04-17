import requests
from bs4 import BeautifulSoup

def quotes():
    url = 'https://quotes.toscrape.com/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        print("Quotes of the day: \n" )
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = quote.find_all('a', class_='tag')
            tag_list = [tag.text for tag in tags]
            
            print(f"Quote: {text}")
            print(f"Author: {author}")
            print(f"Tags: {', '.join(tag_list)}")
            print("\n")
    else:
        print("Failed to fetch the website.")

if __name__ == "__main__":
    quotes()