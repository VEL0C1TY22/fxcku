import discord
import json
from discord.ext import commands
import datetime

class antinuke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        guild = channel.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.channel_create).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            try:
                await nooker.ban()
                await channel.delete()
                return
            except Exception as e:
                await channel.delete()
                print(e)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        guild = channel.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.channel_delete).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            try:
                await nooker.ban()
                await channel.clone()
                return
            except Exception as e:
                await channel.clone()
                print(e)

    @commands.Cog.listener()
    async def on_member_ban(self, user):
        guild = user.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.ban).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            await nooker.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Banning Members")
            return

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.kick).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            await nooker.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Kicking Members")
            return

    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.bot_add).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            await member.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Bot added ( Not Whitelisted )")
            await nooker.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Added unknown Bot")
            return

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        guild = role.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.role_create).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            try:
                await nooker.ban()
                await role.delete()
                return
            except Exception as e:
                await role.delete()
                print(e)


    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        guild = role.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.role_delete).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            try:
                await nooker.ban()
                await role.clone()
                return
            except Exception as e:
                await role.clone()
                print(e)


    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        guild = before.guild
        owner = guild.owner
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.role_update).flatten()
        logs = logs[0]
        if logs.user.id == owner.id:
            return
        else:
            if not before.permissions.ban_members and after.permissions.ban_members:
                await logs.user.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Updating Role")
                permissions = after.permissions
                permissions.update(ban_members=False)
                await after.edit(permissions=permissions)

            if not before.permissions.administrator and after.permissions.administrator:
                await logs.user.ban(reason="Anti-Nuke: Updating Role")
                permissions = after.permissions
                permissions.update(administrator=False)
                await after.edit(permissions=permissions)

            if not before.permissions.ban_members and after.permissions.ban_members:
                await logs.user.ban(reason="Anti-Nuke: Updating Role")
                permissions = after.permissions
                permissions.update(ban_members=False)
                await after.edit(permissions=permissions)

            if not before.permissions.manage_channels and after.permissions.manage_channels:
                await logs.user.ban(reason="Anti-Nuke: Updating Role")
                permissions = after.permissions
                permissions.update(manage_guild=False)
                await after.edit(permissions=permissions)
            return

    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        client = self.client
        guild = channel.guild
        owner = guild.owner
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.webhook_create).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        webhookig = await client.fetch_webhook(logs.target.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        else:
            try:
                await webhookig.channel.set_permissions(guild.default_role, read_messages=False, send_messages=False)
                await nooker.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Creating Webhooks")
                await webhookig.delete()
                await webhookig.delete()
            except:
                await webhookig.delete()

    @commands.Cog.listener()
    async def on_guild_update(self, before, after):
        with open('owner.json') as f:
            owners = json.load(f)
        client = self.client
        guild= after.guild
        owner = guild.owner
        botid = discord.utils.get(guild.members,id=client.user.id)
        logs = await after.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 1), action=discord.AuditLogAction.guild_update).flatten()
        logs = logs[0]
        nooker = discord.utils.get(guild.members,id=logs.user.id)
        if logs.user.id == owner.id:
            return
        elif str(logs.user.id) in owners["eternals"]:
            return
        if not before.public_updates_channel and after.public_updates_channel:
            try:
                await nooker.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Updating Server")
                await after.public_updates_channel.delete()
            except:
                await after.public_updates_channel.delete()
        if not before.name and after.name:
            try:
                await nooker.ban(reason=f"Fxck You: {logs.user} ({logs.user.id}) Updating Server")
                await after.edit(name=f"{before.name}")
            except:
                await after.edit(name=f"{before.name}")
            
