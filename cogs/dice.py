from random import randint

from discord.ext import commands


class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=["r"],
        help="Simple dice roller, returns single dices, their sum and the highest number rolled",
        usage="roll|r [number of dices]d[dice size]"
    )
    async def roll(self, ctx, arg):
        try:
            args = arg.split("d")
            roll = []
            for i in args:
                roll.append(int(i))
            results = []
            for d in range(roll[0]):
                results.append(randint(1, roll[1]))
            message = f"Sum: {sum(results)}, Highest: {max(results)} \nValues:"
            for i in results:
                message += f" {i}"
            message += f"\n{ctx.author.mention}"
        except Exception as e:
            message = "Invalid format"
        await ctx.send(message)


def setup(bot):
    bot.add_cog(DiceCog(bot))
