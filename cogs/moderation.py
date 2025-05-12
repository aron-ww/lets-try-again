
from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def embed_msg(self, title, description):
        embed = discord.Embed(title=title, description=description, color=0x2f3136)
        embed.set_thumbnail(url="https://i.gifer.com/origin/60/606dc4f509be21ae620b538570dc1417_w200.gif")
        embed.set_footer(text="Coded with ❤️ by aron.ww")
        return embed

    @commands.command()
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send(embed=self.embed_msg("🧹 Purged", f"Deleted {limit} messages."), delete_after=5)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.ban(reason=reason)
        await ctx.send(embed=self.embed_msg("🔨 Banned", f"{member.mention} has been banned.
Reason: {reason}"))

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        await member.kick(reason=reason)
        await ctx.send(embed=self.embed_msg("👢 Kicked", f"{member.mention} has been kicked.
Reason: {reason}"))

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, speak=False, send_messages=False)
        await member.add_roles(muted_role)
        await ctx.send(embed=self.embed_msg("🔇 Muted", f"{member.mention} has been muted."))

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(muted_role)
        await ctx.send(embed=self.embed_msg("🔊 Unmuted", f"{member.mention} has been unmuted."))

def setup(bot):
    bot.add_cog(Moderation(bot))
