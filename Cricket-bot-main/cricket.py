import nextcord
from nextcord.ui import Button, View 
from nextcord.utils import get
from nextcord.ext import commands
import os
from dotenv import load_dotenv 
import wikipedia
import smtplib 
import datetime
import webbrowser
import youtube_dl
import humanfriendly
import time
import random
import asyncio

intents=nextcord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="$", intents=intents)
gameOver = True
cricket_p1 = ""
cricket_p2 = ""

@client.command()
async def on_ready():
    print("Bot just landed on the server!")

@client.command()
async def cricket(ctx, p1 : nextcord.Member, p2 : nextcord.Member):   
    global gameOver
    if gameOver and p1 != await client.fetch_user(949215188672974871) and p2 != await client.fetch_user(949215188672974871):
        global runs1
        global runs2
        global wickets1
        global wickets2
        global balls1
        global balls2
        global score1
        global score2
        global length1
        global length2
        global cricket_p1
        global cricket_p2
        global target
        global ing1
        gameOver = False
        ing1 = False
        runs1 = ""
        runs2 = ""
        score1 = 0
        score2 = 0
        target = 0
        wickets1 = 0
        wickets2 = 0
        balls1 = ""
        balls2 = ""
        length1 = 0
        length2 = 0
        cricket_toss = random.randint(1, 2)
        if cricket_toss == 1:
            cricket_p1 = p1
            cricket_p2 = p2
        else:
            cricket_p1 = p2
            cricket_p2 = p1
        myEmbed = nextcord.Embed(title = "World Icc Discord Tournament", description="🎮Cricket🎮", color=0xffff00)
        myEmbed.add_field(name="RULES:-" ,value=f"1.Press the button only once.\n2. {cricket_p1.mention} will bat first.\n3.{cricket_p2.mention} will ball now.\n4. {cricket_p1.mention} should click button immediately while {cricket_p2.mention} will click after 3sec!\n5. Click the button only once!", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        time.sleep(15)
        await play(ctx)
    else:
        await ctx.send(f"A Game is already in progress between {p1.mention} and {p2.mention}!")
        
async def play(ctx):
    global cricket_p1
    global cricket_p2
    button = Button(label="One", style = nextcord.ButtonStyle.green, emoji="1️⃣")
    button2 = Button(label="Two", style = nextcord.ButtonStyle.green, emoji="2️⃣")
    button3 = Button(label="Three", style = nextcord.ButtonStyle.blurple, emoji="3️⃣")
    button4 = Button(label="Four", style = nextcord.ButtonStyle.blurple, emoji="4️⃣")
    button5 = Button(label="Six", style = nextcord.ButtonStyle.danger, emoji="6️⃣")
    view = View(timeout=100)
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "One"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "One"
            move2(ugh)
    button.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Two"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Two"
            move2(ugh)
    button2.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Three"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Three"
            move2(ugh)
    button3.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Four"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Four"
            move2(ugh)
    button4.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Six"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Six"
            move2(ugh)
    button5.callback = button_callback
    await ctx.send(view=view)

#runs 
def move1(abc):
    global runs1
    global score1
    runs1 = abc
    if abc == "One":
        score1+=1
    elif abc == "Two":
        score1+=2
    elif abc == "Three":
        score1+=3
    elif abc == "Four":
        score1+=4
    elif abc == "Six":
        score1+=6
    print(runs1)
    print(score1)
    
#balls
def move2(ugh):
    global balls1
    balls1 = ugh
    print(balls1)
    
async def match(ctx):
    global runs1
    global balls1
    global score1
    global wickets1
    global length1
    global cricket_p1
    global cricket_p2
    if runs1 == "One" and balls1 == "One":
        wickets1 +=1
        score1-=1
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} One ⚔ One {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        wickets1 +=1
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Two" and balls1 == "Two":
        wickets1 +=1
        score1 -=2
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Two ⚔ Two {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Three" and balls1 == "Three":
        wickets1 +=1
        score1-=3
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Three ⚔ Three {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Four" and balls1 == "Four":
        wickets1 +=1
        score1 -=4
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Four ⚔ Four {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Six" and balls1 == "Six":
        wickets1 +=1
        score1 -=6
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Six ⚔ Six {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif balls1 == "":
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} {runs1} ⚔ Did not respond! {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 != balls1:
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} {runs1} ⚔ {balls1} {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
        
async def pointcount(ctx):
    global wickets1
    global length1
    global score1
    global cricket_p1
    global cricket_p2
    global target
    global gameOver
    
    if ing1==False:
        if wickets1==3 or length1==10 :
            score1+=1
            myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Innings One has come to an end!", color=0xffff00)
            myEmbed.add_field(name="Innings 1 Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
            myEmbed.add_field(name="Innings 2 on the Way!", value=f"{cricket_p2.mention} will bat now!\n{cricket_p1.mention} will ball now!")
            myEmbed.add_field(name="Target!", value=f"{cricket_p2.mention} have to score {score1} in 10 balls with 3 wickets in hands!\nCan they do it??")
            myEmbed.set_author(name="Cricket bot#0162")
            await ctx.send(embed=myEmbed)
            await intchange(ctx)
        else:
            await play(ctx)
            
    elif ing1 == True:
        if wickets1==3 or length1==10 :
            myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Innings Two has come to an end!", color=0xffff00)
            myEmbed.add_field(name="Innings 2 Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
            myEmbed.add_field(name="Winner!", value=f"{cricket_p2.mention} defends bravely as {cricket_p1.mention} falls short to chase the target", inline=False)
            myEmbed.set_author(name="Cricket bot#0162")
            await ctx.send(embed=myEmbed)
            gameOver = True
        elif target <= score1:
            myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Innings Two come to an end!", color=0xffff00)
            myEmbed.add_field(name="Innings 2 Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
            myEmbed.add_field(name="Winner!", value=f"{cricket_p1.mention} beat the crap out of {cricket_p2.mention} as they finish off in style!", inline=True)
            myEmbed.set_author(name="Cricket bot#0162")
            await ctx.send(embed=myEmbed)
            gameOver = True
        else:
            await play(ctx)
        
async def intchange(ctx):
    global cricket_p1
    global cricket_p2
    global score1
    global score2
    global length1
    global length2
    global target
    global ing1
    global wickets1
    global wickets2
    wickets1 = wickets2
    cricket_p1,cricket_p2 = cricket_p2,cricket_p1
    target = score1
    score1 = score2
    length1 = length2
    ing1 = True
    await asyncio.sleep(5)
    await play(ctx)

@client.command()
async def endgame(ctx):
    global cricket_p1
    global cricket_p2 
    global gameOver
    if ctx.author == cricket_p1 or ctx.author == cricket_p2:
        num =random.randint(1, 2)
        if num == 1:
            await ctx.send(f"{cricket_p1.mention} Wins the Game By Random choice")
        else:
            await ctx.send(f"{cricket_p2.mention} Wins the Game By Random choice")
        gameOver = True
        await ctx.send("Game Over.\nYou may start a new one!")
    else:
        await ctx.send(f"You can only end the game played by you!\nCurrently the game is being played between {cricket_p1.mention} and {cricket_p2.mention}")
            
client.run("******BOT-TOKEN******")
