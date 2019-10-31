from discord.ext import commands


class Mod(commands.Cog):
    "Moderation commands"
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Deletes the last x messages from the channel.")
    @commands.has_role("Staff")
    async def clean(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)
        print(f"{amount} messages cleaned from {ctx.channel} in {ctx.guild}")


def setup(bot):
    bot.add_cog(Mod(bot))
