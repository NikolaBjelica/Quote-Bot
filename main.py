import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

# Load in token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up Bot
intents = Intents.default()
intents.message_content = True
client = Client(intents = intents)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty was intents were not enabled probably)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response = get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Handling Startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling Incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# Main Entry Point
def main() -> None:
    client.run(token = TOKEN)

if __name__ == '__main__':
    main()