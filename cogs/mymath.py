from discord.ext import commands

class MyMath():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, *numbers : float):
        sum = 0
        for x in numbers:
            sum+=x
        await self.bot.say(sum)

    @commands.command()
    async def multiply(self, *numbers : float):
        product = 0
        for x in numbers:
            product *= x
        await self.bot.say(product)

def setup(bot):
    bot.add_cog(MyMath(bot))