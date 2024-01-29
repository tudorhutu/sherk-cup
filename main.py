
import os
from discord import Intents, Client, Message
from responses import get_response
from reactions import get_reaction

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
NOT_A_TOKEN='MTIwMTU4NzM1MDE0O'
BROKEN='TUzMzg0Ng.GTY47Q.4jillLkb5i5Bp1cUHb5rOS4E4M0xUQ303TBFsg'
TOKEN = NOT_A_TOKEN+BROKEN

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message,str(message.author))
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
# REACTION FUNCTIONALITY
async def add_reaction(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_reaction(user_message,str(message.author))
        if response:
            for i in response:
                await message.add_reaction(i) if is_private else await message.add_reaction(i)
    except Exception as e:
        print(e)

# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    await add_reaction(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()