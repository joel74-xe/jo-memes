import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme') #Fetches memes from reddit
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme()) #Sends meme from reddit
    if message.content.startswith('$hello'):
      await message.channel.send(f"Hey there!!!") #Greets user 
    if message.content.startswith('$insta_dev'):
      await message.channel.send("https://www.instagram.com/x.j03l")#sends instagram account link of developer
    if message.content.startswith('$link'):
      await message.channel.send('https://discord.com/oauth2/authorize?client_id=1349824669099888710&permissions=51200&integration_type=0&scope=bot')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('BOT TOKEN IS NOT GIVEN DUE TO PRIVACY ISSUES') #Please add your bot token here obtained from discord developer portal.
