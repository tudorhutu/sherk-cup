from discord import Intents, Client, Message
from random import  randint
from import_emijos import *
import random

def get_reaction(user_input: str,user_name) -> str:
    lowered: str = user_input.lower()
    if 'react to this message with literally all emojis' == lowered:
        random_emojis = random.sample(list(emojilist), 20)
        return random_emojis
    else:
        emmojichance = randint(1, 100)
        if emmojichance > 85:
            random_emoji = random.sample(list(emojilist), 1)
            return random_emoji