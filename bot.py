import discord
from discord.utils import get

bot = discord.Client()

# Add the bot command

@bot.event 

async def on_raw_reaction_add(payload):
  user = payload.member
  messageId = payload.message_id
  guild_id = payload.guild_id
  guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
  if messageId == MESSAGE-ID-HERE and payload.emoji.name == 'EMOJI HERE': # Make sure the message id is not in ""
      ifRole = discord.utils.find(lambda r: r.name == 'Just Joined', guild.roles)
      if ifRole in user.roles:
        channel = bot.get_channel(826407433466937377)
        role = get(guild.roles, id=826418133048754187)
        await user.add_roles(role,reason=None, atomic=True)
        role = get(guild.roles, id=758243490529804298)
        await user.add_roles(role,reason=None, atomic=True)
        removeRole = get(guild.roles, id=826420305731125268)
        verifiedMessage = f'<@{payload.member.id}> just got verified'
        emb = discord.Embed(title='New User Verified', description=verifiedMessage)
        await channel.send(embed=emb)
        await user.remove_roles(removeRole, reason=None,atomic=True)
        await user.send("Welcome to the Sharkz Server! Hope you have a good time!")
        
bot.run("TOKEN HERE")
