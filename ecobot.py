from discord.ext import commands
import discord 
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)


# Evento: quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Fizemos login como {bot.user}")

# Evento: quando alguém entra no servidor
@bot.event
async def on_member_join(member):
    canal = discord.utils.get(member.guild.text_channels, name="geral")

    if canal:
        await canal.send(f"🎉 Bem-vindo(a) ao servidor ecobot, {member.mention}!")
    else:
        print("⚠️ Canal 'geral' não encontrado!")



@bot.command()
async def reciclomando(ctx):
    lista = ["🌍 Uma garrafa PET pode levar cerca de 400 anos para se decompor na natureza.",
"🔋 Uma bateria de lítio pode levar mais de 100 anos para se decompor e pode contaminar o solo.",
"♻️ Materiais recicláveis como papel, plástico, metal e vidro devem ir na coleta seletiva.",
"🍎 Restos de comida e cascas de frutas devem ser descartados como lixo orgânico ou usados na compostagem.",
"☣️ Materiais contaminados, como seringas e curativos, devem ser descartados em locais apropriados de resíduos hospitalares.",
"🧴 Óleo de cozinha usado nunca deve ser jogado na pia; leve a um ponto de coleta.",
"🪫 Pilhas e baterias devem ser descartadas em postos de coleta específicos, nunca no lixo comum.",
"🚯 Jogar lixo no chão contribui para a poluição dos rios e oceanos.",
"🌳 Reduzir, reutilizar e reciclar são atitudes essenciais para proteger o meio ambiente.",
"💧 Pequenas ações, como economizar água e energia, ajudam a diminuir os impactos ambientais."]

    neymar = random.choice(lista)

    await ctx.send(neymar)

@bot.command()
async def reciclopedia(ctx):
    
    await ctx.send(f"> 🌍 Uma garrafa PET pode levar cerca de 400 anos para se decompor na natureza."
"🔋 Uma bateria de lítio pode levar mais de 100 anos para se decompor e pode contaminar o solo."
"♻️ Materiais recicláveis como papel, plástico, metal e vidro devem ir na coleta seletiva."
"🍎 Restos de comida e cascas de frutas devem ser descartados como lixo orgânico ou usados na compostagem."
"☣️ Materiais contaminados, como seringas e curativos, devem ser descartados em locais apropriados de resíduos hospitalares."
"🧴 Óleo de cozinha usado nunca deve ser jogado na pia; leve a um ponto de coleta."
"🪫 Pilhas e baterias devem ser descartadas em postos de coleta específicos, nunca no lixo comum."
"🚯 Jogar lixo no chão contribui para a poluição dos rios e oceanos."
"🌳 Reduzir, reutilizar e reciclar são atitudes essenciais para proteger o meio ambiente."
"💧 Pequenas ações, como economizar água e energia, ajudam a diminuir os impactos ambientais.")

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="Botzinho top",
        description="Eu gero ideais importantes para você cuidar do meio ambiente, e quanto tempo algumas coisa demoram para se decompor!",
        color=discord.Color.green()
    )
    embed.add_field(
        name="Funcionalidades disponíveis:",
        value="\n.reciclomando\n.reciclopedia\n.info",
        inline=False
    )
    embed.set_footer(text="Criado durante a aula de programação!")
    await ctx.send(embed=embed)



bot.run("TOKEN")
