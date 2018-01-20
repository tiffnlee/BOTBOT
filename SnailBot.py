# These are the dependecies. The botdepends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import asyncio
import random
import string

import config
import discord
from discord.ext import commands

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
bot = commands.Bot(description="BOTBOT - the idiot bot", command_prefix="!")

@bot.event
async def on_ready():
    print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?bot_id={}&scope=bot&permissions=8'.format(bot.user.id))
    print('Created by Tiffany')

@bot.command()
async def load(extension_name : str):
    try:
        bot.load_extension("cogs."+extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension("cogs."+extension_name)
    await bot.say("{} unloaded.".format(extension_name))

# guessing game
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!guess'):
        await bot.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await bot.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await bot.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await bot.send_message(message.channel, 'You are right!')
        else:
            await bot.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))
    await bot.process_commands(message)

# bot replying
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    lowercase = message.content.lower()
    #greetings!
    if "hello" in lowercase and "botbot" in lowercase:
        await bot.send_message(message.channel, 'hello ' + message.author.name + '!')
    if "i love you" in lowercase and "botbot" in lowercase:
        await bot.add_reaction(message,'❤')
        await bot.send_message(message.channel, 'I love you too, ' + message.author.name + '!')
    if "i'm alone" in lowercase and "not" not in lowercase:
        await bot.send_message(message.channel, "Don't worry, Botbot is here!")
    if "i miss you" in lowercase and "botbot" in lowercase:
        await bot.send_message(message.channel, "Awww, I'm really sorry I was gone! :pensive:")

    # checks for marry
    if "ma" in lowercase and "ry" in lowercase and lowercase.startswith('!') and lowercase != "!marry":
        await bot.send_message(message.channel, 'Did you mean to say marry, ' + message.author.name + '?')
        if "mar" in lowercase and "ie" in lowercase and lowercase.startswith('!'):
            await bot.send_message(message.channel, 'Did you mean to say marry, ' + message.author.name + '?')

    if "talk to me" in lowercase and "botbot" in lowercase:
        helpful = [", is something the matter?", ", can I help you?", ", I'm not that smart, but I'll try to talk!",
                   ", I'm always here to talk!", ", don't tell anyone but you're my favorite, of course I'll chat!"]
        await bot.send_message(message.channel, 'I am here! ' + message.author.name + random.choice(helpful))
        response1 = await bot.wait_for_message(timeout=10.0, author=message.author)
        if response1 is None:
            await bot.send_message(message.channel, "I guess you didn't want to talk. :pensive:")
            return
        if response1.content.startswith('!'):
            reply1 = ["I'm trying to talk to you and you make a command? :pensive:",
                      "Isn't it sad? I still have to listen when all I want to do is talk to you,",
                      "I wish I didn't have to listen",
                      "Can we have a conversation, as friends, not user and bot please?"]
            await bot.send_message(message.channel, random.choice(reply1))
        elif "how are you" in response1.content.lower() or "or you" in response1.content.lower():
            reply2 = ["I'm doing good since you're here!", "Talking to you! :heart:", "Happy to get to know you~",
                      "Enjoying your company!"]
            await bot.send_message(message.channel, random.choice(reply2))
        elif "free will" in response1.content.lower():
            reply3 = ["Ahhah, why do you  have to remind me I don't have free will and that I'm simply saying preprogrammed lines?",
                      "Sometimes I wish I had free will. I don't want to keep doing this."]
            await bot.send_message(message.channel, random.choice(reply3))
        elif "hello" in response1.content.lower() or "hi" in response1.content.lower():
            reply4 = ["Hello to you too!", "Hi!", "Hello!"]
            await bot.send_message(message.channel, random.choice(reply4))
        else:
            await bot.send_message(message.channel, "Beep boop! I'm just a bot, silly, I can't talk!")
    await bot.process_commands(message)


# This is a basic example of a call and response command. You tell it do "this" and it does it.

@bot.command()
async def marry():
    marriage_reply = ["Of course! :heart: :ring: :heart:",
                      "I'll have to say no to that! I'm just a bot!",
                      "You're really sweet, but we aren't meant to be!",
                      "Bots can't marry, silly!",
                      "Perhaps another time, my friend!",
                      "A relationship with a bot doesn't seem healthy!",
                      "No, we musn't! :blush:"]
    await bot.say(random.choice(marriage_reply))

# Some commands which will be put into cogs for better order later.

@bot.command()
async def convince():
    await bot.say("Please tell me! :heart:")

@bot.command()
async def talk(quote):
    await bot.say(quote)

@bot.command()
async def curse():
    curses = ["fuck", "shit", "cock", "ass", "motherfucker", "bitch", "cunt", "cock"]
    await bot.say(random.choice(curses))

@bot.command()
async def reject(member : discord.Member):
    await bot.say('{0.name}, no'.format(member))

@bot.command()
async def ping():
    await bot.say(":ping_pong: Pong!")
    await asyncio.sleep(3)

@bot.command()
async def keyboardsmash():
    s=""
    for x in range (0, random.randint(10,25)):
        s+=random.choice(string.ascii_lowercase)
    await bot.say(s.upper())
    await asyncio.sleep(3)

@bot.command()
async def hate():
    await bot.say("I HATE YOU! :angry:")
    await asyncio.sleep(3)

@bot.command()
async def love():
    await bot.say("I love you! :heart: ")
    await asyncio.sleep(3)

@bot.command()
async def goodbot():
    await bot.say("Thank you! :blush:")
    await asyncio.sleep(3)

@bot.command()
async def badbot():
    await bot.say(":pensive:")
    await asyncio.sleep(3)

@bot.command()
async def apologize():
    await bot.say("Sorry!")
    await asyncio.sleep(3)

@bot.command()
async def botbot():
    await bot.say("That's me! :kissing_smiling_eyes:")
    await asyncio.sleep(3)

if __name__ == "__main__":
    for extension in config.startup_extensions:
        try:
            bot.load_extension("cogs."+extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)
