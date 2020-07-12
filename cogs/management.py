import discord
import json
from discord.ext import commands, tasks
import random
import asyncio
import datetime


def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True)
Bot = discord.client
client = bot
client.remove_command('help')


class Management(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

        # Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('Management Cog is on')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        random.randint(0, 0xffffff)
        if isinstance(error, commands.CommandNotFound):
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(
                colour=value,
                title="Command non-existent or broken."
            )
            embed.add_field(name="Do <prefix>help", value="for the available commands")
            await ctx.send(embed=embed)


    @commands.Cog.listener()  # invite filter
    async def on_message(self, message):
        if "discord.gg" in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention} please don't send invites to other discord servers ")
        await client.process_commands(message)

    @commands.Cog.listener()        # suggestion command
    async def on_message(self, message):
        channel = client.get_channel(731849431573331999)

        if message.channel.id == 731849431573331999:
            if message.author.bot:
                await message.add_reaction("\u2705")
                await message.add_reaction("\u274C")

            if message.author.bot:
                return

            content = message.content

            value = random.randint(0, 0xffffff)
            embed = discord.Embed(

                colour=value,
            )
            embed.add_field(name="**SUGGESTION** by {}\n\n".format(message.author) + "`{}`\n\n".format(
                content) + "React :white_check_mark: for yes, or :x: for no.", value='\u200b')
            await message.channel.send(embed=embed)



    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(

            colour=discord.Colour.purple(),
            title="Invite the Bot!"
        )
        embed.add_field(name="Bot Invite", value="[Bot Invite Link](https://bit.ly/3dBozNZ)")
        await ctx.send(embed=embed)


    @commands.command()
    async def ping(self, ctx):

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(

            colour=value,
            title=":ping_pong: Pong:ping_pong: "
        )
        embed.add_field(name=f'Ponged! {round(self.bot.latency * 1000)}ms', value=":ping_pong: Pong:ping_pong:")
        await ctx.send(embed=embed)

    @commands.command(aliases=['prefix'])
    async def change_prefix(self, ctx, prefix):
        with open('./prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')


def setup(bot):
    bot.add_cog(Management(bot))
    print('Management Loaded')
