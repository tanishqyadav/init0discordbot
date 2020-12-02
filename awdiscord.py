import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!")

#Bot status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='my game'))

    # or, for watching:
    activity = discord.Activity(name='You', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)


@client.command()
async def say(ctx, *args):
    info = ctx.author
    print(info)
    for arg in args:
        await ctx.send(arg)

@client.command()
async def i(ctx, *args):
    info = ctx.author
    print(info)
    channel = client.get_channel(782310277956763658)
    for arg in args:
        await channel.send(arg)



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

#client = MyClient()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('what the fuck'):
        await message.channel.send('Pls behave properly')

    if message.content.startswith('?dm' ):
        message.author.send(message)


#mod_mail
@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="test")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "test" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)






@client.event
async def on_message(message):
    await client.process_commands(message)
    # rest of your on_message code

client.run('NzgyNDExODc0NDc3ODAxNTAy.X8Lz1w.rQJzq8Eky6bDyUDkATRjw9BviOs')