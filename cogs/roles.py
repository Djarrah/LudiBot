from discord.ext import commands
from discord.utils import get


class Roles(commands.Cog):
    "Self-roles and other related commands"

    def __init__(self, bot):
        self.bot = bot


    @commands.command(help="Add or remove the Available role from yourself")
    @commands.guild_only()
    async def available(self, ctx):
        try:
            role = get(ctx.guild.roles, name="Available")
            member = ctx.author
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(
                    f"You are no longer listed as Available, {member.mention}!"
                )
                print(f"Available role removed from {member.name}")
            else:
                await member.add_roles(role)
                await ctx.send(
                    f"You are now listed as Available, {member.mention}!"
                )
                print(f"Available role added to {member.name}")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(help="Add or remove the Organizer role from yourself")
    @commands.guild_only()
    async def organizer(self, ctx):
        try:
            role = get(ctx.guild.roles, name="Organizer")
            member = ctx.author
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(
                    f"You are no longer listed as Organizer, {member.mention}!"
                )
                print(f"Organizer role removed from {member.name}")
            else:
                await member.add_roles(role)
                await ctx.send(
                    f"You are now listed as Organizer, {member.mention}!"
                )
                print(f"Organizer role added to {member.name}")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    '''
    Temp command until i figure a simpler way to let Game Organizers
    hand out their Game's Role, like reaction to posts
    '''
    @commands.command(help="Add or remove the Faded City role from yourself")
    @commands.guild_only()
    async def fadedcity(self, ctx):
        try:
            role = get(ctx.guild.roles, name="Faded City")
            member = ctx.author
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(
                    f"You are no longer listed as Faded City, {member.mention}!"
                )
                print(f"Faded City role removed from {member.name}")
            else:
                await member.add_roles(role)
                await ctx.send(
                    f"You are now listed as Faded City, {member.mention}!"
                )
                print(f"Faded City role added to {member.name}")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


def setup(bot):
    bot.add_cog(Roles(bot))
