import discord
from discord.ext import commands
import ctypes
import json
import os
import random
import requests
import asyncio
import string
import time
import datetime
from colorama import Fore
import platform
import google.generativeai as genai

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

__version__ = "3.2"

start_time = datetime.datetime.now(datetime.timezone.utc)

with open("config/config.json", "r") as file:
    config = json.load(file)
    token = config.get("token")
    prefix = config.get("prefix")
    gemini_api_key = config["gemini"]["api_key"]
    gemini_enabled_channels = config["gemini"]["enabled_channels"]
    gemini_enabled_users = config["gemini"]["enabled_users"]

genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel('gemini-pro')

def save_config(config):
    with open("config/config.json", "w") as file:
        json.dump(config, file, indent=4)

def selfbot_menu(bot):
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print(f"""\n{Fore.RESET}
                            ██████╗ ████████╗██╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                           ██╔═══██╗╚══██╔══╝██║██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                           ██║██╗██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ██║██║██║   ██║   ██║██║   ██║       ██║   ██║   ██║██║   ██║██║     
                           ╚█║████╔╝   ██║   ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                            ╚╝╚═══╝    ╚═╝   ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n""".replace('█', f'{b}█{y}'))
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------
{w}raadev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com/AstraaDev {b}|{w} https://github.com
{y}------------------------------------------------------------------------------------------------------------------------\n""")
    print(f"""{y}[{b}+{y}]{w} SelfBot Information:\n
\t{y}[{w}#{y}]{w} Version: v{__version__}
\t{y}[{w}#{y}]{w} Logged in as: {bot.user} ({bot.user.id})
\t{y}[{w}#{y}]{w} Cached Users: {len(bot.users)}
\t{y}[{w}#{y}]{w} Guilds Connected: {len(bot.guilds)}\n\n
{y}[{b}+{y}]{w} Settings Overview:\n
\t{y}[{w}#{y}]{w} SelfBot Prefix: {prefix}
\t{y}[{w}#{y}]{w} Remote Users Configured:""")
    if config["remote-users"]:
        for i, user_id in enumerate(config["remote-users"], start=1):
            print(f"\t\t{y}[{w}{i}{y}]{w} User ID: {user_id}")
    else:
        print(f"\t\t{y}[{w}-{y}]{w} No remote users configured.")
    print(f"""
\t{y}[{w}#{y}]{w} AFK Status: {'Enabled' if config["afk"]["enabled"] else 'Disabled'}
\t{y}[{w}#{y}]{w} AFK Message: "{config["afk"]["message"]}"\n
\t{y}[{w}#{y}]{w} Total Commands Loaded: 9\n\n
{y}[{Fore.GREEN}!{y}]{w} SelfBot is now online and ready!""")


bot = commands.Bot(command_prefix=prefix, description='not a selfbot', self_bot=True, help_command=None)

@bot.event
async def on_ready():
    if platform.system() == "Windows":
        ctypes.windll.kernel32.SetConsoleTitleW(f"SelfBot v{__version__} - Made By a5traa")
        os.system('cls')
    else:
        os.system('clear')
    selfbot_menu(bot)

@bot.event
async def on_message(message):
    if config["afk"]["enabled"]:
        if bot.user in message.mentions and message.author != bot.user:
            await message.reply(config["afk"]["message"])
            return
        elif isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
            await message.reply(config["afk"]["message"])
            return
    
    if message.guild and message.guild.id == 1279905004181917808 and message.content.startswith(config['prefix']):
        await message.delete()
        await message.channel.send("> SelfBot commands are not allowed here. Thanks.", delete_after=5)
        return

    if message.author != bot.user and str(message.author.id) not in config["remote-users"]:
        if str(message.author.id) in gemini_enabled_users or str(message.channel.id) in gemini_enabled_channels:
            try:
                response = gemini_model.generate_content(message.content)
                await message.reply(response.text)
            except Exception as e:
                print(f"Error generating Gemini response: {e}")
                await message.reply(f"> **[**ERROR**]**: Unable to get Gemini response. Error: `{str(e)}`", delete_after=5)
        return

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return


@bot.command(aliases=['h'])
async def help(ctx):
    await ctx.message.delete()

    help_text = f"""
**Astraa SelfBot | Prefix: `{prefix}`**\n
**Commands:**\n
> :space_invader: `{prefix}astraa` - Show my social networks.
> :wrench: `{prefix}changeprefix <prefix>` - Change the bot's prefix.  
> :x: `{prefix}shutdown` - Stop the selfbot.  
> :notepad_spiral: `{prefix}uptime` - Returns how long the selfbot has been running.
> :closed_lock_with_key: `{prefix}remoteuser <@user>` - Authorize a user to execute commands remotely.
> :pushpin: `{prefix}ping` - Returns the bot's latency.
> :brain: `{prefix}gemini <ON|OFF> <@user|#channel>` - Enable or disable Gemini AI responses for a user or channel.
> :zzz: `{prefix}afk <ON/OFF>` - Enable or disable AFK mode. Sends a custom message when receiving a DM or being mentioned.
"""
    await ctx.send(help_text)


@bot.command()
async def uptime(ctx):
    await ctx.message.delete()

    now = datetime.datetime.now(datetime.timezone.utc)
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

@bot.command()
async def ping(ctx):
    await ctx.message.delete()

    before = time.monotonic()
    message_to_send = await ctx.send("Pinging...")

    await message_to_send.edit(content=f"`{int((time.monotonic() - before) * 1000)} ms`")

@bot.command(aliases=['astra'])
async def astraa(ctx):
    await ctx.message.delete()

    embed = f"""**MY SOCIAL NETWORKS | Prefix: `{prefix}`**\n
    > :pager: `Discord Server`\n*https://discord.gg/PKR7nM9j9U*
    > :computer: `GitHub Page`\n*https://github.com/AstraaDev*
    > :robot: `SelfBot Project`\n*https://github.com/AstraaDev/Discord-SelfBot*"""

    await ctx.send(embed)

@bot.command(aliases=['remote'])
async def remoteuser(ctx, action: str, users: discord.User=None):
    await ctx.message.delete()

    if not users:
        await ctx.send("> **[ERROR]**: Invalid command.\n> __Command__: `remoteuser ADD|REMOVE <@user(s)>`", delete_after=5)
        return

    if action not in ["ADD", "REMOVE"]:
        await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ADD` or `REMOVE`.\n> __Command__: `remoteuser ADD|REMOVE <@user(s)>`", delete_after=5)
        return
    
    if action.upper() == "ADD":
        for user in users:
            if str(user.id) not in config["remote-users"]:
                config["remote-users"].append(str(user.id))

        save_config(config)
        selfbot_menu(bot)

        await ctx.send(f"> **Success**: {len(users)} user(s) added to remote-users", delete_after=5)
    elif action.upper() == "REMOVE":
        for user in users:
            if str(user.id) in config["remote-users"]:
                config["remote-users"].remove(str(user.id))

        save_config(config)
        selfbot_menu(bot)

        await ctx.send(f"> **Success**: {len(users)} user(s) removed from remote-users", delete_after=5)

@bot.command(aliases=['ai'])
async def gemini(ctx, action: str, target: discord.User or discord.TextChannel = None):
    await ctx.message.delete()

    if action not in ["ON", "OFF"]:
        await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ON` or `OFF`.\n> __Command__: `gemini ON|OFF <@user|#channel>`", delete_after=5)
        return

    if not target:
        await ctx.send(f"> **[**ERROR**]**: Please specify a user or channel.\n> __Command__: `gemini ON|OFF <@user|#channel>`", delete_after=5)
        return

    target_id = str(target.id)
    target_type = "user" if isinstance(target, discord.User) else "channel"
    config_key = "gemini_enabled_users" if target_type == "user" else "gemini_enabled_channels"
    
    if action.upper() == "ON":
        if target_id not in config["gemini"][config_key]:
            config["gemini"][config_key].append(target_id)
            save_config(config)
            selfbot_menu(bot)
            await ctx.send(f"> **Gemini AI enabled for {target_type} {target.mention}.**", delete_after=5)
        else:
            await ctx.send(f"> **[**ERROR**]**: Gemini AI is already enabled for {target_type} {target.mention}.", delete_after=5)
    elif action.upper() == "OFF":
        if target_id in config["gemini"][config_key]:
            config["gemini"][config_key].remove(target_id)
            save_config(config)
            selfbot_menu(bot)
            await ctx.send(f"> **Gemini AI disabled for {target_type} {target.mention}.**", delete_after=5)
        else:
            await ctx.send(f"> **[**ERROR**]**: Gemini AI is not currently enabled for {target_type} {target.mention}.", delete_after=5)

@bot.command()
async def afk(ctx, status: str, *, message: str=None):
    await ctx.message.delete()

    if status not in ["ON", "OFF"]:
        await ctx.send(f"> **[**ERROR**]**: Invalid action. Use `ON` or `OFF`.\n> __Command__: `afk ON|OFF <message>`", delete_after=5)
        return

    if status.upper() == "ON":
        if not config["afk"]["enabled"]:
            config["afk"]["enabled"] = True
            if message:
                config["afk"]["message"] = message
            save_config(config)
            selfbot_menu(bot)
            await ctx.send(f"> **AFK mode enabled.** Message: `{config['afk']['message']}`", delete_after=5)
        else:
            await ctx.send("> **[**ERROR**]**: AFK mode is already enabled", delete_after=5)
    elif status.upper() == "OFF":
        if config["afk"]["enabled"]:
            config["afk"]["enabled"] = False
            save_config(config)
            selfbot_menu(bot)
            await ctx.send("> **AFK mode disabled.** Welcome back!", delete_after=5)
        else:
            await ctx.send("> **[**ERROR**]**: AFK mode is not currently enabled", delete_after=5)

@bot.command(aliases=["prefix"])
async def changeprefix(ctx, *, new_prefix: str=None):
    await ctx.message.delete()

    if not new_prefix:
        await ctx.send(f"> **[**ERROR**]**: Invalid command.\n> __Command__: `changeprefix <prefix>`", delete_after=5)
        return
    
    config['prefix'] = new_prefix
    save_config(config)
    selfbot_menu(bot)
    
    bot.command_prefix = new_prefix

    await ctx.send(f"> Prefix updated to `{new_prefix}`", delete_after=5)

@bot.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()

    msg = await ctx.send("> Shutting down...")
    await asyncio.sleep(2)

    await msg.delete()
    await bot.close()

bot.run(token)
