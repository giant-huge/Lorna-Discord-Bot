import discord
from discord.ext import commands

import requests

bot = commands.Bot(command_prefix='^')

server_id = 799333787388739654
channel_id = 802340305118429249
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
    await bot.change_presence(activity=discord.Game(name="^help, type assistant"))
    print('ASSISTANT 7 has arrived...')


@bot.event
async def on_message(message):
    server = bot.get_guild(server_id)
    channel = server.get_channel(channel_id)
    if not message.author.bot:
        await channel.send(message.content)


@bot.event
async def on_message(message):
    if message.content == 'assistant':
        await message.channel.send(f'Hello! Welcome to Ruble House. What you do need ^help with?')
    if message.content == 'god':
        await message.channel.send(f'**Very Political**')
    if message.content == 'f':
        await message.channel.send(f'Rest in Peace...')
    if message.content == 'sex':
        await message.channel.send(f'Dm me.')
    if message.content == 'drugs':
        await message.channel.send(f'When, where, and why.')
    if message.content == 'minecraft':
        await message.channel.send(f'Are you 5?')
    if message.content == 'latest':
        await message.channel.send(f'Looks like Ruble has not published any music yet.')
    if message.content == 'gay':
        await message.channel.send(f'No you.')
    if message.content == 'yo':
        await message.channel.send(f'What up?')
    if message.content == 'ty':
        await message.channel.send(f'Your Welcome.')
    if message.content == 'boi':
        await message.channel.send(f'Please use Sir.')
    if message.content == 'girl':
        await message.channel.send(f'Please use Madam.')
    if message.content == 'gurl':
        await message.channel.send(f'Please use Madam.')
    if message.content == 'sir':
        await message.channel.send(f'Good lad.')
    if message.content == 'madam':
        await message.channel.send(f'Good lass.')
    if message.content == 'who':
        await message.channel.send(f'Probably not me.')
    if message.content == 'sup':
        await message.channel.send(f'Heya')
    if message.content == 'Heya':
        await message.channel.send(f':wink:')
    if message.content == 'cringe':
        await message.channel.send(f'Visible cringe.')
    if message.content == 'trash':
        await message.channel.send(f':fire:')
    if message.content == 'dyvor':
        await message.channel.send(f'How the fuck do you know about that... who are you?')
    if message.content == 'loerna':
        await message.channel.send(f'Probably doing something high speed, not speed tho, heavens she would never!')
    if message.content == 'music':
        await message.channel.send(f'I like music aswell, I recommend you lookup AVAAVA when they drop an EP soon...')
    await bot.process_commands(message)


@bot.command()
async def ride(ctx):
    await ctx.send("Daddy?")


@bot.command()
async def emoji(ctx, name):
    await ctx.send(str(find_by_name(find_by_name(bot.guilds, 'Ruble House').emojis, name)))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Assistant Bot Latency is currently: {bot.latency}')



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
    await ctx.send('https://discord.gg/9YTsZFdtWJ')


@bot.command()
async def hungry(ctx):
    await ctx.send('You know I cannot eat right?')


@bot.command()
async def dance(ctx):
    await ctx.send('https://media.tenor.com/images/0f35f4424cd82fcd83a4d43c745424cf/tenor.gif')


@bot.command()
async def emergency(ctx):
    await ctx.send('**C a l l  9 1 1**')


@bot.command()
async def serverinfo(ctx):
    await ctx.send('The official discord server of Ruble House.')


@bot.command()
async def covid(ctx):
    await ctx.send('Never forget your mask! :mask:')
    await ctx.send('https://coronavirus.thebaselab.com')
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/masks.png?w=318')


@bot.command()
async def spanish(ctx):
    await ctx.send('No mas.')


@bot.command()
async def french(ctx):
    await ctx.send('Je ne suis française.')


@bot.command()
async def lgbt(ctx):
    await ctx.send('если ты идиот скажи.')


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
