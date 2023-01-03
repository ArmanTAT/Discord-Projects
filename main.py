import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command()
async def pastnames(ctx, user: discord.Member):
    server = ctx.guild
    audit_logs = []
    async for entry in server.audit_logs(limit=100):
        audit_logs.append(entry)
    nickname_entries = [entry for entry in audit_logs if entry.action == discord.AuditLogAction.member_update]
    user_nickname_entries = [entry for entry in nickname_entries if entry.target.id == user.id]
    past_names = [entry.before.nick for entry in user_nickname_entries if entry.before.nick is not None]
    if past_names:
        embed = discord.Embed(
            title= f"{user.display_name}'s past names",
            description= ', '.join(past_names),
            color= discord.Color.green()
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title= f"{user.display_name}'s past names",
            description= "This user has no past names.",
            color= discord.Color.red()
        )
        await ctx.send(embed=embed)


client.run("bot token here") #Change this to your bot token!
