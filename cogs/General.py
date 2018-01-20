import discord
import random
import string
from discord.ext import commands
class General:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def marry(self):
        marriage_reply = ["Of course! :heart: :ring: :heart:",
                          "I'll have to say no to that! I'm just a bot!",
                          "You're really sweet, but we aren't meant to be!",
                          "Bots can't marry, silly!",
                          "Perhaps another time, my friend!",
                          "A relationship with a bot doesn't seem healthy!",
                          "No, we musn't! :blush:"]
        await self.bot.say(random.choice(marriage_reply))
    
    # Some commands which will be put into cogs for better order later.
    
    @commands.command()
    async def convince(self):
        await self.bot.say("Please tell me! :heart:")
    
    @commands.command()
    async def talk(self,quote):
        await self.bot.say(quote)
    
    @commands.command()
    async def curse(self):
        curses = ["fuck", "shit", "cock", "ass", "motherfucker", "bitch", "cunt", "cock"]
        await self.bot.say(random.choice(curses))
    
    @commands.command()
    async def reject(self, member : discord.Member):
        await self.bot.say('{0.name}, no'.format(member))
    
    @commands.command()
    async def ping(self):
        await self.bot.say(":ping_pong: Pong!")
    
    @commands.command()
    async def keyboardsmash(self):
        s=""
        for x in range (0, random.randint(10,25)):
            s+=random.choice(string.ascii_lowercase)
        await self.bot.say(s.upper())
    
    @commands.command()
    async def hate(self):
        await self.bot.say("I HATE YOU! :angry:")
    
    @commands.command()
    async def love(self):
        await self.bot.say("I love you! :heart: ")
    
    @commands.command()
    async def goodbot(self):
        await self.bot.say("Thank you! :blush:")
    
    @commands.command()
    async def badbot(self):
        await self.bot.say(":pensive:")
    
    @commands.command()
    async def apologize(self):
        await self.bot.say("Sorry!")
    
    @commands.command()
    async def botbot(self):
        await self.bot.say("That's me! :kissing_smiling_eyes:")

def setup(bot):
    bot.add_cog(General(bot))