from discord.ext import commands
from discord.utils import get


class Roles(commands.Cog):
    "Self-roles and other related commands"

    def __init__(self, bot):
        self.bot = bot


    @commands.command(hidden=True)
    @commands.guild_only()
    async def dontplay(self, ctx):
        role = get(ctx.guild.roles, name="Player")
        member = ctx.author
        if role in member.roles:
            await ctx.message.delete()
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} won the game!")


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


    @commands.command(help="Add or remove the Streamfan role from yourself")
    @commands.guild_only()
    async def streamfan(self, ctx):
        try:
            role = get(ctx.guild.roles, name="Streamfan")
            member = ctx.author
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(
                    f"You are no longer listed as Streamfan, {member.mention}!"
                )
                print(f"Streamfan role removed from {member.name}")
            else:
                await member.add_roles(role)
                await ctx.send(
                    f"You are now listed as Streamfan, {member.mention}!"
                )
                print(f"Streamfan role added to {member.name}")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(help="Add or remove the Masquerader role from yourself")
    @commands.guild_only()
    async def masquerader(self, ctx):
        try:
            role = get(ctx.guild.roles, name="Masquerader")
            member = ctx.author
            if role in member.roles:
                await member.remove_roles(role)
                await ctx.send(
                    f"You are no longer listed as Masquerader, {member.mention}!"
                )
                print(f"Masquerader role removed from {member.name}")
            else:
                await member.add_roles(role)
                await ctx.send(
                    f"You are now listed as Masquerader, {member.mention}!"
                )
                print(f"Masquerader role added to {member.name}")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(
        help="Give/Take a Game Role if you are the Organizer of that Game",
        aliases=["take"]
    )
    @commands.guild_only()
    async def give(
        self, ctx,
        target: commands.MemberConverter,
        role: commands.RoleConverter
    ):
        try:
            orgrole = get(ctx.guild.roles, name=role.name + "Organizer")
            if orgrole in ctx.author.roles:
                if not role in target.roles:
                    await target.add_roles(role)
                    message = f"{role.name} added to {target.name}"
                else:
                    await target.remove_roles(role)
                    message = f"{role.name} removed from {target.name}"
                message += f" by {ctx.author.name}"
                await ctx.send(message)
                print(message)
            else:
                await ctx.send("You don't have permissions for this role")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(
        help="Sends you a list of members for a role via DM",
        aliases=["rlist"]
    )
    @commands.guild_only()
    async def rolelist(self, ctx, role: commands.RoleConverter):
        try:
            message = f"List of members for {role.name}:"
            for m in role.members:
                message += f"\n{m.name}"
            await ctx.author.send(message)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


def setup(bot):
    bot.add_cog(Roles(bot))
