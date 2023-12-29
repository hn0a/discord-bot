import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")
default_intents = discord.Intents.default()
default_intents.members = True
bot = commands.Bot(command_prefix="!", intents=default_intents)

# Global variable for the points system
points = {}

# Event for when the bot is ready
@bot.event
async def on_ready():
    print("The bot is connected.")

# Event for when a new member joins
@bot.event
async def on_member_join(member):
    print(f"A new member has arrived: {member.display_name}")

# Command to delete messages
@bot.command(name="delete")
@commands.has_permissions(manage_messages=True)
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()

# Command to kick a member
@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')

# Command to ban a member
@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned.')

# Assign role by command
@bot.command(name="role")
async def assign_role(ctx, role: discord.Role):
    await ctx.author.add_roles(role)
    await ctx.send(f"Role {role.name} added to {ctx.author.mention}.")

# Automatic responses
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "keyword" in message.content.lower():
        await message.channel.send("Automatic response for the keyword")

    await bot.process_commands(message)

# Points system
@bot.command(name="points")
async def points_command(ctx, member: discord.Member = None):
    member = member or ctx.author
    score = points.get(member.id, 0)
    await ctx.send(f"{member.mention} has {score} points.")

@bot.command(name="addpoints")
@commands.has_permissions(manage_messages=True)
async def add_points(ctx, member: discord.Member, amount: int):
    points[member.id] = points.get(member.id, 0) + amount
    await ctx.send(f"{amount} points added to {member.mention}.")

bot.run(os.getenv("TOKEN"))
