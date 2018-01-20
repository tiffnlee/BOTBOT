import aiohttp
import config
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

            youtube = build("youtube", "v3", developerKey=config.youtubekey)
            search_response = youtube.search().list(q=message.split(), part="id,snippet",
                                                        maxResults=1, type="video").execute()
            if len(search_response.get('items')) == 0:
                await self.bot.say("No videos found.")
            else:
                vidid = search_response.get('items')[0]['id']['videoId']
                vidurl = "https://www.youtube.com/watch?v=" + vidid
                await self.bot.send_message(ctx.message.channel, vidurl)
        except Exception:
            await self.bot.send_message(ctx.message.channel, "Something went wrong with the search, sorry!")

def setup(bot):
    bot.add_cog(Youtube(bot))