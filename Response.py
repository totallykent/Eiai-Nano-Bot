import discord
import GeminiConvo
import os

def bot_start(token):
    intents = discord.Intents.default()

    intents.messages = True
    intents.message_content = True
    intents.members = True
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('Eiai-san is ready!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if client.user in message.mentions and "!invite" in message.content:
            await message.reply(GeminiConvo.inviteLink())
            return
        
        if client.user in message.mentions:
            user_message = removeMention(str(message.content)) 
            geminiReply = GeminiConvo.main(user_message)
            await message.reply(geminiReply)

    client.run(token)

def removeMention(userMessage):
    return userMessage.replace(GeminiConvo.botID(), "'Note: Please reply in under 2000 characters'")

def main():
    GeminiConvo.loadEnv()
    bot_start(os.getenv('discord_api'))
