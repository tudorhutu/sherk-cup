from random import choice, randint, sample
import re
from import_emijos import *
from scrape import *
from translate import *
from bible import *
import nltk
from nltk.corpus import words, brown
from nltk.probability import FreqDist

def generate_string():
    # nltk.download('brown')
    english_words = brown.words()
    selected_words = random.sample(list(set(english_words)), randint(1, 50))
    return ' '.join(selected_words)

def find_ips(message):
    pattern = re.compile(
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
        r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    )
    return pattern.findall(message)

def generate_random_ip():
        return ".".join(str(randint(0, 255)) for _ in range(4))

def check_string(s):
        pattern = r'^https.*gif'
        if re.search(pattern, s):
                return True
        else:
                return False

def add_line_to_file(file_path, line):
    with open(file_path, 'a') as file:
        file.write(line + '\n')

adding_car = False
car_to_add = ''

def get_response(user_input: str,user_name) -> str:
        global adding_car, car_to_add
        lowered: str = user_input.lower()
        if lowered == 'antidisestablishmentarianism':
            return 'muie'
        if 'weed' in lowered:
            weedchane = randint(1,1000)
            if weedchane > 977:
                return 'weed'
        if 'mansplain' in lowered:
            return scrape_random_wiki_article()
        if find_ips(lowered):
            return '[Imgur](https://imgur.com/kyo6sPn)'
        if lowered.startswith('translate'):
            lowered = lowered.replace("translate",'', 1)
            return translate_to_greek(lowered)
        if 'bless me' in lowered:
            return get_random_bible_verse()
        if 'talk to god' in lowered:
            return generate_string()
        if '7' in lowered:
             return '7'
        if 'sapte' in lowered:
             return 'sapte'
        if 'pacanele' in lowered:
             return ''.join(random.sample(list(emojilist), 3))
        else:
            ipchance = randint(1,1000)
            if ipchance > 995:
                return user_name +' your ip address is '+generate_random_ip()+' I am inside your walls'
        
