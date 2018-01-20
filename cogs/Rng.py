import random

from discord.ext import commands


class Rng():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def choose(self, *choices: str):
        """Chooses between multiple choices."""
        await self.bot.say(random.choice(choices))

    # coin flip
    @commands.command()
    async def coinflip(self):
        coin = ["Heads", "Tails"]
        await self.bot.say(random.choice(coin))

def setup(bot):
    bot.add_cog(Rng(bot))