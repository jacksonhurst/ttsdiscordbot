import discord
import asyncio
from gtts import gTTS


client = discord.Client()



@client.event
async def on_ready():
    print("Bot online") 

@client.event
async def on_message(message):
      
    if message.content.startswith('!TTV') or message.content.startswith('!ttv') or message.content.startswith('!say'):
        text = message.content[5:]
        tts = gTTS(text=text, lang='en')
        tts.save('TTV.mp3')
        channel = client.get_channel('INSERT YOUR VOICE CHANNEL HERE')
        vc = await client.join_voice_channel(channel)
        player = vc.create_ffmpeg_player('TTV.mp3')
        player.start()
        while player.is_playing():
            async for message in client.logs_from(channel, limit=1):
                if message.content.startswith('!stop'):
                    break
        i = 0
        while i == 0:
            try:
                for x in client.voice_clients:
                    await x.disconnect()
                    i = 1
            except:
                i = 1
                continue
        
    elif message.content.startswith('!stop'):
        i = 0
        while i == 0:
            try:
                for x in client.voice_clients:
                    await x.disconnect()
                    i = 1
            except:
                i = 1
                continue

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Hello, please type !say followed by a space and then the text you would like the bot to say in your main voice channel! Type !stop to stop the bot during text to speech')       

    
    
client.run('INSERT YOUR BOT KEY HERE')
