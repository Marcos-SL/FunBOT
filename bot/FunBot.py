import json
from nextcord import Intents
from nextcord.ext import commands
import requests
from nextcord import ButtonStyle, Embed
from nextcord.ui import Button, View

intents = Intents.default()
intents.message_content = True

helpGuide = json.load(open("help.json"))

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")


def createHelpEmbed(pageNum=0, inline=False):
    pageNum = (pageNum) % len(list(helpGuide))
    pageTitle = list(helpGuide)[pageNum]
    embed = Embed(color=0xFF0080, title=pageTitle)
    for key, val in helpGuide[pageTitle].items():
        embed.add_field(name=bot.command_prefix + key, value=val, inline=inline)
        embed.set_footer(text=f"Page {pageNum + 1} of {len(list(helpGuide))}")
    return embed


@bot.command(name="commands")
async def Commands(ctx):
    currentPage = 0

    async def next_callback(interaction):
        nonlocal currentPage, sent_msg
        currentPage += 1
        await sent_msg.edit(embed=createHelpEmbed(pageNum=currentPage), view=myview)

    async def previous_callback(interaction):
        nonlocal currentPage, sent_msg
        currentPage -= 1
        await sent_msg.edit(embed=createHelpEmbed(pageNum=currentPage), view=myview)

    previousButton = Button(label="<", style=ButtonStyle.blurple)
    nextButton = Button(label=">", style=ButtonStyle.blurple)
    previousButton.callback = previous_callback
    nextButton.callback = next_callback

    myview = View(timeout=200)
    myview.add_item(previousButton)
    myview.add_item(nextButton)

    sent_msg = await ctx.send(embed=createHelpEmbed(currentPage), view=myview)


@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('HELLO WORLD')


@bot.command(name="hug")
async def Hug(ctx):
    response = requests.get("https://some-random-api.ml/animu/hug")
    imagem_link = response.json()["link"]
    await ctx.send(imagem_link)


@bot.command(name="facepalm")
async def Facepalm(ctx):
    response = requests.get("https://some-random-api.ml/animu/face-palm")
    imagem_link = response.json()["link"]
    await ctx.send(imagem_link)


@bot.command(name="quote")
async def Quote(ctx):
    response = requests.get("https://some-random-api.ml/animu/quote")
    frase = response.json()["sentence"]
    await ctx.send(frase)
    personagem = response.json()["character"]
    await ctx.send(personagem)
    anime = response.json()["anime"]
    await ctx.send(anime)


@bot.command(name="panda")
async def Panda(ctx):
    response = requests.get("https://some-random-api.ml/animal/panda")
    panda = response.json()["image"]
    await ctx.send(panda)
    fato = response.json()["fact"]
    await ctx.send(fato)


@bot.command(name="dog")
async def Dog(ctx):
    response = requests.get("https://some-random-api.ml/animal/dog")
    dog = response.json()["image"]
    await ctx.send(dog)
    fato = response.json()["fact"]
    await ctx.send(fato)


@bot.command(name="bird")
async def Bird(ctx):
    response = requests.get("https://some-random-api.ml/animal/bird")
    bird = response.json()["image"]
    await ctx.send(bird)
    fato = response.json()["fact"]
    await ctx.send(fato)


@bot.command(name="redpanda")
async def RedPanda(ctx):
    response = requests.get("https://some-random-api.ml/animal/red_panda")
    redpanda = response.json()["image"]
    await ctx.send(redpanda)
    fato = response.json()["fact"]
    await ctx.send(fato)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


if __name__ == '__main__':
    bot.run("YOUR_TOKEN")
