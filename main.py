from dotenv import load_dotenv
import discord
import os

load_dotenv()

token = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print('Rain is ready for battle!!')

# welcomes new users 
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
      embed = discord.Embed(title=f"{member}", color=0xe9ec36)
      embed.set_thumbnail(url=member.avatar_url)
      embed.add_field(name="yo", value=f"""{member.mention} has lefts the battle bus.""")
      await channel.send(content=None, embed=embed)

# chat sec  
@client.event
async def on_message(message):
  id = client.get_guild(os.getenv('SERVER_ID'))
  channels = ["rain-discord-bot"]
  if str(message.channel) in channels:
    if message.content.find("hello") != -1:
      # Todo: add name split id of author 
      await message.channel.send(f"👋 Hi {message.author}") 

client.run(token)