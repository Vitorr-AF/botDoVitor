# Importação das bibliotecas random e discord
import discord
from discord.ext import commands
import random

# Permissões do bot (permissões padrões além de ver mensagens e usuários)
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True


#define o token do bot usando input e o prefixo de comandos
token = input("Seu token aqui: ")
bot = commands.Bot(command_prefix=".", intents=permissoes)

# Comando de rolar dado (.dado)
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

# Comando .ola
@bot.command()
async def ola(ctx: commands.Context):
    user = ctx.author
    await ctx.reply(f'Olá {user.display_name}')

# Mensagem de inicialização
@bot.event
async def on_ready():
    print("ESTOU VIVO!!!")

# Teste de embed
@bot.command()
async def teste1(ctx: commands.Context):
    meu_embed = discord.Embed(title="Olá mundo", description="ESTOU VIVO MUAHAHHAHAHAHAHA")
    await ctx.reply(embed=meu_embed)

bot.run(token)