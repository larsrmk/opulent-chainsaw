import discord
from discord.ext import commands, tasks
from discord.commands import  Option
import asyncio

import os
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.voice_states = True

bot = discord.Bot( 
    intents=intents, 
    debug_guildes=['debug_guildes']
    )

#Konsolenausgabe, dass der Bot sich erfolgreich mit Discord verbunden hat
@bot.event
async def on_ready():
    await bot.sync_commands()
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Activity(name="zu!", type=discord.ActivityType.watching, status=discord.Status.online)) # Status

@bot.event
async def on_message(msg):
    if msg.author.bot: # Auf Nachrichten, die der Bot schreibt, antwortet er nicht selber
        return
    await msg.channel.send("Stop writing") # Bot antwortet auf jede geschrieben Nachricht
    print(msg.channel) # Bot gibt in Konsole aus, in welchem Channel eine Nachricht gescheiben wurde

@bot.event
async def on_message_delete(msg):
    await msg.channel.send(f"Eine Nachricht von {msg.author.name} wurde gelöscht.") # Schreib, wenn eine Nachricht gelöscht wurde

@bot.slash_command(description="fährt den bot herunter")
async def stop(ctx):
    await ctx.respond(f'{bot.user.name} has disconnected!' ,ephemeral=True)
    print(f'{bot.user.name} has disconnected!')
    await bot.close()

@bot.slash_command(description="Verwarnung")
async def warn(
    ctx,
    user: Option(discord.Member, "Der Benutzer, den du verwarnen möchtest"),
    text: Option(str, "Bitte unterlasse dieses Verhalten!"),
    channel: Option(discord.TextChannel, "Der Textkanal, in dem die Verwarnung gesendet werden soll")
):
    await channel.send(f"{user.mention} {text}")
    await ctx.respond("Die Nachricht wurde gesendet", ephemeral=True)

@bot.command()
async def link(ctx, button_name: str, url: str):
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label=button_name, url=url, style=discord.ButtonStyle.link))
    await ctx.send(view=view)

@bot.slash_command()
async def clear(ctx, amount: int):
    role = discord.utils.get(ctx.guild.roles, id=1205972715425628210) # User muss diese Rolle haben (höhergestellte Rollen und Admin können Command nicht ausführen)
    if role and role in ctx.author.roles:
        await ctx.channel.purge(limit=amount)
        await ctx.respond(f'{amount} Nachrichten wurden gelöscht', ephemeral=True)
    else:
        await ctx.respond("Du hast nicht die erforderliche Rolle, um diesen Befehl auszuführen.", ephemeral=True)

# Alle User die eine bestimmte Rolle haben und alle User die eine höhergestellte Rolle haben, können diesen Command ausführen
# @bot.slash_command()
# async def clear1(ctx, amount: int):
#     role = discord.utils.get(ctx.guild.roles, id=1205972715425628210)
#     user_roles = ctx.author.roles
#     if any(role >= r for r in user_roles):
#         await ctx.channel.purge(limit=amount)
#         await ctx.respond(f'{amount} Nachrichten wurden gelöscht', ephemeral=True)
#     else:
#         await ctx.respond("Du hast nicht die erforderliche Rolle oder eine höhere Rolle, um diesen Befehl auszuführen.", ephemeral=True)

@bot.event # Create temp-channels
async def on_voice_state_update(user, before, after):
    category_id = 1197671296251744386  # ID der Kategorie
    trigger_channel_id = 1197671353227149363  #  ID des Voice Channels

    if after.channel and after.channel.id == trigger_channel_id:
        category = bot.get_channel(category_id)
        user = user

        # Name des Kanals
        channel_name = f"{user.display_name}s Channel"

        # moved den user in den temporären Kanal
        new_channel = await category.create_voice_channel(channel_name)
        await user.move_to(new_channel)
        
        # überprüfen ob der Channel noch existiert und ob sich noch jemand im Channel befindet
        while new_channel.members:
            await asyncio.sleep(5)
            
        await new_channel.delete()

load_dotenv()
bot.run(os.getenv('Token'))
