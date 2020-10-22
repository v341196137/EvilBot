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