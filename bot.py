import os

import discord
from discord.ext import commands


# Setup
TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix="/")
console_channel = "bot-console"


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Symvasi RPG"))
    print(f"{bot.user} connected to Discord in those servers:")
    for guild in bot.guilds:
        print(guild.name)
        for channel in guild.channels:
            if channel.name == console_channel:
                await channel.send("Bot ready!")
                print("...with console!")


# Load Cogs
if __name__ == "__main__":
    for extension in [
        f.replace('.py', '') for f in os.listdir("cogs") if os.path.isfile(
            os.path.join("cogs", f)
        )
    ]:
        try:
            bot.load_extension("cogs" + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')


bot.run(TOKEN)
