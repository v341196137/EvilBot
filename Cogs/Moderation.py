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

    #role management
    @commands.command(aliases = ["mkRole", "createRole"])
    @commands.has_permissions(manage_roles = True)
    async def makeRole(self, ctx, name, r = 0, g = 0, b = 0):
        guild = ctx.guild
        await guild.create_role(name = name, colour = discord.Colour.from_rgb(r, g, b), mentionable = True)
        role = discord.utils.get(guild.roles, name = name)
        if role is not None:
            await ctx.send(f"{ctx.author.mention} created role {role.mention}")
        else:
            await ctx.send("/shrug Some role creation thing went wrong")

    @commands.command(aliases = ["addRole", "giveRole"])
    @commands.has_permissions(manage_roles = True)
    async def assignRole(self, ctx, member:discord.Member, role:discord.Role):
        await member.add_roles(role)
        await ctx.send(f"{ctx.author.mention} gave {member.mention} a {role.mention} role")

    @commands.command(aliases = ["removeRole rmRole"])
    @commands.has_permissions(manage_roles = True)
    async def deleteRole(self, ctx, member:discord.Member, role:discord.Role):
        await member.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} removed {role.mention} from {member.mention}")
        
def setup(client):
    client.add_cog(Moderation(client))