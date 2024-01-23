import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
import asyncio


intents = discord.Intents.all()
intents.voice_states = True


bot = commands.Bot(command_prefix='py')


#Konsolenausgabe, dass der Bot sich erfolgreich mit Discord verbunden hat
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    # Status
    await bot.change_presence(activity=discord.Activity(name="zu!", type=discord.ActivityType.watching, status=discord.Status.online))


@bot.event
async def on_message(msg):
    if msg.author.bot: # Auf Nachrichten, die der Bot schreibt, antwortet er nicht selber
        return
    await msg.channel.send("Stop writing") # Bot antwortet auf jede geschrieben Nachricht
    print(msg.channel) # Bot gibt in Konsole aus, in welchem Channel eine Nachricht gescheiben wurde

@bot.event
async def on_message_delete(msg):
    await msg.channel.send(f"Eine Nachricht von {msg.author.name} wurde gelöscht.") # Schreib, wenn eine Nachricht gelöscht wurde


@bot.event
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

        # plant, das der Channel nach 5 Sekunden gelöscht wird, wenn kein user mehr im Channel ist
        await asyncio.sleep(5) # braucht man nicht unbedingt
        
        # überprüfen ob der Channel noch existiert und ob sich noch jemand im Channel befindet
        while new_channel.members:
            await asyncio.sleep(5)
            
        await new_channel.delete()

load_dotenv()
bot.run(os.getenv("Token"))
