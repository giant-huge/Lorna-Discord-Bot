import ffmpeg as ffmpeg
import discord
from discord.ext import commands
import youtube_dl

import os
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
WEATHER_TOKEN = os.getenv('WEATHER_TOKEN')

bot = commands.Bot(command_prefix='^')

server_id = 799333787388739654
channel_id = 802340305118429249

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
    print('Bot is Online!')


@bot.event
async def on_message(message):
    server = bot.get_guild(server_id)
    channel = server.get_channel(channel_id)
    if not message.author.bot:
        await channel.send(message.content)


@bot.event
async def on_message(message):
    if message.content == 'hannah':
        await message.channel.send('I am here my liege, what you do need assistance with?')
        await message.channel.send('Do ^help for a list of commands.')
    await bot.process_commands(message)


@bot.command()
async def play(ctx, url : str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send("Wait for the music to stop please and if your in such a rush use the ^stop command.")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Music Bot VC')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)


    ydl_opts = {
        'format': 'bestaudio/best',
        "postprocessors": [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'song.mp3')
    voice.play(discord, ffmpeg('song.mp3')

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('I am not connected to the voice channel love, try the ^join command')


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('No audio is playing love, are you alright? :ms_hannah_paint: ')


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


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
async def contacthannah(ctx):
    await ctx.send('Hannah is from Essex, UK. She is 18 years of age.')
    await ctx.send('Here is her email: hannahstewart2028@gmail.com')


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
    await ctx.send(
        'Dyvor Records, a label founded with the goal to release top quality music from emerging artists all over the world.')
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
    await ctx.send(
        'JAAMS is a joint project by American label exec Andreas Von Dyvor and Portuguese producer Jay Alex. They have known eachother since late 2017, stay tuned for new releases!')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('**Current Discography:**')
    await ctx.send('Papa Putin feat. Andreas Von Dyvor (04-07-2020) [Single]')


@bot.command()
async def karenvegas(ctx):
    await ctx.send(
        'Karen Vegas, while her true identity is currently a closely guarded secret by the Dyvor Records team, she is from the EU and she is speculated to be twenty five years of age.')
    await ctx.send('---------------------------------------------------------')
    await ctx.send('**Current Discography:**')
    await ctx.send('Promises (?) [Single, to be re-released late Q1 2021]')


@bot.command()
async def latest(ctx):
    await ctx.send('https://ffm.to/avd-benefits-ep')


@bot.command()
async def epic(ctx):
    await ctx.send('F off Bruv, go back to whatever gutter you came from.')
    await ctx.send('Tosser. **spits on ground**')
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/screenshot-27.png?w=897')


@bot.command()
async def soundcloud(ctx):
    await ctx.send('Andreas Von Dyvor: https://soundcloud.com/dyvor-music')
    await ctx.send('Dyvor Records: https://soundcloud.com/dyvor-records')


@bot.command()
async def miketyson(ctx):
    await ctx.send('**EXPERIENCE THE TOAD** :eye: :frog:')
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/mike-tyson.jpg?w=512')


@bot.command()
async def hungry(ctx):
    await ctx.send('**YOU THINK THIS IS A RESTURANT MATE? GO GET A JOB TOSSER')
    await ctx.send(':anger:')


@bot.command()
async def tiktok(ctx):
    await ctx.send('Are you serious rn love? TikTok?!')
    await ctx.send(
        'Nvm, here you go :stuck_out_tongue_winking_eye: : https://nogood.io/wp-content/uploads/2019/09/TikTokFeatureImage-3000x1500.jpg')


@bot.command()
async def emergency(ctx):
    await ctx.send('Oh')
    await ctx.send('emergency? aw- yeah sorry no :lips:')


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
    await ctx.send('On what exactly?')
    await ctx.send('**this be a simulation**')


@bot.command()
async def spanish(ctx):
    await ctx.send('Q lo q mani? Y este?!!!')
    await ctx.send('Q hombre, dios mio! :heart_eyes: :kiss: me llamas mas tarde papi :smirk:')
    await ctx.send('Call me: 0908 145 4754')


@bot.command()
async def uk(ctx):
    await ctx.send('UK? Basically :england: (feat.) :scotland: :wales: :northen_ireland_flag_not_found:')


@bot.command()
async def french(ctx):
    await ctx.send('Hannah est française maintenant,')
    await ctx.send('Achetez-lui un sac Burkin, si possible je voudrais celui-ci:')
    await ctx.send('https://i.insider.com/5ec717884dca6806e011dd9a?width=700&format=jpeg&auto=webp')


@bot.command()
async def lgbt(ctx):
    await ctx.send('You forgot QIA+.')
    await ctx.send('Any extra letters will be added en el proximo patch, cest bien mon ami?')
    await ctx.send('I think you broke my language codex, если ты идиот скажи да?')


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
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/donna-did-not-pick-up.gif?w=320')


@bot.command()
async def naw(ctx):
    await ctx.send('I literally do not need your opinion')
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/naw-reaction.jpg?w=828')


@bot.command()
async def smash(ctx):
    await ctx.send(':love_letter: Come here!')
    await ctx.send('https://mshannahbotassets.files.wordpress.com/2021/02/smash-hannah.jpeg?w=1024')


@bot.command()
async def sing(ctx):
    await ctx.send('I tried:')
    await ctx.send('https://drive.google.com/file/d/13voSmZvwiqJoOGlulDZO9biwC3mJf207/view?usp=sharing')


@bot.command()
async def savage(ctx):
    await ctx.send('https://drive.google.com/file/d/1rWtNr-kICCa5MRl8DigqcluoMOzsa682/view?usp=sharing')


@bot.command()
async def calc(ctx, expression: str):
    try:
        x = eval(expression)
        await ctx.send(str(x))
    except ArithmeticError:
        await ctx.send('that is a not valid expression my love.')


if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
