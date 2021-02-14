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
    print('Hannah (the assistant) Bot is ready for deployment!')


@bot.event
async def on_message(message):
    server = bot.get_guild(server_id)
    channel = server.get_channel(channel_id)
    if not message.author.bot:
        await channel.send(message.content)


@bot.event
async def on_message(message):
    if message.content == 'assistant':
        await message.channel.send('I am here, what you do need assistance with?')
        await message.channel.send('Do ^help for a list of commands.')
    await bot.process_commands(message)


@bot.command()
async def eclipse(ctx):
    await ctx.send('Yeah they have another me there, join here: https://discord.gg/T7Pu6cqnh9')


@bot.command()
async def emoji(ctx, name):
    await ctx.send(str(find_by_name(find_by_name(bot.guilds, 'Dyvor Records').emojis, name)))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def lol(ctx):
    await ctx.send('lmao?')


@bot.command()
async def love(ctx):
    await ctx.send('Please stop.')


@bot.command()
async def email(ctx):
    await ctx.send('Andreas Von Dyvor: dyvormusic@gmail.com')
    await ctx.send('Dyvor Records: dyvorrecords@gmail.com')


@bot.command()
async def youtube(ctx):
    await ctx.send('Andreas Von Dyvor: https://www.youtube.com/channel/UCKnmmN818_bESzsc5xFGXdA')
    await ctx.send('Dyvor Records: https://www.youtube.com/channel/UCpppRmlQOrG9S6arbQy8RAg')


@bot.command()
async def contactbot(ctx):
    await ctx.send('You cannot contact me, I am not real.')


@bot.command()
async def instagram(ctx):
    await ctx.send('Andreas Von Dyvor: https://www.instagram.com/andreasvondyvor')
    await ctx.send('Dyvor Records: https://www.instagram.dyvorrecords')


@bot.command()
async def artists(ctx):
    await ctx.send('Andreas Von Dyvor')
    await ctx.send('JAAMS (previously Jay Alex)')
    await ctx.send('Karen Vegas')


@bot.command()
async def dyvorrecords(ctx):
    await ctx.send('Dyvor Records, a label founded with the goal to release top quality music from emerging artists,')
    await ctx.send('all over the world.')
    await ctx.send('To date all of the labels releases have over 3 Million streams and over 1 Million downloads.')
    await ctx.send('To contact the label and Dyvor himself, do ^email')


@bot.command()
async def andreasvondyvor(ctx):
    await ctx.send('The founder and current CEO of Dyvor Records')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('**Current Discography:**')
    await ctx.send('SPACE (05-17-2019) [Single]')
    await ctx.send('Something (In It) (10-23-2019) [Single]')
    await ctx.send('WTFISHOUSEMUSIC (01-23-2020) [Single]')
    await ctx.send('Papa Putin feat. Andreas Von Dyvor (04-07-2020) [Single]')
    await ctx.send('Benefits (04-17-2020) [EP, 5 Tracks]')


@bot.command()
async def jaams(ctx):
    await ctx.send('JAAMS is a duo created by American label exec Andreas Von Dyvor and,')
    await ctx.send('Portuguese producer Jay Alex. They have known eachother since 2017.')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('**Current Discography:**')
    await ctx.send('Papa Putin feat. Andreas Von Dyvor (04-07-2020) [Single]')


@bot.command()
async def karenvegas(ctx):
    await ctx.send('Karen Vegas, while her true identity is a closely guarded secret,')
    await ctx.send('she is from the EU and she is speculated to be twenty five years of age.')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('**Current Discography:**')
    await ctx.send('Promises (?) [Single, to be re-released late Q1 2021]')


@bot.command()
async def latest(ctx):
    await ctx.send('https://ffm.to/avd-benefits-ep')


@bot.command()
async def f(ctx):
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/screenshot-27.png?w=897')


@bot.command()
async def soundcloud(ctx):
    await ctx.send('Andreas Von Dyvor: https://soundcloud.com/dyvor-music')
    await ctx.send('Dyvor Records: https://soundcloud.com/dyvor-records')


@bot.command()
async def invite(ctx):
    await ctx.send('https://discord.gg/asPGWf3PH3')


@bot.command()
async def hungry(ctx):
    await ctx.send('Same, takeout?')


@bot.command()
async def dance(ctx):
    await ctx.send('https://wmpics.pics/di-GRFS.gif')


@bot.command()
async def emergency(ctx):
    await ctx.send('Call 911.')


@bot.command()
async def serverinfo(ctx):
    await ctx.send('Dyvor Records: The official discord server of Dyvor Records')


@bot.command()
async def covid(ctx):
    await ctx.send('Never forget your mask! :mask:')
    await ctx.send('https://coronavirus.thebaselab.com')
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/masks.png?w=318')


@bot.command()
async def info(ctx):
    await ctx.send('Not specific enough, try ^help for more info commands :sunglasses:')


@bot.command()
async def spanish(ctx):
    await ctx.send('Hola!')


@bot.command()
async def french(ctx):
    await ctx.send('Je suis française maintenant.')


@bot.command()
async def lgbt(ctx):
    await ctx.send('You forgot QIA+.')
    await ctx.send('Any extra letters will be added en el proximo patch, cest bien mon ami?')
    await ctx.send('I think you broke my language codex, если ты идиот скажи да?')


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
        await ctx.send('that is a not valid expression my love.')


if __name__ == '__main__':
    bot.run('ODA5ODgzNjg5NDcwOTE4NjY2.YCbk9g.OngsIQ_2a0qZtMv3Aa61UlRrhfs')
