#Original code - https://replit.com/@RexanWONG/neonInspiration-DISCORD-BOT-1#main.py
import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

# reply and random response
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]


starter_encouragements = [
    "Cheer up!",
    "May the light be with you",
    "🐶 Woof woof don't be sad",
    "Neonpuppies to the rescue, cheer up!",
    "Don't worry - WAGMI"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


@client.event  # instances
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event  # instances
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('/hello'):
        await message.channel.send('Hello')

    if message.content.startswith('/What will be BTC price in 3 months?'):
        await message.channel.send('100k')

    if message.content.startswith('/inspire_me'):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements
    if "encouragements" in db.keys():
        options.extend(db["encouragements"])

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith("/new"):
        encouraging_message = msg.split("/new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("/del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("/del", 1)[1])
            delete_encouragment(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("/list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)


keep_alive()
my_secret = os.environ['botToken']
# bot token/password
client.run(my_secret)


   







