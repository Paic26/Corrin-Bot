import discord
from discord.ext import commands
import json

def get_prefix(client, message):
    with open('./json/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix = get_prefix,  case_insensitive=True, owner_id=382947478422421516)

class Moderation(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot


        #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation Cog is on')

        #Commands

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
        print(f'{member} was Banned from a server')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                print(f'{member} was Unbanned from a server')
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member = None):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send('Please specify a member')
            return
        await member.add_roles(role)
        await ctx.send('Muted')
        print(f'{member} was Muted from a server')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member = None):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send('Please specify a member')
            return
        await member.remove_roles(role)
        await ctx.send('Unmuted')
        print(f'{member} was Unmuted from a server')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        print(f'{member} was Kicked from a server')

    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=6):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=['purgeall', 'purge_all'])
    @commands.has_permissions(manage_messages=True)
    async def clearall(self, ctx, amount=9999999999999):
        await ctx.channel.purge(limit=amount)



    #bad-words zone
    @commands.Cog.listener()
    async def on_message(self, message):
        filter = ["nigga", "nigger", "Nigga", "Nigger"]

        for word in filter:
            if message.content.count(word) > 0:
                await message.channel.purge(limit=1)

        #errors

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please select a user to kick.')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please select a user to ban.')


def setup(bot):
    bot.add_cog(Moderation(bot))
    print('Moderation Loaded')