# Moderation.py
# 2020/11/01
# adoisjdfoij
# dw
import discord
from discord.ext import commands
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)#only works when user has permissions
    async def clear(self, ctx, amount = 2): #clears [amount] messages, will default as 2 when nothing is specified
        await ctx.channel.purge(limit=amount + 1)#ctx, access channel, purge function, destroys amount

    #kick and ban
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):#* is actually really useful wow 
        await member.kick(reason = reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):#* is actually really useful wow 
        await member.ban(reason = reason)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        memberName, memberDisc = member.split("#") #get the name and the tag

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (memberName, memberDisc):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

def setup(client):
    client.add_cog(Moderation(client))