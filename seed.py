import os
import django
import requests
import random
from faker import Faker
fake = Faker(['it_IT', 'en_US', 'ja_JP'])



# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HunterPrime.settings')
django.setup()

from rewardPrime.models import Character, Bounty, Location, Hunter, ClaimBounty
from rewardPrime.constants import Currency, SearchStatus

class URLS():
    CHARACTERS = 'https://rickandmortyapi.com/api/character'
    LOCATIONS = 'https://rickandmortyapi.com/api/location'

def fetch_characters():
    url = URLS.CHARACTERS
    characters = []

    while url:
        response = requests.get(url)
        data = response.json()
        characters.extend(data['results'])
        url = data['info']['next']

    return characters

def fetch_locations():
    url = URLS.LOCATIONS
    locations = []

    while url:
        response = requests.get(url)
        data = response.json()
        locations.extend(data['results'])
        url = data['info']['next']

    return locations

def populate_characters():
    characters = fetch_characters()

    for char in characters:
        character = Character.objects.get_or_create(
            name=char['name'],
            status=char['status'],
            species=char['species'],
            gender=char['gender'],
            origin=char['origin']['name'],
            last_location=char['location']['name'],
            image=char['image']
        )
    print("Database characters population completed.")

def populate_locations():
    locations = fetch_locations()
    
    for location in locations:
        location = Location.objects.get_or_create(
            name=location['name'],
            type_location=location['type'],
            dimension=location['dimension']
        )
    print("Database locations population completed.")

def populate_bounties():
    target_characters = Character.objects.all()

    currency_choices = list(Currency.choices)
    search_choices = list(SearchStatus.choices)

    for character in target_characters:
        amount = round(random.uniform(1000.00, 10000000.00), 2)
        currency_type = random.choice(currency_choices)[0]
        search_status = random.choice(search_choices)[0]

        bounty = Bounty.objects.get_or_create(
            title = character,
            character_id=character,
            search_status=search_status,
            description="Find and capture this character!",
            amount=amount,
            currency_type=currency_type
        )

def populate_hunters():
    characters = fetch_characters()

    for char in characters:
        if char['id'] % 3 == 0 or char['id'] % 5 == 0:
            Hunter.objects.get_or_create(
                name=char['name'],
                nickname=fake.name(),
                image=char['image'],
                skill = fake.paragraph()
            )
    print("Database hunters population completed.")


if __name__ == "__main__":
    populate_characters()
    populate_locations()
    populate_bounties()
    populate_hunters()
    print("Database population completed.")