import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'

def Main():
    input('Press ENTER to start the IMDB TOP 250 Random Movie Picker')
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movie_tags = soup.select("td.titleColumn")
    inner_movietags = soup.select("td.titleColumn a")
    rating_tag = soup.select('td.ratingColumn strong')

##    for testing purposes:
##    movietag0 = movie_tags[0]
##    print(movietag0)

    def Years(movie_tags):
        movie_split = movie_tags.text.split()
        years = movie_split[-1]
        return years

    movie_list = [tag.text.rstrip() for tag in inner_movietags]
    director_list = [tag['title'].split('(dir.), ')[0] for tag in inner_movietags]
    actors_list = [tag['title'].split('(dir.), ')[1] for tag in inner_movietags]
    years_list = [Years(tag) for tag in movie_tags]
    rating_list = [tag.text for tag in rating_tag]

    total_movie_number = len(inner_movietags)
    index = random.randrange(0, total_movie_number)

    while True:
        print(f"""
{movie_list[index]} {years_list[index]}.
The movie is rated {rating_list[index]}/10 and currently positioned #{index}.
Starring: {actors_list[index]} and directed by {director_list[index]}.
""")
        user_input = input('Do you want another pick? y/n')
        while user_input != 'y' and user_input != 'n':
            user_input = input('Only y/n values are expected. Do you want another pick? y/n')
        if user_input == 'y':
            continue
        elif user_input == 'n':
            print('Thank you for using IMDB TOP 250 Random Movie Picker. Bye!')
            break

if __name__ == '__main__':
    Main()
