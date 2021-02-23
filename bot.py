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
    await bot.change_presence(activity=discord.Game(name="^help"))
    print('Assistant Bot v3009 is ready for deployment!!!')


@bot.event
async def on_message(message):
    server = bot.get_guild(server_id)
    channel = server.get_channel(channel_id)
    if not message.author.bot:
        await channel.send(message.content)


@bot.event
async def on_message(message):
    if message.content == 'assistant':
        await message.channel.send(f'Hello! Welcome to Dyvor Records. What you do need ^help with?')
    if message.content == 'god':
        await message.channel.send(f'**I LOVE DYVOR! HE LITERALLY CREATED ME.**')
    if message.content == 'f':
        await message.channel.send(f'Fuck You.')
    if message.content == 'sex':
        await message.channel.send(f'No thank you.')
    await bot.process_commands(message)


@bot.command()
async def ride(ctx):
    await ctx.send("It's time to ride... you're not recording, right?")


@bot.command()
async def emoji(ctx, name):
    await ctx.send(str(find_by_name(find_by_name(bot.guilds, 'Dyvor Records').emojis, name)))


@bot.command()
async def ping(ctx):
    await ctx.send(f'Assistant Bot Latency is currently: {bot.latency}')


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
    await ctx.send('In chronological order.')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('Andreas Von Dyvor')
    await ctx.send('JAAMS (previously Jay Alex)')
    await ctx.send('Karen Vegas')
    await ctx.send('Jausla')


@bot.command()
async def labelinfo(ctx):
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
async def jausla(ctx):
    await ctx.send('Jausla. Jausla?')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('**Current Discography:**')
    await ctx.send('Not available.')


@bot.command()
async def latest(ctx):
    await ctx.send('https://ffm.to/avd-benefits-ep')


@bot.command()
async def rave(ctx):
    # This code will say "Hi, @username!"
    # this uses an 'f' befoe a string so I can input the username
    # ctx has many propertys, including .send .author and .content (there are more)
    await ctx.send(f"Join {ctx.author.mention} for an impromptu rave!")


@bot.command()
async def soundcloud(ctx):
    await ctx.send('Andreas Von Dyvor: https://soundcloud.com/dyvor-music')
    await ctx.send('Dyvor Records: https://soundcloud.com/dyvor-records')


@bot.command()
async def invite(ctx):
    await ctx.send('https://discord.gg/asPGWf3PH3')


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
    await ctx.send('The official discord server of Dyvor Records.')


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
