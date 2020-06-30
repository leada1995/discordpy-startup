from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

embed5 = discord.Embed(title="今のボスは", description="***カルキノス***\n" 
                       "[**リマクリスレイプッコロミズナ**]"
                       "(https://discordapp.com/channels/716279661033947207/724105654490497055/726397867836702752)\n",
                       color=0xff0000)
embed5.set_thumbnail(url="https://gamewith.akamaized.net/article_tools/pricone-re/gacha/93_enemy.png")

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
async def on_message(message):
    if message.content == 'ムノカマエ':
        await message.channel.send('╭( ´ ᵕ ` )╮')

bot.run(token)
