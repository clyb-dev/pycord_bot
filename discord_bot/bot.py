import discord
import asyncio
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv

intents = discord.Intents.default()
client = discord.Client(intents=intents)
token = 'token_value_here'  # Remplacez par votre token réel('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!start_timer'):
        await start_timer()

async def start_timer():
    now = datetime.now()
    end_time = now + timedelta(days=60)  # 2 mois

    while now < end_time:
        remaining_time = end_time - now
        remaining_seconds = remaining_time.total_seconds()

        if remaining_seconds <= 0:
            break

        await asyncio.sleep(1)
        now = datetime.now()

        # Affiche le temps restant
        remaining_minutes = int(remaining_seconds // 60)
        remaining_seconds %= 60
        remaining_time_str = f'{remaining_minutes:02d}:{remaining_seconds:02d}'
        print(f'Timer: {remaining_time_str}')

    print('Timer terminé!')

client.run(token)