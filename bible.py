import requests

def get_random_bible_verse():
    response = requests.get('https://bible-api.com/?random=verse')
    if response.status_code == 200:
        verse = response.json()
        return f"{verse['reference']}: {verse['text']}"
    else:
        return "Error: Could not retrieve verse."

