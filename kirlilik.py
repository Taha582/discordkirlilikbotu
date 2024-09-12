import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Merhaba {client.user}! ben bir botum!')
    if message.content.startswith('petşişe'):
        await message.channel.send('pet şişeler doğada 450 yılda yok olur')
    if message.content.startswith('hava kirliliği nedir'):
        await message.channel.send('Hava kirliliği, havanın doğal bileşiminin çeşitli nedenlerle değişmesi, havada katı, sıvı ve gaz şeklindeki yabancı maddelerin insan sağlığına, canlı hayatına, ekolojik dengeye ve eşyalara zararlı olabilecek derişim ve sürede bulunmasıdır.')
    if message.content.startswith('kirliliği nasıl azaltabilirim'):
        await message.channel.send('kirliliği geri dönüşüm yaparak veya toplu taşıma araçları kullanarak kirliliği azaltabilirsin')
    if message.content.startswith('atıkları nasıl ayrıştırabilirim'):
        await message.channel.send('pet şişeleri(vb) plastik atıklara metalleri metal pilleri pil ve camları cam atık kutusuna atabilirsin')
    if message.content.startswith('atık yağları ne yapmalıyım'):
        await message.channel.send('atık yağları eğer yakın illerde bulunan atık yağ depolama kutularına atabilirsin eğer yoksa kavanoz petşişe vb saklama kaplarında saklayabilirsin')
    if message.content.startswith('pil'):
        await message.channel.send('piller doğada 300 yılda yok olur')
    if message.content.startswith('küresel ısınma nedir'):
        await message.channel.send('küresel ısınma sera gazlarının artması ve bu gazların dünyadaki ortalama ısıyı arttırmasıdır')
    if message.content.startswith('sera gazı nedir'):
        await message.channel.send('fabrikaların bacasından çıkan dumanların veya araba egzozlarından çıkan dumanların sera etkisi yapıp güneş ışığının yer yüzüne çarpıp uzaya geri dönmesini engeller ')
    if message.content.startswith('sera gazını nasıl azaltabiliriz'):
        await message.channel.send('sera gazlarını fabrika bacalarına filitre takarak toplu taşıma araçları kullanarak yada işe/okula giderken bisiklet kullanabilirsin')   
    if message.content.startswith('cam'):
        await message.channel.send('camlar doğada 4000-4500 yılları arasında yok olur')
    if message.content.startswith('kirlilik nedir'):
        await message.channel.send('Kirlilik, hava, su veya toprak gibi bir ortamı insanlara veya doğaya zarar verecek şekilde değiştirir')
    if message.content.startswith('toprak kirliliği nedir'):
        await message.channel.send('web de toprak kirliliği hakkında şınu buldum:https://tr.wikipedia.org/wiki/Toprak_kirlili%C4%9Fi')
    if message.content.startswith('su kirliliği hakkında bir video önerebilirmisin'):
        await message.channel.send('webde şunu buldum:https://www.youtube.com/watch?v=gLtyn6UyCwk')



client.run("")
