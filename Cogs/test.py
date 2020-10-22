# test.py
# 2020/08/25
# stan SCP-049
# testing cogs, cogs are useful when being too lazy to rerun the bot :P (literally just a big dump of random functions for testing)

import discord
from discord import File
import random
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Events
    """
    @commands.Cog.listener()#necessary for cog events
    async def on_message(self, message):
        if (not message.author.id == BOT_ID):
            channel = discord.utils.get(self.client.get_all_channels(), guild__name = SERVER, name = CHANNEL)
            await channel.send(f"{message.author} sent: " + message.content)
    """
    #Commands   
    @commands.command()
    #@commands.check(ctx.author.id == ID_OF_PERSON_WHO_CAN_USE)
    async def talk(self, ctx, user, *, talk):
        person = None
        for member in self.client.get_all_members():
            if str(member) == user:
                person = member
        if member is not None:
            await person.send(talk)

    @commands.command()
    async def channel(self, ctx):
        await ctx.send("<#CHANNEL_ID>!")

    @commands.command(aliases = ["picture", "pic"])
    async def gif(self, ctx):
        response = [
            "Stealin' yo sandwich\nhttps://media0.giphy.com/media/XGVAtWJuWrcsSgJ1Gk/giphy.gif",
            "Skateboardzzzz\nhttps://media2.giphy.com/media/jS8ehyobAA7ARDKx3B/giphy.gif",
            "You're mean >:(\nRevenge.....\nhttps://media3.giphy.com/media/L3Laf82vGo46iPoN8Y/giphy.gif",
            "Zzzz.... me wanna sweep\nhttps://media0.giphy.com/media/hUG7CRdQt2F8VZdyGQ/giphy.gif",
            "Dunna dunna yeah >:D\nhttps://media0.giphy.com/media/RiyhV8m4vIa1ejSlOI/giphy.gif",
            "Boing! Boing!\nHehe\nhttps://media1.giphy.com/media/MXWT6G23gJucdVKpGO/giphy.gif",
            "Join ussssss\nCommunism\nhttps://c10.patreonusercontent.com/3/eyJ3Ijo0MDB9/patreon-media/p/reward/4538298/9c18718aa3de471d95c289b9d570369e/1.gif?token-time=2145916800&token-hash=GqXg3lnvNGQRXUijieC5Rb9UDeG52XJt8zmr1b--byo%3D"
        ]
        await ctx.send(random.choice(response))

    @commands.command()
    async def file(self, ctx):
        file = discord.File("./triANGLES.png",  filename = "triANGLES.png")
        #fix the thing later
        await ctx.send("triangles", file = file)
        #figure out how to send file from web later
        #await ctx.send("lol", file=discord.File("https://cloud.netlifyusercontent.com/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/3458ed80-d139-49df-b055-512c639735f2/136.jpg"))

    @commands.command()
    async def link(self, ctx):
        await ctx.send("https://www.webtoons.com/en/challenge/the-doodle-demon/list?title_no=347043&page=1")

def setup(client):
    client.add_cog(Test(client))