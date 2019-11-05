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
            "{} picked up the phone booth and died",
            "{} was eaten by a gazebo",
            "A piano fell from the sky, landing precisely on {}’s head",
            "{} was executed for being too cute",
            "{} choked on air while trying to breathe",
            "{} tried to bake a cake using the wrong recipe",
            "The atoms comprising {} were repurposed into paperclips",
            "A wave of grey goo swept over {} and, for that matter, everything else",
            "{} unwisely ate of the fruit of the underworld, and must remain there forevermore",
            "{} died in a video game, which of course led to dying in real life",
            "{} forgot to set the alarm clock and just never got around to waking up",
            "{} got hungry and ate a horse but it turned out that the horse was Trojan",
            "{} sparkled to death in the sun"
        ]
        self.kills = [
            "{0} stabbed {1} 28 times, just to be sure",
            "{0} spiked {1}'s protein shake with arsenic",
            "{0} booped {1} gently on the aorta",
            "{0} took a photograph of {1}, thereby stealing their soul",
            "{0} snuggled {1} to a comfy cosy death",
            "{0} baked {1} into delicious, delicious pie",
            "{0} punished {1} in the name of the moon",
            "{0} banished {1} to the shadow realm",
            "{0} yeeted {1} into the sun",
            "{0} stole {1}’s blood to make black pudding",
            "{0} fed {1} to a litter of fluffy kittens",
            "{0} made {1} into a doll",
            "{1} was found dead at sunrise, lying next to a note scrawled in {0}’s hand…",
            "In an astonishing twist, {1} turned the tables on {0}, who was subsequently crushed by said tables"
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
