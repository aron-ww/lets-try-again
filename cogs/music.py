
from discord.ext import commands
import discord

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_msg(self, title, description):
        embed = discord.Embed(title=title, description=description, color=0x2f3136)
        embed.set_thumbnail(url="https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif")
        embed.set_footer(text="Coded with ❤️ by aron.ww")
        return embed

    @commands.command()
    async def play(self, ctx, *, query: str):
        await ctx.send(embed=self.embed_msg("🎶 Play", f"Now playing: **{query}**"))

    @commands.command()
    async def pause(self, ctx):
        await ctx.send(embed=self.embed_msg("⏸️ Paused", "Music paused."))

    @commands.command()
    async def skip(self, ctx):
        await ctx.send(embed=self.embed_msg("⏭️ Skipped", "Skipped the current song."))

    @commands.command()
    async def queue(self, ctx):
        await ctx.send(embed=self.embed_msg("🎵 Queue", "The queue is currently empty."))

    @commands.command()
    async def volume(self, ctx, volume: int):
        await ctx.send(embed=self.embed_msg("🔊 Volume", f"Set the volume to **{volume}%**"))

def setup(bot):
    bot.add_cog(Music(bot))
