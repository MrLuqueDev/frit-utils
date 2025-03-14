import discord
from discord.ext import commands
import yt_dlp
import os

class Downloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def download(self, ctx, url: str):
        try:
            download_folder = os.path.join(os.path.expanduser('~'), 'desktop', 'bot', 'downloads') # change this to your direcctory
            os.makedirs(download_folder, exist_ok=True)

            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'quiet': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                video_title = info_dict.get('title', None)
                video_path = os.path.join(download_folder, f"{video_title}.mp4")
            await ctx.send(f"Downloading **'{video_title}'**...")
            await ctx.send(file=discord.File(video_path))
            os.remove(video_path)
        except Exception as e:
            await ctx.send(f"Help i died: {e}")
async def setup(bot):
    await bot.add_cog(Downloader(bot))
