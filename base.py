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


#.help (mostra a lista de comandos)
@bot.command()
async def ajuda(ctx: commands.Context):
    help_m= discord.Embed(title="Lista de comandos atuais:", description=".ajuda(mostra a lista de comandos)\n.dado(joga um dado do número de lados fornecido)\n.ola(o bot manda um oi)\n\nO bot pode ter algumas reações secretas dependendo do que você mandar")
    await ctx.reply(embed=help_m)


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

@bot.event
async def on_message(message):
    if "escola dominicana" in message.content.lower():
        await message.reply("Não falamos desse assunto, APAGUE")
    elif "69" in message.content:
        await message.add_reaction("🤤")
    await bot.process_commands(message)


# Mensagem de inicialização
@bot.event
async def on_ready():
    print("ESTOU VIVO!!!")

# Comando .ola
@bot.command()
async def ola(ctx: commands.Context):
    user = ctx.author
    await ctx.reply(f'Olá {user.display_name}')


bot.run(token)