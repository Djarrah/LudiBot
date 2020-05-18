import os

import discord
from discord.ext import commands
from discord.utils import get


# Setup and constants
TOKEN = os.environ["TOKEN"]
bot = commands.Bot(command_prefix="/")
CONSOLE_CHANNEL = "bot-console"
WELCOME_ROLE = "Masquerader"
GAME = "Umbreal"
WELCOME_MSG = '''Hello and Welcome to the Ludi Personis Server!
A place to organize, participate and discuss your favorite Role Playing Games, Board Games and also other stuff!
There are few #rules here, and most fall under common sense, but check them out anyway.

Looking for a game or for players to your game? Post in one of the channels in the Organization group.
Do you want to discuss specific RPGs? Use the Game Discussions' channels.
Do you simply want to chill? We got General Topics' channels for that.
There are also channel sections for specific, server-organized games sometimes: check them out if you are interested.

When you joined the server you also got the Masquerader role: this is used for important server-wide communications or events, but you can opt out of it if you want. Just type /masquerader in one of the server's channels (we have a #command-room to prevent cluttering) and if you change your mind, do the same to get your role back!
Other roles you can get or remove yourself are:
The Available role (/available) to signal you are available for future games and receive pings by organizers.
The Organizer role (/organizer) to post in the organization channels.
The Streamfan role (/streamfan) to be notified when a server-themed stream is happening (Yes, we have those sometimes, and you can stream too if you want!).

Check the #faq channel for any doubt you could have, and if you still got them don't hesitate to ask in #general or even a Staff member.
Now, go introduce yourself if you want, and don't forget to have fun!'''


# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(GAME))

@bot.event
async def on_member_join(member):
    role = get(member.guild.roles, name=WELCOME_ROLE)
    await member.add_roles(role)
    await member.send(WELCOME_MSG)

@bot.event
async def on_member_remove(member):
    console = get(member.guild.channels, name=CONSOLE_CHANNEL)
    await console.send(f"{member.name} left the server :(")


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
