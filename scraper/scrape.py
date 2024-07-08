import requests
from bs4 import BeautifulSoup
from scraper.models import Algorithm

def scrape_algorithms():
    url = 'https://www.mayocliniclabs.com/articles/resources/algorithms'



    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust based on the actual structure of the webpage
    algorithm_items = soup.find_all('div', class_='algorithm-list')

    for item in algorithm_items:
        title = item.find('div').text.strip()
        link = item.find('a')['href']
        description = item.find('li').text.strip()

        # Save to the database
        algorithm, created = Algorithm.objects.get_or_create(
            title=title,
            defaults={'url': link, 'description': description},
        )
        if not created:
            algorithm.url = link
            algorithm.description = description
            algorithm.save()




