from random import choice, randint, sample
import re
from import_emijos import *
from scrape import *


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
        elif 'weed' in lowered:
            weedchane = randint(1,1000)
            if weedchane > 977:
                return 'weed'
        elif lowered == 'mansplain':
            return scrape_random_wiki_article()
        elif find_ips(lowered):
              return '[Imgur](https://imgur.com/kyo6sPn)'
        else:
            ipchance = randint(1,1000)
            if ipchance > 995:
                return user_name +' your ip address is '+generate_random_ip()+' I am inside your walls'
        