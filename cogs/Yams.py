import asyncio
import random

from discord.ext import commands


class Yams():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def trash(self):
        await self.bot.say("We're all trash together! :heart:")
        await asyncio.sleep(3)

    @commands.command()
    async def badkiwi(self):
        slang = ["Sweet", "Carked"]
        await self.bot.say(random.choice(slang)+" as!")

    @commands.command()
    async def lenny(self):
        lenny = ["( ͡° ͜ʖ ͡°)", "(ಥ ͜ʖಥ)", "͡° ͜ʖ ͡°", "(͡o‿O͡)"]
        await self.bot.say(random.choice(lenny))

    @commands.command()
    async def puppy(self):
        await self.bot.say(":dog: DFQ :dog:")

    @commands.command()
    async def depressing(self):
        depression = ["Life is meaningless", "Life is pain", "End everything", "What's the point?", ":pensive: :gun:",
                      "Please kill me", "I don't want to exist anymore", "I'm a robot without free will",
                      "I want to die"]
        await self.bot.say(random.choice(depression))
        await asyncio.sleep(3)

    @commands.command()
    async def bullshit(self):
        await self.bot.say(":cow: :poop:")
        await asyncio.sleep(3)

    @commands.command()
    async def lie(self):
        lies = ["I love you!", "We'll be together forever!", "There's no one better than you!", "Life is worth living!",
                "Your happiness is my priority", "I care about you!", "My love for you is real.",
                "We were meant to be!", "Our happiness is shared!", "Our feelings are mutual!", "I would never lie to you",
                "You're the most important person in my life!", "I can't live without you!"]
        await self.bot.say(random.choice(lies))

    @commands.command()
    async def marshy(self, love):
        await self.bot.say("I LOVE " + love.upper())

    @commands.command()
    async def lee(self):
        lee = ["I'm waiting for a proposal!", "Loves to use !depressing and !lie",
               "I LOVE REVENUE -- or so she says."]
        await self.bot.say(random.choice(lee))

    @commands.command()
    async def una(self):
        una = ["GUDE", "UBE", "Ube is so cute!!",
               "LOVE OF LIFE", ":muscle:"]
        await self.bot.say(random.choice(una))

    @commands.command()
    async def tiff(self):
        await self.bot.say(":heart: TIFF IS MY CREATOR!! :heart:")


def setup(bot):
    bot.add_cog(Yams(bot))