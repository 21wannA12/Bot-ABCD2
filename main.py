import discord, os, requests
from discord.ext import commands
from random import choice
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

images = os.listdir('images_meme')

images_eco = os.listdir('images')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

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
async def calk(ctx, num1 = 0, sim = 'Введите число, оператор и второе число', num2 = 0):
    if sim == '+':
        await ctx.send(num1 + num2)

    elif sim == '-':
        await ctx.send(num1 - num2)

    elif sim == '/':
        await ctx.send(num1 / num2)

    elif sim == '*':
        await ctx.send(num1 * num2)
        
    else:
        await ctx.send(sim)

@bot.command()
async def meme(ctx, num_meme = 0):
    if num_meme  >= 1 and num_meme <= len(images):
        with open(f'images/{images[num_meme -1]}', 'rb')as f:
            image = discord.File(f)
    else:
        with open(f'images/{choice(images)}', 'rb')as f:
            image = discord.File(f)

    await ctx.send(file = image)

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def info(ctx):
    with open(f'images/{choice(images_eco)}', 'rb')as f:
        image_eco = discord.File(f)
    await ctx.send('Загрязнение окружающей среды — это ущерб, наносимый природе, среде обитания вредными веществами, выбросами, отходами.')
    await ctx.send(file = image_eco)
    await ctx.send('Вы хотите узнать побольше?')

    def check(q):
        return q.author == ctx.author and q.channel == ctx.channel 
    try:
        answer = await bot.wait_for('message', check=check, timeout=30)
        if answer.content == 'да' or answer.content == 'Да': 
            await ctx.send("Тут будет да")
        else:
            await ctx.send('Вы всё ещё можете ввести команду /info!')

    except asyncio.TimeoutError:
        await ctx.send("Время вышло, попробуйте снова.")



bot.run("Your token")