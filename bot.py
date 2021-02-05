import discord
from discord.ext import commands

import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

bot = commands.Bot(command_prefix='^')

server_id = 799333787388739654
channel_id = 802340305118429249


def get_weather_api(token: str, city: str):
    with requests.get(
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric') as req:
        if req.status_code == 200:
            return req.json()
        if req.status_code == 404:
            return False
        else:
            return False


@bot.event
async def on_ready():
    print('Bot is Online!')


@bot.event
async def on_message(message):
    server = bot.get_guild(server_id)
    channel = server.get_channel(channel_id)
    if not message.author.bot:
        await channel.send(message.content)


@bot.event
async def on_message(message):
    if message.content == 'test':
        await message.channel.send('Testing 1 2 3')
    await bot.process_commands(message)



@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def lol(ctx):
    await ctx.send('lmao')


@bot.command()
async def love(ctx):
    await ctx.send('I love you! :kiss:')


@bot.command()
async def email(ctx):
    await ctx.send('Andreas Von Dyvor: dyvormusic@gmail.com')
    await ctx.send('Dyvor Records: dyvorrecords@gmail.com')


@bot.command()
async def youtube(ctx):
    await ctx.send('Andreas Von Dyvor: https://www.youtube.com/channel/UCKnmmN818_bESzsc5xFGXdA')
    await ctx.send('Dyvor Records: https://www.youtube.com/channel/UCpppRmlQOrG9S6arbQy8RAg')


@bot.command()
async def hannah(ctx):
    await ctx.send('Hannah is from Essex, UK. She is 18 years of age.')
    await ctx.send('Here is her email: hannahstewart2028@gmail.com')


@bot.command()
async def instagram(ctx):
    await ctx.send('Andreas Von Dyvor: https://www.instagram.com/andreasvondyvor')
    await ctx.send('Dyvor Records: https://www.instagram.dyvorrecords')


@bot.command()
async def artists(ctx):
    await ctx.send('JAAMS (previously Jay Alex)')
    await ctx.send('Karen Vegas')


@bot.command()
async def jaams(ctx):
    await ctx.send(
        'JAAMS is a joint project by American label exec Andreas Von Dyvor and Portuguese producer Jay Alex. They have known eachother since late 2017, stay tuned for new releases!')
    await ctx.send('Current Discography: Papa Putin (featuring Andreas Von Dyvor')


@bot.command()
async def karenvegas(ctx):
    await ctx.send(
        'Karen Vegas, who is she? Her true identity is currently a closely guarded secret by the Dyvor Records team. She is from the EU, and she is estimated to be twenty five years of age.')
    await ctx.send('Curent Discography: Promises')


@bot.command()
async def latest(ctx):
    await ctx.send('https://ffm.to/avd-benefits-ep')


@bot.command()
async def epic(ctx):
    await ctx.send('F off Bruv, go back to whatever gutter you came from.')
    await ctx.send('Tosser. **spits on ground**')
    await ctx.send('https://drive.google.com/file/d/1y4NbxP9ekViKPnxdID_rpCH28OWUOoSE/view?usp=sharing')


@bot.command()
async def soundcloud(ctx):
    await ctx.send('Andreas Von Dyvor: https://soundcloud.com/dyvor-music')
    await ctx.send('Dyvor Records: https://soundcloud.com/dyvor-records')


@bot.command()
async def miketyson(ctx):
    await ctx.send('**EXPERIENCE THE TOAD** :eye: :frog:')


@bot.command()
async def hungry(ctx):
    await ctx.send('**YOU THINK THIS IS A RESTURANT MATE? GO GET A JOB TOSSER')
    await ctx.send(':anger:')


@bot.command()
async def tiktok(ctx):
    await ctx.send('Are you serious rn bruv?')
    await ctx.send('Nvm, here you go: https://nogood.io/wp-content/uploads/2019/09/TikTokFeatureImage-3000x1500.jpg')


@bot.command()
async def emergency(ctx):
    await ctx.send('Oh')
    await ctx.send('emergency? aw- yeah sorry no :lips:')


@bot.command()
async def serverinfo(ctx):
    await ctx.send('You want info?')
    await ctx.send('Dyvor Records: The official discord server of Dyvor Records')


@bot.command()
async def covid(ctx):
    await ctx.send('Never Forget to Mask up! :mask:')
    await ctx.send('https://coronavirus.thebaselab.com')


@bot.command()
async def info(ctx):
    await ctx.send('On what exactly?')
    await ctx.send('**this be a simulation**')


@bot.command()
async def spanish(ctx):
    await ctx.send('Q lo q mani? Y este?!!!')
    await ctx.send('Q hombre, dios mio! :heart_eyes: :kiss: me llamas mas tarde papi :smirk:')


@bot.command()
async def UK(ctx):
    await ctx.send('UK? Basically :england: (feat.) :scotland: :wales: :northen_ireland_flag_not_found:')


@bot.command()
async def french(ctx):
    await ctx.send('Hannah est française maintenant,')
    await ctx.send('Achetez-lui un sac Burkin.')


@bot.command()
async def lgbt(ctx):
    await ctx.send('You forgot QIA+ mate.')
    await ctx.send('extra letters will be added en el proximo patch, cest bien mon ami?')
    await ctx.send('I think you broke my language codex, если ты идиот скажи да')


@bot.command()
async def booty(ctx):
    await ctx.send(':peach:')
    await ctx.send('^smash or ^naw?')


@bot.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@bot.command()
async def donna(ctx):
    await ctx.send('@donna#8475')
    await ctx.send('https://drive.google.com/file/d/1bxXhUDdBcOOythf-s7bFLfbNgY0LsSXA/view?usp=sharing')


@bot.command()
async def naw(ctx):
    await ctx.send('I literally do not need your opinion')
    await ctx.send('https://drive.google.com/file/d/1NaBwdvM5qP0hr-gSUMn7ejH-T3Ow3llw/view?usp=sharing')


@bot.command()
async def smash(ctx):
    await ctx.send(
        ':love_letter: say less: https://drive.google.com/file/d/1EEj6YCTw9uTQlzcTVv2PYRiTccown35J/view?usp=sharing')


@bot.command()
async def sing(ctx):
    await ctx.send('Mang I got you: https://drive.google.com/file/d/13voSmZvwiqJoOGlulDZO9biwC3mJf207/view?usp=sharing')


@bot.command()
async def savage(ctx):
    await ctx.send('https://drive.google.com/file/d/1rWtNr-kICCa5MRl8DigqcluoMOzsa682/view?usp=sharing')


@bot.command()
async def calc(ctx, expression: str):
    try:
        x = eval(expression)
        await ctx.send(str(x))
    except ArithmeticError:
        await ctx.send('that is a not valid expression')


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
