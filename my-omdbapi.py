import requests
import os

movie_title = input('What movie we want know Rotten Tomatoes rating?\n')
api_key = os.environ['python_api']
URL = 'http://www.omdbapi.com/?apikey='
api_url = URL + api_key + '&t=' + movie_title
response = requests.get(api_url).json()
result = response.get('Ratings')
rating=''

if response['Response'] == 'False':
    print(f"🔴 Movie {movie_title} not found!")
    exit()

for d in result:
    for k, v in d.items():
        if v == 'Rotten Tomatoes':
            rating = d['Value']
            
if rating != '':
    print(f"🟢 Rotten Tomatoes rating of the movie {movie_title} is \033[95m\033[1m{rating}\033[0m")
else:
    print(f"🟡 Cant find Rotten Tomatoes rating for {movie_title}")
