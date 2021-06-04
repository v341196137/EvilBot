# Games.py
# 2020/08/28
# Imaginary brain cells
# Let's make a cog to add some games to Discord bots because that's fun

import discord
from discord.ext import commands
from GameClasses import Hangman
from GameClasses import Math
from GameClasses import Connect4

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.games = {}
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.games[ctx.channel] is not None:
            msg = ctx.content
            if len(msg) == 1:
                if type(self.games[ctx.channel]) == Hangman.Hangman:
                    self.games[ctx.channel].guessLetter(msg)
                    await ctx.channel.send(self.games[ctx.channel].returnGuess())
                    if self.games[ctx.channel].checkWin():
                        await ctx.channel.send("Good job!")
                        del self.games[ctx.channel]
                    elif self.games[ctx.channel].checkLoss():
                        await ctx.channel.send(":( y'all suck\nThe word/phrase was: " + self.games[ctx.channel].word)
                        del self.games[ctx.channel]
                if type(self.games[ctx.channel]) == Connect4.Connect4:
                    if msg.isnumeric():
                        if (ctx.author == self.games[ctx.channel].player1 and self.games[ctx.channel].turn%2 == 0) or (ctx.author == self.games[ctx.channel].player2 and self.games[ctx.channel].turn%2 == 1):
                            self.games[ctx.channel].move(int(msg))
                            await ctx.channel.send(self.games[ctx.channel].be_string_lol())
            if type(self.games[ctx.channel]) == Math.Math and (msg.isnumeric() or (msg[0] == '-' and (msg[1:].isnumeric()))):
                if(self.games[ctx.channel].checkAnswer(int(msg))):
                    await ctx.channel.send(f"Good job! {ctx.author}")
                    del self.games[ctx.channel]

    @commands.command(aliases = ["hm"])
    async def hangman(self, ctx):
        person = ctx.author
        await person.send("What communistic word would you like the peasants under your rule to guess?")
        #msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
        message = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        self.games[ctx.channel] = Hangman.Hangman(message.content)
        await ctx.send("Let the evil games begin!\n" + self.games[ctx.channel].returnGuess())

    @commands.command()
    async def math(self, ctx):
        self.games[ctx.channel] = Math.Math()
        await ctx.send(str(self.games[ctx.channel]))

    @commands.command(aliases = ["c4", "connect4"])
    async def connect_four(self, ctx, member:discord.Member, p1 = ":red_circle:", p2 = ":blue_circle:", dark=False):
        self.games[ctx.channel] = Connect4.Connect4(ctx.author, member, dark, p1, p2)
        await ctx.send(f"{ctx.author.mention} challenges {member.mention} to a game of connect 4!!!")
        await ctx.send(self.games[ctx.channel].be_string_lol())

    @commands.command(aliases = ["ttt"])
    async def tictactoe(self, ctx):
        person = ctx.author
        #have some thing to get message id then check for reaction to message and host game

    # @commands.command(aliases = ["g"])
    # async def guess(self, ctx, letter):
    #     if len(letter) == 1:
    #         if self.games[ctx.channel] is not None and type(self.games[ctx.channel]) == Hangman.Hangman:
    #             self.games[ctx.channel].guessLetter(letter)
    #             await ctx.send(self.games[ctx.channel].returnGuess())
    #             if self.games[ctx.channel].checkWin():
    #                 await ctx.send("Good job!")
    #                 del self.games[ctx.channel]
    #             elif self.games[ctx.channel].checkLoss():
    #                 await ctx.send(":( y'all suck\nThe word/phrase was: " + self.games[ctx.channel].word)
    #                 del self.games[ctx.channel]
    #     else:
    #         await ctx.send("Guess 1 letter at a time")

    @commands.command()
    async def stop(self, ctx):
        del self.games[ctx.channel]
        await ctx.send("How dare you puny mortal distrupt the rule of communism!")

def setup(client):
    client.add_cog(Games(client))
    