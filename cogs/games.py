from random import randint, choice

from discord.ext import commands

from .utils.cards import Deck


class Games(commands.Cog):
    "Rolling dices and other chance commands"

    def __init__(self, bot):
        self.bot = bot
        self.decks = {}


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


    @commands.command(help="Pick a card. Shuffles the deck after")
    async def card(self, ctx):
        tag = ctx.author.mention
        suit = choice(["Hearts", "Spades", "Clubs", "Diamonds"])
        value = choice(["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"])
        joker = randint(1, 27)
        if joker == 27:
            color = choice(["Red", "Black"])
            message = f"You picked the {color} joker, {tag}!"
        else:
            message = f"You picked the {value} of {suit}, {tag}!"
        await ctx.send(message)


    @commands.command(
        help="Draw a card from your deck. Shuffles the deck if empty"
    )
    async def draw(self, ctx):
        try:
            user = ctx.author.id
            if not user in self.decks:
                self.decks[user] = Deck()
                print(f"Deck created for {ctx.author.name}")
            card = self.decks[user].draw()
            message = f"You drew the {card}, {ctx.author.mention}"
            if self.decks[user].isempty():
                self.decks[user] = Deck()
                message += "\nDeck emptied, shuffling..."
                print(f"{ctx.author.name}'s deck has been shuffled")
            await ctx.send(message)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(help="Shuffles back all cards in your deck")
    async def shuffle(self, ctx):
        try:
            self.decks[ctx.author.id] = Deck()
            await ctx.send(
                f"Shuffled all cards back in your deck, {ctx.author.mention}"
            )
            print(f"{ctx.author.name}'s deck has been shuffled")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(help="Draws a Major Arcana")
    async def tarot(self, ctx):
        try:
            arcana = choice([
                "The Fool",
                "The Magician",
                "The High Priestess",
                "The Empress",
                "The Emperor",
                "The Hierofant",
                "The Lovers",
                "The Chariot",
                "Strength",
                "The Hermit",
                "Wheel of Fortune",
                "Justice",
                "The Hanged Man",
                "Death",
                "Temperance",
                "The Devil",
                "The Tower",
                "The Star",
                "The Moon",
                "The Sun",
                "Judgment",
                "The World"
            ])
            await ctx.send(f"{ctx.author.mention} {arcana}")
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")


    @commands.command(
        usage="[number of d20s]+[bonus] Ex: /sab 3+5"
    )
    async def sab(self, ctx, *args):
        "Souls & Blood dice roller"

        # Formula splitting
        command = "".join(args)
        parts = command.split("+")
        dice = int(parts[0])
        mod = int(parts[1])

        # Rolls list
        mess = f"{ctx.author.mention} Rolls: "
        rolls = []
        for d in range(dice):
            t = randint(1, 20)
            rolls.append(t)
            mess+=f"{t} "

        # Doubles control
        unique = set()
        doubles = []
        for t in rolls:
            if t in unique:
                if not (t in doubles):
                    doubles.append(t)
                doubles.append(t)
            else:
                unique.add(t)
        doubles_sum = sum(doubles)

        # Results check
        res = max(max(rolls), doubles_sum)
        mess+=f"\nDice result: {res}"
        mess+=f"\nTotal result: {res+mod}"
        await ctx.send(mess)



    # To do: additive dice rolls


def setup(bot):
    bot.add_cog(Games(bot))
