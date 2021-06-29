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
from PIL import Image
from colorama import Fore
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
Blank = commands.Bot(description='Blank SelfBot', command_prefix=prefix, self_bot=True)
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
        print("-------------------------------")
        print(f"Connected to: [{Blank.user.name}]")
        print(f"Token: {Blank.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()
        
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
        
print(f'''{Fore.GREEN}Log in successful!''' + Fore.RESET)

@Blank.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        global embed
        embed = discord.Embed(title = "Blank's SelfBot",url="https://github.com/SauhardGaming/SelfBot",color=discord.Colour.random())
        embed.add_field(name="\uD83E\uDDCA `help`", value="Shows all commands' info", inline=False)
        embed.add_field(name="\uD83E\uDDCA `embed`", value="Sends embed: "+prefix+"embed <message>", inline=False)
        embed.add_field(name="\uD83E\uDDCA `ping`", value="Shows the latency of the bot", inline=False)
        embed.add_field(name="\uD83E\uDDCA `empty`", value="Sends an empty character", inline=False)
        embed.add_field(name="\uD83E\uDDCA `whois`", value="Sends the user's info: "+prefix+"whois [user]", inline=False)
        embed.add_field(name="\uD83E\uDDCA `quickdel/del`", value="Sends a message and instantly deletes it", inline=False)
        embed.add_field(name="\uD83E\uDDCA `purge`", value="Purge the message: "+prefix+"purge <amount>", inline=False)
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
    
@Blank.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)


@Blank.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, *, args):
    await ctx.message.delete()
    await ctx.send(args, delete_after=1)
    
@Blank.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Blank.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass
    
@Blank.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173)) 

@Blank.event
async def on_message_edit(before, after):
    await Blank.process_commands(after)

@Blank.command()
async def embed(ctx, *, description):
    await ctx.message.delete()
    embed = discord.Embed(description=description,color=discord.Colour.random())
    await ctx.send(embed=embed)
    
if __name__ == '__main__':
    Init()
