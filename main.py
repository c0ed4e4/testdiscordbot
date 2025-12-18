import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"❌ Error in event {event}", flush=True)

bot.run(TOKEN)
