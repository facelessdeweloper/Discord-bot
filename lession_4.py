import discord, random
from discord.ext import commands
from key_ds import *
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def coin(ctx):
    await ctx.send(random.choice(['Орёл', 'Решка']))
@bot.command()
async def game(ctx, number = 0):
    x = random.randint(1, 10)
    if number == x:
        await ctx.send('Верно!')
    else:
        await ctx.send('Попробуйте снова')
bot.run(token_ds())