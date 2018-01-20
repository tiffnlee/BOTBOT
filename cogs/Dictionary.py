from PyDictionary import PyDictionary
from discord.ext import commands

class Dictionary:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, to_define: str):
        dictionary = PyDictionary()
        await self.bot.say(dictionary.meaning(to_define))

    @commands.command()
    async def synonym(self, word: str):
        dictionary = PyDictionary()
        await self.bot.say(dictionary.synonym(word))

    @commands.command()
    async def antonym(self, word: str):
        dictionary = PyDictionary()
        await self.bot.say(dictionary.antonym(word))

def setup(bot):
    bot.add_cog(Dictionary(bot))