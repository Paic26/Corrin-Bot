import discord
import json
from discord.ext import commands, tasks
import random
import datetime


def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')


class Help(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        # Events

        @commands.Cog.listener()
        async def on_ready(self):
            print('Help Cog is on')



    # HELP COMMANDS

    @commands.command()
    async def help(self, ctx):
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(
            colour=value,
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_author(name="Commands", icon_url="https://cdn.discordapp.com/attachments/731598260472643595/731858655825363006/image0.jpg")
        embed.add_field(name="Help_fun", value="Gives all the entertainment commands.", inline=False)
        embed.add_field(name="Help_moderation", value="Gives all the moderation commands.", inline=False)
        embed.add_field(name="Help_management", value="Gives all the management commands.", inline=False)
        embed.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['helpf','help_fun','help1'])
    async def helpfun(self, ctx):
        value1 = random.randint(0, 0xffffff)
        embed1 = discord.Embed(
            colour=value1,
            timestamp=datetime.datetime.utcnow()
        )

        embed1.set_author(name="Fun Commands", icon_url="https://cdn.discordapp.com/attachments/731598260472643595/731858655825363006/image0.jpg")
        embed1.add_field(name="HowGay", value="Tells you how gay you are", inline=False)
        embed1.add_field(name="HowThicc", value="Tells you how thicc you are", inline=False)
        embed1.add_field(name="8ball", value="Ask a question and the bot will give an answer", inline=False)
        embed1.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed1)

    @commands.command(aliases=['helpmod','help2','helpstaff','help_staff'])
    async def helpmoderation(self, ctx):
        value2 = random.randint(0, 0xffffff)
        embed2 = discord.Embed(
            colour=value2,
            timestamp=datetime.datetime.utcnow()
        )

        embed2.set_author(name="Moderation Commands",icon_url="https://cdn.discordapp.com/attachments/731598260472643595/731858655825363006/image0.jpg")
        embed2.add_field(name="Ban", value="Bans Users", inline=False)
        embed2.add_field(name="Unban", value="Unbans Users", inline=False)
        embed2.add_field(name="Kick", value="Kicks Users", inline=False)
        embed2.add_field(name="Mute", value="Mutes Users", inline=False)
        embed2.add_field(name="Unmute", value="Unmutes muted users", inline=False)
        embed2.add_field(name="Clear", value="Clears messages (clearall deletes all the messages from the channel)", inline=False)
        embed2.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed2)

    @commands.command(aliases=['helpmanage','help_management','help3'])
    async def helpmanagement(self, ctx):
        value3 = random.randint(0, 0xffffff)
        embed3 = discord.Embed(
            colour=value3,
            timestamp=datetime.datetime.utcnow()
        )

        embed3.set_author(name="Management Commands", icon_url="https://cdn.discordapp.com/attachments/731598260472643595/731858655825363006/image0.jpg")
        embed3.add_field(name="Change_prefix", value="Use your favourite prefix", inline=False)
        embed3.add_field(name="Ping", value="Pong with latency", inline=False)
        embed3.add_field(name="Suggestions", value="For this to work go to <#488418208697810947>", inline=False)
        embed3.set_footer(text=f"Just helped{ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed3)


def setup(bot):
    bot.add_cog(Help(bot))
    print('Help Loaded')