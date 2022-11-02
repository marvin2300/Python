import nextcord
from nextcord.ext import commands

guild_id = 1031897754475188224

bot = commands.Bot()


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.slash_command(description="My first slash command", guild_ids=[guild_id])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

bot.run("MTAzMTk2NzU0MjQwMDUyMDI1Mg.GwlgKA.Slomnk0sVfyLZKzAFeWH89FZLm9SH2Pdr38KHY")


