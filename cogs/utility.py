
from discord.ext import commands
import discord

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_msg(self, title, description):
        embed = discord.Embed(title=title, description=description, color=0x2f3136)
        embed.set_thumbnail(url="https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif")
        embed.set_footer(text="Coded with ❤️ by aron.ww")
        return embed

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(embed=self.embed_msg("🏓 Pong!", f"Latency: {round(self.bot.latency * 1000)}ms"))

    @commands.command()
    async def help(self, ctx):
        msg = "Available commands:
`.ping`, `.help`, `.purge`, `.ban`, `.kick`, `.mute`, `.unmute`, `.play`, `.pause`, `.skip`, `.queue`"
        await ctx.send(embed=self.embed_msg("📜 Help", msg))

def setup(bot):
    bot.add_cog(Utility(bot))
