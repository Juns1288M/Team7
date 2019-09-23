import discord
import os


client = discord.client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("M하이"):
        await message.channel.send("안녕!")
        
        
 



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
