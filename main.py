import discord, os
import translators as ts
client = discord.Client()
lang = "off"
@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
  global lang
  if message.author.id == 600415718076448808:
    if message.content.startswith(".setlang"):
      lang = message.content.split(" ")[1]
      await message.edit(content=f"**`{client.user} changed language to {lang}`**")
    else:
      if lang != "off":
        msg = message.content
        translation = ts.translate_html(msg, translator=ts.google, to_language=lang)
        await message.edit(content=translation)
client.run(os.environ["token"], bot=False)