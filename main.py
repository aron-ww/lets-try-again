
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = "."

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

GIF_URL = "https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif"
FOOTER_TEXT = "Coded with ❤️ by aron.ww"

# Global embed function
def embed_msg(title, description):
    embed = discord.Embed(title=title, description=description, color=0x2f3136)
    embed.set_thumbnail(url=GIF_URL)
    embed.set_footer(text=FOOTER_TEXT)
    return embed

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync()

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEN)
