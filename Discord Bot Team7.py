import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith("M하이"):
        await message.channel.send("안녕!")




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
