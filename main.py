
import os
from discord import Intents, Client, Message
from responses import get_response
from reactions import get_reaction
import sys
import git 
import asyncio

dir_path = os.path.dirname(os.path.realpath(__file__))
g = git.cmd.Git(dir_path)
g.pull()
# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
TOKEN =  str(sys.argv[1])
print (TOKEN)
# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)
message_to_edit=''
need_to_edit=False

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    global message_to_edit,need_to_edit
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message,str(message.author))
        if '☃' in response:
            response=response.replace("☃",'', 1)
            need_to_edit=True 
        if response:
           message_to_edit = await message.author.send(response) if is_private else await message.channel.send(response)
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
    global message_to_edit,need_to_edit
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    if message.author == client.user:
        return    
  
    await send_message(message, user_message)
    await asyncio.sleep(1)
    i=1
    while need_to_edit:
        await message_to_edit.edit(content=str(i)) # Edit it
        i+=1
        await asyncio.sleep(1)
    await add_reaction(message, user_message) 
          


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()