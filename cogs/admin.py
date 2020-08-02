import discord
from discord.ext import commands
from datetime import datetime, date, time
from config import config_bot_log_channel, config_error_log_channel

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def say(self, ctx, *, content):
        await ctx.send(content)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def setpresence(self, ctx, *, presence):
        bot_log_channel = self.bot.get_channel(config_bot_log_channel)
        guild_count = len(list(self.bot.guilds))
        default = f"Nordic + Baltic | {guild_count} guilds"
        guilds = f"{guild_count} guilds"
        site = "https://github.com/Mileven1/BTEbot"
        if presence == 'default':
            presence = default
        if presence == 'guilds':
            presence = guilds
        if presence == 'docs':
            presence = docs
        if presence == 'site':
            presence = site
        presence = presence.replace('[guild_count]', str(guild_count))
        presence = presence.replace('[docs]', "N/A")
        presence = presence.replace('[site]', "https://github.com/Mileven1/BTEbot")
        await self.bot.change_presence(activity=discord.Game(name=presence))
        await ctx.send(f":ok_hand::computer: Bot presence set to `{presence}`")
        setpresenceembed=discord.Embed(title="Bot presence set",description=f"**New Presence:** `{presence}`\n**Set by:** {ctx.message.author}",color=0xff6fe1)
        setpresenceembed.timestamp=datetime.utcnow()
        await bot_log_channel.send(embed=setpresenceembed)

    @commands.command(aliases=['logout'],hidden=True)
    @commands.is_owner()
    async def close(self, ctx):
        bot_log_channel = self.bot.get_channel(config_bot_log_channel)
        closingembed = discord.Embed(title="Bot closed", color=0xff2121)
        closingembed.timestamp=datetime.utcnow()
        await bot_log_channel.send(embed=closingembed)
        await self.bot.close()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, module):
        bot_log_channel = self.bot.get_channel(config_bot_log_channel)
        error_log_channel = self.bot.get_channel(config_error_log_channel)
        """Loads a module"""
        try:
            self.bot.load_extension(f'cogs.{module}')
            await ctx.send(f':ok_hand: Loaded module: {module}')
            loadedcogembed = discord.Embed(title= "Module Manually Loaded", description= f"**Module:** {module} \n **Actor:** {ctx.message.author}", color= 0x35fff0)
            await bot_log_channel.send(embed=loadedcogembed)
        except commands.ExtensionError as e:
            await ctx.send(f':x: Failed to load module {e.__class__.__name__}: {e}')
            loaderrorembed = discord.Embed(title="Command Error", description=
            f"""
            **Command:** {ctx.command}
            **User:** {ctx.message.author} ({ctx.message.author.id})
            **Guild:** {ctx.message.guild} ({ctx.message.guild.id})
            **Channel:** {ctx.message.channel} ({ctx.message.channel.id})
            **Usage:** `{ctx.message.content}`
            **Error:** {e.__class__.__name__}: {e}
            """,color=0xff7d51)
            await error_log_channel.send(embed=loaderrorembed)


    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, module):
        error_log_channel = self.bot.get_channel(config_error_log_channel)
        bot_log_channel = self.bot.get_channel(config_bot_log_channel)
        try:
            self.bot.unload_extension(f'cogs.{module}')
            await ctx.send(f':ok_hand: Unloaded module: {module}')
            unloadedcogembed = discord.Embed(title= "Module Manually Unloaded", description= f"**Module:** {module} \n **Actor:** {ctx.message.author}", color= 0xd85e34)
            await bot_log_channel.send(embed=unloadedcogembed)
        except commands.ExtensionError as e:
            await ctx.send(f':x: Failed to unload module {e.__class__.__name__}: {e}')
            unloaderrorembed = discord.Embed(title="Command Error", description=
            f"""
            **Command:** {ctx.command}
            **User:** {ctx.message.author} ({ctx.message.author.id})
            **Guild:** {ctx.message.guild} ({ctx.message.guild.id})
            **Channel:** {ctx.message.channel} ({ctx.message.channel.id})
            **Usage:** `{ctx.message.content}`
            **Error:** {e.__class__.__name__}: {e}
            """,color=0xff7d51)
            await error_log_channel.send(embed=unloaderrorembed)

def setup(bot):
    bot.add_cog(Admin(bot))
