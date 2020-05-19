#! /usr/bin/env python3
"""Discord bot based the Arthur Character"""
from random import choice
import json
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")

DESCRIPTION = "Liste des commandes disponibles, utilise le préfixe '!' devant la commande"
client = commands.Bot(command_prefix="!", description=DESCRIPTION)


@client.event
async def on_ready():
    print("{0.user} est en ligne".format(client))
    channel = client.get_channel(700716211180404769)
    await channel.send(
        "**{0.user} est en ligne** https://tenor.com/view/kaamelott-gif-5330988".format(
            client
        )
    )
    await channel.send(
        'Le roi Arthur vient de se connecter, tape "!help" pour en savoir plus !'
    )


@client.command(help="755 citations de Kaameloot en une seule commande")
async def quote(ctx):
    with open("data.json") as f:
        json_file = f.read()
        data = json.loads(json_file)
        quote_id = choice(range(len(data)))
        quote_text = data[f"{quote_id}"]["citation"]
        personnage = data[f"{quote_id}"]["infos"]["personnage"]
        episode = data[f"{quote_id}"]["infos"]["episode"]
        if ":" in episode:
            discord_quote = (
                f"__**{personnage}**__ : {quote_text} - *Episode {episode.strip()}*"
            )
        else:
            discord_quote = (
                f"__**{personnage}**__ : {quote_text} - *Episode : {episode.strip()}*"
            )
        await ctx.send(discord_quote)


@client.command(help="Quand c'est pas faux")
async def faux(ctx):
    """Display a gif for the command 'faux'"""
    await ctx.send("https://tenor.com/view/kaa-kaamelott-pas-faux-perceval-gif-8896787")


@client.command(help="Quand c'est de la merdeeee !")
async def merde(ctx):
    """Display a gif for the command 'merde'"""
    await ctx.send("https://giphy.com/gifs/kaamelott-GSAyeyIkEs6Z2")

client.run(TOKEN)