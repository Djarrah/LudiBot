import os

import discord
from discord.ext import commands
from discord.utils import get


# Setup and constants
TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix="/")
CONSOLE_CHANNEL = "bot-console"
WELCOME_ROLE = "Masquerader"
GAME = "The Faded City RPG"


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(GAME))
    print(f"{bot.user} connected to Discord in those servers:")
    for guild in bot.guilds:
        print(guild.name)
        for channel in guild.channels:
            if channel.name == CONSOLE_CHANNEL:
                await channel.send("Bot ready!")
                print("...with console!")

@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name=WELCOME_ROLE)
    await member.add_roles(role)
    print(f"{member.name} joined the server {member.guild.name}")


@bot.event
async def on_member_remove(member):
    console = get(member.guild.channels, name=CONSOLE_CHANNEL)
    await console.send(f"{member.name} left the server :(")
    print(f"{member.name} left the {member.guild.name} server")


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
