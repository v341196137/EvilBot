# testbot.py
# 2020/08/24
# cubic disappointment
# time to be less bad at Python
# kudos Lucas, https://www.youtube.com/watch?v=zOVl7tAexl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ

#-------------------------IMPORTS---------------------------------
import discord
from discord.ext import commands, tasks
from discord.utils import find
import random
import os
from itertools import cycle
import json

#-----------------------PRE MAIN FUNCTIONS------------------------
def getPrefix(client, message):#get prefixes from a json file
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    if message.guild is not None:
        return prefixes[str(message.guild.id)]
    else:
        return "!"

#--------------------------MAIN-----------------------------------
client = commands.Bot(command_prefix = getPrefix) # prefix that is used to call bot
status = cycle([
    'Implementing communism', 
    'Taking over the world >:D', 
    'Water is definitely wet',
    'Stealing sandwiches', 
    'Starting a new cult'
])

#-------------------------EVENTS----------------------------------

@client.event #function declarator 
async def on_ready(): #asychronus (independent of clock cycles) function, on_ready is when bot is ready, got all info necessary from Discord
    print('Bot says hi, taking over the world is fun >:D') #just show the world the bot is ready and exists
    #-------------------------STATUS----------------------------------
    change_status.start()
    # Lots of other possible statuses to use
    """
    # Setting `Playing ` status
    await client.change_presence(status = "Commiting acts of communism", activity=discord.Game(name="Let's take over the world"))
    
    # Setting `Streaming ` status
    await client.change_presence(activity=discord.Streaming(name="idk", url="www.google.ca"))

    # Setting `Listening ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="🎵"))

    # Setting `Watching ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=":P"))
    """

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}!'.format(guild.name))
    

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)

@client.event
async def on_member_join(member): #takes in member param
    print(f'{member} has entered the cult') #no clue how printf works XD
    channel = discord.utils.get(client.get_all_channels(), guild__name = GUILD_NAME, name = CHANNEL_NAME) #replace those with your own
    await channel.send(f"Oh no! {member.mention} is good! Go be EVIL! Read <#CHANNEL_ID>!") #replace with a channel ID to direct the person to
    await member.send(f"Welcome good and soon-to-be-evil {member}!")
    goodRole = discord.utils.get(member.guild.roles, name = ROLE_TO_ADD_ON_JOIN) #replace that
    if goodRole is not None:
        await member.add_roles(goodRole)

@client.event
async def on_member_remove(member):
    print(f'noooo {member} left') #for uh no actual reason

@client.event
async def on_command_error(ctx, error):#error handling :D
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Input all arguments because dictator said so")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Dictator didn't make this command yet")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Dictator did not grant you such permissions you egg")
    else:
        print(error, type(error))

#----------------------REACTION HANDLING--------------------------
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == ID: # Message ID to react to for adding/removing roles
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda x:x.id==guild_id, client.guilds)

        name = payload.emoji.name
        goodRole = discord.utils.get(guild.roles, name = ROLE_TO_REMOVE) #replace with your own
        member = discord.utils.find(lambda x:x.id == payload.user_id, guild.members)
        if name == NAME_OF_EMOJI_TO_REACT_TO: #replace
            role = discord.utils.get(guild.roles, name = ROLE_TO_ADD) #replace
            if goodRole is not None and member is not None:
                await member.remove_roles(goodRole)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            if member is not None:
                await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == ID:# The message to unreact to for doing a certain thing
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda x:x.id==guild_id, client.guilds)

        name = payload.emoji.name
        goodRole = discord.utils.get(guild.roles, name = ROLE_TO_ADD)#replace
        member = discord.utils.find(lambda x:x.id == payload.user_id, guild.members)
        if name == EMOJI_TO_REACT_TO:#replace
            role = discord.utils.get(guild.roles, name = ROLE_TO_REMOVE)#replace
            if goodRole is not None and member is not None:
                await member.add_roles(goodRole)
        else:
            role = discord.utils.get(guild.roles, name = payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda x:x.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
#--------------------------COMMANDS-------------------------------
#makes bot do stuff (if it can)

@client.command() #these are stuff that get used with command prefix
async def ping(ctx):#ctx = context? idk bro
    await ctx.send(f'Pong :P {round(client.latency * 1000)}ms') #sends :P to the channel, latency is how long it takes to send stuff

@client.command(aliases = ['8ball', 'ball'])#this is list of all other commands that can be used to write this command
async def _8ball(ctx, *,question):#because function can't start with 8, * allows to take in multiple params as one
    responses = [
        "Yes",
        "No",
        "I give up",
        "Whatever math time",
        "Idk",
        "Maybe",
        "Zzzz",
        "42",
        "Low batteeeeeeer- bleh XP",
        "Error: Wifi connection unstable",
        "404 answer not found",
        ".....lagging"
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages = True)#only works when user has permissions
async def clear(ctx, amount = 2): #clears [amount] messages, will default as 2 when nothing is specified
    await ctx.channel.purge(limit=amount + 1)#ctx, access channel, purge function, destroys amount

#kick and ban
@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):#* is actually really useful wow 
    await member.kick(reason = reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):#* is actually really useful wow 
    await member.ban(reason = reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    memberName, memberDisc = member.split("#") #get the name and the tag

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (memberName, memberDisc):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

@client.command()
async def greet(ctx, member:discord.Member):
    await ctx.send(f'Hi {member}!')

@client.command()
async def tryStuff(ctx):
    await ctx.send("~~does~~ *this* ```python\nprint('work?')\n``` :thinking:")

@client.command(aliases = ['wet', 'waters', 'dry'])
async def water(ctx):
    for i in range(20):
        await ctx.send("WATER IS WET!!!💧💦💧")

@client.command(aliases = ['burn', 'burned', 'burnt', 'burning', 'fires'])
async def fire(ctx):
    for i in range(20):
        await ctx.send("FIRE IS BURNT!!!🔥🔥🔥")

def isItMe(ctx):
    return ctx.author.id == USER_ID # replace that with a specific user ID, will restrict who is capable of using that command

@client.command()
@commands.check(isItMe)#make specific to a certain user
async def exposeFun(ctx):
    await ctx.send(f'Salute {ctx.author}')

@client.command()
async def changePrefix(ctx, newPrefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = newPrefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)

    await ctx.send('Prefix changed to ' + newPrefix)

#--------------------------COGS-----------------------------------
@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f'Loaded {extension}')

@client.command()
async def unload(ctx, extension): #unloads a class file of events
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send(f'Unloaded {extension}')

@client.command()
async def reload(ctx, extension): #unloads a class file of events then loads it back
    client.unload_extension(f'Cogs.{extension}')
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f"Reloaded {extension}")

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

#-------------------------TASKS-----------------------------------
@tasks.loop(seconds = 10)
async def change_status():
    await client.change_presence(activity = discord.Game(next(status)))
    

#-------------------SPECIFIC ERROR HANDLING------------------------
@greet.error
async def greet_error(ctx, error):
    await ctx.send('Please add a member')
    
# Put your own bot token here instead of TOKEN
client.run(TOKEN)# stick in the token (basically gives access to the bot), run client, magic!