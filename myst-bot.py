import configparser
import discord
from discord.ext import commands
import commands as myst

config = configparser.ConfigParser()
config.read('config/config.ini')
mConfig = config['MYST']
bot = commands.Bot(description="I'm Myst AI 2.0!", command_prefix=("m!", "myst!"))


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(ctx):
    """I reply Pong, this is for testing purposes only."""
    await ctx.send("Pong!")


@bot.command()
async def say(ctx, *, something):
    await ctx.send(something)

@bot.group(invoke_without_command=True)
async def foo(ctx):
    await ctx.send("this is m!foo")

@foo.command(name="bar")
async def foo_bar(ctx):
    await ctx.send("this is m!foo bar")

@bot.command()
async def mention(ctx):

    await ctx.author.send("Sup " + ctx.author.mention)


bot.run(token)
