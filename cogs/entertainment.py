import discord
from discord.ext import commands
from bs4 import BeautifulSoup as Soup
import datetime
import requests
import random
from random import choice
import json

s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'})
with open("./json/memes.json", "r") as f:
    src = json.load(f)

gif = []


class Entertainment(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Entertainment Cog is on')

    with open("./json/memes.json", "r") as f:
        src = json.load(f)

    gif = []

        #Commands



    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.']


        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,

        )
        embed.add_field(name=f'**Question:** {question}\n**Answer:** {random.choice(responses)}', value="hope you feel good with this answer.", inline=False)

        await ctx.send(embed=embed)



    @commands.command(aliases=['gay'])
    async def howgay(self, ctx):
        value = random.randint(0, 0xffffff)
        gay = random.randint(1, 100)
        gay = str(gay)
        embed = discord.Embed(title='',
                              description='You are ' + gay + '% gay :gay_pride_flag:',
                              color=value)
        await ctx.send(embed=embed)

    @commands.command(aliases=['thicc'])
    async def howthicc(self, ctx):
        value = random.randint(0, 0xffffff)
        thicc = random.randint(1, 100)
        thicc = str(thicc)
        embed = discord.Embed(
            title='',
            description='You are ' + thicc + '% Thicc 🍑',
            color=value
        )
        await ctx.send(embed=embed)
    #errors


    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please ask a question.')


def setup(bot):
    bot.add_cog(Entertainment(bot))
    print('Entertainment Loaded')
