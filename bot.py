from bot_logic import gen_pass
from discord.ext import commands
import discord
import requests

# Permissões do bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.message_content = True
# Prefixo para chamar a resposta do bot
bot = commands.Bot(command_prefix="$", intents=intents)

# Evento: quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")

# Evento: quando alguém entra no servidor
@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="geral")
    if canal:
        await canal.send(f"Seja bem-vindo(a) ao servidor, {member.mention}!")
    else:
        print("⚠️ Canal 'geral' não encontrado!")

# Comando: hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Comando: bye
@bot.command()
async def bye(ctx):
    await ctx.send("Bye! 🙂")

# Comando: senha
@bot.command()
async def senha(ctx):
    senha_gerada = gen_pass(10)
    await ctx.send(f"🔐 Sua senha gerada é: {senha_gerada}")

# Comando: meme
@bot.command()
async def meme(ctx):
    with open('Imagens/meme1.png', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
        await ctx.send(file=picture)

# Comando: informações
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Botzinho top",
        description="Eu converso com você, gero senhas e mando memes!",
        color=discord.Color.green()
    )

    embed.add_field(
        name="Funcionalidades disponíveis:",
        value="$hello\n$bye\n$senha\n$meme\n$info\n$duck",
        inline=False
    )

    embed.set_footer(text="Criado durante a aula de programação!")

    await ctx.send(embed=embed)

# API
def get_duck_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

# Comando: duck
@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Token
bot.run("TOKEN")
