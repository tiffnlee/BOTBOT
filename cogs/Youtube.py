import aiohttp
import config
import discord  # discord api
from apiclient.discovery import build  # youtube api
from discord.ext import commands  # commands extension


# credit to Francis#6565 to which i based code off of
class Youtube:

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command(pass_context = True)
    async def search(self, ctx, message):
        """Searches YouTube for a video.
        Returns the first result."""
        try:
            if not message:
                await self.bot.say("Arguments needed!\n\nExample: `!search Darude Sandstorm`")
            else:
                youtube = build("youtube", "v3", developerKey=config.youtubekey)
                search_response = youtube.search().list(q=message.split(), part="id,snippet",
                                                        maxResults=1, type="video").execute()
                if len(search_response.get('items')) == 0:
                    await self.bot.say("No videos found.")
                else:
                    video = search_response.get('items')[0]
                    vidid = search_response.get('items')[0]['id']['videoId']
                    vidurl = "https://www.youtube.com/watch?v=" + vidid
                    yt_url = "http://www.youtube.com/oembed?url={0}&format=json".format(vidurl)
                    data = discord.Embed(title="**__Search Result__**", colour=discord.Colour(value=11735575))
                    data.add_field(name="Video Title", value=video['snippet']['title'], inline=False)
                    data.add_field(name="Video Link", value=vidurl, inline=False)
                    data.set_image(url="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(vidid))
                    try:
                        await self.bot.send_message(ctx.message.channel, embed=data)
                    except discord.HTTPException:
                        await self.bot.say("Looks like BOTBOT doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")
        except Exception as e:
            print(e)
            data = discord.Embed(title="__***Error in video search!***__", description="No data for video ID!", colour=discord.Colour(value=11735575))
            data.add_field(name="Whoops!",
                           value="Looks like the API returned a video, but there is no associated data with it!\nThis could be due to the video being unavailable anymore, or it is country blocked!",
                           inline=False)
            data.add_field(name="What can I do now?",
                           value="Not much really. *__Please don't re-search the video__*, as this adds unnecessary strain on the bot, and you'll get the same result.",
                           inline=False)
            try:
                await self.bot.send_message(ctx.message.channel, embed=data)
            except discord.HTTPException:
                await self.bot.say("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")

def setup(bot):
    bot.add_cog(Youtube(bot))