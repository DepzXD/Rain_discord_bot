from dotenv import load_dotenv
import discord
import os
import random
import time

load_dotenv()

token = os.getenv('TOKEN')
client = discord.Client()

async def schedule_for_progress():
  channelID = int(os.getenv('SCHEDULE_CHANNEL'))
  channel = client.get_channel(channelID)
  daily = ["@everyone showoff what you've learned or learning #100-days-of-code", "@everyone it's a new day #100-days-of-code!!", "@everyone #100-days-of-code", "@everyone 👉 #100-days-of-code", "100-days-of-code @everyone 🤗", "100-days-of-code @everyone 🤬"]
  await channel.send(random.choice(daily))
  
  

@client.event
async def on_ready():
  print('Rain is ready for battle!!')
  activity = discord.Activity(name="something!! IDK, i'm anime girl", type=discord.ActivityType.listening)
  await client.change_presence(activity=activity)


# welcomes new users s
@client.event
async def on_member_join(member):
  for channel in member.guild.channels:
    if str(channel) == "the-lobby":
      embed = discord.Embed(title=f"{member}", color=0x2a8ef8)
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="!hello", value=f"""{member.mention} has joined the battle bus.""")
      await channel.send(content=None, embed=embed)

# user lefts 
@client.event
async def on_member_remove(member):
  for channel in member.guild.channels:
    if str(channel) == "the-lobby":
      embed = discord.Embed(title=f"{member}", color=0xe31635)
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="yo", value=f"""{member.mention} has lefts the battle bus.""")
      await channel.send(content=None, embed=embed)

# profile updates
@client.event
async def on_user_update(before, after):
  id = client.get_guild(int(os.getenv('SERVER_ID')))
  for channel in id.channels:
    if str(channel) == "🛸bot-spam":
      embed = discord.Embed(title=f"{after}", description=f"{after.mention}Updated Profile!", color=0xeca427)
      embed.set_thumbnail(url=after.avatar_url)
      embed.add_field(name="before", value=before)
      embed.add_field(name="after", value=after)
      await channel.send(content=None, embed=embed)

# chat sec  
@client.event
async def on_message(message):
  id = client.get_guild(int(os.getenv('SERVER_ID')))
  author = os.getenv('AUTHOR_ID')
  admin = client.get_user(int(author))
  hellos = ["hello", "Hello", "Hey", "hey", "Hi", "hi"]

  if (message.guild is None):
    for channel in id.channels:
      if str(channel.name) == "soluctions" and "#soluction id:" in str(message.content):
        await channel.send(f"{message.content}")

    # ADMIN sec
    if str(message.author.id) == str(author):
      if message.content.split(', ')[0] == "sendMSG":
        try:
          authorID = int(message.content.split(', ')[1])
          msg = message.content.split(', ')[2]
          user = client.get_user(int(authorID))
          await user.send(msg)            
        except:
          print('(ADMIN)LOG: ', message.content)
          await message.author.send("didn't geddt, Try again")
      elif message.content.split(', ')[0] == "announce":
        try:
          channelID = int(message.content.split(', ')[1])
          msg = message.content.split(', ')[2]
          channel = client.get_channel(channelID)
          await channel.send(msg)            
        except:
          print('(ADMIN)LOG: ', message.content)
          await message.author.send("didn't geddt, Try again")
      elif str(message.content) == "codey":
        await schedule_for_progress()
        
    # USER sec
    elif message.content.split(', ')[0] == "send":
      try:
        msg = message.content.split(', ')[1]
        await admin.send('user : ', message.author,'msg: ', msg)
      except:
        print('(user)Log: ', message.content)
        await message.author.send("didn't geddt, Try again")

  elif str(message.channel):
    if message.content.split(' ', 1)[0] in hellos:
      # Todo: pass random messages 
      await message.channel.send(f"👋 {random.choice(hellos)} {message.author.mention}")
  
client.run(token)