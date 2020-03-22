from dotenv import load_dotenv
import discord
import os

load_dotenv()

token = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print('Rain is ready for battle!!')

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
      embed = discord.Embed(title=f"{after}")
      # embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="before", value=before)
      embed.add_field(name="after", value=after)
      await channel.send(content=None, embed=embed)

# chat sec  
@client.event
async def on_message(message):
  id = client.get_guild(int(os.getenv('SERVER_ID')))
  hellos = ["hello", "Hello", "Hey", "hey", "Hi", "hi"]

  if (message.guild is None):
    for channel in id.channels:
      if str(channel.name) == "soluctions" and "#soluction id:" in str(message.content):
        await channel.send(f"{message.content}")

  if str(message.channel):
    if message.content.split(' ', 1)[0] in hellos:
      # Todo: pass random messages 
      await message.channel.send(f"👋 Hi {message.author.mention}")

client.run(token)