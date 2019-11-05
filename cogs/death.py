from random import choice

from discord.ext import commands


class Death(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.deaths = [
            "{} stumbled and accidentally stabbed themselves to death",
            "{} had a stroke while on the toilet",
            "{} drowned in shallow waters",
            "{} was run over by a toy car",
            "{} fell off a lego block and died",
            "{} spoke the wrong name three times before the mirror",
            "{} picked up the phone booth and died"
        ]
        self.kills = [
            "{} stabbed {} 28 times, just to be sure",
            "{} spiked {}'s protein shake with arsenic",
            "{} booped {} gently on the aorta",
        ]


    @commands.command(help="Stab someone")
    @commands.guild_only()
    async def stab(self, ctx, victim):
        await ctx.send(f"{victim} was stabbed by {ctx.author.display_name}!")


    @commands.command(help="Die a horribly ridiculous death")
    @commands.guild_only()
    async def die(self, ctx):
        message = choice(self.deaths).format(ctx.author.display_name)
        await ctx.send(message)


    @commands.command(help="Kill someone in a random way")
    @commands.guild_only()
    async def kill(self, ctx, victim):
        message = choice(self.kills).format(ctx.author.display_name, victim)
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Death(bot))
