import requests
import random

## Populating from URL so we don't have to make another network call. We should probably put this into a CSV to have it work as a DB.
dog_breeds_from_url = set()

def populate_breeds(dog_breeds_from_url):
    source = 'https://dog.ceo/api/breeds/list/all'

    response = requests.get(source)

    if response.status_code == 200:
        data = response.json()
        for dog in data['message']:
            dog_breeds_from_url.add(dog)


populate_breeds(dog_breeds_from_url)


## Function to select a dog at random from the set.
def select_random_dog():
    random_dog = random.choice(list(dog_breeds_from_url))
    return random_dog


random_dog = select_random_dog()


def get_random_dog_img(random_dog):
    source = f'https://dog.ceo/api/breed/{random_dog}/images/random'

    response = requests.get(source)

    if response.status_code == 200:
        data = response.json()
        if 'message' in data:
            dog_img = data['message']
            return dog_img
        else:
            return "Couldn't find img"


get_random_dog_img(random_dog)
