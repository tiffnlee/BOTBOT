from discord.ext import commands

class Images():

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def thisisfine(self, ctx):
        await self.bot.send_file(ctx.message.channel, 'img/fine.jpg')

    @commands.command(pass_context=True)
    async def truth(self, ctx):
        await self.bot.send_file(ctx.message.channel, 'img/truth.jpg')

    @commands.command(pass_context=True)
    async def pbj(self, ctx):
        await self.bot.send_file(ctx.message.channel, 'img/pbj.gif')

def setup(bot):
    bot.add_cog(Images(bot))