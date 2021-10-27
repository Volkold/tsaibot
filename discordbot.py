from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='n')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def msl(ctx):
    await ctx.send('nmsl')

@bot.command()
async def mczcl(ctx):
    await ctx.send('你媽城中城了')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
