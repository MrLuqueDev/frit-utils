import discord
from discord.ext import commands
import os

class Echo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, msg: str):
        await ctx.send(f"'{msg}'")

# The setup function that loads the cog
async def setup(bot):
    await bot.add_cog(Echo(bot))
