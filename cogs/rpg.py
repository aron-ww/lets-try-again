
from discord.ext import commands
import discord
import random

class RPG(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_msg(self, title, description):
        embed = discord.Embed(title=title, description=description, color=0x2f3136)
        embed.set_thumbnail(url="https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif")
        embed.set_footer(text="Coded with ❤️ by aron.ww")
        return embed

    @commands.command()
    async def adventure(self, ctx):
        outcome = random.choice(["You found treasure! 💰", "A dragon appeared! 🐉", "You fell into a trap! 💀", "You gained a new ally! 🏰", "You discovered a hidden cave! 🕳️"])
        await ctx.send(embed=self.embed_msg("🧙 Adventure", outcome))

def setup(bot):
    bot.add_cog(RPG(bot))
