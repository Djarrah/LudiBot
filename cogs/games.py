from random import randint, choice

from discord.ext import commands


class Games(commands.Cog):
    "Rolling dices and other chance commands"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=["r"],
        help="Simple dice roller",
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

    @commands.command(
        help="Pick a card. Shuffles the deck after"
    )
    async def card(self, ctx):
        tag = ctx.author.mention
        suit = choice(["hearts", "spades", "clubs", "diamonds"])
        value = choice(["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])
        joker = randint(1, 27)
        if joker == 27:
            color = choice(["red", "black"])
            message = f"You picked the {color} joker, {tag}!"
        else:
            message = f"You picked the {value} of {suit}, {tag}!"
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Games(bot))
