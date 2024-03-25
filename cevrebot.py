import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz konuşalım!')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Ne hakkında konuşalım?')

@bot.command()
async def cevre(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bilgiler edinmek istiyorsanız oneri komutunu kullanın!')

@bot.command()
async def oneri(ctx):
    await ctx.send(f"Geri dönüşüm ile ilgili bilgi almak için gd, atıkları ne kadar süre içinde ayrıştırıldığını öğrenmek için ay komutu kullanın:")

@bot.command()
async def gd(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f'Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1)
    await ctx.send(f'Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.')
    time.sleep(1)
    await ctx.send(f'Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.')
    time.sleep(1)
    await ctx.send(f'Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.')
    time.sleep(1)
    await ctx.send(f'Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın..')
    time.sleep(1)
    await ctx.send(f'Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.')
    time.sleep(1)
    await ctx.send(f'Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve kullanmaya çalışın.')

@bot.command()
async def ay(ctx):
    await ctx.send(f"Strafor 5000 yıl - 2 Milyon yıl")
    time.sleep(1)
    await ctx.send(f"Cam Şişe 4000 yıl")
    time.sleep(1)
    await ctx.send(f"Plastik 1000 yıl")
    time.sleep(1)
    await ctx.send(f"Pet Şişe 400 yıl")
    time.sleep(1)
    await ctx.send(f"Pil 300 yıl yıl")
    time.sleep(1)
    await ctx.send(f"Alüminyum 100 yıl")
    time.sleep(1)
    await ctx.send(f"Kutu Kola 10 yıl")

@bot.command()
async def res(ctx):
    with open('M2L2\cevre-kirliligi-beste.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
    
    

