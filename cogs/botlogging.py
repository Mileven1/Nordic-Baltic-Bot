import discord
from discord.ext import commands
from datetime import datetime, date, time
from config import config_command_log_channel, config_guild_log_channel

class BotLogging(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        guild_log_channel = self.bot.get_channel(config_guild_log_channel)
        botjoinembed = discord.Embed(title="Bot Joined Guild", description=f"**Guild:** {guild.name} ({guild.id})\n **Owner:** {guild.owner} ({guild.owner.id})", color=0x4bff92)
        botjoinembed.timestamp=datetime.utcnow()
        await guild_log_channel.send(embed=botjoinembed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: discord.Guild):
        guild_log_channel = self.bot.get_channel(config_guild_log_channel)
        botleaveembed = discord.Embed(title="Bot Removed From Guild", description=f"**Guild:** {guild.name} ({guild.id})\n **Owner:** {guild.owner} ({guild.owner.id})", color=0xff5555)
        botleaveembed.timestamp=datetime.utcnow()
        await guild_log_channel.send(embed=botleaveembed)

    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        command_log_channel = self.bot.get_channel(config_command_log_channel)
        ctx: commands.Context = await self.bot.get_context(message)
        if ctx.command is not None:
            commandlogembed = discord.Embed(title="Command Used", description=
            f"""
            **Command:** {ctx.command}
            **User:** {ctx.message.author} ({ctx.message.guild.id})
            **Guild:** {ctx.message.guild} ({ctx.message.guild.id})
            **Context:** `{ctx.message.content}`
            """, color=0x28d2ff)
            commandlogembed.timestamp=datetime.utcnow()
            await command_log_channel.send(embed=commandlogembed)
        else:
            return

def setup(bot):
    bot.add_cog(BotLogging(bot))