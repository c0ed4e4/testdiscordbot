import os
import discord
import random
import string
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

# ✅ คำสั่งสร้างไฟล์สุ่มขนาด 10MB
@bot.command()
async def genfile(ctx):
    # สุ่มชื่อไฟล์ (10 ตัวอักษร)
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".bin"

    file_size = 10 * 1024 * 1024  # 10 MB

    with open(filename, "wb") as f:
        f.write(os.urandom(file_size))

    await ctx.send(f"📁 สร้างไฟล์เรียบร้อยแล้ว: `{filename}` (10 MB)")

@bot.event
async def on_error(event, *args, **kwargs):
    print(f"❌ Error in event {event}", flush=True)

bot.run(TOKEN)
