import discord
from discord.ext import commands
import json

config_path = r"YourDirectory(json)"
with open(config_path, encoding='utf-8') as f:
    config = json.load(f)

TOKEN = config['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        await bot.load_extension('cogs.downloader')
        print("Downloader cog loaded!")
        await bot.load_extension('cogs.ping')
        print("Ping loaded!")
    except Exception as e:
        print(f"Failed to load cogs.downloader: {e}")

# main
bot.run(TOKEN)
