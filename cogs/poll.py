import discord
from discord.ext import commands
from datetime import datetime, date, time

class Poll(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases= ['p'], description="Creates a poll by adding thumbs up and down reactions", usage="[content/question of poll]")
    async def poll(self, ctx):
    	await ctx.message.add_reaction('👍')
    	await ctx.message.add_reaction('👎')

    @commands.command(aliases=['mp','maybepoll'], description="Creates a poll by adding thumbs up, thumbs down, and shrug reactions", usage='[content/question of poll]')
    async def mpoll(self, ctx):
        await ctx.message.add_reaction('👍')
        await ctx.message.add_reaction('👎')
        await ctx.message.add_reaction('🤷')

    @commands.Cog.listener()
    async def on_message(self, message, ctx):
        if '--poll' or '--p' in message.content:
            await ctx.message.add_reaction('👍')
            await ctx.message.add_reaction('👎')
        if '--mpoll' or '--mp' in message.content:
            await ctx.message.add_reaction('👍')
            await ctx.message.add_reaction('👎')
            await ctx.message.add_reaction('🤷')

def setup(bot):
    bot.add_cog(Poll(bot))