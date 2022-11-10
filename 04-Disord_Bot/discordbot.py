import discord

intents = discord.Intents.default()
intents.messages= True
client = discord.Client(intents=intents)
bottoken=open("c:/geheim/discordbot.txt", "r").readline()

@client.event
async def on_ready():
    # De bot kan op veel verschillende servers draaien. Met deze regel code pak je de eerste server die deze bot heeft. Als jouw bot maar 1 server heeft is het makkelijk.
    guild = client.guilds[0]
    # De naam van de server printen we gelijk uit.
    print(guild.name, "is the name of the server")

    # We printen de naam van de bot user uit.
    print(client.user, "has connected to the client")


client.run(bottoken)
