from discord.ext import commands


class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="unloads a cog", hidden=True, aliases=["unload"])
    @commands.is_owner()
    async def unload_cog(self, ctx, cogname: str):
        try:
            cog = "cogs." + cogname
            self.bot.unload_extension(cog)
            await ctx.send(f"{cogname} disabled")
            print(f"{cogname} disabled")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")

    @commands.command(help="loads a cog", hidden=True, aliases=["load"])
    @commands.is_owner()
    async def load_cog(self, ctx, cogname: str):
        try:
            cog = "cogs." + cogname
            self.bot.load_extension(cog)
            await ctx.send(f"{cogname} enabled")
            print(f"{cogname} enabled")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")

    @commands.command(help="reloads a cog", hidden=True, aliases=["reload"])
    @commands.is_owner()
    async def reload_cog(self, ctx, cogname: str):
        try:
            cog = "cogs." + cogname
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send(f"{cogname} reloaded")
            print(f"{cogname} reloaded")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
