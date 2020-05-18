#! /usr/bin/env python3
"""Discord bot based the Arthur Character"""
import os
from random import randint
import json
import discord
from discord.ext import commands
from secret import TOKEN

client = commands.Bot(command_prefix="!", description="Liste des commandes disponibles, utilise le préfixe '!' devant la commande")

@client.event
async def on_ready():
    print('{0.user} est en ligne'.format(client))
    channel = client.get_channel(686237845937192999)
    await channel.send('**{0.user} est en ligne** https://tenor.com/view/kaamelott-gif-5330988'.format(client))
    await channel.send('Le roi Arthur vient de se connecter, tape "!help" pour en savoir plus')

@client.command(help="755 citations de Kaameloot en une seule commande")
async def quote(ctx):
    with open("data.json") as f:
        f = f.read()
        data = json.loads(f)
        quote_id = randint(0, 755)
        quote = data[f"{quote_id}"]["citation"]
        personnage = data[f"{quote_id}"]["infos"]["personnage"]
        episode = data[f"{quote_id}"]["infos"]["episode"]
        discord_quote = f"{personnage} :{quote} - Episode :{episode}"
        await ctx.send(discord_quote)

@client.command(help="Quand c'est pas faux")
async def faux(ctx):
    await ctx.send("https://tenor.com/view/kaa-kaamelott-pas-faux-perceval-gif-8896787")

@client.command(help="Quand c'est de la merdeeee !")
async def merde(ctx):
    await ctx.send("https://giphy.com/gifs/kaamelott-GSAyeyIkEs6Z2")

client.run(TOKEN)