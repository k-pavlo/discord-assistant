import os
import sys
import discord
from discord import app_commands
from dotenv import load_dotenv
from AttendatsList import AttendatsList

load_dotenv()
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@tree.command(name="create_list", description="Create an empty list of the event's attendants.")
@app_commands.describe(title="Event's title", date="Event's date")
async def create_list_command(interaction: discord.Interaction, title: str, date: str):
    al1 = AttendatsList(title, date, str(interaction.user))
    await interaction.response.send_message(al1.print_list())

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user} (ID: {client.user.id})")

token = os.getenv('TOKEN')
if not token:
    print('There is no token specified')
    sys.exit(1)
client.run(token)