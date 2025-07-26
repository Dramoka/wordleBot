import asyncio
from datetime import datetime
from operator import truediv

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True


bot = commands.Bot(command_prefix='//', intents=intents)

channelID = 1265869230092583054


@bot.event
async def on_ready():
    print("The Wordle answer for today: nigga")


@bot.command()
async def answer(ctx):
    await ctx.send("The Wordle answer for today: nigga")

@bot.command()
async def sapphire(ctx):
    id = 678344927997853742
    sapphireUser = await bot.fetch_user(id)
    await ctx.send(f"{sapphireUser.mention} shut your CLANKER ass up")

##@bot.event
##async def on_message(message):
##    if message.content.lower() == "wordle":
##        await message.channel.send("The Wordle answer for today: nigga")
##
##    await bot.process_commands(message)

async def dailyMessage():
    await bot.wait_until_ready()
    channel = bot.get_channel(channelID)

    while not bot.is_closed():
        now = datetime.now()
        nextPost = now.replace(hour=6, minute=0, second=0, microsecond=0)
        if now >= nextPost:
            nextPost += datetime.timedelta(days=1)

        secondsWait = (nextPost - now).total_seconds()

        await asyncio.sleep(secondsWait)

        await channel.send("The Wordle answer for today: nigga")

        await asyncio.sleep(86400)


bot.run(TOKEN, log_handler=handler, log_level=logging.DEBUG)



