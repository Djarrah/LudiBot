from os import getenv

from discord.ext import commands
from dotenv import load_dotenv


# Setup
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="/")

# Events
@bot.event
async def on_ready():
    print(f'{bot.user} connected to discord')


if __name__ == "__main__":
    bot.run(TOKEN)
