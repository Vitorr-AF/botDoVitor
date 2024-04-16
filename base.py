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
    help_descricao = """
    Lista de comandos atuais:
    .ajuda: Mostra a lista de comandos.
    .dado: Joga um dado do número de lados fornecido.
    .ola: O bot manda um oi.
    .calculadora: calcula dois números 
    
    O bot pode ter algumas reações secretas dependendo do que você mandar.
    """
    help_m= discord.Embed(title="Lista de comandos atuais:", description= help_descricao)
    help_m= discord.Color.blue()
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

# Comando de teste de botões
@bot.command()
async def teste2(ctx: commands.Context):
    #função que será ativada quando o botão for pressionado
    async def resposta_botao(interact: discord.Interaction):
        #ephemeral quer dizer que só quem apertou pode ver a mensagem
        await interact.response.send_message('Botão pressionado', ephemeral= True)
        #followup vai fazer a mensagem vir em seguida da outra
        await interact.followup.send('Segunda mensagem', ephemeral=True)
    #visualização do botão (ainda não entendi o que faz)
    view = discord.ui.View()
    #cria o botão e define sua cor
    botao = discord.ui.Button(label='Botão', style=discord.ButtonStyle.red)
    #chama a função quando o botão é pressionado
    botao.callback = resposta_botao
    
    #coloca o botão na visualização
    view.add_item(botao)
    #finalmente manda a visualização
    await ctx.reply(view=view)


# Comando informações
@bot.command()
async def calculadora(ctx: commands.Context, num1:float, num2:float):
    async def resposta_botao(interact: discord.Interaction):
        escolha = int(interact.data['values'][0])  # Converte a string para um inteiro
        match escolha:
            case 1:
                result = num1 + num2
            case 2:
                result = num1 - num2
            case 3:
                result = num1 * num2
            case 4:
                result = num1 / num2
        await interact.response.send_message(f'Resultado = {result}')
    
    
    selecao= discord.ui.Select(placeholder="Escolha a operação")
    opcoes= [
        discord.SelectOption(label="Adição", value=1),
        discord.SelectOption(label="Subtração", value=2),
        discord.SelectOption(label="Multiplicação", value=3),
        discord.SelectOption(label="Divisão", value=4)
    ]
    selecao.options = opcoes
    view = discord.ui.View()
    view.add_item(selecao)
    selecao.callback = resposta_botao
    await ctx.reply(view=view)
    

@bot.command()
async def info(ctx: commands.Context):
    view = discord.ui.View()
    #
    botao = discord.ui.Button(label='Canal do Vitor', style=discord.ButtonStyle.green, url='https://www.youtube.com/@6vitor9')

    view.add_item(botao)
    await ctx.reply(view=view)

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