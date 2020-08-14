import discord
from discord.ext import commands
from datetime import datetime, date, time
from config import config_bot_log_channel, config_description, config_error_log_channel, config_owner_id, config_prefix
from discord.ext import commands
import discord, asyncio, logging, json
from discord import Embed

#Place your token below!

token  = 'NzMyNTY4MzE4MjU4NzA4NTUw.Xw2faQ.Os_hKJVIli9YVDPyoY3Y-KAuEVE'

bot = commands.Bot(command_prefix=config_prefix, description=config_description, owner_id=config_owner_id)

cogs = ['cogs.admin', 'cogs.basic', 'cogs.poll', 'cogs.botlogging']

#DO NOT REMOVE BELOW
#Help Command
bot.remove_command('help')

@bot.command(pass_context=True)
async def help(message):
        embedVar = discord.Embed(title="Nordic + Baltic Bot Commands", description = "Please do not spam these commands or misuse them! Use = for each command.", color=0x9400D3)
        embedVar.add_field(name="Basic", value="welcome, about, applications, guide, documentation.", inline=False)
        embedVar.add_field(name="Support Commands", value="support, ip, coords, tpll, schematics, builder, waypoint, download, measure.", inline=False)
        embedVar.add_field(name="Other", value="aboutbot, ping.", inline=False)
        embedVar.add_field(name="Poll", value="poll, mpoll.", inline=False)
        embedVar.add_field(name="Admin Commands", value="In Development.", inline=False)
        await message.channel.send(embed=embedVar)

#Support Commands

@bot.command(pass_context=True)
async def support(ctx):
    await ctx.send("To get support go to #support or ask one of our Head Builders!")

@bot.command(pass_context=True)
async def ip(ctx):
    await ctx.send("Our IP is currently: **GAME-PL-01.MTXSERV.COM:27070**! Do .status to check the servers status")

@bot.command(pass_context=True)
async def coords(ctx):
    await ctx.send("https://imgur.com/a/JWJqqxU")

@bot.command(pass_context=True)
async def tpll(ctx):
    await ctx.send("```/cs tpll (coords here)```")

@bot.command(pass_context=True)
async def schematics(ctx):
    await ctx.send("https://www.youtube.com/watch?v=wcq6O50m6b8")

@bot.command(pass_context=True)
async def builder(ctx):
    await ctx.send("https://youtu.be/myzOPqaNIPk")

@bot.command(pass_context=True)
async def waypoint(ctx):
    await ctx.send("https://imgur.com/a/9LpBZlA")

@bot.command(pass_context=True)
async def measure(ctx):
    await ctx.send("https://gyazo.com/d58446cec35cc504bb36b749346041a9 Credit: BTE Server")

@bot.command(pass_context=True)
async def guide(ctx):
    await ctx.send("https://docs.google.com/document/d/1L7fzjEC3KnxSA-1OKdTy_4xBpbkG-4aTQ1ogXlqRJPA/edit")

@bot.command(pass_context=True)
async def documentation(ctx):
    await ctx.send("https://bte.rtfd.io/")

@bot.command(pass_context=True)
async def applications(ctx):
    await ctx.send("Please visit #applications for staff roles or use this link to join the build team: buildtheearth.net/bte-Nordic and press join!")

@bot.command(pass_context=True)
async def download(message):
        embedVar = discord.Embed(title="Mod Pack downloads!", color=0x00BFFF)
        embedVar.add_field(name="Windows", value="||https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-windows.zip||", inline=False)
        embedVar.add_field(name="Mac", value="||https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-mac.dmg||", inline=False)
        embedVar.add_field(name="Universal", value="||https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-linux.tar.gz||", inline=False)
        embedVar.add_field(name="Linux", value="||https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-universal.jar||", inline=False)
        await message.channel.send(embed=embedVar)

#Other commands

@bot.command(pass_context=True)
async def about(ctx):
    await ctx.send("Welcome to Build The Earth Nordic+Baltic!! We are a community dedicated towards creating the world as it stands today in Minecraft, 1:1 scale. Our team is building Sweden, Norway, Denmark, Finland, Lithuania, Latvia, Estonia and Iceland!")

@bot.command(pass_context=True)
async def aboutbot(ctx):
    await ctx.send("This bot was coded for Nordic + Baltic, it was built by @CaptainJackHarkness#6942 and @Tinonb#1600! Any problems feel free to contact me.")

@bot.command(pass_context=True)
async def welcome(message):
        embedVar = discord.Embed(title="Welcome to the Nordic + Baltic Build Team!", description = "Our build team focuses on Sweden, Denmark, Norway, Iceland, Estonia, Lithuania and Iatvia", color=0x00BFFF)
        embedVar.add_field(name="About", value="To find more infomation make sure you read #faq and #rules, as it will tell you some important infomation.", inline=False)
        embedVar.add_field(name="Support", value="If you need any support feel free to ask in #support and one of our friendly staff will answer your questions.", inline=False)
        embedVar.add_field(name="What is BTE", value="Built The Earth is a massive project that is building the whole earth in Minecraft, if you want to learn more make sure you join the official discord server: https://discord.gg/PYPtHMf", inline=False)
        await message.channel.send(embed=embedVar)


#Presence

@bot.event
async def on_ready():
    bot_log_channel = bot.get_channel(config_bot_log_channel)
    error_log_channel = bot.get_channel(config_error_log_channel)
    print(f"Bot logged on as {bot.user.name}({bot.user.id})")
    print("_____")
    guild_count = len(list(bot.guilds))
    pstatus = f"=HELP | Nordic + Baltic"
    onreadyembed=discord.Embed(title="Bot connected",description=f"Bot logged on as {bot.user.name} ({bot.user.id})", color=0x4bff68)
    onreadyembed.timestamp=datetime.utcnow()
    await bot_log_channel.send(embed=onreadyembed)
    await bot.change_presence(activity=discord.Game(name=pstatus), status=discord.Status.online)
    presencesetembed=discord.Embed(title="Bot presence set",description=f"**Presence:** `{pstatus}`\n**Status:** Online",color=0xff6fe1)
    presencesetembed.timestamp=datetime.utcnow()
    await bot_log_channel.send(embed=presencesetembed)
    try:
        for cog in cogs:
    	    bot.load_extension(cog)
    except commands.ExtensionError as e:
        loaderrorembed = discord.Embed(title="Command Error", description=
        f"""
        **Error:** {e.__class__.__name__}: {e}
        """,color=0xff7d51)
        await error_log_channel.send(embed=loaderrorembed)
    else:
        cogsloadedembed=discord.Embed(title="Cogs Loaded",description="Loaded all cogs",color=0x50beff)
        cogsloadedembed.timestamp=datetime.utcnow()
        await bot_log_channel.send(embed=cogsloadedembed)

@bot.command(hidden=True)
@commands.is_owner()
async def forceload(ctx, *, module):
    try:
        bot.load_extension(f'cogs.{module}')
    except commands.ExtensionError as e:
        await ctx.send(f':x: Failed to load module {e.__class__.__name__}: {e}')
    else:
        await ctx.send(f':ok_hand: Forceloaded module: {module}')


bot.run(token)
