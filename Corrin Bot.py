import discord
import json
from discord.ext import commands
import  os
import asyncio
import datetime
import random


def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix = get_prefix,  case_insensitive=True, owner_id=343150191924346881)
Bot = discord.client
client = bot
client.remove_command('help')

#cogs
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')



for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension((f'cogs.{filename[:-3]}'))



@bot.event
async def on_ready():
    print('Corrin Bot is ready \n-------------------')

#Costumizable Prefixes

@client.event
async def on_guild_join(guild):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '_'

    with open('./json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('./json/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


#stop the bot

@bot.command(aliases=["quit", "kill"])
@commands.is_owner()
async def shutdown(ctx):
    value = random.randint(0, 0xffffff)
    kill = discord.Embed(
        colour=value,
        timestamp=datetime.datetime.utcnow(),
        title='Corrin Bot is now turned off!'
    )
    kill.set_footer(text=f"Shutdowned By {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=kill)
    await asyncio.sleep(2)
    await bot.close()



bot.run(os.environ['DISCORD_TOKEN'])
