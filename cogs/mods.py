import asyncio
import requests
import json
import os
import discord
import datetime
from discord.ext import commands

start_time = datetime.datetime.utcnow()

URBAN_API_KEY = os.getenv('URBAN_API_KEY')


class mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uptime(self, ctx):
        uptime = datetime.datetime.utcnow() - start_time
        uptime = str(uptime).split('.')[0]
        await ctx.send(f"**Current Uptime:** "+''+uptime+'')

    @commands.command()
    async def ping(self, ctx):
        await ctx.reply(f"**Latency is `{round(self.bot.latency * 1000)}` ms**")

    @commands.command(aliases=['mc'])
    async def members(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title="Member Count", color=discord.Color.dark_grey(), timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
        embed.set_author(name="Fxck You")
        embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
        embed.add_field(name="Members:",value=f"{len(guild.members)}",inline=False)
        embed.add_field(name="Requested by:",value=f"{ctx.author}",inline=False)
        await ctx.reply(embed=embed)
        
    @commands.has_permissions(kick_members=True)
    @commands.command()
    @commands.has_any_role(985230660023255070, 982336284632678490, 981607641983909919, 981607636673921054)
    @commands.cooldown(1, 40, commands.BucketType.guild)
    async def kick(self, ctx,  user: discord.Member, *, reason="No reason provided"): 
        if user == ctx.author:
            return await ctx.reply("***You can't Kick yourself !!***")
        elif ctx.author.top_role.id == 984222241896136764 or ctx.author.top_role.id == 984823411496845383 or ctx.author.top_role.id == 984222247537487882 or ctx.author.top_role.id == 984222251622744135 or ctx.author == ctx.guild.owner:
            embed = discord.Embed(title="Moderation Action", color=discord.Color.dark_grey(), timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
            embed.set_author(name="Fxck You")
            embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
            embed.add_field(name="User kicked:", value=f"{user}")
            embed.add_field(name="Requested by:", value=f"{ctx.author}")
            embed.add_field(name="Reason:", value=f"{reason}")
            await user.kick(reason=reason)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Moderation Action", color=discord.Color.dark_grey(), timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
            embed.set_author(name="Fxck You")
            embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
            embed.add_field(name="Cant Kick user", value=f"{user} has same or above role !")
            await ctx.reply(embed=embed)
    @kick.error 
    async def kick_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="Fxck You", description=f"You Dont have the permission to KicK")
            await ctx.reply(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Fxck You", description=f"You didnt mention a user to kick")
            await ctx.reply(embed=embed)
        if isinstance(error, commands.MissingAnyRole):
            embed = discord.Embed(title="Fxck You", description=f"You dont have the required role ||kal aana kal||")
            await ctx.reply(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    @commands.has_any_role(984222241896136764, 984823411496845383, 984222247537487882, 986273196368093184)
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def ban(self, ctx,  user: discord.Member, *, reason="No reason provided"): 
        if user == ctx.author:
            return await ctx.reply("***You can't Ban yourself !!***")
        elif ctx.author.top_role.id == 984222241896136764 or ctx.author.top_role.id == 984823411496845383 or ctx.author.top_role.id == 984222247537487882 or ctx.author.top_role.id == 984222251622744135 or ctx.author == ctx.guild.owner:
            embed = discord.Embed(title="Moderation Action", color=discord.Color.dark_grey(), timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
            embed.set_author(name="Fxck You")
            embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
            embed.add_field(name="User Banned:", value=f"{user}")
            embed.add_field(name="Requested by:", value=f"{ctx.author}")
            embed.add_field(name="Reason:", value=f"{reason}")
            await user.ban(reason=reason)
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(title="Moderation Action", color=discord.Color.dark_grey(), timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
            embed.set_author(name="Fxck You")
            embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
            embed.add_field(name="Cant ban user", value=f"{user} has same or above role !")
            await ctx.reply(embed=embed)
    @ban.error 
    async def ban_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="Fxck You", description=f"You Dont have the permission to ban")
            await ctx.reply(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Fxck You", description=f"You didnt mention a user to ban")
            await ctx.reply(embed=embed)
        if isinstance(error, commands.MissingAnyRole):
            embed = discord.Embed(title="Fxck You", description=f"You dont have the required role ||kal aana kal||")
            await ctx.reply(embed=embed)
        
    @commands.command(aliases = ['channelnuke', 'nchan', 'nukechan'])
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 100, commands.BucketType.guild)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        embed = discord.Embed(description=f"**Fxck You**")
        embed.set_image(url="https://cdn.discordapp.com/attachments/984222284728373268/986278865347412058/hehe.jpg")
        embed.set_footer(text=f'Channel nuked by {ctx.author}')
        channel = channel or ctx.channel
        position = channel.position
        newchannel = await channel.clone(reason=f"Chat Nuked by {ctx.author}")
        await channel.delete()
        await newchannel.edit(position=position)
        await newchannel.send(embed=embed)

    @commands.command(aliases = ['blacklist'])
    @commands.has_permissions(administrator=True)
    async def block(self, ctx, user: discord.Member=None):
        if not user:
            await ctx.send("Please specify a member")
            return
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send(f"`{user.name}#{user.discriminator}` was blocked by `{ctx.author}`.")
    @block.error
    async def block_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to block people!")

    @commands.command(aliases = ['removeblacklist' , 'rb'])
    @commands.has_permissions(administrator=True)
    async def unblock(self, ctx, user: discord.Member=None):
        if not user:
            await ctx.send("Please specify a member")
            return
        await ctx.channel.set_permissions(user, send_messages=None)
        await ctx.send(f"`{user.name}#{user.discriminator}` was unblocked by `{ctx.author}`.")
    @block.error
    async def unblock_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("You are not allowed to unblock people!")

    @commands.command(usage="[#channel/id]", name="lock", description="Locks a channel")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def lock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply(f"The channel {channel.mention} has been locked!")

    @lock.error 
    async def lock_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have `Manage channel Permissions` To Use This Command!*")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You Must `Mention` A User To channel!*")
            await ctx.send(embed=embed)

    @commands.command(usage="[#channel/id]", name="unlock", description="Unlocks a channel")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.reply(f"The channel {channel.mention} has been unlocked!")

    @unlock.error 
    async def unlock_error(self, ctx, error):
        if isinstance(error, (commands.MissingPermissions)):
            embed = discord.Embed(title="*You Do Not Have `Manage channel Permissions` To Use This Command!*")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="*You Must `Mention` A User To channel!*")
            await ctx.send(embed=embed)
    
    @commands.command(aliases = ['ar' , 'Ar', 'arole'])
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        if ctx.author == member:
            await ctx.reply("<a:Srw_cross:950400419996237894> | Cant give role to yourself !")
        elif role.permissions.administrator is True:
            await ctx.reply("<a:Srw_cross:950400419996237894> | Admin roles cant be assigned !")
        elif (role.permissions.manage_roles is True) or (role.permissions.ban_members is True) or (role.permissions.kick_members is True):
            await ctx.reply("<a:Srw_cross:950400419996237894> | Roles is not assignable !")
        elif role.position >= ctx.author.top_role.position:
            await ctx.reply("<a:Srw_cross:950400419996237894> | That role has the same position as your top role !")
        elif role in member.roles:
            await ctx.reply("<a:Srw_cross:950400419996237894> | The member already has this role assigned !")
        elif role.position >= ctx.guild.me.top_role.position:
            await ctx.reply("<a:Srw_cross:950400419996237894> | This role is higher than my role !")
        else:
            embed = discord.Embed(title="Moderation Action", color=discord.Color.dark_grey())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
            embed.set_author(name="Fxck You")
            embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
            embed.add_field(name="<a:RAGE_hype:950374862336184340> Role Given", value=f"{role.mention} | {role.id}",inline= False)
            embed.add_field(name="<a:RAGE_hype:950374862336184340> Requestion by", value=f"{ctx.author.mention}",inline= False)
            embed.add_field(name="<a:RAGE_hype:950374862336184340> Given to", value=f"{member.mention}",inline= False)
            await member.add_roles(role)
            await ctx.reply(embed=embed)

    @commands.command(aliases = ['rr' , 'Rr', 'rrole'])
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        if ctx.author == member:
            await ctx.reply("<a:Srw_cross:950400419996237894> | Cant remove role from yourself !")
        elif role.position >= ctx.author.top_role.position:
            await ctx.reply("<a:Srw_cross:950400419996237894> | That role has the same/higher position as your top role !")
        elif role not in member.roles:
            await ctx.reply("<a:Srw_cross:950400419996237894> | The member dont have this role assigned !")
        elif role.position >= ctx.guild.me.top_role.position:
            await ctx.reply("<a:Srw_cross:950400419996237894> | This role is higher than my role !")
        else:
            embed = discord.Embed(title="Moderation Action", color=discord.Color.dark_grey())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/976110436883791962/985219208008835122/server_lol.gif")
            embed.set_author(name="Fxck You")
            embed.set_footer(text='! K R Λ K Ξ N', icon_url="https://media.discordapp.net/attachments/956883290747441162/956957830471106580/Andreas_Gif_886.gif")
            embed.add_field(name="<a:RAGE_hype:950374862336184340> Role Removed", value=f"{role.mention} | {role.id}",inline= False)
            embed.add_field(name="<a:RAGE_hype:950374862336184340> Requestion by", value=f"{ctx.author.mention}",inline= False)
            embed.add_field(name="<a:RAGE_hype:950374862336184340> Removed from", value=f"{member.mention}",inline= False)
            await member.remove_roles(role)
            await ctx.reply(embed=embed)
