import discord
from discord.ext import commands
import random

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
#define o token do bot
token = 'seu token aqui'

bot = commands.Bot(command_prefix=".", intents=permissoes)

@bot.command()
async def dado(ctx: commands.Context, numLados: int):
    try:
        if numLados > 0:
            randomN = random.randint(1, numLados)
            await ctx.reply(f'Número rolado: {randomN}')
        else:
            raise ValueError
    except ValueError:
        await ctx.reply("Digite um número válido (positivo e sem vírgula)")





@bot.command()
async def ola(ctx: commands.Context):
    user = ctx.author
    await ctx.reply(f'Olá {user.display_name}')


@bot.event
async def on_ready():
    print("ESTOU VIVO!!!")


bot.run(token)