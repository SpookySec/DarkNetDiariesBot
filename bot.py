
#===================#
import time
import discord
from discord.ext import commands
import discord.ext
import random
from discord.utils import get
import youtube_dl
import asyncio
import requests
import os
from lxml.html import fromstring
import requests
from datetime import datetime
from tqdm import tqdm
#===================#


#===================#
TOKEN = 'Njc2ODE5OTk5MjEzNDg2MTMw.XkMKXw.z6GDHkmw4FANc3zf5u3C0YOwCww'
BOT_PREFIX = '.'
CURRENT_TIME = datetime.now().strftime("%d/%m/%Y %H:%M")
bot = commands.Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('DarkNet Diaries'))
    os.system("clear")

    print("~#============================#~")
    print(f"[*] LOGGED IN AS : {bot.user.name} ON {CURRENT_TIME}")
    print("~#============================#~\n")
#===================#


#===================#
@bot.command(pass_context=True, aliases=['j'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    user = ctx.message.author

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"[*] {CURRENT_TIME} : BOT CONNECTED TO : {channel}")

    await ctx.send(f"> joined channel : {channel} with {user}")

@join.error
async def join_error(ctx, error):
    user = ctx.message.author
    if isinstance(error, commands.CommandError):
        print(f"[!] {CURRENT_TIME} : {user} ASKED THE BOT TO JOIN WHILE NOT CONNECTED")
        await ctx.send(f"> {user} you aren't connected to a voice channel")
#===================#


#===================#
@bot.command(pass_context=True)
async def leave(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)
    user = ctx.message.author

    if voice and voice.is_connected():
        channel = ctx.message.author.voice.channel
        await voice.disconnect()
        print(f"[*] {CURRENT_TIME} : BOT LEFT : {channel}")
        await ctx.send(f"> Left : {channel}")
    else:
        print(f"[!] {CURRENT_TIME} : {user} ASKED BOT TO LEAVE BUT IT WASN'T CONNECTED TO ANYTHING")
        await ctx.send("> Don't think I am in a voice channel")
#===================#


#===================#
@bot.command(pass_context=True)
async def play(ctx, eps):
    title = None

    if eps == "e1":
        eps = "ADV5008883012"
        title = 1

    elif eps == "e2":
        eps = "ADV9527233503"
        title = 2

    elif eps == "e3":
        eps = "ADV5119980399"
        title = 3
    elif eps == "e4":
        eps = "ADV3675761065"
        title = 4
    elif eps == "e5":
        eps = "ADV9180667884"
        title = 5
    elif eps == "e6":
        eps = "ADV3092049688"
        title = 6
    elif eps == "e7":
        eps = "ADV7870416400"
        title = 7
    elif eps == "e8":
        eps = "ADV7325000300"
        title = 8
    elif eps == "e9":
        eps = "ADV6668031883"
        title = 9
    elif eps == "e10":
        eps = "ADV8817646028"
        title = 10
    elif eps == "e11":
        eps = "ADV9140175464"
        title = 11
    elif eps == "e12":
        eps = "ADV6745265125"
        title = 12
    elif eps == "e13":
        eps = "ADV1006335411"
        title = 13
    elif eps == "e14":
        eps = "ADV6666881571"
        title = 14
    elif eps == "e15":
        eps = "ADV2718856516"
        title = 15
    elif eps == "e16":
        eps = "ADV9369246412"
        title = 16
    elif eps == "e17":
        eps = "ADV7492515166"
        title = 17
    elif eps == "e18":
        eps = "ADV4979232758"
        title = 18
    elif eps == "e19":
        eps = "ADV5170372742"
        title = 19
    elif eps == "e20":
        eps = "ADV1679665922"
        title = 20
    elif eps == "e21":
        eps = "ADV9980377945"
        title = 21
    elif eps == "e22":
        eps = "ADV4596635129"
        title = 22
    elif eps == "e23":
        eps = "ADV2249492375"
        title = 23
    elif eps == "e24":
        eps = "ADV2660822180"
        title = 24
    elif eps == "e25":
        eps = "ADV9451764404"
        title = 25
    elif eps == "e26":
        eps = "ADV3145014219"
        title = 26
    elif eps == "e27":
        eps = "ADV5783978660"
        title = 27
    elif eps == "e28":
        eps = "ADV7699953220"
        title = 28
    elif eps == "e29":
        eps = "ADV2476504070"
        title = 29
    elif eps == "e30":
        eps = "ADV7593743116"
        title = 30
    elif eps == "e31":
        eps = "ADV7422385695"
        title = 31
    elif eps == "e32":
        eps = "ADV9889785443"
        title = 32
    elif eps == "e33":
        eps = "ADV8668553535"
        title = 33
    elif eps == "e34":
        eps = "ADV4340254351"
        title = 34
    elif eps == "e35":
        eps = "ADV6828800477"
        title = 35
    elif eps == "e36":
        eps = "ADV6715709308"
        title = 36
    elif eps == "e37":
        eps = "ADV9708504478"
        title = 37
    elif eps == "e38":
        eps = "ADV2564803266"
        title = 38
    elif eps == "e39":
        eps = "ADV8534430497"
        title = 39
    elif eps == "e40":
        eps = "ADV1142224672"
        title = 40
    elif eps == "e41":
        eps = "ADV5671687285"
        title = 41
    elif eps == "e42":
        eps = "ADV2845437271"
        title = 42
    elif eps == "e43":
        eps = "ADV9896380815"
        title = 43
    elif eps == "e44":
        eps = "ADV2330388531"
        title = 44
    elif eps == "e45":
        eps = "ADV2651046249"
        title = 45
    elif eps == "e46":
        eps = "ADV7236741619"
        title = 46
    elif eps == "e47":
        eps = "ADV8262954242"
        title = 47
    elif eps == "e48":
        eps = "ADV5331304146"
        title = 48
    elif eps == "e49":
        eps = "ADV8221836709"
        title =49
    elif eps == "e50":
        eps = "ADV5529569827"
        title =50
    elif eps == "e51":
        eps = "ADV5003101655"
        title =51
    elif eps == "e52":
        eps = "ADV1104544195"
        title =52
    elif eps == "e53":
        eps = "ADV9906244248"
        title =53
    elif eps == "e54":
        eps = "ADV7741006833"
        title =54
    elif eps == "e55":
        eps = "ADV9304669806"
        title =55
    elif eps == "e56":
        eps = "ADV4333614155"
        title =56
    elif eps == "e57":
        eps = "ADV3206792063"
        title =57
    elif eps == "e58":
        eps = "ADV3598870537"
        title =58

    elif eps == "e59":
        eps = "ADV2874730743"
        title =59

    url = "https://dcs.megaphone.fm/" + eps + ".mp3"
    song_there = os.path.isfile("eps.mp3")
    try:
        if song_there:
            os.remove("eps.mp3")
            print(f"[*] {CURRENT_TIME} : DELETED OLD eps.mp3 FILE")
    except PermissionError:
        print(f"[*] {CURRENT_TIME} : TRYING TO DELETE BUT FILE IS BEING USED")
        await ctx.send("> ERROR  : song is playing")
        return
    await ctx.send("> setting everything up")
    print(f"[*] {CURRENT_TIME} : INSTALLING...")
    voice = get(bot.voice_clients, guild=ctx.guild)
    r = requests.get(url)
    name = eps + ".mp3"
    open(name, "wb").write(r.content)
    print(f"[*] {CURRENT_TIME} : INSTALLED : {eps}.mp3")
    os.rename(name, "eps.mp3")
    print(f"[*] {CURRENT_TIME} : RENAMED {eps}.mp3 TO eps.mp3")
    nname = requests.get("https://darknetdiaries.com/episode/" + str(title))
    tree = fromstring(nname.content)
    name = tree.findtext(".//title")
    await ctx.send(f"> Playing now 	")
    voice.play(discord.FFmpegPCMAudio("eps.mp3"), after=lambda e: print(f"[*] {CURRENT_TIME} : DONE PLAYING!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
    print(f"[*] {CURRENT_TIME} : STARTED PLAYING")
@play.error
async def play_error(ctx, error):
  user = ctx.message.author
  if isinstance(error, commands.CommandError):
    print(f"[!] {CURRENT_TIME} : {user} TRIED TO PLAY BUT ISN'T CONNECTED")
    await ctx.send(f"> couldn't play, {user} you didn't invite me to your voice channel")
    await ctx.send(f"ERROR: {error}")
#===================#


#===================#
@bot.command(pass_context=True)
async def pause(ctx):
    user = ctx.message.author
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.pause()
    print(f"[*] {CURRENT_TIME} : {user} PAUSED THE BOT")
    await ctx.send(f"> {user} paused me")
@pause.error
async def pause_error(ctx, error):
  user = ctx.message.author
  if isinstance(error, commands.CommandError):
    print(f"[!] {CURRENT_TIME} : {user} TRIED TO PAUSE BUT BOT ISNT PLAYING")
    await ctx.send("> couldn't pause, I wasn't playing anything")
#===================#


#===================#
@bot.command(pass_context=True)
async def resume(ctx):
    user = ctx.message.author
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.resume()
    print(f"[*] {CURRENT_TIME} : {user} RESUMED")
    await ctx.send(f"> {user} resumed me")
@resume.error
async def resume_error(ctx, error):
  user = ctx.message.author
  if isinstance(error, commands.CommandError):
    print(f"[!] {CURRENT_TIME} : {user} TRIED TO RESUME BUT BOT ISNT PLAYING")
    await ctx.send("> couldn't resume, I wasn't playing anything")
#===================#


#===================#
@bot.command(pass_context=True)
async def stop(ctx):
    user = ctx.message.author
    voice = get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
    print(f"[*] {CURRENT_TIME} : {user} STOPPED THE BOT")
    await ctx.send(f"> {user} stopped me")
@stop.error
async def stop_error(ctx, error):
  user = ctx.message.author
  if isinstance(error, commands.CommandError):
    print(f"[!] {CURRENT_TIME} : {user} TRIED TO STOP BUT BOT ISNT PLAYING")
    await ctx.send("> couldn't stop, I wasn't playing anything")
#===================#


#===================#
@bot.command(pass_context=True)
async def Help(ctx):
    user = ctx.message.author
    print(f"[*] {CURRENT_TIME} : {user} ASKED FOR HELP")
    await ctx.send("> AVAILABLE COMMANDS:\n> .Help\n> .join\n> .leave\n> .play {episode} ex(.play e10)\n> .pause\n> .resume\n> .stop\n> .ping")
#===================#


#===================#
@bot.command()
async def ping(ctx):
    user = ctx.message.author
    ping = round(bot.latency * 1000)
    print(f"[*] {CURRENT_TIME} : {user} ASKED FOR PING : {ping} MS")
    await ctx.send(f"> ping : {round(bot.latency * 1000)}ms")
#===================#


#===================#
@bot.command()
async def spam(ctx):
    for i in tqdm(range(17)):
        await ctx.send("spam")
#===================#


#===================#
@bot.command()
async def k(ctx):
    await ctx.send("k")
#===================#


# BOT RUN
bot.run(TOKEN)
