from discord.ext import commands


class Owner(commands.Cog):
    "Just for Djarrah's eyes"

    def __init__(self, bot):
        self.bot = bot


    @commands.command(help="unloads a cog", hidden=True, aliases=["unload"])
    @commands.is_owner()
    async def unload_cog(self, ctx, cogname: str):
        try:
            cog = "cogs." + cogname
            self.bot.unload_extension(cog)
            await ctx.send(f"{cogname} commands disabled")
            print(f"{cogname} commands disabled")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(help="loads a cog", hidden=True, aliases=["load"])
    @commands.is_owner()
    async def load_cog(self, ctx, cogname: str):
        try:
            cog = "cogs." + cogname
            self.bot.load_extension(cog)
            await ctx.send(f"{cogname} commands enabled")
            print(f"{cogname} commands enabled")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(help="reloads a cog", hidden=True, aliases=["reload"])
    @commands.is_owner()
    async def reload_cog(self, ctx, cogname: str):
        try:
            cog = "cogs." + cogname
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send(f"{cogname} commands reloaded")
            print(f"{cogname} commands reloaded")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


def setup(bot):
    bot.add_cog(Owner(bot))
