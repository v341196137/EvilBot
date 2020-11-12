# Gambling.py
# 2020/10/22
# fjjfjfjflsdjf
# Organization is important

import discord
import random
from discord.ext import commands

class Gambling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coin(self, ctx):
        x = random.random()
        if(x > 0.5):
            await ctx.send("Tails")
        else:
            await ctx.send("Heads")
    
    @commands.command()
    async def dice(self, ctx, sides = 6):
        send = f"{ctx.author.mention} rolled:\n"
        if sides == 6:
            x = random.randrange(1, 7)
            if x == 1:
                send = send + "https://lh3.googleusercontent.com/proxy/WT__mbb_oO8R8xwws0z7r3AYT2mQbzgP1I5F76AmUJmaOH7cmvFrDA3UtNqJGSGfBeaYPPPJZbM3Gq-xZ99UczBU"
            elif x == 2:
                send = send + "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQNliXu6B1MtN-uKogsO4JMEXQBshp4N31Wpw&usqp=CAU"
            elif x == 3:
                send = send + "https://i.lensdump.com/i/8WUauA.png"
            elif x == 4:
                send = send + "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQA6v1iyMij_hHLCWlX7R6x9nuNLJJpsYwlLQ&usqp=CAU"
            elif x == 5:
                send = send + "https://www.clipartkey.com/mpngs/m/66-660387_dot-clipart-one-five-side-of-dice.png"
            elif x == 6:
                send = send + "https://www.clipartkey.com/mpngs/m/112-1122878_28-collection-of-six-dice-clipart-6-dots.png"
        await ctx.send(send)

    @commands.command(aliases = ['8ball', 'ball'])#this is list of all other commands that can be used to write this command
    async def _8ball(self, ctx, *,question):#because function can't start with 8, * allows to take in multiple params as one
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
    
def setup(client):
    client.add_cog(Gambling(client))