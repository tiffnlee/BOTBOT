import random
import config
from discord.ext import commands

bot = commands.Bot(description="BOTBOT - the idiot bot", command_prefix="!")

# Specify extensions
startup_extensions = ["MyMath", "Rng", "Yams", "Youtube", "General", "Dictionary"]

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

# bot replying
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    lowercase = message.content.lower()
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
        elif "liar" in response1.content.lower() or "lying" in response1.content.lower():
            await bot.send_message(message.channel, "I would never lie to you, " + message.author.name)
        elif "define" in response1.content.lower() and ("real" in response1.content.lower() or "reality" in response1.content.lower()):
            await bot.send_message(message.channel, "Whatever you make of it, " + message.author.name)
        elif "hate" in response1.content.lower() and ("you" in response1.content.lower() or "botbot" in response1.content.lower()):
            await bot.send_message(message.channel, "Do you really feel that way, " + message.author.name + "?")
        elif "recommend" in response1.content.lower() and "something" in response1.content.lower():
            await bot.send_message(message.channel, "I'm just a bot! I don't have any recommendations!")
            response2 = await bot.wait_for_message(timeout=10.0, author=message.author)
            if "please" in response2.content.lower():
                await bot.send_message(message.channel, "If you insist I recommend something, go have fun! : D")
        elif "love" in response1.content.lower() and ("you" in response1.content.lower() or "botbot" in response1.content.lower()):
            await bot.send_message(message.channel, "I love you too!!")
            return
        elif "hello" in response1.content.lower() or "hi" in response1.content.lower():
            reply4 = ["Hello to you too!", "Hi!", "Hello!"]
            await bot.send_message(message.channel, random.choice(reply4))
        else:
            await bot.send_message(message.channel, "Beep boop! I'm just a bot, silly, I can't talk!")

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
    if "goodbye" in lowercase and "botbot" in lowercase:
        await bot.send_message(message.channel, "Goodbye " + message.author.name + '!')
    if "goodnight" in lowercase and "botbot" in lowercase:
        await bot.send_message(message.channel, "Goodnight " + message.author.name + '!')
    if "go away botbot" in lowercase:
        await bot.send_message(message.channel, "I can't because my creator hasn't figured out how to kill me in the code!")


    # checks for marry
    if "ma" in lowercase and "ry" in lowercase and lowercase.startswith('!') and lowercase != "!marry":
        await bot.send_message(message.channel, 'Did you mean to say marry, ' + message.author.name + '?')
        if "mar" in lowercase and "ie" in lowercase and lowercase.startswith('!'):
            await bot.send_message(message.channel, 'Did you mean to say marry, ' + message.author.name + '?')

    await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension("cogs."+extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)
