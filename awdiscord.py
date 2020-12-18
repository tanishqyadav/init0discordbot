import discord
import random
from discord.ext import commands
import asyncio

from discord.ext.commands import Bot

bot: Bot = commands.Bot(command_prefix="!")
client = discord.Client()


# Bot status
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name='my game'))

    # or, for watching:
    activity = discord.Activity(name='You', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)


@bot.command()
async def says(ctx, *args):
    await ctx.message.delete()
    info = ctx.author
    print(info)
    for arg in args:
        await ctx.send(arg)


@bot.command()
async def say(ctx, *, msgs):
    await ctx.message.delete()
    await ctx.send(msgs)


@bot.command()
async def ii(ctx, *args):
    info = ctx.author
    print(info)
    channelii = bot.get_channel(782310277956763658)
    for arg in args:
        await channelii.send(arg)


@bot.command(pass_context=True)
async def i(ctx, *, msg):
    info = ctx.author
    print(info)
    channeli = bot.get_channel(782310277956763658)
    # await channel.send(format(m))
    await channeli.send(msg)


@bot.command(pass_context=True)
async def aq(ctx, *, msg):
    channelaq = bot.get_channel(756555807897682070)
    # await channel.send(format(m))
    await channelaq.send(msg)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # rest of your on_message code
    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        await asyncio.sleep(75)
        await message.channel.send('Hello!')
        await asyncio.sleep(15)
        await message.delete()

    if message.content.startswith('Good Night'):
        await asyncio.sleep(75)
        await message.channel.send('Good Night!')
        await asyncio.sleep(15)
        await message.delete()

    if message.content.startswith('Good Morning'):
        await asyncio.sleep(75)
        await message.channel.send('Good Morning!')
        await asyncio.sleep(15)
        await message.delete()

    if message.content.startswith('Cute Bot'):
        await message.channel.send('Just Same as You!')

    if message.content.startswith('Thnxs'):
        await message.channel.send('Thanks')

    # if message.content.startswith('Aqua'):
    #     myid = '<@413686157579124747>'
    #     await message.channel.send('Master %s ' % myid)

    # if message.content.startswith('aqua'):
    #     myid = '<@413686157579124747>'
    #     await message.channel.send(myid)

    if message.content.startswith('Free Hugs'):
        mybotid = '<@782411874477801502>'
        mention = message.author.mention
        await message.channel.send(f'Here %s For {mention}' % mybotid)

        # mention = message.author.mention
        # response = f"hey {mention}, you're great!"
        # await message.channel.send(response)

    # if message.content.startswith('free hugs'):
    #     mybotid = '<@782411874477801502>'
    #     await message.channel.send('Here %s For You' % mybotid)

    if message.content.startswith('free Hugs'):
        mybotid = '<@782411874477801502>'
        await message.channel.send('Here %s For You' % mybotid)

    if message.content.startswith('Free hugs'):
        mybotid = '<@782411874477801502>'
        await message.channel.send('Here %s For You' % mybotid)

    if message.content.startswith('+'):
        # Waits for 5 seconds before continuing to the next line of code
        await asyncio.sleep(7)
        await message.delete()

    if message.content.startswith('.'):
        # Waits for 5 seconds before continuing to the next line of code
        await asyncio.sleep(5)
        await message.delete()

    if message.content.startswith('!'):
        # Waits for 5 seconds before continuing to the next line of code
        await asyncio.sleep(10)
        await message.delete()

    if message.content.startswith('-'):
        # Waits for 5 seconds before continuing to the next line of code
        await asyncio.sleep(10)
        await message.delete()

    if message.content.startswith('AquaBell'):
        with open('C:/Users/tanis/Avi/Untitled Folder/gif/aquaBell.png', 'rb') as fp:
            await message.channel.send(file=discord.File('C:/Users/tanis/Avi/Untitled Folder/gif/aquaBell.png'))

    if message.content.startswith('Free Hugs For homies'):
        with open('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png', 'rb') as fp:
            await message.channel.send(file=discord.File('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png'))

    if message.content.startswith('Free Hugs for Homies'):
        with open('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png', 'rb') as fp:
            await message.channel.send(file=discord.File('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png'))

    if message.content.startswith('Free hugs For Homies'):
        with open('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png', 'rb') as fp:
            await message.channel.send(file=discord.File('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png'))

    if message.content.startswith('free Hugs For Homies'):
        with open('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png', 'rb') as fp:
            await message.channel.send(file=discord.File('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png'))

    if message.content.startswith('free hugs for'):
        user = message.mentions[0]
        mention = message.author.mention
        await message.channel.send(f"{mention} Sending... Love To {user.mention}")
        with open('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png', 'rb') as fp:
            await message.channel.send(file=discord.File('C:/Users/tanis/Avi/Untitled Folder/gif/Screenshot_20201217-190601.png'))


    if message.content.startswith('Dead Chat XD'):
        deadchat = 'https://tenor.com/view/dead-chat-gif-18792024'
        await message.channel.send(deadchat)

                    # if message.content.startswith('sendgif'): links = [
    # 'https://tenor.com/view/hug-virtual-hug-hug-sent-gif-5026057',
    # 'https://tenor.com/view/milk-and-mocha-hug-love-heart-couple-gif-17258498',
    # 'https://tenor.com/view/virtual-hug-penguin-love-heart-gif-14712845'] random_links = random.choice(links) await
    # message.channel.send(random_links)

    if bot.user.mentioned_in(message):
        await asyncio.sleep(3)
        await message.channel.send("Free Hugs are For Everyone But This One especially For You.")
        await asyncio.sleep(5)
        links = ['https://tenor.com/view/hug-virtual-hug-hug-sent-gif-5026057',
                 'https://tenor.com/view/milk-and-mocha-hug-love-heart-couple-gif-17258498',
                 'https://tenor.com/view/virtual-hug-penguin-love-heart-gif-14712845',
                 'https://tenor.com/view/peach-cat-hug-hug-up-love-mochi-mochi-peach-cat-gif-16334628',
                 'https://tenor.com/view/hug-love-hi-bye-cat-gif-15999080',
                 'https://tenor.com/view/hugging-hug-gif-10592461',
                 'https://tenor.com/view/warm-hug-gif-10592083',
                 'https://tenor.com/view/%E3%83%8F%E3%82%B0-%E4%BB%B2%E8%89%AF%E3%81%97-%E3%83%A9%E3%83%96-hug-friend-gif-15782411',
                 'https://tenor.com/view/peach-cat-hug-hug-up-love-mochi-mochi-peach-cat-gif-16334628'
                 ]
        random_links = random.choice(links)
        await message.channel.send(random_links)

        if message.content.startswith(random_links):
            await asyncio.sleep(7)
            await message.delete()
        # images = ["gochiusa-istheorderarabbit.gif", "tenor(2).gif", "tanor(3).gif"]
        # random_image = random.choice(images)

    # if message.content.startswith(':yawning_face:'):
    #     Waits for 5 seconds before continuing to the next line of code
    # await asyncio.sleep(2)
    # await message.delete()
    #
    # if message.content.startswith('<@!?435379055253127178>'):
    #     await asyncio.sleep(5)
    #     await message.channel.send('Thike vai')

    # if message.content.startswith('$<@!?435379055253127178>'):
    #     await asyncio.sleep(5)
    #     await message.channel.send('Thike vai')

    # if bot.user.mentioned_in(message):
    #     await asyncio.sleep(5)
    #     await message.channel.send("You Mentioned me, i see")
    #
    # if message.content.startswith('You Mentioned me, i see'):
    #     await asyncio.sleep(7)
    #     await message.delete()
    #     await message.channel.send('For Help Contact Master')


bot.run('token')
