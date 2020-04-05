import discord
import os
import traceback

client = discord.Client(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    print("logged in as " + client.user.name)

@client.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if message.author != client.user:
        msg = message.author.mention + "おはよう！いい朝だね！！"
        #await client.send_message(message.channel, msg)
    
@client.command()
async def ping(ctx):
    await ctx.send('pong')


client.run("token")
