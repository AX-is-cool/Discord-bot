import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a SİGMA bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 10):
    await ctx.send("he" * count_heh)

@bot.command()
async def who(ctx):
    await ctx.send(f'Me!')

@bot.command()
async def why(ctx):
    await ctx.send(f'BeCaUsE I sAiD sO')

@bot.command()
async def never(ctx):
    await ctx.send(f'ever')

@bot.command()
async def Dude(ctx):
    await ctx.send(f'Yes, dude?')

@bot.command()
async def bot(ctx):
    await ctx.send(f'Looking at how you play games, you ARE a bot!')

@bot.command()
async def open(ctx):
    await ctx.send(f'Close')

@bot.command()
async def sigma(ctx):
    await ctx.send(f'I am!')

@bot.command()
async def cool(ctx):
    await ctx.send(f'Thank you')

@bot.command()
async def sweet(ctx):
    await ctx.send(f'AWWW, THANK YOUUU')

@bot.command()
async def candy(ctx):
    await ctx.send(f'stop, you are making me hungry')

@bot.command()
async def bread(ctx):
    await ctx.send(f'Oh I love that!')

@bot.command()
async def angry(ctx):
    await ctx.send(f'AYO CHİLLL')

@bot.command()
async def cheetos(ctx):
    await ctx.send(f'mmm, tasty')

@bot.command()
async def goodnight(ctx):
    await ctx.send(f'Always waiting for you!')

@bot.command()
async def get_out(ctx):
    await ctx.send(f'get out')

@bot.command()
async def bro(ctx):
    await ctx.send(f'Yes bro, anything I can help you with?')

@bot.command()
async def no(ctx):
    await ctx.send(f'yes')

@bot.command()
async def go(ctx):
    await ctx.send(f'come')

@bot.command()
async def copy(ctx):
    await ctx.send(f'paste')

@bot.command()
async def destroy(ctx):
    await ctx.send(f're-build')

@bot.command()
async def grade_3_bot(ctx):
    await ctx.send(f'with this treasure I summon, mahoragaaaaa!')

@bot.command()
async def wobble(ctx):
    await ctx.send(f'jiggle')

@bot.command()
async def wiggle(ctx):
    await ctx.send(f'wobble')

@bot.command()
async def jiggle(ctx):
    await ctx.send(f'wiggle')

@bot.command()
async def word(ctx):
    await ctx.send(f'Why did you say that dude? Just, why?')

@bot.command()
async def talk(ctx):
    await ctx.send(f'Hello, I am talking, talking is realy good and talking is so fun that I cant stop taking!')

@bot.command()
async def who_are_you(ctx):
    await ctx.send(f'I, am steve, a.k.a. a bot that is smart')

@bot.command()
async def reference(ctx):
    await ctx.send(f'I have a lot of those! Try Who_are_you')



bot.run("TOKEN")
