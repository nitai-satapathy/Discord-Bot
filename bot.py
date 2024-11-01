import discord
import aiohttp
import datetime
import pytz
from jokes import get_joke, get_compliment

timezone = pytz.timezone('Asia/Kolkata')
# Fetch meme asynchronously
async def get_meme():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme') as response:
            if response.status != 200:
                print(f"Error fetching meme: {response.status}")
                return "Could not fetch meme."
            json_data = await response.json()
            return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Define available commands
        available_commands = [
            "meme",
            "hello",
            "joke",
            "compliment",
            "help",
            "bye",
            "status",
            "poll",
            "$serverinfo",
            "userinfo",
            "time"
        ]
        

        # Check for specific commands
        if message.content.startswith('meme'):
            meme_url = await get_meme()
            await message.channel.send(meme_url)
        elif message.content.startswith('hello'):
            await message.channel.send(f'Hello {message.author}!')
        elif message.content.startswith('joke'):
            await message.channel.send(get_joke())
        elif message.content.startswith('help'):
            await message.channel.send("Available commands: " + ", ".join(available_commands))
        elif message.content.startswith('bye'):
            await message.channel.send(f'Goodbye {message.author}, see you next time!')
        elif message.content.startswith('👍'):
            await message.channel.send("Glad you liked it!")
        elif message.content.startswith('compliment'):
            await message.channel.send(get_compliment())
        elif message.content.startswith('status'):
            await message.channel.send(f'{message.author}, the bot is running smoothly!')
        elif message.content.startswith('serverinfo'):
            server = message.guild
            region = server.preferred_region if hasattr(server, 'preferred_region') else "Region info not available"
            await message.channel.send(f'Server Name: {server.name}\nMember Count: {server.member_count}\nRegion: {region}')
        elif message.content.startswith('userinfo'):
            user = message.author
            await message.channel.send(f'Username: {user.name}\nID: {user.id}\nJoined: {user.joined_at}')
        elif message.content.startswith('time'):
            current_time = datetime.datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S %Z')
            await message.channel.send(f'Current time: {current_time}')
        else:
            await message.channel.send(f"Hey {message.author}, this command is not found. Available commands:\n" + "\n".join(f"• {cmd}" for cmd in available_commands))

# Create intents keyword argument
intents = discord.Intents.default()
intents.message_content = True

# Create the client with intents
client = MyClient(intents=intents)

#bot token
client.run('token')
