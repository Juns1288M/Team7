import discord

client = discord.client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("M하이"):
        await message.channel.send("안녕!")




client.run("NjI1NjcxNDYyNjEwNTM0NDQx.XYi8Fg.DN9nUPnNG-YkdvcqMp_sIA8ZG-E")