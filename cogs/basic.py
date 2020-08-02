import discord
from discord.ext import commands
from datetime import datetime, date, time
import time


class Basic(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Returns bot response time")
    async def ping(self, ctx):
        t1 = time.perf_counter()
        async with ctx.typing():
            pass
        t2 = time.perf_counter()
        await ctx.send(":ping_pong: Pong! It took {}ms".format(round((t2-t1)*1000)))

    @commands.command(description="A novelty command, sends user to the ranch")
    async def ranch(self, ctx):
        await ctx.send("TO THE RANCH!")

    @commands.command(description="A novelty command, for our gang")
    async def gang(self, ctx):
        await ctx.send("***Nordic + Baltic Gang***")

def setup(bot):
    bot.add_cog(Basic(bot))
