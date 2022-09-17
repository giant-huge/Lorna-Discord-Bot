import discord
from discord.ext import commands

import requests

bot = commands.Bot(command_prefix='^')

server_id = 850903993018089493
channel_id = 991327631054209175
client_id = 809883689470918666

client = discord.Client()


def get_weather_api(token: str, city: str):
    with requests.get(
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric') as req:
        if req.status_code == 200:
            return req.json()
        if req.status_code == 404:
            return False
        else:
            return False


def find_by_name(obj, name):
    for item in obj:
        if item.name == name:
            return item


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="/help, type Lorna"))
    print('Lorna v11 has arrived...')


@bot.event
async def on_message(message):
    server = bot.get_guild(server_id)
    channel = server.get_channel(channel_id)
    if not message.author.bot:
        await channel.send(message.content)


@bot.event
async def on_message(message):
    if message.content == 'Lorna':
        await message.channel.send(f'Hello! Welcome to the Discord Server. What you do need /help with?')


@bot.command()
async def ride(ctx):
    await ctx.send("Oh baby...")


@bot.command()
async def emoji(ctx, name):
    await ctx.send(str(find_by_name(find_by_name(bot.guilds, '').emojis, name)))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Lorna Bot Latency is currently: {bot.latency}')



@bot.command()
async def contactbot(ctx):
    await ctx.send('You cannot contact me, I am not real.')


@bot.command()
async def rave(ctx):
    # This code will say "Hi, @username!"
    # this uses an 'f' befoe a string so I can input the username
    # ctx has many propertys, including .send .author and .content (there are more)
    await ctx.send(f"Join {ctx.author.mention} for an impromptu rave!")


@bot.command()
async def invite(ctx):
    await ctx.send('https://discord.gg/fCUWXuVhU9')


@bot.command()
async def dance(ctx):
    await ctx.send('https://media.tenor.com/images/0f35f4424cd82fcd83a4d43c745424cf/tenor.gif')

    
@bot.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

    
@bot.command()
async def calc(ctx, expression: str):
    try:
        x = eval(expression)
        await ctx.send(str(x))
    except ArithmeticError:
        await ctx.send('I literally cannot.')


if __name__ == '__main__':
    bot.run('ODA5ODgzNjg5NDcwOTE4NjY2.YCbk9g.SYwHhy-KD19mqBQpxs8_p4lrhfQ')
