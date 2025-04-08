import discord
from discord.ext import commands
from datetime import timedelta
import json
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=",", intents=intents)

bot.remove_command("help")
stats_file = "mod_stats.json"

mod_role_id = 1027539545564123207
reg_role_id = 1090722307921686649
admin_role_id = 1007038689563643924
tester_role_id = 1007038689500741810
dev_id = 660879218321784852

def increment_stat(user_id):
    user_id = str(user_id)  # JSON keys must be strings

    # Load existing stats or create empty dict
    if os.path.exists(stats_file):
        with open(stats_file, "r") as f:
            stats = json.load(f)
    else:
        stats = {}

    # Increment stat
    stats[user_id] = stats.get(user_id, 0) + 1

    # Save updated stats
    with open(stats_file, "w") as f:
        json.dump(stats, f, indent=2)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def help(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(title="<:potlogo:1359008364482396160> PotPvP Commands", description="**All commands** : ", color=0xFFFFFF)
            embed.add_field(name="`,check`", value="Checks if the bot is up and running.", inline=False)
            embed.add_field(name="`,mute [user] [minutes] [reason]`", value="Mute a user for a certain amount of time.", inline=False)
            embed.add_field(name="`,unmute [user]`", value="Unmutes a user.", inline=False)
            embed.add_field(name="`,ban [user] [reason]`",value="Bans a user",inline=False)
            embed.add_field(name="`,unban [user]`",value="Unbans a user",inline=False)
            embed.add_field(name="`,softban [member]`",value="Bans a user then immediately unbans them (Deletes a day worth of messages)", inline=False)
            embed.add_field(name="`,kick [member] [reason]`",value="Kicks a user", inline=False)
    
            embed.set_footer(text="Commands are limited to Mods+")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@help.error
async def check_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def check(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: The bot is up and working!", color=0x00ff00)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@check.error
async def check_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def modrole(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: The mod role ID is : {mod_role_id}", color=0x00ff00)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@modrole.error
async def modrole_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def regrole(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: The regulator role ID is : {reg_role_id}", color=0x00ff00)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@regrole.error
async def regrole_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def adminrole(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: The admin role ID is : {admin_role_id}", color=0x00ff00)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@adminrole.error
async def adminrole_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
@commands.has_permissions(moderate_members=True)
async def mute(ctx, member: discord.Member, minutes: int, *, reason="No reason provided"):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            duration = timedelta(minutes=minutes)
            try:
                await member.timeout(duration, reason=reason)
                increment_stat(ctx.author.id)
                embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: {member.mention} has been muted out for {minutes} minutes for {reason}", color=0x00ff00)
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: Failed to mute {member.mention}: {e}", color=0xFFB347)
                await ctx.send(embed=embed)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
@commands.has_permissions(moderate_members=True)
async def unmute(ctx, member: discord.Member):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            try:
                await member.timeout(None)
                increment_stat(ctx.author.id)
                embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: {member.mention} has been unmuted", color=0x00ff00)
                await ctx.send(embed=embed)
            except Exception as e:
                embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: Failed to unmute {member.mention}: {e}", color=0xFFB347)
                await ctx.send(embed=embed)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
@commands.has_permissions(ban_members=True)
async def ban(ctx, target, *, reason="No reason provided"):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        return await ctx.send(embed=embed)

    if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
        try:
            member = await commands.MemberConverter().convert(ctx, target)
            await member.ban(reason=reason)
            increment_stat(ctx.author.id)
            embed = discord.Embed(
                description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: `{member}` has been banned for `{reason}`.", color=0x00ff00)
        except commands.BadArgument:
            try:
                user = await bot.fetch_user(int(target))
                await ctx.guild.ban(user, reason=reason)
                embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: `{user}` has been banned by ID for `{reason}`.", color=0x00ff00)
            except Exception as e:
                embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: Couldn't ban user: `{e}`", color=0xFFB347)
        await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user_id: int):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        return await ctx.send(embed=embed)

    if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
        try:
            user = await bot.fetch_user(user_id)
            await ctx.guild.unban(user)
            increment_stat(ctx.author.id)
            embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: `{user}` has been unbanned.", color=0x00ff00)
        except Exception as e:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: Failed to unban user: `{e}`", color=0xFFB347)
        await ctx.send(embed=embed)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
@commands.has_permissions(ban_members=True)
async def softban(ctx, target, *, reason="No reason provided"):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        return await ctx.send(embed=embed)
    
    if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
        try:
            member = await commands.MemberConverter().convert(ctx, target)
            await member.ban(reason=reason, delete_message_days=1)
            increment_stat(ctx.author.id)
            embed = discord.Embed(
                description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: `{member}` has been softbanned for `{reason}`.", color=0x00ff00)
            await ctx.guild.unban(member)
        except Exception as e:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: Failed to softban user: `{e}`", color=0xFFB347)
        await ctx.send(embed=embed)

@softban.error
async def softban_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.default)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        return await ctx.send(embed=embed)
    
    if any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
        try:
            await member.kick(reason=reason)
            increment_stat(ctx.author.id)
            embed = discord.Embed(description=f"<:checkmark:1358991338036662302> {ctx.author.mention}: `{member}` has been kicked for `{reason}`.",color=0x00ff00)
        except Exception as e:
            embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: Failed to kick user: `{e}`", color=0xFFB347)
        await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        retry_after = round(error.retry_after, 1)
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You're on cooldown! Try again in `{retry_after}` seconds.", color=0xFFB347)
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def appeal(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [tester_role_id, mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(title="Appeal <:appeal:1359083584903712920>", description="## **Please answer the following questions:**", color=0xFFFFFF)
            embed.add_field(name= "Link of your punishment message:", value=" ", inline=False)
            embed.add_field(name="How long is left on your punishment:", value=" ", inline=False)
            embed.add_field(name= "Why should we accept your appeal, or lower your duration:", value=" ",inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def alt(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [tester_role_id, mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(title="Alt Report <:alt:1359083852915802152>", description="## **All evidence must follow this format:**", color=0xFFFFFF)
            embed.add_field(name= "Two screenshots of /alts on seperate MC Servers", value=" ", inline=False)
            embed.add_field(name="The user ID of the person your reporting", value=" ", inline=False)
            embed.add_field(name= "ID's of both alt accounts", value=" ",inline=False)
            embed.add_field(name= "UUID's of both MC Accounts -> Use UUID Checker : https://laby.net/", value=" ",inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def serverapp(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [tester_role_id, mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(title="<:potlogo:1359008364482396160> Pot PvP server application questions", description="## Answer the following questions :", color=0xFFFFFF)
            embed.add_field(name= " 🗒️  Give us a description of your server. (Release date, Regions, IP's, Brief summary of what you have to offer)", value=" ", inline=False)
            embed.add_field(name="<:network_staff:1359084971582820532> Give us a list of your staff format, with staff members. (Can be done VIA a screenshot)", value=" ", inline=False)
            embed.add_field(name= "<:ping:1359085444486135810> Which staff members have access to player data such as IP's? ", value=" ",inline=False)
            embed.add_field(name= "<:cheatsexpert:1359085613378437130> Which staff members have access to Anti-Cheat logs?  (For etc Mod+)", value=" ",inline=False)
            embed.add_field(name= "<:potions:1359085754071912570> If your server was added to our verified server, will you grant Regulator+ access to potential alts and anticheat logs? (Only regulator+)", value=" ",inline=False)
            embed.add_field(name= "<:computer:1359085911161176064> What is your average TPS at peak numbers, are there any occurrences of lag we should be informed about?", value=" ",inline=False)
            embed.add_field(name= "<:hammer1:1359086058045833247> Do you currently have any qualified screensharers on your staff team?", value=" ",inline=False)
            embed.add_field(name= "<:key:1359086222328463410> Who has console access?", value=" ",inline=False)
            embed.add_field(name= "🧲 What makes your server better than others, what's unique about it?", value=" ",inline=False)

            embed.set_footer(text="Please answer in one message for better readability. Thanks!")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1,5,commands.BucketType.default)
async def cheating(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!", color=0xFFB347)
        await ctx.send(embed=embed)
    else:
        if any(role.id in [tester_role_id, mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id:
            embed = discord.Embed(title="Cheating Report <:cheatingreport:1359082898095079485>", description="## **All evidence must follow this format:**", color=0xFFFFFF)
            embed.add_field(name= "Video evidence of any evidence. **(Include Date of video)**", value=" ", inline=False)
            embed.add_field(name="Any evidence of user being banned from Verified Server (**In Pot Gamemode**)", value=" ", inline=False)
            embed.add_field(name= "The user ID of the person your reporting", value=" ",inline=False)
            embed.add_field(name= "UUID's of MC Account -> Use UUID Checker : https://laby.net/", value=" ",inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: You are not authorized to use this command!", color=0xFFB347)
            await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def staffstats(ctx):
    if ctx.guild.id != 1007038689412665404:
        embed = discord.Embed(description=f"<:warning:1359076907781722142> {ctx.author.mention}: This is not the PotPvP Discord Server!",color=0xFFB347)
        return await ctx.send(embed=embed)

    if not (any(role.id in [mod_role_id, reg_role_id, admin_role_id] for role in ctx.author.roles) or ctx.author.id == dev_id):
        embed = discord.Embed(description=f"<:crossmark:1358992760262234318> {ctx.author.mention}: You do not have permission to view the staff stats.",color=0xFF0000)
        return await ctx.send(embed=embed)

    try:
        with open("mod_stats.json", "r") as f:
            stats = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return await ctx.send("No staff statistics available.")

    if not stats:
        return await ctx.send("No staff have used moderation commands yet.")

    # Sort stats by number of actions (highest first)
    sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

    # Build the leaderboard message
    description = ""
    for i, (user_id, count) in enumerate(sorted_stats[:10], start=1):
        member = ctx.guild.get_member(int(user_id))
        name = member.mention if member else f"`{user_id}`"
        description += f"**{i}.** {name}\n{count} moderation actions since first moderation\n\n"

    embed = discord.Embed(
        title="📊 Moderator Leaderboard",
        description=description,
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

bot.run("")